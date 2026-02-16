import fitz  # PyMuPDF
import os
import logging
import re
from PIL import Image
from generator.src.config import (
    GATE_ASSETS_DIR, 
    STREAM_ALIASES,
    IMAGE_FORMAT,
    IMAGE_QUALITY,
    IMAGE_LOSSLESS,
    PDF_ZOOM_LEVEL
)
from generator.src.image_utils import optimize_image, get_file_extension

logger = logging.getLogger(__name__)

# Regex Patterns
RE_Q_START = re.compile(r'^\s*Question\s*\d+', re.IGNORECASE)
RE_ANS_START = re.compile(r'^\s*Ans\.\s*', re.IGNORECASE)
RE_SOL_START = re.compile(r'^\s*Sol\.\s*', re.IGNORECASE)
RE_PAGE_ARTIFACT = re.compile(r'^\s*PAGE\s*\d+', re.IGNORECASE)

def process_syllabus(stream_code, filepath, con=None):
    """
    Process syllabus PDF.
    If con is provided, it can insert structure directly, but generally 
    syllabus structure is built via LLM in knowledge_utils. 
    The original PDFProcessor.process_syllabus was heuristic/dummy.
    We will keep the heuristic logic here as a fallback or pre-processor if needed, 
    but modern flow uses LLM.
    """
    logger.info(f"Processing Syllabus: {filepath}")
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    
    # Heuristic parsing logic preserved from OOP version
    lines = text.split('\n')
    subtopics = []
    current_subject = "General"
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        if "Section" in line or "Subject" in line:
            current_subject = line
            continue
            
        if len(line) > 5 and len(line) < 100:
            subtopic_id = f"{stream_code}_{len(subtopics)}"
            subtopics.append({
                "id": subtopic_id,
                "name": line,
                "subject": current_subject,
                "stream": stream_code,
                "order_index": len(subtopics)
            })
    
    # Note: DB insertion was commented out in original code too, 
    # focusing on returning or just logging.
    return subtopics

def process_stream(stream_code):
    stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
    stream_dir = os.path.join(os.path.abspath("data/raw"), stream_alias)
    
    if not os.path.exists(stream_dir):
        logger.warning(f"No raw data found for {stream_code} (Alias: {stream_alias}) at {stream_dir}")
        return

    for filename in os.listdir(stream_dir):
        if not filename.endswith(".pdf"):
            continue
            
        filepath = os.path.join(stream_dir, filename)
        
        if "syllabus" in filename.lower():
            # process_syllabus(stream_code, filepath) # Mostly legacy/unused in favor of LLM
            pass 
        else:
            process_pdf(stream_code, filepath)


def process_pdf(stream, filepath):
    fname = os.path.basename(filepath)
    packet_id = os.path.splitext(fname)[0] # e.g. "2021-M"
    
    year = "Unknown"
    match_year = re.search(r'(\d{4})', packet_id)
    if match_year:
        year = match_year.group(1)
        
    logger.info(f"Processing PDF {packet_id} (Year: {year})")
    
    doc = fitz.open(filepath)
    
    # State Machine Variables
    current_state = None # 'QUESTION', 'ANSWER', 'EXPLANATION'
    current_q_meta = {} 
    
    processed_questions = []

    def flush_question():
        if current_q_meta and current_q_meta.get('id'):
            processed_questions.append(current_q_meta.copy())
        return {
            'id': None, 
            'q_text': [], 'q_rects': [], 
            'a_text': [], 
            'exp_text': [], 'exp_rects': [],
            'type': 'MCQ' # Default
        }

    current_q_meta = flush_question() 

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        sorted_blocks = sorted(blocks, key=lambda b: (b['bbox'][1], b['bbox'][0])) # Sort by Y then X
        
        for block in sorted_blocks:
            if 'lines' not in block: continue
            
            # Reconstruct block text
            block_text = "\n".join([span['text'] for line in block['lines'] for span in line['spans']]).strip()
            
            # Check for Artifacts
            bt_lower = block_text.lower()
            if RE_PAGE_ARTIFACT.match(block_text) or "gate academy" in bt_lower or "general aptitude" in bt_lower:
                    continue

            # State Transitions
            if RE_Q_START.match(block_text):
                # New Question starts -> Flush previous
                if current_q_meta['id']:
                    current_q_meta = flush_question() # Reset
                
                raw_id = block_text.split()[1] if len(block_text.split()) > 1 else "Unknown"
                current_q_meta['id'] = raw_id.rstrip('.')
                current_state = 'QUESTION'
                # Add to Q Logic
                current_q_meta['q_text'].append(block_text)
                current_q_meta['q_rects'].append((page_num, block['bbox']))
                
            elif RE_ANS_START.match(block_text):
                current_state = 'ANSWER'
                current_q_meta['a_text'].append(block_text)
                
            elif RE_SOL_START.match(block_text):
                current_state = 'EXPLANATION'
                current_q_meta['exp_text'].append(block_text)
                current_q_meta['exp_rects'].append((page_num, block['bbox']))
                
            else:
                # Accumulate based on state
                if current_state == 'QUESTION':
                    current_q_meta['q_text'].append(block_text)
                    current_q_meta['q_rects'].append((page_num, block['bbox']))
                elif current_state == 'ANSWER':
                    current_q_meta['a_text'].append(block_text)
                elif current_state == 'EXPLANATION':
                    current_q_meta['exp_text'].append(block_text)
                    current_q_meta['exp_rects'].append((page_num, block['bbox']))

    # Flush last question
    if current_q_meta['id']:
            processed_questions.append(current_q_meta)

    logger.info(f"Extracted {len(processed_questions)} raw questions. Now saving...")
    
    # Post-Processing & Saving
    for q_data in processed_questions:
        try:
            save_question_data(stream, packet_id, year, q_data, doc)
        except Exception as e:
            logger.error(f"Error saving question {q_data.get('id')}: {e}")

def save_question_data(stream, packet_id, year, q_data, doc):
    q_id_str = q_data['id']
    stream_alias = STREAM_ALIASES.get(stream, stream) # Fallback to full name if no alias
    q_clean_id = q_id_str.replace(' ', '')
    
    # 1. Process Texts
    q_text_full = "\n".join(q_data['q_text'])
    a_text_full = "\n".join(q_data['a_text']).replace("Ans.", "").strip()
    exp_text_full = "\n".join(q_data['exp_text'])
    
    # 2. Process Images (Stitching)
    # Get file extension based on configured format
    img_ext = get_file_extension(IMAGE_FORMAT)
    
    # Structure: assets/<stream_alias>/questions/<packet_id>/<id>/q.<ext>
    base_rel_path = f"{stream_alias}/questions/{packet_id}/{q_clean_id}"
    base_abs_path = os.path.join(GATE_ASSETS_DIR, base_rel_path)
    os.makedirs(base_abs_path, exist_ok=True)
    
    q_img_rel_path = f"{base_rel_path}/q{img_ext}"
    exp_img_rel_path = f"{base_rel_path}/exp{img_ext}"
    
    q_img_abs_path = os.path.join(GATE_ASSETS_DIR, q_img_rel_path)
    exp_img_abs_path = os.path.join(GATE_ASSETS_DIR, exp_img_rel_path)
    
    create_stitched_image(doc, q_data['q_rects'], q_img_abs_path)
    
    has_exp = len(q_data['exp_rects']) > 0
    if has_exp:
        create_stitched_image(doc, q_data['exp_rects'], exp_img_abs_path)
    else:
        exp_img_rel_path = None

    # 3. Determine Type (Simple heuristic based on text)
    q_type = "MCQ" # Default
    if "MSQ" in q_text_full: q_type = "MSQ"
    if "NAT" in q_text_full or "Numerical" in q_text_full: q_type = "NAT"
    
    # 4. Save Text Content to Data JSON
    # No separate .txt files as per new spec
    try:
        import json
        data = {
            "id": q_id_str,
            "stream": stream,
            "packet": packet_id,
            "year": year,
            "type": q_type,
            "key": a_text_full,
            "question_text": q_text_full,
            "answer_text": a_text_full,
            "explanation_text": exp_text_full
        }
        with open(os.path.join(base_abs_path, "data.json"), "w") as f:
            json.dump(data, f, indent=2)
            
    except Exception as e:
        logger.error(f"Failed to write data json for {q_id_str}: {e}")
    logger.info(f"Saved Question {q_id_str}")

def create_stitched_image(doc, rects_info, output_path):
    if not rects_info: return
    
    # Group by page
    pages_map = {}
    for page_num, bbox in rects_info:
        if page_num not in pages_map:
            pages_map[page_num] = {'min_y': bbox[1], 'max_y': bbox[3]}
        else:
            pages_map[page_num]['min_y'] = min(pages_map[page_num]['min_y'], bbox[1])
            pages_map[page_num]['max_y'] = max(pages_map[page_num]['max_y'], bbox[3])
            
    # Extract Textures
    images = []
    for page_num in sorted(pages_map.keys()):
        page = doc[page_num]
        y_min = pages_map[page_num]['min_y']
        y_max = pages_map[page_num]['max_y']
        
        # FULL WIDTH as per spec
        rect = fitz.Rect(0, y_min, page.rect.width, y_max)
        
        # Use configurable zoom level instead of hardcoded 2x
        pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(PDF_ZOOM_LEVEL, PDF_ZOOM_LEVEL))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
        
    # Stitch
    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)
    
    final_img = Image.new('RGB', (max_width, total_height), (255, 255, 255))
    
    y_offset = 0
    for img in images:
        final_img.paste(img, (0, y_offset))
        y_offset += img.height
        
    # Use image optimization module instead of direct save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    optimize_image(
        final_img, 
        output_path, 
        format=IMAGE_FORMAT,
        quality=IMAGE_QUALITY,
        lossless=IMAGE_LOSSLESS
    )

def sync_assets_to_db(con, stream_code):
    """Sync generated assets from filesystem to database."""
    logger.info(f"Syncing assets to DB for {stream_code}")
    
    stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
    # New Path: assets/<stream_alias>/questions/
    assets_base = os.path.join(GATE_ASSETS_DIR, stream_alias, "questions")
    
    if not os.path.exists(assets_base):
        logger.warning(f"No assets found for {stream_code} at {assets_base}")
        return
    
    # Get file extension based on configured format
    img_ext = get_file_extension(IMAGE_FORMAT)
    
    synced_count = 0
    for packet_dir in os.listdir(assets_base):
        packet_path = os.path.join(assets_base, packet_dir)
        if not os.path.isdir(packet_path):
            continue
            
        for q_dir in os.listdir(packet_path):
            q_path = os.path.join(packet_path, q_dir)
            if not os.path.isdir(q_path):
                continue
                
            data_file = os.path.join(q_path, "data.json")
            if not os.path.exists(data_file):
                continue
            
            try:
                import json
                with open(data_file, 'r') as f:
                    data = json.load(f)
                
                # Fetch fields from JSON
                q_text = data.get('question_text', '')
                a_text = data.get('answer_text', '')
                exp_text = data.get('explanation_text', '')
                
                # Construct image paths (relative to frontend assets)
                # Use dynamic extension based on IMAGE_FORMAT
                img_q = f"{stream_alias}/questions/{packet_dir}/{q_dir}/q{img_ext}"
                img_exp = f"{stream_alias}/questions/{packet_dir}/{q_dir}/exp{img_ext}"
                
                # Check if exp image exists
                if not os.path.exists(os.path.join(GATE_ASSETS_DIR, img_exp)):
                    img_exp = None
                
                # Insert into DB
                q_id = data.get('id', q_dir)
                global_id = f"{stream_alias}_{packet_dir}_{q_id}"
                
                con.execute("""
                    INSERT OR REPLACE INTO questions 
                    (id, stream_code, packet_id, question_no, q_type, q_key, q_text, a_text, exp_text, img_path_q, img_path_exp)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (global_id, stream_code, packet_dir, q_id, data.get('type', 'MCQ'), 
                        data.get('key', ''), q_text, a_text, exp_text, img_q, img_exp))
                
                synced_count += 1
                
            except Exception as e:
                logger.error(f"Failed to sync {q_dir}: {e}")
    
    logger.info(f"Synced {synced_count} questions for {stream_code}")

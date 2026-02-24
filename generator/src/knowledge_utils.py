import os
import logging
import json
import re
import glob

from generator.src.config import GATE_ASSETS_DIR, RAW_DATA_DIR, STREAM_ALIASES, DATA_DIR, CLASSIFICATION_BATCH_SIZE
from generator.src.llm_utils import generate_text
from generator.src.text_utils import normalize_subtopic, slugify

logger = logging.getLogger("knowledge_utils")

# Response Directory for LLM Outputs
RESPONSE_DIR = os.path.join(DATA_DIR, "responses")
os.makedirs(RESPONSE_DIR, exist_ok=True)

async def process_classification_prompts(limit=None):
    """Processes classification prompts and saves responses as text files."""
    prompt_dir = os.path.join(DATA_DIR, "prompts")
    
    file_pattern = os.path.join(prompt_dir, "classify_*.txt")
    files = sorted(glob.glob(file_pattern))
    logger.info(f"Found {len(files)} classification prompt files.")
    
    processed_count = 0
    response_files = []
    
    for filepath in files:
        if limit and processed_count >= limit:
            logger.info(f"Reached execution limit of {limit} files.")
            break
            
        logger.info(f"Processing: {filepath}")
        processed_count += 1
        
        with open(filepath, 'r') as f:
            prompt = f.read()

        try:
            # Use functional LLM call
            response = generate_text(prompt)
            
            # Save response to file as JSON
            base_name = os.path.basename(filepath).replace('.txt', '')
            response_file = os.path.join(RESPONSE_DIR, f"{base_name}_response.json")
            
            with open(response_file, 'w') as f:
                f.write(response)
            
            response_files.append(response_file)
            logger.info(f"Saved response to: {response_file}")
                        
        except Exception as e:
            logger.error(f"Failed to process {filepath}: {e}")
    
    return response_files

def _extract_json(text):
    """Helper to extract JSON from text."""
    try:
        start = text.find('{')
        end = text.rfind('}') + 1
        if start != -1 and end != -1:
            json_str = text[start:end]
            # Fix trailing commas
            json_str = re.sub(r',\s*}', '}', json_str)
            json_str = re.sub(r',\s*]', ']', json_str)
            return json_str
        return text
    except:
        return text

def parse_classification_responses(con):
    """Parse classification JSON response files to extract subtopics and populate DB."""
    
    if not os.path.exists(RESPONSE_DIR):
        logger.warning(f"Response directory not found: {RESPONSE_DIR}")
        return
    
    response_files = sorted(glob.glob(os.path.join(RESPONSE_DIR, "classify_*_response.json")))
    logger.info(f"Found {len(response_files)} response files to parse")
    
    stream_subtopics = {}
    question_mappings = []
    
    for response_file in response_files:
        filename = os.path.basename(response_file)
        match = re.search(r'classify_([^_]+)_batch_\d+_response\.json', filename)
        
        if not match:
            logger.warning(f"Could not parse stream from filename: {filename}")
            continue
        
        stream_alias = match.group(1)
        stream_code = None
        for full_code, alias in STREAM_ALIASES.items():
            if alias == stream_alias:
                stream_code = full_code
                break
        if not stream_code:
            if stream_alias in STREAM_ALIASES:
                stream_code = stream_alias
            else:
                logger.warning(f"Unknown stream alias: {stream_alias}")
                continue
        
        if stream_code not in stream_subtopics:
            stream_subtopics[stream_code] = {}
        
        try:
            with open(response_file, 'r') as f:
                content = f.read().strip()
            
            content = _extract_json(content)
            if not content: continue
            
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                if content.count('{') > content.count('}'):
                    content += '}' * (content.count('{') - content.count('}'))
                    try:
                        data = json.loads(content)
                    except:
                        data = None
                else:
                    data = None
            
            if not isinstance(data, dict):
                logger.warning(f"Invalid JSON in {filename}")
                continue
            
            for subject_name, subtopics_dict in data.items():
                if isinstance(subtopics_dict, dict):
                    for subtopic_name, question_ids in subtopics_dict.items():
                        
                        # Remap "Other" or "Unclassifiable" to General Aptitude -> Miscellaneous
                        if subject_name.lower() == "other" or subtopic_name.lower() == "unclassifiable":
                            subject_name = "general aptitude"
                            subtopic_name = "miscellaneous"
                        else:
                            subject_name = normalize_subtopic(subject_name)
                            subtopic_name = normalize_subtopic(subtopic_name)
                        
                        if isinstance(question_ids, list) and len(question_ids) > 0:
                            if subject_name not in stream_subtopics[stream_code]:
                                stream_subtopics[stream_code][subject_name] = []

                            if subtopic_name not in stream_subtopics[stream_code][subject_name]:
                                stream_subtopics[stream_code][subject_name].append(subtopic_name)
                            
                            for q_id in question_ids:
                                q_id = str(q_id).strip()
                                question_mappings.append((q_id, subject_name, subtopic_name, stream_code))

        except Exception as e:
            logger.error(f"Error processing {filename}: {e}")
            continue
    
    subtopic_id_map = {}
    for stream_code, subjects in stream_subtopics.items():
        stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
        subj_idx = 0
        for subject_name, subtopics in subjects.items():
            subj_idx += 1
            subject_id = f"{stream_alias}_subj_{subj_idx}"
            con.execute(
                "INSERT OR REPLACE INTO subjects (id, stream_code, name, order_index) VALUES (?, ?, ?, ?)",
                (subject_id, stream_code, subject_name, subj_idx)
            )
            for topic_idx, subtopic_name in enumerate(subtopics, 1):
                subtopic_id = f"{subject_id}_topic_{topic_idx}"
                con.execute(
                    "INSERT OR REPLACE INTO subtopics (id, subject_id, name, description, order_index) VALUES (?, ?, ?, ?, ?)",
                    (subtopic_id, subject_id, subtopic_name, "", topic_idx)
                )
                subtopic_id_map[(stream_code, subject_name, subtopic_name)] = subtopic_id
    
    updated_count = 0
    for q_id, subject_name, subtopic_name, stream_code in question_mappings:
        subtopic_id = subtopic_id_map.get((stream_code, subject_name, subtopic_name))
        if subtopic_id:
            target_q_id = None
            variants = [q_id, q_id.rstrip('.'), q_id + '.']
            for v in variants:
                if con.execute("SELECT 1 FROM questions WHERE id = ?", (v,)).fetchone():
                    target_q_id = v
                    break
            
            if target_q_id:
                con.execute("UPDATE questions SET subtopic_id = ? WHERE id = ?", (subtopic_id, target_q_id))
                updated_count += 1
    
    logger.info(f"Updated {updated_count} question mappings")

async def process_theory_prompts(con, limit=None):
    """Processes generated theory prompt files."""
    prompt_dir = os.path.join(DATA_DIR, "prompts")
    
    file_pattern = os.path.join(prompt_dir, "theory_*.txt")
    files = sorted(glob.glob(file_pattern))
    logger.info(f"Found {len(files)} theory prompt files.")
    
    processed_count = 0
    for filepath in files:
        if limit and processed_count >= limit:
            logger.info(f"Reached execution limit of {limit} files.")
            break
            
        processed_count += 1
        filename = os.path.basename(filepath)
        subtopic_id = filename[7:-4]
        
        logger.info(f"Processing theory for: {subtopic_id}")
        
        # Fetch Metadata for Export
        meta = con.execute("""
            SELECT 
                s.stream_code,
                s.name as subject_name,
                st.name as subtopic_name
            FROM subtopics st
            JOIN subjects s ON st.subject_id = s.id
            WHERE st.id = ?
        """, (subtopic_id,)).fetchone()
        
        if not meta:
            logger.warning(f"Could not find metadata for {subtopic_id}, skipping export")
            stream_code, subject_name, subtopic_name = (None, None, None)
        else:
            stream_code, subject_name, subtopic_name = meta

        with open(filepath, 'r') as f:
            prompt = f.read()
        
        try:
            content = generate_text(prompt)
            
            if content.startswith('```markdown'):
                content = content.replace('```markdown', '', 1)
            if content.startswith('```'):
                content = content.replace('```', '', 1)
            if content.endswith('```'):
                content = content[:-3]
            
            # Save internal response
            resp_filename = f"theory_{subtopic_id}_response.md"
            resp_path = os.path.join(RESPONSE_DIR, resp_filename)
            
            with open(resp_path, 'w') as f:
                f.write(content)
                
            theory_id = f"theory_{subtopic_id}"
            con.execute(
                "INSERT OR REPLACE INTO theory (id, subtopic_id, content_md) VALUES (?, ?, ?)", 
                (theory_id, subtopic_id, content)
            )
            logger.info(f"Generated theory for {subtopic_id}")
            
            # Export to Frontend Assets
            if stream_code:
                stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
                
                subj_slug = slugify(subject_name, normalize=True)
                topic_slug = slugify(subtopic_name, normalize=True)
                
                target_dir = os.path.join(GATE_ASSETS_DIR, stream_alias, subj_slug)
                os.makedirs(target_dir, exist_ok=True)
                
                target_path = os.path.join(target_dir, f"{topic_slug}.md")
                with open(target_path, 'w') as f:
                    f.write(content)
                logger.info(f"Exported theory to {target_path}")
            
        except Exception as e:
            logger.error(f"Theory generation failed for {filepath}: {e}")

def generate_manifest(con, stream_code):
    """Generates a frontend structure.json for the given stream."""
    
    logger.info(f"Generating manifest for {stream_code}...")
    stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
    
    # 1. Fetch Subjects
    subjects = con.execute("""
        SELECT id, name
        FROM subjects 
        WHERE stream_code = ?
        ORDER BY order_index
    """, (stream_code,)).fetchall()
    
    manifest_data = {
        "stream": stream_alias,
        "stream_code": stream_code,
        "subjects": []
    }
    
    for subj_id, subj_name in subjects:
        subj_entry = {
            "name": subj_name,
            "id": subj_id,
            "slug": slugify(subj_name, normalize=True),
            "topics": []
        }
        
        # 2. Fetch Subtopics
        subtopics = con.execute("""
            SELECT id, name
            FROM subtopics
            WHERE subject_id = ?
            ORDER BY order_index
        """, (subj_id,)).fetchall()
        
        for topic_id, topic_name in subtopics:
            topic_slug = slugify(topic_name, normalize=True)
            
            # 3. Fetch Related Questions
            questions = con.execute("""
                SELECT id 
                FROM questions 
                WHERE subtopic_id = ? 
                ORDER BY id
            """, (topic_id,)).fetchall()
            
            q_ids = [q[0] for q in questions]
            q_list = []
            
            # Transform Question IDs to Paths
            for q_id in q_ids:
                try:
                    parts = q_id.split('_')
                    if len(parts) >= 3:
                        path_stream = parts[0]
                        path_year = parts[1]
                        path_qno = parts[2]
                        
                        q_path = f"questions/{path_year}/{path_qno}/"
                        q_list.append(q_path)
                    else:
                        logger.warning(f"Skipping malformed question ID in manifest: {q_id}")
                except Exception as e:
                    logger.warning(f"Error parsing question ID {q_id}: {e}")

            
            # Path relative to 'assets/<stream>/'
            md_path = f"{slugify(subj_name, normalize=True)}/{topic_slug}.md"
            
            topic_entry = {
                "name": topic_name,
                "id": topic_id,
                "slug": topic_slug,
                "md_path": md_path,
                "questions": q_list
            }
            
            subj_entry["topics"].append(topic_entry)
        
        if subj_entry["topics"]:
                manifest_data["subjects"].append(subj_entry)
                
    # Write to file
    target_dir = os.path.join(GATE_ASSETS_DIR, stream_alias)
    os.makedirs(target_dir, exist_ok=True)
    manifest_path = os.path.join(target_dir, "structure.json")
    
    with open(manifest_path, 'w') as f:
        json.dump(manifest_data, f, indent=2)
        
    logger.info(f"Structure generated at {manifest_path}")
    return manifest_path

import os
import logging
import json
import re
import glob
import asyncio

from generator.src.config import (
    GATE_ASSETS_DIR,
    RAW_DATA_DIR,
    STREAM_ALIASES,
    DATA_DIR,
    CLASSIFICATION_BATCH_SIZE
)

from generator.src.llm_utils import generate_text, process_batch
from generator.src.text_utils import normalize_subtopic, slugify

logger = logging.getLogger("knowledge_utils")

# Response Directory for LLM Outputs
RESPONSE_DIR = os.path.join(DATA_DIR, "responses")
os.makedirs(RESPONSE_DIR, exist_ok=True)


# 🚀 FINAL CLEAN FUNCTION (NO DUPLICATES, NO EXTRA ASYNC WRAPPER)
async def process_classification_prompts(limit=None):
    """Async + Batch processing (CLEAN + STABLE)"""

    prompt_dir = os.path.join(DATA_DIR, "prompts")
    file_pattern = os.path.join(prompt_dir, "classify_*.txt")
    files = sorted(glob.glob(file_pattern))

    logger.info(f"Found {len(files)} classification prompt files.")

    if limit:
        files = files[:limit]

    batch_size = CLASSIFICATION_BATCH_SIZE or 3
    response_files = []

    for i in range(0, len(files), batch_size):
        batch_files = files[i:i + batch_size]

        logger.info(f"Processing batch {i//batch_size + 1}")

        prompts = []
        for filepath in batch_files:
            try:
                with open(filepath, 'r') as f:
                    prompts.append(f.read())
            except Exception as e:
                logger.error(f"Failed to read {filepath}: {e}")
                prompts.append("")

        # 🔥 ASYNC BATCH CALL
        results = await process_batch(prompts)

        # 💾 SAVE RESULTS
        for filepath, response in zip(batch_files, results):
            try:
                content = response or ""

                base_name = os.path.basename(filepath).replace('.txt', '')
                response_file = os.path.join(RESPONSE_DIR, f"{base_name}_response.json")

                with open(response_file, 'w') as f:
                    f.write(content)

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

    except Exception as e:
        logger.warning(f"JSON extraction failed: {e}")
        return text


def parse_classification_responses(con):
    """Parse classification JSON response files to extract subtopics and populate DB."""

    if not os.path.exists(RESPONSE_DIR):
        logger.warning(f"Response directory not found: {RESPONSE_DIR}")
        return

    response_files = sorted(
        glob.glob(os.path.join(RESPONSE_DIR, "classify_*_response.json"))
    )

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

        # 🔥 Resolve stream code
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

            if not content:
                continue

            # 🔥 Parse JSON safely
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                if content.count('{') > content.count('}'):
                    content += '}' * (content.count('{') - content.count('}'))
                    try:
                        data = json.loads(content)
                    except Exception:
                        data = None
                else:
                    data = None

            if not isinstance(data, dict):
                logger.warning(f"Invalid JSON in {filename}")
                continue

            # 🔥 Process data
            for subject_name, subtopics_dict in data.items():
                if isinstance(subtopics_dict, dict):

                    for subtopic_name, question_ids in subtopics_dict.items():

                        # Normalize or remap
                        if subject_name.lower() == "other" or subtopic_name.lower() == "unclassifiable":
                            subject_name = "general aptitude"
                            subtopic_name = "miscellaneous"
                        else:
                            subject_name = normalize_subtopic(subject_name)
                            subtopic_name = normalize_subtopic(subtopic_name)

                        if isinstance(question_ids, list) and question_ids:

                            if subject_name not in stream_subtopics[stream_code]:
                                stream_subtopics[stream_code][subject_name] = []

                            if subtopic_name not in stream_subtopics[stream_code][subject_name]:
                                stream_subtopics[stream_code][subject_name].append(subtopic_name)

                            for q_id in question_ids:
                                q_id = str(q_id).strip()
                                question_mappings.append(
                                    (q_id, subject_name, subtopic_name, stream_code)
                                )

        except Exception as e:
            logger.error(f"Error processing {filename}: {e}")
            continue

    # 🔥 Insert into DB
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

    # 🔥 Map questions
    updated_count = 0

    for q_id, subject_name, subtopic_name, stream_code in question_mappings:
        subtopic_id = subtopic_id_map.get(
            (stream_code, subject_name, subtopic_name)
        )

        if subtopic_id:
            target_q_id = None

            variants = [q_id, q_id.rstrip('.'), q_id + '.']

            for v in variants:
                if con.execute(
                    "SELECT 1 FROM questions WHERE id = ?", (v,)
                ).fetchone():
                    target_q_id = v
                    break

            if target_q_id:
                con.execute(
                    "UPDATE questions SET subtopic_id = ? WHERE id = ?",
                    (subtopic_id, target_q_id)
                )
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

        logger.info(f"[Theory] Processing: {subtopic_id}")

        # 🔍 Fetch metadata
        meta = con.execute("""
            SELECT 
                s.stream_code,
                s.name as subject_name,
                st.name as subtopic_name
            FROM subtopics st
            JOIN subjects s ON st.subject_id = s.id
            WHERE st.id = ?
        """, (subtopic_id,)).fetchone()

        if meta:
            stream_code, subject_name, subtopic_name = meta
        else:
            logger.warning(f"No metadata found for {subtopic_id}")
            stream_code, subject_name, subtopic_name = (None, None, None)

        # 📥 Read prompt
        with open(filepath, 'r', encoding='utf-8') as f:
            prompt = f.read()

        try:
            # 🤖 Generate theory
            content = generate_text(prompt) or ""

            # 🧹 Clean markdown wrappers
            if content.startswith("```markdown"):
                content = content.replace("```markdown", "", 1)
            if content.startswith("```"):
                content = content.replace("```", "", 1)
            if content.endswith("```"):
                content = content[:-3]

            content = content.strip()

            # 💾 Save response file
            resp_filename = f"theory_{subtopic_id}_response.md"
            resp_path = os.path.join(RESPONSE_DIR, resp_filename)

            with open(resp_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # 💾 Save to DB
            theory_id = f"theory_{subtopic_id}"
            con.execute(
                "INSERT OR REPLACE INTO theory (id, subtopic_id, content_md) VALUES (?, ?, ?)",
                (theory_id, subtopic_id, content)
            )

            logger.info(f"[Theory] Saved DB entry for {subtopic_id}")

            # 📤 Export to frontend assets
            if stream_code and subject_name and subtopic_name:
                stream_alias = STREAM_ALIASES.get(stream_code, stream_code)

                subj_slug = slugify(subject_name, normalize=True)
                topic_slug = slugify(subtopic_name, normalize=True)

                target_dir = os.path.join(GATE_ASSETS_DIR, stream_alias, subj_slug)
                os.makedirs(target_dir, exist_ok=True)

                target_path = os.path.join(target_dir, f"{topic_slug}.md")

                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                logger.info(f"[Theory] Exported → {target_path}")

        except Exception as e:
            logger.error(f"[Theory] Failed for {subtopic_id}: {e}", exc_info=True)

def generate_manifest(con, stream_code):
    """Generates a frontend structure.json for the given stream."""

    logger.info(f"[Manifest] Generating for stream: {stream_code}")

    stream_alias = STREAM_ALIASES.get(stream_code, stream_code)

    # 📥 Fetch Subjects
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
        subj_slug = slugify(subj_name, normalize=True)

        subj_entry = {
            "name": subj_name,
            "id": subj_id,
            "slug": subj_slug,
            "topics": []
        }

        # 📥 Fetch Subtopics
        subtopics = con.execute("""
            SELECT id, name
            FROM subtopics
            WHERE subject_id = ?
            ORDER BY order_index
        """, (subj_id,)).fetchall()

        for topic_id, topic_name in subtopics:
            topic_slug = slugify(topic_name, normalize=True)

            # 📥 Fetch Questions
            questions = con.execute("""
                SELECT id 
                FROM questions 
                WHERE subtopic_id = ? 
                ORDER BY id
            """, (topic_id,)).fetchall()

            q_list = []

            for (q_id,) in questions:
                try:
                    parts = q_id.split('_')

                    if len(parts) >= 3:
                        path_year = parts[1]
                        path_qno = parts[2]

                        q_path = f"questions/{path_year}/{path_qno}/"
                        q_list.append(q_path)
                    else:
                        logger.warning(f"[Manifest] Skipping malformed ID: {q_id}")

                except Exception as e:
                    logger.warning(f"[Manifest] Error parsing {q_id}: {e}")

            # 📄 Markdown path
            md_path = f"{subj_slug}/{topic_slug}.md"

            topic_entry = {
                "name": topic_name,
                "id": topic_id,
                "slug": topic_slug,
                "md_path": md_path,
                "questions": q_list
            }

            subj_entry["topics"].append(topic_entry)

        # ✅ Only add subject if it has topics
        if subj_entry["topics"]:
            manifest_data["subjects"].append(subj_entry)

    # 📤 Write JSON file
    target_dir = os.path.join(GATE_ASSETS_DIR, stream_alias)
    os.makedirs(target_dir, exist_ok=True)

    manifest_path = os.path.join(target_dir, "structure.json")

    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)

    logger.info(f"[Manifest] Generated at: {manifest_path}")

    return manifest_path 

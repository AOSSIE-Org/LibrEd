
import os
import json
import shutil
from generator.src.text_utils import normalize_subtopic, slugify

def process_stream_assets(stream_path):
    """
    Cleans up duplicate subtopics in the given stream assets directory.
    Merges duplicates based on normalized names.
    """
    structure_path = os.path.join(stream_path, "structure.json")
    if not os.path.exists(structure_path):
        print(f"Skipping {stream_path} (no structure.json)")
        return

    print(f"Processing {structure_path}...")
    try:
        with open(structure_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {structure_path}: {e}")
        return

    subjects = data.get("subjects", [])
    modified = False


    # Deduplicate and normalize SUBJECTS first
    normalized_subjects = {}
    for subj in subjects:
        raw_name = subj.get("name", "")
        norm_name = normalize_subtopic(raw_name) # Reuse for subjects
        if not norm_name: norm_name = raw_name
        
        if norm_name not in normalized_subjects:
            normalized_subjects[norm_name] = []
        normalized_subjects[norm_name].append(subj)
        
    merged_subjects = []
    subj_idx = 0
    
    # Process each merged subject group
    for norm_subj_name in sorted(normalized_subjects.keys()):
        subj_group = normalized_subjects[norm_subj_name]
        subj_idx += 1
        
        # Determine canonical subject name and slug
        display_subj_name = norm_subj_name.title()
        canonical_subj_slug = slugify(display_subj_name, normalize=True)
        canonical_subj_id = f"subj_{subj_idx}" # Simple ID regen or keep first? Let's regen to be clean
        
        # Note: If we change the subject slug, we must move folders.
        # Check if old slugs differ from new canonical slug
        
        # Merge topics from all subjects in this group
        all_topics = []
        for s in subj_group:
            all_topics.extend(s.get("topics", []))
            
            # If folder rename is needed, we should do it here or handle it during topic processing
            # Best to move all files to the new canonical subject folder
            old_subj_slug = s.get("slug")
            if old_subj_slug and old_subj_slug != canonical_subj_slug:
                 old_dir = os.path.join(stream_path, old_subj_slug)
                 new_dir = os.path.join(stream_path, canonical_subj_slug)
                 
                 # We can't simply move the folder because multiple old folders might map to one new folder
                 # and we need to merge contents.
                 # So we will handle file moves during topic processing.
        
        # Now process topics for this merged subject (Deduplicate topics)
        # Group by normalized topic name
        topic_groups = {}
        for topic in all_topics:
            raw_t_name = topic["name"]
            norm_t_name = normalize_subtopic(raw_t_name)
            if not norm_t_name: norm_t_name = raw_t_name
            
            if norm_t_name not in topic_groups:
                topic_groups[norm_t_name] = []
            topic_groups[norm_t_name].append(topic)
            
        new_topics = []
        topic_count = 0
        
        for norm_t_name in sorted(topic_groups.keys()):
            t_group = topic_groups[norm_t_name]
            topic_count += 1
            display_t_name = norm_t_name.title()
            new_t_slug = slugify(display_t_name, normalize=True)
            
            # Merge questions
            all_questions = set()
            for t in t_group:
                all_questions.update(t.get("questions", []))
            
            # Merge Content & Move Files
            content_parts = []
            files_read = set()
            
            # New file path
            new_rel_path = f"{canonical_subj_slug}/{new_t_slug}.md"
            new_abs_path = os.path.join(stream_path, new_rel_path)
            
            for t in t_group:
                old_rel_path = t.get("md_path")
                if not old_rel_path: continue
                
                old_abs_path = os.path.join(stream_path, old_rel_path)
                
                if os.path.exists(old_abs_path) and old_abs_path not in files_read:
                    try:
                        with open(old_abs_path, 'r') as f:
                            c = f.read()
                            if len(t_group) > 1:
                                content_parts.append(f"<!-- Source: {t['name']} -->\n{c}")
                            else:
                                content_parts.append(c)
                        files_read.add(old_abs_path)
                    except Exception as e:
                        print(f"Error reading {old_abs_path}: {e}")

            merged_content = "\n\n---\n\n".join(content_parts)
            
            os.makedirs(os.path.dirname(new_abs_path), exist_ok=True)
            with open(new_abs_path, 'w') as f:
                f.write(merged_content)
                
            # Cleanup old files
            for t in t_group:
                old_rel_path = t.get("md_path")
                if old_rel_path:
                    old_abs_path = os.path.join(stream_path, old_rel_path)
                    if os.path.abspath(old_abs_path) != os.path.abspath(new_abs_path):
                        if os.path.exists(old_abs_path):
                            try:
                                os.remove(old_abs_path)
                                print(f"Deleted old file: {old_rel_path}")
                            except Exception as e:
                                print(f"Could not delete {old_rel_path}: {e}")
            
            # Create new topic object
            # Warning: IDs might conflict if we just use indices.
            # Ideally IDs should be stable or generic.
            # Using data['stream'] if available or inferring from old ID
            
            stream_alias = data.get("stream", "stream")
            new_subj_id = f"{stream_alias}_subj_{subj_idx}"
            new_topic_id = f"{new_subj_id}_topic_{topic_count}"

            new_topics.append({
                "name": display_t_name,
                "id": new_topic_id,
                "slug": new_t_slug,
                "md_path": new_rel_path,
                "questions": sorted(list(all_questions))
            })
            
            if len(t_group) > 1:
                print(f"Merged {len(t_group)} topics into '{display_t_name}' (Subject: {display_subj_name})")
                modified = True
            elif t_group[0]['name'] != display_t_name:
                 # print(f"Renamed topic '{t_group[0]['name']}' to '{display_t_name}'") # Too verbose
                 modified = True

        # Add merged subject to list
        if len(subj_group) > 1:
            print(f"Merged {len(subj_group)} subjects into '{display_subj_name}'")
            modified = True
        elif subj_group[0]['name'] != display_subj_name:
            print(f"Renamed subject '{subj_group[0]['name']}' to '{display_subj_name}'")
            modified = True
            
        merged_subjects.append({
            "name": display_subj_name,
            "id": f"{data.get('stream', 'stream')}_subj_{subj_idx}",
            "slug": canonical_subj_slug,
            "topics": new_topics
        })
        
        # Cleanup Empty Subject Folders
        for s in subj_group:
            old_slug = s.get("slug")
            if old_slug and old_slug != canonical_subj_slug:
                old_dir = os.path.join(stream_path, old_slug)
                # Check if empty (ignoring hidden files if needed, but os.rmdir fails if not empty)
                if os.path.exists(old_dir):
                    try:
                        os.rmdir(old_dir) # Only removes if empty
                        print(f"Removed empty subject dir: {old_slug}")
                    except OSError:
                        pass # Directory not empty

    data["subjects"] = merged_subjects

    if modified:
        shutil.copy(structure_path, structure_path + ".bak")
        with open(structure_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Updated {structure_path}")
    else:
        print(f"No changes for {structure_path}")

def clean_all_assets(assets_dir):
    if not os.path.exists(assets_dir):
        print(f"Assets directory not found: {assets_dir}")
        return

    streams = [d for d in os.listdir(assets_dir) if os.path.isdir(os.path.join(assets_dir, d))]
    for stream in streams:
        process_stream_assets(os.path.join(assets_dir, stream))

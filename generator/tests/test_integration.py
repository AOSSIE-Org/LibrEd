import pytest
import duckdb
import os
import json
import shutil
from unittest.mock import patch, MagicMock
from generator.src.config import GATE_ASSETS_DIR, DATA_DIR, STREAM_ALIASES
import generator.src.knowledge_utils as knowledge_utils
import generator.src.prompt_utils as prompt_utils
import generator.src.db_utils as db_utils

@pytest.fixture
def mock_db():
    """Create a temporary in-memory DB with seeded data."""
    con = duckdb.connect(':memory:')
    db_utils.init_db(con)
    return con

@pytest.fixture
def clean_assets():
    """Clean up assets dir before and after test."""
    # Setup
    test_assets_dir = os.path.join(os.getcwd(), "test_assets")
    original_assets_dir = GATE_ASSETS_DIR
    
    # Mock config paths for test isolation if needed, 
    # but knowledge_utils imports them. We might need to patch config or use temporary dirs.
    # For simplicity, we'll patch FRONTEND_ASSETS_DIR in knowledge_utils if possible, 
    # or just use a mock output.
    
    yield
    
    # Teardown
    if os.path.exists("test_theory_response.md"):
        os.remove("test_theory_response.md")

@patch('generator.src.knowledge_utils.generate_text')
def test_theory_export_pipeline(mock_generate, mock_db, tmp_path):
    """
    Test the full flow:
    1. DB has classified questions.
    2. generate_theory_prompts creates prompt files.
    3. process_theory_prompts generates markdown.
    4. generate_manifest creates structure.json.
    """
    # 1. Setup Data
    stream_code = 'computer-science-information-technology'
    stream_alias = 'cs'
    subj_id = 'cs_subj_1'
    subtopic_id = 'cs_subj_1_topic_1'
    
    mock_db.execute("INSERT OR IGNORE INTO subjects VALUES (?, ?, 'Math', 1)", (subj_id, stream_code))
    mock_db.execute("INSERT OR IGNORE INTO subtopics VALUES (?, ?, 'Graphs', '', 1)", (subtopic_id, subj_id))
    mock_db.execute("INSERT OR IGNORE INTO questions (id, stream_code, subtopic_id, q_text, a_text) VALUES ('cs_2024_1', ?, ?, 'QText', 'AText')", (stream_code, subtopic_id))

    # Mock LLM Response
    mock_generate.return_value = "# Theory of Graphs\n\nContent here."
    
    # Patch Directories to use tmp_path
    with patch('generator.src.prompt_utils.PROMPT_DIR', str(tmp_path / 'prompts')), \
         patch('generator.src.knowledge_utils.DATA_DIR', str(tmp_path)), \
         patch('generator.src.knowledge_utils.RESPONSE_DIR', str(tmp_path / 'responses')), \
         patch('generator.src.knowledge_utils.GATE_ASSETS_DIR', str(tmp_path / 'assets')), \
         patch('generator.src.knowledge_utils.STREAM_ALIASES', {'computer-science-information-technology': 'cs'}):
        
        os.makedirs(tmp_path / 'prompts', exist_ok=True)
        os.makedirs(tmp_path / 'responses', exist_ok=True)
        os.makedirs(tmp_path / 'assets', exist_ok=True)

        # 2. Generate Prompts
        prompts = prompt_utils.generate_theory_prompts(mock_db, stream_code)
        assert len(prompts) == 1
        assert os.path.exists(prompts[0])
        
        # 3. Process Theory
        # We need an async loop wrapper or just call the logic if it was synchronous. 
        # process_theory_prompts is async.
        import asyncio
        asyncio.run(knowledge_utils.process_theory_prompts(mock_db))
        
        # Verify DB updated
        count = mock_db.execute("SELECT COUNT(*) FROM theory").fetchone()[0]
        assert count == 1
        
        # Verify Asset Export (slugify converts "Graphs" to "graph")
        expected_md = tmp_path / 'assets' / stream_alias / 'math' / 'graph.md'
        assert expected_md.exists()
        with open(expected_md) as f:
            assert "# Theory of Graphs" in f.read()

        # 4. Generate Manifest
        manifest_path = knowledge_utils.generate_manifest(mock_db, stream_code)
        assert os.path.exists(manifest_path)
        
        with open(manifest_path) as f:
            manifest = json.load(f)
            
        assert manifest['stream'] == stream_alias
        assert manifest['subjects'][0]['name'] == 'Math'
        assert manifest['subjects'][0]['topics'][0]['name'] == 'Graphs'
        assert manifest['subjects'][0]['topics'][0]['md_path'] == 'math/graph.md'
        # Check Q Path
        assert "questions/2024/1/" in manifest['subjects'][0]['topics'][0]['questions'][0]

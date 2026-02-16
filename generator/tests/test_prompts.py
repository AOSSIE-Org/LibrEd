import pytest
import duckdb
import os
from unittest.mock import patch, MagicMock
from generator.src.prompt_utils import generate_classification_prompts, generate_theory_prompts
from generator.src.config import STREAM_ALIASES

@pytest.fixture
def mock_db():
    con = duckdb.connect(':memory:')
    con.execute("CREATE TABLE questions (id TEXT, stream_code TEXT, subtopic_id TEXT, q_text TEXT, a_text TEXT)")
    con.execute("CREATE TABLE subjects (id TEXT, stream_code TEXT, name TEXT, order_index INTEGER)")
    con.execute("CREATE TABLE subtopics (id TEXT, subject_id TEXT, name TEXT, description TEXT, order_index INTEGER)")
    return con

@patch('generator.src.prompt_utils._read_syllabus')
def test_generate_classification_prompts(mock_read_syllabus, mock_db):
    """Test classification prompt generation."""
    mock_read_syllabus.return_value = "Mock Syllabus Content"
    stream_code = 'computer-science-information-technology'
    
    # Seed Data
    mock_db.execute("INSERT INTO questions VALUES ('q1', ?, NULL, 'Question 1 Text', 'Answer 1')", (stream_code,))
    
    with patch('builtins.open', new_callable=MagicMock) as mock_open:
        files = generate_classification_prompts(mock_db, stream_code, batch_size=1)
        
        assert len(files) == 1
        assert "classify_cs_batch_0.txt" in files[0]
        
        # Verify content written
        handle = mock_open.return_value.__enter__.return_value
        content = handle.write.call_args[0][0]
        assert "Mock Syllabus Content" in content
        assert "Question 1 Text" in content

def test_generate_theory_prompts(mock_db):
    """Test theory prompt generation."""
    stream_code = 'computer-science-information-technology'
    subj_id = 'cs_subj_1'
    subtopic_id = 'cs_subj_1_topic_1'
    
    # Seed Data
    mock_db.execute("INSERT INTO subjects VALUES (?, ?, 'Math', 1)", (subj_id, stream_code))
    mock_db.execute("INSERT INTO subtopics VALUES (?, ?, 'Graphs', '', 1)", (subtopic_id, subj_id))
    mock_db.execute("INSERT INTO questions VALUES ('q1', ?, ?, 'QText', 'AText')", (stream_code, subtopic_id))
    
    with patch('builtins.open', new_callable=MagicMock) as mock_open:
        files = generate_theory_prompts(mock_db, stream_code)
        
        assert len(files) == 1
        assert f"theory_{subtopic_id}.txt" in files[0]
        
        content = mock_open.return_value.__enter__.return_value.write.call_args[0][0]
        assert "Graphs" in content
        assert "QText" in content

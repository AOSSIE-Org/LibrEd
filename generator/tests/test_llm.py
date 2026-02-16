import pytest
from unittest.mock import patch, MagicMock
from generator.src.llm_utils import generate_text

def test_generate_text_local_success():
    """Test successful generation from local Ollama."""
    mock_response = {
        "response": "Test response content",
        "done": True
    }
    
    with patch('requests.post') as mock_post:
        mock_post.return_value.json.return_value = mock_response
        mock_post.return_value.status_code = 200
        
        result = generate_text("Test Prompt")
        
        assert result == "Test response content"
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        assert kwargs['json']['model'] == 'llama3.1' # Default model

def test_generate_text_local_failure():
    """Test failure path handling."""
    with patch('requests.post') as mock_post:
        # Simulate connection error
        mock_post.side_effect = Exception("Connection refused")
        
        result = generate_text("Test Prompt")
        assert result == ""

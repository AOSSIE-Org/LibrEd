import pytest
import json
from generator.src.knowledge_utils import _extract_json

class TestJsonExtraction:
    def test_clean_json(self):
        """Test extraction of already clean JSON."""
        input_text = '{"key": "value"}'
        assert _extract_json(input_text) == input_text

    def test_surrounding_text(self):
        """Test extraction with text before and after."""
        input_text = """
        Here is the output:
        {
            "key": "value"
        }
        Hope this helps!
        """
        expected = """{
            "key": "value"
        }"""
        assert _extract_json(input_text).strip() == expected.strip()

    def test_markdown_block(self):
        """Test extraction from markdown code blocks."""
        input_text = """
        ```json
        {
            "key": "value"
        }
        ```
        """
        # The function extracts from first { to last }
        expected = """{
            "key": "value"
        }"""
        assert _extract_json(input_text).strip() == expected.strip()

    def test_trailing_comma_object(self):
        """Test fixing trailing comma in object."""
        input_text = '{"key": "value",}'
        expected = '{"key": "value"}'
        assert _extract_json(input_text) == expected
        assert json.loads(_extract_json(input_text)) == {"key": "value"}

    def test_trailing_comma_array(self):
        """Test fixing trailing comma in array."""
        input_text = '{"list": [1, 2,]}'
        expected = '{"list": [1, 2]}'
        assert _extract_json(input_text) == expected
        assert json.loads(_extract_json(input_text)) == {"list": [1, 2]}

    def test_nested_trailing_commas(self):
        """Test fixing multiple trailing commas in nested structures."""
        input_text = """
        {
            "obj": {
                "inner": "val",
            },
            "arr": [
                "item",
            ],
        }
        """
        cleaned = _extract_json(input_text)
        # Verify parsability
        data = json.loads(cleaned)
        assert data["obj"]["inner"] == "val"
        assert len(data["arr"]) == 1

    def test_markdown_no_lang(self):
        """Test markdown block without language specifier."""
        input_text = """
        ```
        {"a": 1}
        ```
        """
        assert json.loads(_extract_json(input_text)) == {"a": 1}

    def test_noisy_llm_response(self):
        """Test a realistic noisy LLM response."""
        input_text = """
        Sure, here is the classification:
        ```json
        {
            "Subject": {
                "Topic": ["id1", "id2"],
            }
        }
        ```
        Let me know if you need changes.
        """
        cleaned = _extract_json(input_text)
        data = json.loads(cleaned)
        assert "id2" in data["Subject"]["Topic"]

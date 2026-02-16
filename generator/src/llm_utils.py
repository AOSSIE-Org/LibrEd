import requests
import logging
from generator.src.config import OLLAMA_MODEL

logger = logging.getLogger(__name__)

def generate_text(prompt, model=None, url_override=None):
    """Generate text from prompt using local Ollama."""
    target_model = model or OLLAMA_MODEL
    
    # Use centralized config unless overridden
    if url_override:
        url = url_override
    else:
        from generator.src.config import OLLAMA_BASE_URL
        url = f"{OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": target_model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": -1,
            "num_ctx": 8192
        }
    }
    
    logger.info(f"Sending request to Ollama (model: {target_model}, prompt length: {len(prompt)} chars)")
    
    try:
        resp = requests.post(url, json=payload, timeout=600)
        resp.raise_for_status()
    except Exception as e:
        logger.error(f"Error calling Ollama at {url}: {e}", exc_info=True)
        return ""

    try:
        data = resp.json()
        response_text = data.get("response", "")
        
        logger.info(f"Received response from Ollama (length: {len(response_text)} chars)")
        logger.info(f"Response done: {data.get('done', False)}")
        
        if not response_text:
            logger.warning(f"Empty response from Ollama. Full data: {data}")
        
        return response_text
    except Exception as e:
        logger.error(f"Error parsing Ollama response: {e}", exc_info=True)
        return ""

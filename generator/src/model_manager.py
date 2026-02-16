"""
Ollama model management utilities.
"""
import requests
import logging
from generator.src.config import OLLAMA_MODEL, OLLAMA_BASE_URL

logger = logging.getLogger(__name__)

def ensure_model_available(model_name=None, ollama_url=None):
    """
    Ensure the specified Ollama model is available, pulling it if necessary.
    
    Args:
        model_name: Model to check/pull (defaults to OLLAMA_MODEL from config)
        ollama_url: Ollama API URL (optional override)
    
    Returns:
        bool: True if model is available, False otherwise
    """
    if model_name is None:
        model_name = OLLAMA_MODEL
    
    # Use centralized config if not provided
    if ollama_url is None:
        from generator.src.config import OLLAMA_BASE_URL
        ollama_url = OLLAMA_BASE_URL

    logger.info(f"Checking if model '{model_name}' is available at {ollama_url}...")
    
    try:
        # Check if model exists
        response = requests.get(f"{ollama_url}/api/tags", timeout=5)
        response.raise_for_status()
        
        models = response.json().get("models", [])
        model_names = [m.get("name") for m in models]
        
        if model_name in model_names:
            logger.info(f"Model '{model_name}' is already available")
            return True
        
        # Model not found, pull it
        logger.info(f"Model '{model_name}' not found. Pulling...")
        pull_response = requests.post(
            f"{ollama_url}/api/pull",
            json={"name": model_name},
            stream=True,
            timeout=600
        )
        pull_response.raise_for_status()
        
        # Stream the pull progress
        for line in pull_response.iter_lines():
            if line:
                logger.info(f"Pull progress: {line.decode('utf-8')}")
        
        logger.info(f"Successfully pulled model '{model_name}'")
        return True
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to ensure model availability at {ollama_url}: {e}")
        return False

def list_available_models(ollama_url=None):
    """
    List all available Ollama models.
    
    Args:
        ollama_url: Ollama API URL (optional override)
    
    Returns:
        list: List of model names
    """
    if ollama_url is None:
        from generator.src.config import OLLAMA_BASE_URL
        ollama_url = OLLAMA_BASE_URL

    try:
        response = requests.get(f"{ollama_url}/api/tags", timeout=5)
        response.raise_for_status()
        
        models = response.json().get("models", [])
        return [m.get("name") for m in models]
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to list models: {e}")
        return []

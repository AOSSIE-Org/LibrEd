import requests
import logging
import asyncio
from functools import partial
from generator.src.config import OLLAMA_MODEL

logger = logging.getLogger(__name__)

# 🔥 Limit concurrency
semaphore = asyncio.Semaphore(5)


def generate_text(prompt, model=None, url_override=None):
    """Generate text from prompt using local Ollama."""
    target_model = model or OLLAMA_MODEL

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

    try:
        resp = requests.post(url, json=payload, timeout=600)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", "")
    except Exception as e:
        logger.error(f"LLM error: {e}", exc_info=True)
        return ""


async def generate_text_async(prompt, model=None, url_override=None):
    loop = asyncio.get_event_loop()
    func = partial(generate_text, prompt, model, url_override)
    return await loop.run_in_executor(None, func)


async def controlled_generate_text(prompt):
    async with semaphore:
        return await generate_text_async(prompt)


async def process_batch(prompts):
    tasks = [controlled_generate_text(p) for p in prompts]
    return await asyncio.gather(*tasks, return_exceptions=True)

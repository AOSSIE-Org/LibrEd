#!/usr/bin/env python3
"""
Test multiple Ollama models side-by-side to compare classification quality.
"""
import asyncio
import os
import sys
import logging
from generator.src.config import DATA_DIR, TARGET_STREAMS, DB_PATH
from generator.src.knowledge_builder import KnowledgeBuilder
from generator.src.prompt_generator import PromptGenerator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Models to test (4-5GB range)
MODELS_TO_TEST = [
    "qwen",
    "llama3.2:latest",  # ~4.7GB
    "mistral:latest",   # ~4.1GB
]

async def test_model(model_name: str, limit: int = 3):
    """Test a single model with the classification task."""
    logger.info(f"=" * 60)
    logger.info(f"TESTING MODEL: {model_name}")
    logger.info(f"=" * 60)
    
    # Initialize knowledge builder with specific model
    kb = KnowledgeBuilder(DB_PATH, model=model_name)
    
    # Process classification prompts
    logger.info(f"Processing {limit} classification prompts with {model_name}...")
    await kb.process_classification_prompts(limit=limit)
    
    # Parse responses
    logger.info(f"Parsing responses from {model_name}...")
    kb.parse_classification_responses()
    
    # Get stats
    subtopic_count = kb.con.execute("SELECT COUNT(*) FROM subtopics").fetchone()[0]
    mapping_count = kb.con.execute("SELECT COUNT(*) FROM questions WHERE subtopic_id IS NOT NULL").fetchone()[0]
    
    logger.info(f"{model_name} Results: {subtopic_count} subtopics, {mapping_count} question mappings")
    
    kb.close()
    
    return {
        "model": model_name,
        "subtopics": subtopic_count,
        "mappings": mapping_count
    }

async def main():
    """Test all models and compare results."""
    logger.info("Starting multi-model comparison test")
    
    # Generate prompts once (shared across all models)
    logger.info("Generating classification prompts...")
    kb_temp = KnowledgeBuilder(DB_PATH)
    pg = PromptGenerator()
    
    for stream in TARGET_STREAMS:
        logger.info(f"Generating prompts for {stream}...")
        pg.generate_classification_prompts(kb_temp.con, stream)
    
    kb_temp.close()
    
    # Test each model
    results = []
    for model in MODELS_TO_TEST:
        try:
            result = await test_model(model, limit=3)
            results.append(result)
        except Exception as e:
            logger.error(f"Failed to test {model}: {e}", exc_info=True)
            results.append({
                "model": model,
                "subtopics": 0,
                "mappings": 0,
                "error": str(e)
            })
    
    # Print comparison
    logger.info("=" * 60)
    logger.info("COMPARISON RESULTS")
    logger.info("=" * 60)
    for result in results:
        if "error" in result:
            logger.info(f"{result['model']}: ERROR - {result['error']}")
        else:
            logger.info(f"{result['model']}: {result['subtopics']} subtopics, {result['mappings']} mappings")
    
    # Recommend best model
    best = max([r for r in results if "error" not in r], key=lambda x: x['mappings'], default=None)
    if best:
        logger.info(f"\nRECOMMENDED MODEL: {best['model']} ({best['mappings']} mappings)")

if __name__ == "__main__":
    asyncio.run(main())

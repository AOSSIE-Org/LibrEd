import duckdb
import os
import logging
from generator.src.config import DB_PATH, STREAM_ALIASES

logger = logging.getLogger("db_utils")

def get_connection():
    """Returns a DuckDB connection."""
    return duckdb.connect(DB_PATH)

def init_db(con):
    """Initializes database schema and seeds seeds."""
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    if os.path.exists(schema_path):
        with open(schema_path, "r") as f:
            con.execute(f.read())
        logger.info("Schema loaded.")
    else:
        logger.error(f"Schema file not found at {schema_path}")

    # Seed Streams
    for code, alias in STREAM_ALIASES.items():
        con.execute("INSERT OR IGNORE INTO streams (code, name) VALUES (?, ?)", (code, code.replace('-', ' ').title()))
    logger.info("Streams seeded.")

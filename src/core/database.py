import os
import logging
from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


def get_database_config():
    """Get database configuration based on environment variables"""
    db_url = os.getenv("DATABASE_URL")

    if db_url and db_url.startswith("postgres://"):
        return {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": os.getenv("DB_HOST", "localhost"),
                        "port": int(os.getenv("DB_PORT", "5432")),
                        "user": os.getenv("DB_USER", "postgres"),
                        "password": os.getenv("DB_PASSWORD", ""),
                        "database": os.getenv("DB_NAME", "nexios"),
                    },
                }
            },
            "apps": {
                "models": {
                    "models": ["src.models", "aerich.models"],
                    "default_connection": "default",
                }
            },
        }
    else:
        # Fallback to SQLite
        logger.info("DATABASE_URL not provided or not PostgreSQL, using SQLite")
        return {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.sqlite",
                    "credentials": {"file_path": "db.sqlite3"},
                }
            },
            "apps": {
                "models": {
                    "models": ["src.models", "aerich.models"],
                    "default_connection": "default",
                }
            },
        }


async def init_db():
    """Initialize Tortoise ORM with logging"""
    try:
        logger.info("Initializing database connection...")
        config = get_database_config()

        if "postgres" in config["connections"]["default"]["engine"]:
            logger.info("Using PostgreSQL database")
        else:
            logger.info("Using SQLite database")

        await Tortoise.init(config=config)
        await Tortoise.generate_schemas()
        logger.info("Database initialized successfully")

    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


async def close_db():
    """Close Tortoise ORM connections with logging"""
    try:
        logger.info("Closing database connections...")
        await Tortoise.close_connections()
        logger.info("Database connections closed successfully")

    except Exception as e:
        logger.error(f"Failed to close database connections: {e}")
        raise


TORTOISE_ORM = get_database_config()

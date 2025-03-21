import os
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

class BaseConfig:
    """Base configuration shared across environments."""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///idea_engine.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_default_key")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    ENV = os.getenv("ENV", "production")

    # Optional: Email/Redis/API Security
    MAIL_SERVER = os.getenv("MAIL_SERVER", "")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True").lower() == "true"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "")

    REDIS_URL = os.getenv("REDIS_URL", "")
    API_RATE_LIMIT = int(os.getenv("API_RATE_LIMIT", 1000))
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*")
    TOKEN_EXPIRY = int(os.getenv("TOKEN_EXPIRY", 3600))


class DevelopmentConfig(BaseConfig):
    """Development environment-specific config."""
    DEBUG = True
    ENV = "development"
    FLASK_ENV = "development"


class ProductionConfig(BaseConfig):
    """Production environment-specific config."""
    DEBUG = False
    ENV = "production"
    FLASK_ENV = "production"


# Default export (you can customize how it's loaded in app.py)
Config = DevelopmentConfig if os.getenv("ENV") == "development" else ProductionConfig


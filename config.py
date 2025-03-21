import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class BaseConfig:
    """Base configuration with defaults."""
    # Core configurations
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///idea_engine.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")

    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    ENV = os.getenv("ENV", "production")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")

    # Email configuration (optional)
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True").lower() == "true"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

    # Redis & Security configurations
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    API_RATE_LIMIT = int(os.getenv("API_RATE_LIMIT", 1000))
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*")
    TOKEN_EXPIRY = int(os.getenv("TOKEN_EXPIRY", 3600))

class DevelopmentConfig(BaseConfig):
    """Development environment-specific configuration."""
    DEBUG = True
    ENV = "development"
    FLASK_ENV = "development"

class ProductionConfig(BaseConfig):
    """Production environment-specific configuration."""
    DEBUG = False
    ENV = "production"
    FLASK_ENV = "production"

# Select configuration based on environment variable
if os.getenv("ENV") == "development":
    Config = DevelopmentConfig
else:
    Config = ProductionConfig



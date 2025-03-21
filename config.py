import os
from dotenv import load_dotenv

# Load variables from .env file if present
load_dotenv()

class Config:
    """Base configuration for the AI Idea Engine app."""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    DATABASE_URL = os.getenv("DATABASE_URL", "idea_engine.db")

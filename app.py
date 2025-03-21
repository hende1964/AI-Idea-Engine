from flask import Flask
import openai
import os
import logging
from config import Config
from routes import routes as main_routes  # Ensure Blueprint is named 'routes' in routes.py

# Initialize Flask App
app = Flask(__name__)

# Load configuration from config.py and .env
app.config.from_object(Config)

# Ensure OpenAI API Key is loaded
openai.api_key = app.config.get('OPENAI_API_KEY')
if not openai.api_key:
    logging.error("❌ ERROR: OpenAI API Key is missing. Check your .env or Railway secrets.")

# Register Blueprints
app.register_blueprint(main_routes)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler("error_log.txt")  # Logs to file
    ]
)

if __name__ == '__main__':
    from waitress import serve

    # Dynamically set port for deployment (Railway uses dynamic port)
    port = int(os.getenv("PORT", 8080))  # Adjusted to 8080 for Railway
    logging.info(f"🚀 AI Idea Engine starting on http://0.0.0.0:{port}")
    
    try:
        serve(app, host='0.0.0.0', port=port)
    except Exception as e:
        logging.error(f"❌ Failed to start server: {e}")








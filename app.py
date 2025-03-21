from flask import Flask, jsonify
import openai
import os
import logging
from config import Config
from routes import routes as main_routes
from waitress import serve

# Initialize Flask Application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Securely load OpenAI API Key
openai.api_key = app.config.get("OPENAI_API_KEY")

# Validate API key availability
if not openai.api_key:
    logging.error("❌ ERROR: OpenAI API Key is missing. Check your .env or Railway secrets.")

# Register Blueprint routes
app.register_blueprint(main_routes)

# Configure logging for both console and file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("error_log.txt", mode="a")
    ]
)

# Health-check endpoint for deployment validation
@app.route("/health")
def health_check():
    return jsonify({"status": "✅ Server is running"}), 200

# Launch server (Railway-compatible port setup)
if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))  # Use Railway's dynamically assigned port
    logging.info(f"🚀 AI Idea Engine launching at http://0.0.0.0:{port}")

    try:
        serve(app, host='0.0.0.0', port=port)
    except Exception as e:
        logging.error(f"❌ Server startup failed: {e}")





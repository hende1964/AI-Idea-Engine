from flask import Flask, jsonify
import openai
import os
import logging
from config import Config
from routes import routes as main_routes
from waitress import serve

# Initialize Flask App
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Securely load OpenAI API key
openai.api_key = app.config.get('OPENAI_API_KEY')
if not openai.api_key:
    logging.error("❌ OpenAI API Key is missing. Check your .env or Railway secrets.")
else:
    logging.info("✅ OpenAI API Key loaded successfully.")

# Register Blueprint
app.register_blueprint(main_routes)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("error_log.txt", mode="a")
    ]
)

# Health check (optional)
@app.route("/health")
def health_check():
    return jsonify({"status": "Server is running"}), 200

# Run app using waitress (production-ready)
if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    logging.info(f"🚀 AI Idea Engine launching at http://0.0.0.0:{port}")
    try:
        serve(app, host="0.0.0.0", port=port)
    except Exception as e:
        logging.error(f"❌ Server failed to start: {e}")









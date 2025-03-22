from flask import Flask, jsonify
import openai
import os
import logging
from config import Config
from routes import routes as main_routes
from waitress import serve

# Initialize Flask application
app = Flask(__name__)

# Load app configuration from Config object
app.config.from_object(Config)

# Set OpenAI API key securely from configuration
openai.api_key = app.config.get('OPENAI_API_KEY')
if not openai.api_key:
    logging.error("❌ ERROR: OpenAI API Key is missing. Check .env or Railway secrets.")
else:
    logging.info("✅ OpenAI API Key successfully loaded.")

# Register blueprints
app.register_blueprint(main_routes)

# Setup logging (console and persistent file)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("error_log.txt", mode='a')
    ]
)

# Health check endpoint (used by Railway)
@app.route("/health")
def health_check():
    return jsonify({"status": "✅ Server is running"}), 200

# Entry point for production server using Waitress
if __name__ == '__main__':
    try:
        port = int(os.getenv("PORT", 8080))  # Default fallback
        logging.info(f"🚀 AI Idea Engine launching at http://0.0.0.0:{port}")
        serve(app, host='0.0.0.0', port=port)
    except Exception as e:
        logging.error(f"❌ Failed to start server: {e}")






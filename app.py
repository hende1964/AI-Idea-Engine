from flask import Flask, jsonify
import openai
import os
import logging
from config import Config
from routes import routes as main_routes
from waitress import serve

# Initialize Flask application
app = Flask(__name__)

# Load configuration from .env or Railway variables
app.config.from_object(Config)

# Setup logging (console and persistent file)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("error_log.txt", mode='a')
    ]
)

# Load OpenAI API key securely
openai.api_key = app.config.get("OPENAI_API_KEY")
if not openai.api_key:
    logging.error("❌ ERROR: OpenAI API Key is missing. Check Railway or .env.")
else:
    logging.info("✅ OpenAI API Key successfully loaded.")

# Register routes
app.register_blueprint(main_routes)

# Health check for Railway
@app.route("/health")
def health_check():
    return jsonify({"status": "✅ Server is running"}), 200

# Run app using Waitress
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    logging.info(f"🚀 Launching AI Idea Engine on http://0.0.0.0:{port}")
    try:
        serve(app, host='0.0.0.0', port=port)
    except Exception as e:
        logging.error(f"❌ Failed to start server: {e}")








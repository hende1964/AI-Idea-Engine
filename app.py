from flask import Flask, render_template, request, jsonify
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

# Securely load the OpenAI API Key
openai.api_key = app.config.get('OPENAI_API_KEY')
if not openai.api_key:
    logging.error("ERROR: OpenAI API Key is missing. Check your .env or Railway secrets.")

# Register Blueprints
app.register_blueprint(main_routes)

# Configure logging without emojis (console and file logging)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler("error_log.txt")  # Logs to file
    ]
)

# Simple health check route
@app.route("/health")
def health_check():
    return jsonify({"status": "Server is running"}), 200

if __name__ == '__main__':
    # Dynamically set the port for Railway
    port = int(os.getenv("PORT", 8080))
    logging.info(f"AI Idea Engine launching at http://0.0.0.0:{port}")

    try:
        serve(app, host='0.0.0.0', port=port)
    except Exception as e:
        logging.error(f"Failed to start server: {e}")





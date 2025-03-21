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

# Set OpenAI API Key
openai.api_key = app.config['OPENAI_API_KEY']

# Register Blueprints
app.register_blueprint(main_routes)

# Set up basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == '__main__':
    from waitress import serve

    # Set port for deployment (e.g., Railway uses dynamic port)
    port = int(os.getenv("PORT", 5000))
    logging.info(f"🚀 Launching AI Idea Engine on port {port}...")
    serve(app, host='0.0.0.0', port=port)







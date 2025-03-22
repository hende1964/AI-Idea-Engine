from flask import Flask, jsonify
import openai
import os
<<<<<<< HEAD
import logging
from config import Config
from routes import routes as main_routes
=======
>>>>>>> 6ad74a8 (Forced rebuild)
from waitress import serve

# Initialize Flask application
app = Flask(__name__)

<<<<<<< HEAD
# Load app configuration from Config object
app.config.from_object(Config)
=======
# Securely get the OpenAI API Key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
>>>>>>> 6ad74a8 (Forced rebuild)

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

<<<<<<< HEAD
# Health check endpoint (used by Railway)
@app.route("/health")
def health_check():
    return jsonify({"status": "✅ Server is running"}), 200
=======
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative AI assistant."},
                {"role": "user", "content": prompt}
            ],
            stream=True  # Enables OpenAI's streaming response
        )

        # Streaming response
        def generate():
            for chunk in response:
                if "content" in chunk["choices"][0]["message"]:
                    yield chunk["choices"][0]["message"]["content"]

        return app.response_class(generate(), mimetype='text/plain')

    except Exception as e:
        return jsonify({'error': str(e)}), 500
>>>>>>> 6ad74a8 (Forced rebuild)

# Entry point for production server using Waitress
if __name__ == '__main__':
<<<<<<< HEAD
    try:
        port = int(os.getenv("PORT", 8080))  # Default fallback
        logging.info(f"🚀 AI Idea Engine launching at http://0.0.0.0:{port}")
        serve(app, host='0.0.0.0', port=port)
    except Exception as e:
        logging.error(f"❌ Failed to start server: {e}")
=======
    # Ensure Flask runs on Railway's provided port dynamically
    port = int(os.environ.get("PORT", 8080))  # Defaults to 8080 if Railway doesn't provide a port
    serve(app, host='0.0.0.0', port=port)
>>>>>>> 6ad74a8 (Forced rebuild)






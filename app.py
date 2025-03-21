<<<<<<< HEAD
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


=======
from flask import Flask, render_template, request, jsonify
import openai
import os
from waitress import serve

app = Flask(__name__)

# Securely get the OpenAI API Key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-idea', methods=['POST'])
def generate_idea():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

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

if __name__ == '__main__':
    # Ensure Flask runs on Railway's provided port dynamically
    port = int(os.environ.get("PORT", 8080))  # Defaults to 8080 if Railway doesn't provide a port
    serve(app, host='0.0.0.0', port=port)
>>>>>>> 6ad74a83fa7a74c219f6f25392b7bfcb9942cdf9






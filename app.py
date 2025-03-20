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






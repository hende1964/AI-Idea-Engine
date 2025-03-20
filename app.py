from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set OpenAI API Key securely from environment variable
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
            ]
        )
        idea = response.choices[0].message['content'].strip()

        return jsonify({'idea': idea})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)





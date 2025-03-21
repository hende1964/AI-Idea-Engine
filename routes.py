from flask import Blueprint, request, jsonify, render_template
import openai
import os
from database import insert_idea, get_all_ideas

# Define Blueprint with a clear name
main_routes = Blueprint('main_routes', __name__)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@main_routes.route('/')
def home():
    """Render the homepage with the index template."""
    return render_template('index.html')

@main_routes.route('/generate-idea', methods=['POST'])
def generate_idea():
    """Generate an AI idea based on user input."""
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

        # Save idea to the database
        insert_idea(prompt, idea)

        return jsonify({'idea': idea})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_routes.route('/ideas', methods=['GET'])
def fetch_ideas():
    """Fetch all stored ideas from the database."""
    try:
        ideas = get_all_ideas()
        return jsonify({'ideas': ideas})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


from flask import Blueprint, request, jsonify, render_template
import openai
import os
from database import insert_idea, get_all_ideas
import logging

# Define Blueprint clearly
routes = Blueprint('routes', __name__)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    logging.error("❌ OpenAI API key is missing. Check your .env file.")

@routes.route('/')
def home():
    """Render the homepage with the index template."""
    return render_template('index.html')

@routes.route('/generate-idea', methods=['POST'])
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

    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API error: {e}")
        return jsonify({'error': 'OpenAI API error occurred.'}), 500

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'Unexpected server error.'}), 500

@routes.route('/ideas', methods=['GET'])
def fetch_ideas():
    """Fetch all stored ideas from the database."""
    try:
        ideas = get_all_ideas()
        return jsonify({'ideas': ideas})
    except Exception as e:
        logging.error(f"Database retrieval error: {e}")
        return jsonify({'error': 'Failed to retrieve ideas from the database.'}), 500


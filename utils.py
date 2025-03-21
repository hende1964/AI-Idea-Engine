import re
import json

def clean_text(text):
    """Removes extra spaces, special characters, and standardizes text format."""
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^\w\s,.!?]', '', text)  # Remove special characters except punctuation
    return text

def format_response(idea):
    """Formats the AI-generated response into a structured JSON output."""
    return json.dumps({"idea": idea}, indent=2)

def validate_prompt(prompt):
    """Ensures the prompt is not empty and meets minimum length requirements."""
    if not prompt or len(prompt) < 5:
        return False, "Prompt must be at least 5 characters long."
    return True, None

if __name__ == "__main__":
    # Example Usage
    sample_prompt = "   What are some startup ideas?  "
    cleaned_prompt = clean_text(sample_prompt)
    is_valid, error_msg = validate_prompt(cleaned_prompt)
    
    if is_valid:
        print(f"Validated Prompt: {cleaned_prompt}")
    else:
        print(f"Error: {error_msg}")

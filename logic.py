# ai_engine/logic.py

def build_prompt(user_input):
    return f"User prompt: {user_input}\nNow generate a unique, creative idea from this."

def parse_response(response):
    return response.strip()

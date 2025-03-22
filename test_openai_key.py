import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env vars

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    print("Testing OpenAI API key...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say hello."}]
    )
    print("✅ OpenAI is working:", response['choices'][0]['message']['content'])

except Exception as e:
    print("❌ Error:", e)




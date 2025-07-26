import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_emotion(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # make sure this is correct
            messages=[
                {"role": "system", "content": "You are an emotion detection assistant."},
                {"role": "user", "content": f"What is the emotion behind this text: '{text}'?"}
            ],
            temperature=0.5
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("❌ Error from OpenAI API:", e)
        return "Error"

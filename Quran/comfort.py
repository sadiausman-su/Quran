import requests

def generate_comfort(text, emotion):
    prompt = f"""
    A person is feeling {emotion} and wrote the following journal entry:

    "{text}"

    Please respond with a short, gentle, comforting message inspired by Islamic values.
    """
    payload = {
        "model": "mistral-7b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    headers = {
        "Authorization": "Bearer YOUR_OPENROUTER_API_KEY"
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
    return response.json()['choices'][0]['message']['content'].strip()

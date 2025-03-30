import os
import requests

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def generate_image(prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {"Authorization": f"Token {REPLICATE_API_TOKEN}"}
    payload = {
        "version": "your-model-version-id",  # Replace with actual model ID
        "input": {
            "prompt": prompt
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

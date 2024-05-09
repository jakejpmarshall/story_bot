import requests
from os import getenv

API_TOKEN = getenv('API_TOKEN')
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom-1b7"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "Can you please let us know more details about your ",
})

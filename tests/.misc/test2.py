import os
import requests
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base_dir, ".source", ".env")

load_dotenv(dotenv_path=env_path)

url = os.getenv("NINJA_AUTH_API_ENDPOINT")
payload = {
    "grant_type": "client_credentials",
    "client_id": os.getenv("NINJA_CLIENT_ID"),
    "client_secret": os.getenv("NINJA_CLIENT_SECRET"),
    "scope": "monitoring"
}

resp = requests.post(url, data=payload)
print(resp.json())

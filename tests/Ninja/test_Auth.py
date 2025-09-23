import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".source" / "vars.env"
load_dotenv(dotenv_path=env_path)

url = os.getenv("NINJA_AUTH_ENDPOINT")
payload = {
    "grant_type": "client_credentials",
    "client_id": os.getenv("NINJA_CLIENT_ID"),
    "client_secret": os.getenv("NINJA_CLIENT_SECRET"),
    "scope": "monitoring"
}

try:
    resp = requests.post(url, data=payload)
    resp = resp.json()
    print(f'Access token is: {resp["access_token"]}')
    print(f'TTL is: {resp["expires_in"]}')
    print(f'Scope is: {resp["scope"]}')
    print(f'Token Type is: {resp["token_type"]}')
except ValueError:
    print(f'Failed to validate. Review Code.')
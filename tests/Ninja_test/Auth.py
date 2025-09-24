import os
import requests
from dotenv import load_dotenv
from pathlib import Path

def get_auth():
    try:
        env_path = Path(__file__).resolve().parent.parent.parent / ".source" / ".env"
        load_dotenv(dotenv_path=env_path)
        url = os.getenv("NINJA_AUTH_ENDPOINT")
        payload = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("NINJA_CLIENT_ID"),
            "client_secret": os.getenv("NINJA_CLIENT_SECRET"),
            "scope": "monitoring"
        }
        
        resp = requests.post(url, data=payload)
        resp.raise_for_status()
        resp = resp.json()
        
        authData = {
            "authToken": resp.get("access_token"),
            "ttl": resp.get("expires_in"),
            "scope": resp.get("scope"),
            "tokenType": resp.get("token_type")
        }
        
        if not authData["authToken"]:
            print("No access token given.")
            return None

        return authData
    except (ValueError, requests.exceptions.RequestException) as e:
        print(f'Failed to validate, review code: {e}')
        return None
    
if __name__ == "__main__":
    authData = get_auth()
    if not authData["authToken"]:
        print("No access token given.")
    else:
        print(f'Authentication Token is: {authData["authToken"]}')
        print(f'TTL is: {authData["ttl"]}')
        print(f'Scope is: {authData["scope"]}')
        print(f'Token Type is: {authData["tokenType"]}')
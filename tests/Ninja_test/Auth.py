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
        
        auth_Data = {
            "auth_Token": resp.get("access_token"),
            "ttl": resp.get("expires_in"),
            "scope": resp.get("scope"),
            "token_Type": resp.get("token_type")
        }
        
        if not auth_Data["auth_Token"]:
            print("No access token given.")
            return None

        return auth_Data
    except (ValueError, requests.exceptions.RequestException) as e:
        print(f'Failed to validate, review code: {e}')
        return None
    
if __name__ == "__main__":
    auth_Data = get_auth()
    if not auth_Data["auth_Token"]:
        print("No access token given.")
    else:
        print(f'Authentication Token is: {auth_Data["auth_Token"]}')
        print(f'TTL is: {auth_Data["ttl"]}')
        print(f'Scope is: {auth_Data["scope"]}')
        print(f'Token Type is: {auth_Data["token_type"]}')
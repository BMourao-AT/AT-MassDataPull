import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".source" / "vars.env" # Resolve path to ../.source/.env relative to this file
load_dotenv(dotenv_path=env_path)

base_url = os.getenv("NINJA_BASE_URL")

# get 
def get_auth():
    auth_url = os.getenv("NINJA_AUTH_ENDPOINT")
    payload = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("NINJA_CLIENT_ID"),
        "client_secret": os.getenv("NINJA_CLIENT_SECRET"),
        "scope": "monitoring"
    }
    resp = requests.post(auth_url, data=payload)
    resp = resp.json()
    auth_Data = {
            "auth_Token": resp.get("access_token"),
            "ttl": resp.get("expires_in"),
            "scope": resp.get("scope"),
            "token_Type": resp.get("token_type")
        }
    return auth_Data

# Get orgs
def get_orgs(auth_Token):   
    endpoint = os.getenv("NINJA_ORGS_ENDPOINT")
    url = f'{base_url}{endpoint}'
    
    headers = {
        "Authorization": f'Bearer {auth_Token}',
        "Accept": "application/json"
    }
    
    resp = requests.get(url, headers=headers)
    orgData = resp.json()
    return orgData

# Get devices
def get_devices(auth_Token):
    devs = ''
    return devs

# main program
auth_key = get_auth()
print(auth_key)
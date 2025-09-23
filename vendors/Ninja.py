import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".source" / "vars.env" # Resolve path to ../.source/.env relative to this file
load_dotenv(dotenv_path=env_path)

base_url = os.getenv("NINJA_BASE_URL")

# Function for authentication
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
    auth_key = resp["access_token"] # auth key given to the session
    return auth_key

# Get orgs
def get_orgs(auth_key):
    endpoint = os.getenv("NINJA_ORGS_ENDPOINT")
    url = f'{base_url}{endpoint}'
    headers = {
        "Authorization": f'Bearer {auth_key}',
        "Accept": "application/json"
    }
    resp = requests.get(url, headers=headers)
    orgs = resp.json()    
    return orgs

# Get devices
def get_devices(auth_key):
    devs = ''
    return devs

# main program
auth_key = get_auth()
print(auth_key)

orgs_list = get_orgs(auth_key)
for org in orgs_list:
    print(f'Organization Name: {org["name"]}')
#devs = get_devices(auth_key)

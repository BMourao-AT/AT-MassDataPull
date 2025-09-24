import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# get 
def get_auth(envData):
    auth_url = envData.get("NINJA_AUTH_ENDPOINT")
    payload = {
        "grant_type": "client_credentials",
        "client_id": envData.get("NINJA_CLIENT_ID"),
        "client_secret": envData.get("NINJA_CLIENT_SECRET"),
        "scope": "monitoring"
    }
    resp = requests.post(auth_url, data=payload)
    resp = resp.json()
    authData = {
            "authToken": resp.get("access_token"),
            "ttl": resp.get("expires_in"),
            "scope": resp.get("scope"),
            "tokenType": resp.get("token_type")
        }
    return authData

# Get orgs
def get_orgs(envData, baseURL, authToken):   
    endpoint = envData.get("NINJA_ORGS_ENDPOINT")
    url = f'{baseURL}{endpoint}'
    
    headers = {
        "Authorization": f'Bearer {authToken}',
        "Accept": "application/json"
    }
    
    resp = requests.get(url, headers=headers)
    orgData = resp.json()
    return orgData

# Get devices
def get_devices(envData, baseURL, authToken):   
    endpoint = envData.get("NINJA_DEVICES_ENDPOINT")
    url = f'{baseURL}{endpoint}'
    
    headers = {
        "Authorization": f'Bearer {authToken}',
        "Accept": "application/json"
    }
    
    resp = requests.get(url, headers=headers)
    deviceData = resp.json()
    return deviceData

# main program
if __name__ == "__main__":
    path_env = Path(__file__).resolve().parent.parent / ".source" / ".env" # Resolve path to ../.source/.env relative to this file
    load_dotenv(dotenv_path=path_env)
    envData = dict(os.environ)
    
    authData = get_auth(envData)
    authToken = authData["authToken"]
    
    print(get_devices(envData=envData, baseURL=envData.get("NINJA_BASE_URL"), authToken=authToken))
import os
import requests
from dotenv import load_dotenv

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
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

import Auth

def get_devices(authToken):   
    env_path = Path(__file__).resolve().parent.parent.parent / ".source" / ".env"
    load_dotenv(dotenv_path=env_path)
    baseURL = os.getenv("NINJA_BASE_URL")
    endpoint = os.getenv("NINJA_DEVICES_ENDPOINT")
    url = f'{baseURL}{endpoint}'
    
    headers = {
        "Authorization": f'Bearer {authToken}',
        "Accept": "application/json"
    }
    
    resp = requests.get(url, headers=headers)
    deviceData = resp.json()
    return deviceData

if __name__ == "__main__":
    authData = Auth.get_auth()
    if not authData["authToken"]:
        print("No access token given. Result: ")
        print(authData)
    else:
        print('Auth token retrieved. Passing...')
        print("Grabbing devices data...")
        devData = get_devices(authData["authToken"])
        sortby_Name = sorted(devData, key=lambda x: x["systemName"])
        sortby_Org = sorted(devData, key=lambda x: (x["organizationId"], x["systemName"]))
        
        print(f"DONE! Total devices: {len(devData)}")
        adminPrompt = -1
        while adminPrompt != 0:
            print("Select one of the viewing options: ")
            print("1: Raw - Sorted")
            print("2: Names only - Sorted")
            print("3: Sorted by Organization - Names Only")
            print("0: Exit")
            adminPrompt = int(input("Enter a viewing option: "))
            match adminPrompt:
                case 0:
                    break
                case 1:
                    print('========== List of sorted devices (Raw) ==========')
                    for num, device in enumerate(devData, start=1):
                        print(f'Device {num}: {device}')
                    print("====================== END =======================")
                case 2:
                    print('========= List of sorted devices (Name) ==========')
                    for num, device in enumerate(sortby_Name, start=1):
                        print(f'{num}: {device["systemName"]}')
                    print("====================== END =======================")
                case 3:
                    print('========== List of sorted devices (Org) ==========')
                    for num, device in enumerate(sortby_Org, start=1):
                            print(f'{num}: {device["systemName"]}')
                    print("====================== END =======================")
                case 99:
                    for num, device in enumerate(devData, start=1):
                        print(f'Device {num}: {device}')
                        break
                case _:
                    print("Invalid choice.")
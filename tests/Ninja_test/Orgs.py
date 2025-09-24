import os
import requests
from dotenv import load_dotenv
from pathlib import Path

import Auth

def get_orgs(authToken):
    env_path = Path(__file__).resolve().parent.parent.parent / ".source" / ".env"
    load_dotenv(dotenv_path=env_path)
    baseURL = os.getenv("NINJA_BASE_URL")
    endpoint = os.getenv("NINJA_ORGS_ENDPOINT")
    url = f'{baseURL}{endpoint}'
    
    headers = {
        "Authorization": f'Bearer {authToken}',
        "Accept": "application/json"
    }
    
    resp = requests.get(url, headers=headers)
    orgData = resp.json() 
    return orgData

if __name__ == "__main__":
    authData = Auth.get_auth()
    if not authData["authToken"]:
        print("No access token given. Result: ")
        print(authData)
    else:
        print('Auth token retrieved. Passing...')
        print("Grabbing org data...")
        
        orgData = get_orgs(authData["authToken"])
        sortedOrgs = sorted(orgData, key=lambda x: x["name"])
        print(f"DONE! Total organizations: {len(orgData)}")
        adminPrompt = -1
        while adminPrompt != 0:
            print("Select one of the viewing options: ")
            print("1: Raw - Sorted")
            print("2: Names only - Sorted")
            print("0: Exit")
            adminPrompt = int(input("Enter a viewing option: "))
            match adminPrompt:
                case 0:
                    break
                case 1:
                    print('======= List of sorted Organizations (Raw) =======')
                    for num, org in enumerate(sortedOrgs, start=1):
                        print(f'{num}: {org}')
                    print("====================== END =======================")
                case 2:
                    print('====== List of sorted Organizations (Names) ======')
                    for num, org in enumerate(sortedOrgs, start=1):
                        print(f'{num}: {org["name"]}')
                    print("====================== END =======================")
                case 99:
                    for num, org in enumerate(orgData, start=1):
                        print(f'Org {num}: {org}')
                        break
                case _:
                    print("Invalid choice.")
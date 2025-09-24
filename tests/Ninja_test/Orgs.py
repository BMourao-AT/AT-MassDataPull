import os
import requests
from dotenv import load_dotenv
from pathlib import Path

import Auth

def get_orgs(auth_Token):
    env_path = Path(__file__).resolve().parent.parent.parent / ".source" / ".env"
    load_dotenv(dotenv_path=env_path)
    base_url = os.getenv("NINJA_BASE_URL")
    endpoint = os.getenv("NINJA_ORGS_ENDPOINT")
    url = f'{base_url}{endpoint}'
    
    headers = {
        "Authorization": f'Bearer {auth_Token}',
        "Accept": "application/json"
    }
    
    resp = requests.get(url, headers=headers)
    orgs = resp.json() 
    return orgs

if __name__ == "__main__":
    auth_Data = Auth.get_auth()
    if not auth_Data["auth_Token"]:
        print("No access token given.")
    else:
        print(f'Auth token retrieved. Passing...')
        print("Grabbing org data...")
        orgData = sorted(get_orgs(auth_Data["auth_Token"]), key=lambda x: x["name"])
        sortedOrgs = sorted(orgData, key=lambda x: x["name"])
        
        print(f"DONE! Total organizations: {len(orgData)}")
        adminPrompt = -1
        while adminPrompt != 0:
            print("Select one of the viewing options: ")
            print("1: Raw")
            print("2: Names only - Alphabetical")
            print("0: Exit")
            adminPrompt = int(input("Enter a viewing option: "))
            match adminPrompt:
                case 0:
                    break
                case 1:
                    for num, org in enumerate(orgData, start=1):
                        print(f'{num}: {org}')
                case 2:
                    print('====== List of alphabetized orgs ======')
                    for num, org in enumerate(sortedOrgs, start=1):
                        print(f'{num}: {org["name"]}')
                    print("================= END =================")
                case _:
                    print("Invalid choice.")
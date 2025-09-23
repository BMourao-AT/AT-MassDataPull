import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# import custom functions
import validation
from vendors import Cove
from vendors import Ninja
from vendors import O365
from vendors import ScreenConnect
from vendors import SentinelOne

# Prompt to add users to the email delivery list
def mail_distro():
    dist_path = Path(__file__).resolve().parent / ".source" / "distribution.txt"
    with open(dist_path, "r", encoding="utf-8") as f:
        content = f.read()
    send_to = [address.strip() for address in content.split(";") if address.strip()]
    
    print(f'Currently, SMTP alerts are set up to go to {os.getenv("TO_EMAIL_ADDRESS")} by default along with:')
    for num, em_address in enumerate(send_to, start=1):
        print(f'{num}. {em_address}')

    add_more = input("Would you like to add more? (Y/N): ")
    while add_more not in ["Y" or "y" or "N" or "n"]:
        add_more = input("Invalid input. Try again. (Y/N): ")
    if add_more == "Y" or "y":
        while True:
            new_address = input('Add another address: (press enter when finished): ')
            if new_address == "":
                break
            with open(".source/distribution.txt", "a", encoding="utf-8") as new_distro:
                new_distro.write(f"{new_address};\n")
    return

# Cove
coveAuth = Cove.get_auth()


# Ninja
ninjaAuth = Ninja.get_auth() # this returns a dictionary


# O365
O365Auth = O365.get_auth()


# ScreenConnect
screenconnectAuth = ScreenConnect.get_auth()


# SentinelOne
sentintelAuth = SentinelOne.get_auth()


# main script
if __name__ == "__main__":
    # fill
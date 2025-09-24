import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# import custom functions
import validation
import sendMail
from vendors import Cove
from vendors import Ninja
from vendors import O365
from vendors import ScreenConnect
from vendors import SentinelOne

# Load the .env file
path_env = Path(__file__).resolve().parent.parent / ".source" / "vars.env" # Resolve path to ../.source/.env relative to this file
load_dotenv(dotenv_path=path_env)
envData = dict(os.environ)

# Cove
coveAuth = Cove.get_auth()


# Ninja
ninjaURL = os.getenv("NINJA_BASE_URL")
ninjaAuthData = Ninja.get_auth(envData)
ninjaToken = ninjaAuthData["access_token"]

Ninja.get_orgs(envData, ninjaURL, ninjaToken)
Ninja.get_devices(envData, ninjaURL)


# O365
O365Auth = O365.get_auth()


# ScreenConnect
screenconnectAuth = ScreenConnect.get_auth()


# SentinelOne
sentintelAuth = SentinelOne.get_auth()


# main script
if __name__ == "__main__":
    validation.check_Logs()
    validation.check_Source()
    validation.check_Vendors()
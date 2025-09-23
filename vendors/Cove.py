import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".source" / "vars.env" # Resolve path to ../.source/.env relative to this file
load_dotenv(dotenv_path=env_path)

def get_auth():
    return
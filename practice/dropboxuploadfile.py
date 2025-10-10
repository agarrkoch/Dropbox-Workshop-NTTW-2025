#!/usr/bin/env python3

import requests
import json
import os

KEYS_JSON_PATH = os.path.join(os.path.dirname(__file__), "dropbox_keys.json")
APP_KEY = ''
APP_SECRET = ''
REFRESH_TOKEN = ''
ACCESS_TOKEN = ''

def load_keys():
    global APP_KEY, APP_SECRET, REFRESH_TOKEN
    with open(KEYS_JSON_PATH, "r") as f:
        data = json.load(f)

    APP_KEY = data["app_key"]
    APP_SECRET = data["app_secret"]
    REFRESH_TOKEN = data["refresh_token"]

def refresh_access_token():
    global APP_KEY, APP_SECRET, REFRESH_TOKEN, ACCESS_TOKEN
    url = "https://api.dropbox.com/oauth2/token"

    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": APP_KEY,
        "client_secret": APP_SECRET
    }

    response = requests.post(url, data=data)
    ACCESS_TOKEN = response.json()["access_token"]

def upload_file(fp, dbp):
    global ACCESS_TOKEN

    url = "https://content.dropboxapi.com/2/files/upload"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Dropbox-API-Arg": json.dumps({
            "path": dbp,
            "mode": "add",
            "autorename": False,
            "mute": False,
            "strict_conflict": False
        }),
        "Content-Type": "application/octet-stream"
    }

    with open(fp, "rb") as f:
        data = f.read()

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    print(response.json())

load_keys()
refresh_access_token()

file_path = os.path.join(os.path.dirname(__file__), "brendanbehan.jpeg")
dropbox_path = f"/NTTW_Demo/Photos/{os.path.basename(file_path)}"

upload_file(file_path, dropbox_path)

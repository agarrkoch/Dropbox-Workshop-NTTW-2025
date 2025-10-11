#!/usr/bin/env python3

import requests
import json
import os
import hashlib

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

def calculate_db256_checksum(fp, block_size=4 * 1024 * 1024):
    hash_object = hashlib.sha256()
    bytes_read = 0
    block_hashes = []

    with open(fp, 'rb') as f:
        while True:
            block = f.read(block_size)
            if not block:
                break  # End of file

            block_hash = hashlib.sha256(block).digest()
            block_hashes.append(block_hash)
            bytes_read += len(block)
            hash_object.update(block_hash)

    final_hash = hash_object.hexdigest()
    return final_hash

def downloadfile(dbp):
    global ACCESS_TOKEN
    url = "https://content.dropboxapi.com/2/files/download"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Dropbox-API-Arg": json.dumps({
            "path": dbp
        })
    }

    response = requests.post(url, headers=headers)

    binary_media_data = response.content
    metadata = json.loads(response.headers.get("Dropbox-API-Result"))

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    download_path = os.path.join(desktop, dropbox_path.lstrip('/'))
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    with open(download_path, "wb") as file:
        file.write(binary_media_data)

    origin_checksum = metadata["content_hash"]
    dest_checksum = calculate_db256_checksum(download_path)

    if origin_checksum == dest_checksum:
        print (f"{origin_checksum} / {dest_checksum}")
        print(f"{os.path.basename(download_path)} successfully downloaded and passed fixity check")
    else:
        print(f"{origin_checksum} / {dest_checksum}")
        print(f"{os.path.basename(download_path)} downloaded, but did not pass fixity check")

load_keys()
refresh_access_token()

file_path = os.path.join(os.path.dirname(__file__), "brendanbehan.jpeg")
dropbox_path = f"/NTTW_Demo/Photos/{os.path.basename(file_path)}"

downloadfile(dropbox_path)

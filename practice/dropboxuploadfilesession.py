import requests
import json
import os
import queue


class DropboxUploadFileSession:
    def __init__(self, fp, dbp):
        self.FILE_PATH = fp
        self.KEYS_JSON_PATH = os.path.join(os.path.dirname(__file__), "dropbox_keys.json")
        self.APP_KEY = ''
        self.APP_SECRET = ''
        self.REFRESH_TOKEN = ''
        self.ACCESS_TOKEN = ''
        self.SUCCESS = ''

        self.load_keys()
        self.refresh_access_token()
        self.upload_file(fp, dbp)

    def load_keys(self):
        with open(self.KEYS_JSON_PATH, "r") as f:
            data = json.load(f)

        self.APP_KEY = data["app_key"]
        self.APP_SECRET = data["app_secret"]
        self.REFRESH_TOKEN = data["refresh_token"]

    def refresh_access_token(self):
        url = "https://api.dropbox.com/oauth2/token"

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.REFRESH_TOKEN,
            "client_id": self.APP_KEY,
            "client_secret": self.APP_SECRET
        }

        response = requests.post(url, data=data)
        self.ACCESS_TOKEN = response.json()["access_token"]

    def upload_file(self, fp, dbp):
        url = "https://content.dropboxapi.com/2/files/upload"

        headers = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}",
            "Dropbox-API-Arg": json.dumps({
                "path": dbp,
                "mode": "add",
                "autorename": True,
                "mute": False,
                "strict_conflict": False
            }),
            "Content-Type": "application/octet-stream"
        }

        with open(fp, "rb") as f:
            data = f.read()


        try:
            requests.post(url, headers=headers, data=data)
            self.SUCCESS = True
        except:
            self.SUCCESS = False


if __name__ == "__main__":
    file_path = "/Users/aidagarrido/Downloads/IMG_1585.jpg"
    dropbox_path = f"/NTTW_Demo/Photos/{os.path.basename(file_path)}"

    session_behan = DropboxUploadFileSession(file_path, dropbox_path)



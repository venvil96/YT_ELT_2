import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLE = "MrBeast"

MAX_RESULTS = 50

if not API_KEY:
    raise ValueError("API_KEY was not found. Check your .env file.")

def get_playlist_id():

    url = (
        "https://youtube.googleapis.com/youtube/v3/channels"
        f"?part=contentDetails"
        f"&forHandle={CHANNEL_HANDLE}"
        f"&key={API_KEY}"
    )

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    playlist_id = (
        data["items"][0]
        ["contentDetails"]
        ["relatedPlaylists"]
        ["uploads"]
    )

    return playlist_id


if __name__ == "__main__":
    playlist_id = get_playlist_id()
    print(f"Playlist ID: {playlist_id}")


import os
from dotenv import load_dotenv
from spotify_api import SpotifyHandler

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

playlist_id = input("Enter playlist ID: ")

spotify = SpotifyHandler(CLIENT_ID, CLIENT_SECRET)

playlist = spotify.get_playlist(playlist_id)

for song in playlist:
    print(song)

print(len(playlist))
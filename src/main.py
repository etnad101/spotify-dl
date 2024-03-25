import os
from dotenv import load_dotenv
from spotify_api import SpotifyHandler
from downloader import downlaod_playlist

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

playlist_id = input("Enter playlist url: ")

spotify = SpotifyHandler(CLIENT_ID, CLIENT_SECRET)

playlist = spotify.get_playlist(playlist_id)

downlaod_playlist(playlist, "./songs")

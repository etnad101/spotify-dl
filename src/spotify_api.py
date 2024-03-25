import requests

BASE_URL = "https://api.spotify.com/v1"

class SpotifyHandler:

    def __init__(self, client_id, client_secret):
        self._token = self._get_access_token(client_id, client_secret)

    def _get_access_token(self, client_id, client_secret):
        base_url = "https://accounts.spotify.com/api/token"
        query = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

        request_url = base_url + "?" + query

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = requests.post(request_url, headers=headers)

        status = response.status_code
        if status == 200:
            return response.json()["access_token"]
        else:
            print(f"Error getting access token Code: {status}")
            quit()

    def _url_to_id(self, url):
        id = url.removeprefix("https://open.spotify.com/playlist/")
        id = id.split("?")
        return id[0]


    def get_playlist(self, playlist_url):
        id = self._url_to_id(playlist_url)
        songs = []
        query = "market=CA&fields=next, items"
        url = BASE_URL + "/playlists/" + id + "/tracks?" + query

        return self.get_playlist_aux(id, songs, url)


    def get_playlist_aux(self, id, songs, url):

        header = {"Authorization": f"Bearer {self._token}"}

        response = requests.get(url, headers=header)

        status = response.status_code
        if status != 200:
            print(f"Error getting access token Code: {status}")
            quit()

        tracks = response.json()

        for item in tracks["items"]:
            name = item["track"]["name"]
            artists = []
            for artist in item["track"]["artists"]:
                artists.append(artist["name"])

            song = {}
            song[name] = artists

            songs.append(song)

        next = tracks["next"]

        if next != None:
            songs = self.get_playlist_aux(id, songs, next)

        return songs

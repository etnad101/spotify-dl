import requests
import json

from dotenv import load_dotenv

def req_access_token():
    base_url = "https://accounts.spotify.com/api/token"
    query = "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"

    request_url = base_url + "?" + query

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(request_url, headers=headers)

    print(response.json())

req_access_token()
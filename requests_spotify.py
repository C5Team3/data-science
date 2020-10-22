# This module made requests to spotify API
# This module request a token to Spotify API, based into developer data
# The data developer is client_id and client_secret
# To create a Client Id -> https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app

import base64

import requests

# Data of Developer in App-Spotify
client_id = 'bad84b6413fc444d82539ec1aad0c63c'
client_secret = '843ea45beb0045ebbe8360a8cd2aab1f'


# Function that create a valid token to connect to API Spotify
def _get_token(client_id=client_id, client_secret=client_secret):
    """Return a token valid by 1 hour"""

    encoded = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8'))

    params = {'grant_type': 'client_credentials'}
    header = {'Authorization': 'Basic ' + str(encoded, 'utf-8')}

    r = requests.post('https://accounts.spotify.com/api/token', headers=header, data=params)

    if r.status_code != 200:
        print('Error en la request.', r.json())
        return None

    #print('Token válido por {} segundos.'.format(r.json()['expires_in']))

    return r.json()['access_token']

def request_spotify(uri):
    """Made a request to Spotify-API"""
    token = _get_token()
    header = {'Authorization': f'Bearer {token}'}

    request = requests.get(uri, headers=header)

    return request


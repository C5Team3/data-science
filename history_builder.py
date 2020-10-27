# We are going to create a DataFrame simulating a user's playing history from a Spotify playlist.
# https://open.spotify.com/playlist/37i9dQZF1DX5d5pMk8ynO3
# From where we will obtain data such as genre, artists, etc.
# For this we will use the Spotify API

import random
from datetime import datetime

from requests_spotify import request_spotify


def get_playback_history(uid, playback):
    """Returns a playback history for a user from a playlist"""
    playback_history = []

    for i in range(10000):
        register = {}

        date = get_random_date()
        track = random.choice(playback).copy()

        register['user_id'] = uid
        register['date'] = date
        register['track'] = track

        playback_history.append(register)

    return playback_history


def get_playback(id_playlist):
    """Return an arrangement of songs from a Playlist-ID"""
    url = "https://api.spotify.com/v1/playlists/{}/tracks?market=CO".format(id_playlist)
    playlist = request_spotify(url)

    if playlist.status_code == 200:
        playback = []

        pl = playlist.json()
        size_playlist = len(pl['items'])

        for i in range(size_playlist):
            pb = {}

            track_title = pl['items'][i]['track']['name']
            track_id = pl['items'][i]['track']['id']
            artist_name = pl['items'][i]['track']['artists'][0]['name']
            artist_id = pl['items'][i]['track']['artists'][0]['id']
            album_name = pl['items'][i]['track']['album']['name']
            album_id = pl['items'][i]['track']['album']['id']

            #pb['date'] = None

            pb['track_title'] = track_title
            pb['track_id'] = track_id
            pb['artist_name'] = artist_name
            pb['artist_id'] = artist_id
            pb['album_name'] = album_name
            pb['album_id'] = album_id

            playback.append(pb)
    else:
        print('Status Code Error {}'.format(playlist.status_code))

    return playback


def get_random_date():
    """Returns a date object between a time interval"""
    start = datetime(2020, 1, 1)
    end = datetime(2020, 10, 28)
    random_date = start + (end - start) * random.random()

    return random_date


def get_user_id():
    """"""
    user_id = 'jose-melendez@platzi.com'
    return user_id

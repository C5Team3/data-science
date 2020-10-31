from datetime import datetime

from playlist_builder import get_playlist
from recommendation_finder import get_recommendation
from seeds_generator import get_seeds_to_recommendation


def create_playlist_user(uid):
    playlist = {}
    playlist['type'] = 'user-playlist'
    playlist['user_id'] = uid
    playlist['date'] = datetime.now()

    seeds = get_seeds_to_recommendation(uid)
    recommendation = get_recommendation(seeds)
    tracks_playlist = get_playlist(recommendation)

    playlist['tracks'] = tracks_playlist

    return playlist


def create_playlist_general():
    playlist = {}
    playlist['type'] = 'general-playlist'
    playlist['date'] = datetime.now()

    seeds = get_seeds_to_recommendation()
    recommendation = get_recommendation(seeds)
    tracks_playlist = get_playlist(recommendation)

    playlist['tracks'] = tracks_playlist

    return playlist

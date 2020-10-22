# This script create a play-list based in a Spotify-recommendation
import pandas as pd

def get_playlist(recommendation):
    """Returns a playlist"""
    playlist = {}
    tracks_id = []
    tracks_titles = []
    tracks_preview_url = []

    for track_info in recommendation:
        _track_id = track_info['id']
        _title = track_info['name']
        _url = track_info['preview_url']

        tracks_id.append(_track_id)
        tracks_titles.append(_title)
        tracks_preview_url.append(_url)

    playlist['id'] = tracks_id
    playlist['title'] = tracks_titles
    playlist['preview_url'] = tracks_preview_url

    return pd.DataFrame(playlist)




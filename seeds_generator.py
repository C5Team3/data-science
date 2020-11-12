# This script connects to the database and looks at the playback history.
# Then process the history and get a seed arrangement with
# the most popular songs and artists.
# This arrangement will be used later to get a recommendation from the spotify API.

import pandas as pd

from connection import connection_database


def get_seeds_to_recommendation(user_id=None):
    """Gets the seeds based into top Tracks and Top Artists"""
    if user_id:
        history = get_user_history(user_id)
    else:
        history = get_all_history()

    df = _get_df_history_user(history)

    # Top 2 - Artists
    top_artists = df.groupby('artist_id')['artist_name'].count()
    top_artists.sort_values(ascending=False, inplace=True)
    top2_artists_id = list(top_artists.iloc[0:2].keys())

    # Top 3 - Tracks
    top_tracks = df.groupby('track_id')['track_title'].count()
    top_tracks.sort_values(ascending=False, inplace=True)
    top3_tracks_id = list(top_tracks.iloc[0:3].keys())

    # Join Seeds
    seeds = {}
    seeds['artists'] = top2_artists_id
    seeds['tracks'] = top3_tracks_id

    return seeds


def get_all_history():
    """Gets all the playback history of the application"""
    db = connection_database()
    collection = db['playback_history']
    cursor = collection.find({})
    df = pd.DataFrame(cursor)
    return df


def get_user_history(user_id):
    """Gets all the playback of an specific user"""
    db = connection_database()
    collection = db['playback_history']
    cursor = collection.find({'user_id': user_id})
    df = pd.DataFrame(cursor)
    return df


def _get_df_history_user(user_history):
    """Process the user playback history and returns a DataFrame"""
    dates = list(user_history['date'])
    tracks = user_history['track']

    history = {}

    track_titles = []
    track_ids = []
    artist_names = []
    artist_ids = []
    album_names = []
    album_ids = []
    genres = []

    for track in tracks:
        track_titles.append(track['track_title'])
        track_ids.append(track['track_id'])
        artist_names.append(track['artist_name'])
        artist_ids.append(track['artist_id'])
        album_names.append(track['album_name'])
        album_ids.append(track['album_id'])
        genres.append(track['genre'])

    history['date'] = dates
    history['track_title'] = track_titles
    history['track_id'] = track_ids
    history['artist_name'] = artist_names
    history['artist_id'] = artist_ids
    history['album_name'] = album_names
    history['album_id'] = album_ids
    history['genre'] = genres

    return pd.DataFrame(history)


if __name__ == '__main__':
    # Test Getting Seeds
    uid = "abrant0@elegantthemes.com"
    seeds = get_seeds_to_recommendation(uid)

    print(seeds)
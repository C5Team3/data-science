import pandas as pd

from connection import connection_database
from playlist_builder import get_playlist
from recommendation_finder import get_recommendation


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


def get_seeds_to_recommendation(user_id):
    """Gets the seeds based into top Tracks and Top Artists"""
    user_history = get_user_history(user_id)
    df = user_history

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


def create_playlist_user(uid):
    seeds = get_seeds_to_recommendation(uid)
    recommendation = get_recommendation(seeds)
    playlist = get_playlist(recommendation)

    return playlist

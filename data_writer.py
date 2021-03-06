# This script write the data in App Database
# The DB is a MongoDB

from connection import connection_database
from data_builder import create_playlist_user, create_playlist_general
from history_builder import get_playback, get_playback_history


def save_new_playlist(uid=None):
    """Gets and saves a New Playlist to a specific user"""

    # Creates a new playlist
    if uid:
        playlist = create_playlist_user(uid)
    else:
        playlist = create_playlist_general()

    # Connects and write into DataBase
    db = connection_database()
    collection = db['spot_playlists']
    collection.insert_one(playlist)

    print("A new Playlist was added to DataBase")


def save_sample_playback_history(uid, id_playlist):
    """Save an example history based on a Playlist for a specific user"""

    # Create a user playback history
    base_playlist = get_playback(id_playlist)
    history_user = get_playback_history(uid, base_playlist)

    # Connects and write into DataBase
    db = connection_database()
    collection = db['playback_history']
    collection.insert_many(history_user)

    print("A Sample of Playback-History was added to DataBase")


def save_multiple_user_histories(uid_list, id_playlist):
    """Create demo play histories for a user list from a playlist"""
    base_playlist = get_playback(id_playlist)
    for uid in uid_list:
        history_user = get_playback_history(uid, base_playlist)
        # Connects and write into DataBase
        db = connection_database()
        collection = db['playback_history']
        collection.insert_many(history_user)
        print("A Sample of Playback-History was added to DataBase")

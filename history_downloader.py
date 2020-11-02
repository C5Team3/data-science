# This script consults the database and returns a csv file
# with all the playback history of the application

import sys

from datetime import datetime

import pandas as pd

from connection import connection_database


def get_history_from_db(uid=None):
    """Returns all the raw history of the application"""
    db = connection_database()
    history = db['playback_history']
    if uid == None:
        cursor = history.find({})
    else:
        cursor = history.find({'user_id': uid})
    df = pd.DataFrame(cursor)

    return df


def _get_df_rokker_history(rokker_history):
    """Process raw history and return clean dataframe"""
    dates = list(rokker_history['date'])
    users = list(rokker_history['user_id'])
    ages = list(rokker_history['age'])
    countries = list(rokker_history['country'])
    genders = list(rokker_history['gender'])

    tracks = rokker_history['track']

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
    history['user_id'] = users
    history['age'] = ages
    history['country'] = countries
    history['gender'] = genders
    history['track_title'] = track_titles
    history['track_id'] = track_ids
    history['artist_name'] = artist_names
    history['artist_id'] = artist_ids
    history['album_name'] = album_names
    history['album_id'] = album_ids
    history['genre'] = genres

    return pd.DataFrame(history)


def get_all_history():
    """Get the clean history of the app and save it as a csv file"""
    print("Obtaining data from Database")
    df = get_history_from_db()

    print("Building DataFrame")
    rokker_history = _get_df_rokker_history(df)

    date_str = datetime.strftime(datetime.now(), '%d-%m-%Y')

    print("DataFrame rokker_history_{}.csv was created successfully".format(date_str))
    rokker_history.to_csv('rokker_history_{}.csv'.format(date_str), index=False)


def get_user_history(uid):
    """Get the clean history for an user"""
    print("Obtaining data of {} from Database".format(uid))
    df = get_history_from_db(uid)

    print("Building DataFrame")
    rokker_history = _get_df_rokker_history(df)

    date_str = datetime.strftime(datetime.now(), '%d-%m-%Y')

    print("DataFrame {}_history_{}.csv was created successfully".format(uid, date_str))
    rokker_history.to_csv('{}_history_{}.csv'.format(uid, date_str), index=False)


if __name__ == '__main__':

    print(sys.argv)

    if len(sys.argv) == 1:
        get_all_history()
    else:
        uid = sys.argv[1]
        get_user_history(uid)
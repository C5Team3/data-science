# This script consults the database and returns a csv file
# with all the playback history of the application

from datetime import datetime

import pandas as pd

from connection import connection_database


def get_history_from_db():
    db = connection_database()
    history = db['playback_history']
    cursor = history.find({})
    df = pd.DataFrame(cursor)

    return df


def _get_df_rokker_history(rokker_history):
    """Process the user playback history and returns a DataFrame"""
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
    history['countrie'] = countries
    history['gender'] = genders
    history['track_title'] = track_titles
    history['track_id'] = track_ids
    history['artist_name'] = artist_names
    history['artist_id'] = artist_ids
    history['album_name'] = album_names
    history['album_id'] = album_ids
    history['genre'] = genres

    return pd.DataFrame(history)


def main():
    print("Obtain data from Database")
    df = get_history_from_db()

    print("Building DataFrame")
    rokker_history = _get_df_rokker_history(df)

    date_str = datetime.strftime(datetime.now(), '%d-%m-%Y')

    print("DataFrame rokker_history_{}.csv was created succesfully".format(date_str))
    rokker_history.to_csv('rokker_history_{}.csv'.format(date_str), index=False)


if __name__ == '__main__':
    main()

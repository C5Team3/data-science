# This script create a play-list based in a Spotify-recommendation
import pandas as pd

def get_playlist(recommendation):
    """Returns a playlist"""
    playlist = {}

    tracks_id = []
    tracks_titles = []
    albums_id = []
    albums_name = []
    imgs_url = []
    years = []
    artists_id = []
    artists_name = []
    tracks_preview_url = []

    for track_info in recommendation:

        _track_id = track_info['id']
        _title = track_info['name']
        _album_id = track_info['album']['id']
        _album_name = track_info['album']['name']
        _img_url = track_info['album']['images'][2]['url']
        _year = track_info['album']['release_date']
        _artist_id = track_info['artists'][0]['id']
        _artist_name = track_info['artists'][0]['name']
        _url = track_info['preview_url']


        tracks_id.append(_track_id)
        tracks_titles.append(_title)
        albums_id.append(_album_id)
        albums_name.append(_album_name)
        imgs_url.append(_img_url)
        years.append(_year)
        artists_id.append(_artist_id)
        artists_name.append(_artist_name)
        tracks_preview_url.append(_url)

    playlist['id'] = tracks_id
    playlist['title'] = tracks_titles
    playlist['album_id'] = albums_id
    playlist['album_name'] = albums_name
    playlist['img_url'] = imgs_url
    playlist['year'] = years
    playlist['artist_id'] = artists_id
    playlist['artist_name'] = artists_name
    playlist['preview_url'] = tracks_preview_url


    return pd.DataFrame(playlist)




# This script create a play-list based in a Spotify-recommendation

from requests_spotify import request_spotify


def get_playlist(recommendation):
    """Returns a playlist based into recommendation-array of Spotify API"""
    playlist = []

    for track_info in recommendation:
        track = {}

        track_id = track_info['id']
        title = track_info['name']
        album_id = track_info['album']['id']
        album_name = track_info['album']['name']
        album_img = track_info['album']['images'][0]['url']
        year = track_info['album']['release_date']
        artist_id = track_info['artists'][0]['id']
        artist_name = track_info['artists'][0]['name']
        artist_img = get_artist_info(artist_id)['artist_img']['url']
        preview_url = track_info['preview_url']
        duration_ms = track_info['duration_ms']
        genre = get_artist_info(artist_id)['genre']

        track['track_id'] = track_id
        track['track_title'] = title
        track['album_id'] = album_id
        track['album_name'] = album_name
        track['album_img'] = album_img
        track['year'] = year
        track['artist_id'] = artist_id
        track['artist_name'] = artist_name
        track['artist_img'] = artist_img
        track['preview_url'] = preview_url
        track['duration_ms'] = duration_ms
        track['genre'] = genre

        playlist.append(track)

    return playlist


def get_artist_info(artist_id):
    """Returns an array with Artist Information"""
    url = 'https://api.spotify.com/v1/artists/{}'.format(artist_id)
    artist = request_spotify(url)

    if artist.status_code == 200:

        artist = artist.json()

        genre = artist['genres']
        artist_img = artist['images'][0]

        artist_info = {}
        artist_info['genre'] = genre
        artist_info['artist_img'] = artist_img

    else:
        print('Status Code Error {}'.format(artist.status_code))

    return artist_info

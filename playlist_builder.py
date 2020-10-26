# This script create a play-list based in a Spotify-recommendation

def get_playlist(recommendation):
    """Returns a playlist"""
    playlist = []

    for track_info in recommendation:
        track = {}

        track_id = track_info['id']
        title = track_info['name']
        album_id = track_info['album']['id']
        album_name = track_info['album']['name']
        img_url = track_info['album']['images'][2]['url']
        year = track_info['album']['release_date']
        artist_id = track_info['artists'][0]['id']
        artist_name = track_info['artists'][0]['name']
        url = track_info['preview_url']

        track['track_id'] = track_id
        track['track_title'] = title
        track['album_id'] = album_id
        track['album_name'] = album_name
        track['img_url'] = img_url
        track['year'] = year
        track['artist_id'] = artist_id
        track['artist_name'] = artist_name
        track['preview_url'] = url

        playlist.append(track)

    return playlist

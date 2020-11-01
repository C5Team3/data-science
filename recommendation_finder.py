# This module Get Recommendations Based on Seeds
# Create a playlist-style listening experience based on seed artists, tracks and genres.
# By this use the API Spotify Recommendations. To see the docs:
# https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/

from requests_spotify import request_spotify


def get_recommendation(seeds):
    """Request to API to get a Recommendation based on the seeds"""
    artists_seeds = ','.join(seeds['artists'])
    tracks_seeds = ','.join(seeds['tracks'])

    MARKET = 'US'
    LIMIT = '20'

    URL_BASE = 'https://api.spotify.com/v1/recommendations?limit={}&market={}&seed_artists={}&seed_tracks={}'

    uri = URL_BASE.format(LIMIT, MARKET, artists_seeds, tracks_seeds)

    recommendation = request_spotify(uri)

    return recommendation.json()['tracks']

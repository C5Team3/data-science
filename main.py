# Create a new playlist and save it in the database
#
# It can be of two types:
#
# 1. Playlist for a specific user
# 2. General Playlist that will be shown to all users

import sys

from data_writer import save_new_playlist


def save_new_playlist_user(uid):
    """Playlist for a specific user"""
    print('Creating a New Playlist to {}'.format(uid))
    print('Please Wait for a moment')
    print('.' * 50)

    save_new_playlist(uid)


def save_new_playlist_general():
    """General Playlist that will be shown to all users"""
    print('Creating a General New Playlist')
    print('Please Wait for a moment')
    print('.' * 50)

    save_new_playlist()


if __name__ == '__main__':

    print(sys.argv)

    if len(sys.argv) == 1:
        save_new_playlist_general()
    else:
        uid = sys.argv[1]
        save_new_playlist_user(uid)

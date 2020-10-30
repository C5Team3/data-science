import sys

from data_writer import save_new_playlist


def save_new_playlist_user(uid):
    print('Creating a New Playlist to {}'.format(uid))
    print('Please Wait for a moment')
    print('.'*50)
    save_new_playlist(uid)


if __name__ == '__main__':
    uid = sys.argv[1]
    save_new_playlist_user(uid)

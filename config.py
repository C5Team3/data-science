# This script load and parse the configuration parameters of the database

from configparser import ConfigParser


def get_config_db(file='database.ini', section='rokket-db'):
    parser = ConfigParser()
    parser.read(file)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} was not found in the file {1}'.format(section, file))
    return db

def get_spotify_credentials(file='database.ini', section='spotify-credentials'):
    parser = ConfigParser()
    parser.read(file)

    credentials = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            credentials[param[0]] = param[1]
    else:
        raise Exception('Section {0} was not found in the file {1}'.format(section, file))
    return credentials
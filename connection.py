# This Script connects the App with Mongo-Database
# pip install pymongo
# pip install dnspython

from pymongo import MongoClient
from config import get_config_db


def connection_database(params_db=get_config_db()):
    """Get a Connection with a Database-Mongodb"""

    USER = params_db['user']
    PASS = params_db['pass']
    HOST = params_db['host']
    DB = params_db['db']

    MONGO_URI = 'mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority'
    URI = MONGO_URI.format(user=USER, password=PASS, host=HOST)

    client = MongoClient(URI)
    db = client[DB]

    return db
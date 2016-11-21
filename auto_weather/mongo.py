import pymongo

from keyring import get_password


def connection():
    connection_info = ['ds159507.mlab.com', 59507]
    client = pymongo.MongoClient(*connection_info)
    return client


def auth(db):
    username = get_password("MongoDB", "username")
    password = get_password("MongoDB", "password")
    db.authenticate(username, password)
    return


def insert(w_list):
    db = connection().weather
    auth(db)
    weather_log = db.weather_log
    result = weather_log.insert_one(w_list)
    print result
    return

import pymongo

from keyring import get_password

# instantiate mongodb connection
def connection():
    connection_info = ['ds159507.mlab.com', 59507]
    client = pymongo.MongoClient(*connection_info)
    return client

# retrieve hidden username and password via keyring library
# which is used to hide sensitive information since code is public
def auth(db):
    username = get_password("MongoDB", "username")
    password = get_password("MongoDB", "password")
    db.authenticate(username, password)

# Takes in the dictionary of weather info, stores it in mongodb instance
def insert(w_list):
    db = connection().weather
    auth(db)
    weather_log = db.weather_log
    result = weather_log.insert_one(w_list)

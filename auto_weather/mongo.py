import pymongo

from keyring import get_password

# instantiate mongodb connection
def connection():
    # connection_info = ['ds159507.mlab.com', 59507]
    connection_info = []
    connection_info.append(get_password("MongoDB", "ConnName"))
    connection_info.append(int(get_password("MongoDB", "port")))
    client = pymongo.MongoClient(*connection_info)
    return client

# retrieve hidden username and password via keyring library
# which is used to hide sensitive information since code is public
def auth(db):
    username = get_password("MongoDB", "username")
    password = get_password("MongoDB", "password")
    db.authenticate(username, password)

<<<<<<< HEAD

def select_db_document():
=======
# Takes in the dictionary of weather info, stores it in mongodb instance
def insert(w_list):
>>>>>>> c1b154561a099436b9b834677d88013242a58ed0
    db = connection().weather
    auth(db)
    weather_log = db.weather_log
    return weather_log


def insert(w_list):
    weather_log = select_db_document()
    result = weather_log.insert_one(w_list)
    print result

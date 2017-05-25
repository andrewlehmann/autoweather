import pymongo

from keyring import get_password


def connection():  # get connection info w/ keyring
    connection_info = []
    connection_info.append(get_password("MongoDB", "ConnName"))
    connection_info.append(int(get_password("MongoDB", "port")))
    client = pymongo.MongoClient(*connection_info)
    return client


def auth(db):  # Authenticate myself with remote DB
    username = get_password("MongoDB", "username")
    password = get_password("MongoDB", "password")
    db.authenticate(username, password)


def select_db_collection():  # select collection within document
    db = connection().weather
    auth(db)
    return db.weather_log


def insert(w_list):
    weather_log = select_db_collection()
    result = weather_log.insert_one(w_list)
    print(result)


def avg_high_and_low():  # calculate avg of highs and lows
    weather_log = select_db_collection()
    # lambda functions retrive either high or low temp from db entry
    getHigh = lambda entry: int(entry['High'])
    getLow = lambda entry: int(entry['Low'])

    highs = list(map(getHigh, weather_log.find()))
    lows = list(map(getLow, weather_log.find()))

    high_avg = sum(highs) / len(highs)
    lows_avg = sum(lows) / len(lows)
    return high_avg, lows_avg

import pymongo

from keyring import get_password


def connection(): # get connection info w/ keyring
    connection_info = []
    connection_info.append(get_password("MongoDB", "ConnName"))
    connection_info.append(int(get_password("MongoDB", "port")))
    client = pymongo.MongoClient(*connection_info)
    return client


def auth(db): # Authenticate myself with remote DB
    username = get_password("MongoDB", "username")
    password = get_password("MongoDB", "password")
    db.authenticate(username, password)


def select_db_collection(): # select collection within document
    db = connection().weather
    auth(db)
    weather_log = db.weather_log
    return weather_log


def insert(w_list):
    weather_log = select_db_collection()
    result = weather_log.insert_one(w_list)
    print result


def avg_high_and_low(w_list): # calculate avg of highs and lows
    highs = []                # easier to do this way than by 
    lows = []                 # using aggregate func. in database
    weather_log = select_db_collection() # but which is faster?
    for obj in weather_log.find():
        highs.append(int(obj['High']))
        lows.append(int(obj['Low']))
    high_avg = sum(highs) / len(highs)
    lows_avg = sum(lows) / len(lows)
    return high_avg, lows_avg

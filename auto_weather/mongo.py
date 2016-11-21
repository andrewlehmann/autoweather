import PyMongo
import keyring


def get_database():
	username = keyring.get_password("MongoDB", "username")
	password = keyring.get_password("MongoDB", "password")
	connection_string = 'mongodb://%s:%s@ds159507.mlab.com:59507' % (username, password)
	client = MongoClient(connection_string)
	db = client.weather
	return db

def insert(db, w_list):
	result = db.insert_one(w_list)
	return










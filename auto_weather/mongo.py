import PyMongo
import keyring


def connection():
	username = keyring.get_password("MongoDB", "username")
	password = keyring.get_password("MongoDB", "password")
	connection_string = 'mongodb://%s:%s@ds159507.mlab.com:59507' % (username, password)
	client = MongoClient(connection_string)
	return client

def insert(db, w_list):
	weather = db.weather
	result = db.weather.insert_one(
		{
			"Current Temperature": w_list[0],
			"Low": w_list[1],
			"High:" w_list[2],
			"Description": w_list[3]
		}
	)









import PyMongo
import keyring


def connection():
	username = keyring.get_password("MongoDB", "username")
	password = keyring.get_password("MongoDB", "password")
	connection_string = 'mongodb://%s:%s@ds159507.mlab.com:59507/weather' % (username, password)
	client = MongoClient(connection_string)
	return client

	


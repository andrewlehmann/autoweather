import unittest

from .context import mongo


class Test(unittest.TestCase):

    def test_testConnection(self):
        connection_info = ['ds159507.mlab.com', 59507]
        client = mongo.pymongo.MongoClient(*connection_info)
        self.assertEqual(client, mongo.connection())

    def test_insert(self): # add extra junk data to document
        w_info = {
            "Current_Temp": 55,
            "Low": 35,
            "High": 58,
            "Description": "test",
            "Date": "2016-12-31"
        }
        mongo.insert(w_info)
        self.assertEqual(True, True)

    if __name__ == '__main__':
        unittest.main()

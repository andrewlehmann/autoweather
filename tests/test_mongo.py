import unittest

from .context import mongo


class Test(unittest.TestCase):

    def test_testConnection(self):
        connection_info = ['ds159507.mlab.com', 59507]
        client = mongo.pymongo.MongoClient(*connection_info)
        self.assertEqual(client, mongo.connection())

    def test_insert(self): # add extra junk data to document
                           # to later test average
        w_info = {
            "Current_Temp": 55,
            "Low": 35,
            "High": 58,
            "Description": "test",
            "Date": "2016-12-31"
        }
        weather_log = select_db_collection()  # but which is faster?

        highs = list(map(lambda e: int(e['High']), weather_log.find()))
        lows = list(map(lambda e: int(e['Low']), weather_log.find()))

        high_avg = sum(highs) / len(highs)
        lows_avg = sum(lows) / len(lows)
        self.assertEqual((high_avg, low_avg), mongo.avg_high_and_low())

    if __name__ == '__main__':
        unittest.main()

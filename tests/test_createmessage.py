import unittest

from .context import message


class Test(unittest.TestCase):

    def test_create_message(self):
        w_dict = {
            "Curr_Temp": 5,
            "Low": 5,
            "High": 10,
            "Description": "lol",
        }

        _string = 'Current temp: 5 \n\tLow: 5 \n\tHigh: 10' \
            ' \n\tDescription: lol'
        self.assertEqual(sendmessage.create_message(w_dict), _string)

    if __name__ == '__main__':
        unittest.main()

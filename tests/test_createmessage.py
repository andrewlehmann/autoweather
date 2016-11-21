import unittest
from .context import sendmessage

class Test(unittest.TestCase):
	def test_create_message(self):
		self.assertEqual(sendmessage.create_message([5, 5, 10, 'lol']), 'Current temp: 5 \nLow: 5 \nHigh: 10 \nDescription: lol \n')

	if __name__ == '__main__':
		unittest.main()
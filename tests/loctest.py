import unittest
#import auto_weather
from .context import location
#from auto_weather.auto_weather import location

class Test(unittest.TestCase):

	def test_ip(self):
		self.assertEqual(location.get_ip(), '129.7.0.27')

	def test_location(self):
		self.assertIsNotNone(location.get_location('129.7.0.27'))

	if __name__ == '__main__':
		unittest.main()
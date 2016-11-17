import unittest
from .context import getweather

class Test(unittest.TestCase):
	def weather_test(self):
		desc = '''Mostly clear, with a low around 62. 
			Southeast wind around 5 mph becoming calm  
			in the evening. '''
		self.assertEqual(get_weather(29.8340,-95.4342), \
			('73', '62', '83', desc))
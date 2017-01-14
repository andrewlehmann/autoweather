import unittest

from .context import getweather


class Test(unittest.TestCase):

    def test_weather(self):
        self.assertEqual(
            getweather.get_weather(29.8340, -95.4342),
            ['73', '62', '83', 'Mostly clear, with a low around 62. ' /
                'Southeast wind around 5 mph becoming calm  in the evening. '])

    if __name__ == '__main__':
        unittest.main()

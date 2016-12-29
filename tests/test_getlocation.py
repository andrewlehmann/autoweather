import unittest

from .context import location


class Test(unittest.TestCase):

    def test_ip(self):
        self.assertEqual(
            location.get_ip(), '129.7.0.27')

    def test_location(self):
        self.assertEqual(
            location.get_location('129.7.0.27'), ('29.8340', '-95.4342'))

    if __name__ == '__main__':
        unittest.main()

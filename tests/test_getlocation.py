import unittest

from .context import location


class Test(unittest.TestCase):

    def test_ip(self):
        self.assertEqual(
            location.get_ip(), '129.7.0.27')  # test specific to own location

    def test_location(self):  # must change if used elsewhere
        self.assertEqual(
            location.get_location('129.7.0.27'), ('29.8340', '-95.4342'))

    if __name__ == '__main__':
        unittest.main()

import unittest
from qu_captcha.drawer import *


class TestDrawer(unittest.TestCase):
    def test_rand_point_except(self):
        for _ in range(10000):
            # no fails
            rand_point_except([rand_point() for _ in range(10)])

    def test_rand_curve(self):
        for _ in range(10000):
            # no fails
            rand_curve(15)


if __name__ == "__main__":
    unittest.main()

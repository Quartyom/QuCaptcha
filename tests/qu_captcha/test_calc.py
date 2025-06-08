import unittest
import math
from qu_captcha.calc import *


class TestCalc(unittest.TestCase):
    def test_point_point_distance(self):
        self.assertAlmostEqual(point_point_distance((12, -4), (12, -4)), 0)
        self.assertAlmostEqual(point_point_distance((0, 0), (0, -7)), 7)
        self.assertAlmostEqual(point_point_distance((0, 0), (1, 1)), math.sqrt(2))
        self.assertAlmostEqual(point_point_distance((20, 20), (23, 16)), 5)

    def test_colors_distance(self):
        self.assertAlmostEqual(colors_distance((0, 0, 0), (0, 0, 0)), 0)
        self.assertAlmostEqual(colors_distance((1, 1, 1), (0, 0, 0)), 1)
        self.assertAlmostEqual(colors_distance((0.2, 0.4, 0.7), (0.1, 0.4, 1)), 0.18257418)

    def test_point_line_distance(self):
        self.assertAlmostEqual(point_line_distance((2, 0), (0, 0), (0, 0)), 2)
        self.assertAlmostEqual(point_line_distance((2, 3), (8, 9), (2, 3)), 0)
        self.assertAlmostEqual(point_line_distance((0, 0), (4, 0), (0, 4)), 2 * math.sqrt(2))
        self.assertAlmostEqual(point_line_distance((-17, 8), (4, 0), (0, 4)), 9.192388155)

    def test_is_projection_in_section(self):
        self.assertTrue(is_projection_in_section(5, (2, 3), (2, 3), (-4, 19)))
        self.assertTrue(is_projection_in_section(1, (1, 2), (1, 1), (3, 3)))
        self.assertFalse(is_projection_in_section(1, (1, 3), (1, 1), (3, 3)))

    def test_is_near_section(self):
        self.assertTrue(is_near_section(5, (2, 3), (2, 3), (-4, 19)))
        self.assertTrue(is_near_section(1, (1, 2), (1, 1), (3, 3)))
        self.assertTrue(is_near_section(math.sqrt(2), (0, 0), (1, 1), (3, 3)))
        self.assertFalse(is_near_section(1, (0, 0), (1, 1), (3, 3)))

    def test_cos_abs(self):
        self.assertAlmostEqual(cos_abc((0, 1), (0, 0), (0, 0)), 0)
        self.assertAlmostEqual(cos_abc((0, 1), (0, 0), (0, 1)), 1)
        self.assertAlmostEqual(cos_abc((0, 1), (0, 0), (-1, 0)), 0)
        self.assertAlmostEqual(cos_abc((2, 7), (-11, 0), (-16, 2)), -0.6414206393)


if __name__ == "__main__":
    unittest.main()

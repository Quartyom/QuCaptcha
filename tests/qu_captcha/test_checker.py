import unittest
from qu_captcha.checker import *


class TestChecker(unittest.TestCase):
    def test_is_straight_order(self):
        self.assertFalse(is_straight_order([], [3, 2]))
        self.assertFalse(is_straight_order([1, 2], []))
        self.assertFalse(is_straight_order([1, 2], [2, [3]]))

        self.assertFalse(is_straight_order([[0, 0], [100, 300]], [[105, 309], [5, 5]]))
        self.assertTrue(is_straight_order([[0, 0], [100, 300]], [[5, 5], [105, 309]]))

    def test_alg_check(self):
        self.assertFalse(alg_check([], [3, 2], 2))
        self.assertFalse(alg_check([1, 2], [], None))
        self.assertFalse(alg_check([1, 2], [2, [3]], []))

        self.assertFalse(is_straight_order([[0, 0], [100, 300]], [[105, 309], [5, 5]]), 1)
        self.assertFalse(is_straight_order([[0, 0], [100, 300]], [[105, 309], [5, 5]]), 15)


if __name__ == "__main__":
    unittest.main()

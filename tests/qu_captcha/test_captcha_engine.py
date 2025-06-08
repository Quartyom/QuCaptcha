import unittest
import time
from qu_captcha.captcha_engine import *


class TestCaptchaEngine(unittest.TestCase):
    def test_load_get(self):
        self.captcha_engine = CaptchaEngine()
        st_time = time.time()

        test_time_s = 5
        i = 0   # должно генерироваться не менее 100 тестов в секунду

        while time.time() - st_time <= test_time_s:
            self.captcha_engine.get()
            i += 1

        print(f"Generated: {i} tasks")
        self.assertTrue(i >= test_time_s * 100)


if __name__ == "__main__":
    unittest.main()

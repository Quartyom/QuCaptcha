import unittest
import time
import requests

class TestServiceLoad(unittest.TestCase):
    def test_load(self):
        st_time = time.time()
        iters = 1000
        for _ in range(iters):
            verify_response = requests.get(f'http://127.0.0.1:7000/get_task')
        t = time.time() - st_time
        print(f"time range: {t}, which is {t / iters} per request")
        self.assertLessEqual(t, iters / 100)


if __name__ == "__main__":
    unittest.main()

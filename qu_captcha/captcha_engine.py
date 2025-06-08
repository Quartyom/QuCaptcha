from uuid import uuid4 as _uuid4
from time import time_ns

from .constants import *
from .drawer import draw_captcha as _draw_captcha
import qu_captcha.checker as _checker
from .expiring_dict import ExpiringDict as _ExpiringDict
from .image_encoder import *


# Provides complete engine to get and check CAPTCHA, using task_id
class CaptchaEngine:
    # expiration time for task_id, captcha image size
    def __init__(self, expiration_time_seconds=60, captcha_size=DEFAULT_CAPTCHA_SIZE):
        self._expiration_time = expiration_time_seconds
        self._captcha_size = captcha_size
        self._captcha_solutions = _ExpiringDict(expiration_time_seconds)

    # returns task_id and image as pillow image if not encoded, base64 in utf-8 image otherwise
    def get(self, is_mobile=False, to_encode=True):
        # st_time = time_ns()
        if is_mobile:
            captcha_image, captcha_dots = _draw_captcha(5, 7, self._captcha_size)
        else:
            captcha_image, captcha_dots = _draw_captcha(captcha_size=self._captcha_size)

        task_id = str(_uuid4())
        self._captcha_solutions.set(task_id, (captcha_dots, is_mobile))

        if to_encode:
            captcha_image = encode_image(captcha_image)

        # print(f"get {(time_ns() - st_time) / 1000000}ms")

        return task_id, captcha_image

    # user_dots
    def check(self, task_id, user_dots):
        solution = self._captcha_solutions.get(task_id, None)
        if not solution:
            return False, None
        self._captcha_solutions.remove(task_id)

        captcha_dots, is_mobile = solution

        # st_time = time_ns()
        r = _checker.alg_check(captcha_dots, user_dots, DOT_RADIUS_FLOAT_MOBILE if is_mobile else DOT_RADIUS_FLOAT)
        # print(f"check {time_ns() - st_time}ns")

        return r, captcha_dots

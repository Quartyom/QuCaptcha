from random import random, randint
import math
from .calc import point_point_distance as pp_dist, cos_abc, colors_distance
from .constants import *
import cv2
import numpy as np


def rand_point():
    return random(), random()


def rand_point3():
    return random(), random(), random()


# avoid points format: [p1, p2, p3], p: [x, y]
def rand_point_except(avoid_points):
    for _ in range(5):  # optimized while True
        p = rand_point()
        result = True

        for ap in avoid_points:     # segment len
            if pp_dist(p, ap) < MIN_CURVE_SEGMENT_LEN:
                result = False
                break

        if result and len(avoid_points) >= 2:   # segment angle
            a = avoid_points[-2]
            b = avoid_points[-1]
            c = cos_abc(a, b, p)
            cos_angle = math.cos(MIN_CURVE_SEGMENT_ANGLE_DEG * math.pi / 180)
            cos_angle2 = math.cos(MAX_CURVE_SEGMENT_ANGLE_DEG * math.pi / 180)
            if cos_angle2 <= c <= cos_angle:
                pass
            else:
                result = False

        if result:
            return p
    return rand_point()


def rand_color(avoid_color=(0, 0, 0)):
    black = (0, 0, 0)
    white = (1, 1, 1)
    for _ in range(5):  # optimized while True
        p = rand_point3()
        if colors_distance(p, avoid_color) > 0.2 and colors_distance(p, black) > 0.1 and colors_distance(p, white) > 0.1:
            return int(p[0] * 255), int(p[1] * 255), + int(p[2] * 255)
    return rand_point3()


def rand_line():
    return [rand_point(), rand_point()]


def rand_curve(size):
    curve = []
    for i in range(size):
        curve.append(rand_point_except(curve))
    return curve


# curve * k
def scale_curve(curve, k):
    scaled_curve = []
    for point in curve:
        scaled_curve.append((int(point[0]*k), int(point[1]*k)))
    return scaled_curve


def add_curve(image, curve, color):
    curve_np = np.array(scale_curve(curve, len(image)), dtype=np.int32).reshape((-1, 1, 2))
    cv2.polylines(image, [curve_np], False, color, thickness=randint(3, 7))


def add_lines(image, n, color):
    line_color = rand_color(color)
    for i in range(n):
        pt1, pt2 = scale_curve(rand_line(), len(image))
        line_color = rand_color(color) if randint(0, 2) else line_color
        cv2.line(image, pt1, pt2, line_color, thickness=randint(3, 7))


def draw_captcha(dots_number=4, noise_number=6, captcha_size=DEFAULT_CAPTCHA_SIZE):
    curve = rand_curve(dots_number)
    main_color = rand_color()

    image = np.full((captcha_size, captcha_size, 3), 255, dtype=np.uint8)

    add_curve(image, curve, main_color)
    add_lines(image, noise_number, main_color)

    noise = np.random.randint(0, 50, (captcha_size, captcha_size, 3), dtype=np.uint8)   # 0, 75
    image -= noise

    return image, curve


if __name__ == 'main':
    im, cr = draw_captcha()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

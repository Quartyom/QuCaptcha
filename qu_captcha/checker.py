from .calc import point_point_distance as pp_dist


# checks if user_dots correlate with captcha_dots in straight order
def is_straight_order(captcha_dots, user_dots):
    try:
        bg = user_dots[0]
        bg_dist = pp_dist(bg, captcha_dots[0])
        end = user_dots[-1]
        end_dist = pp_dist(end, captcha_dots[0])
        return bg_dist < end_dist
    except:
        return False


# checks if solution is provided, user dots correlate with captcha
def alg_check(captcha_dots, user_dots, max_distance):
    try:
        if not captcha_dots or not user_dots:
            # print("some of lists is empty")
            return False

        if len(captcha_dots) != len(user_dots):
            # print("captcha dots size differs from user dots")
            return False

        if not is_straight_order(captcha_dots, user_dots):
            captcha_dots.reverse()

        for i in range(len(captcha_dots)):
            if pp_dist(captcha_dots[i], user_dots[i]) > max_distance:
                # print("some dots are far from captcha")
                return False

        return True
    except:
        return False


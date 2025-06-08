# Module for calculations

def point_point_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5


def colors_distance(c1, c2):    # normalized distance between two colors (black, white) -> 1
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    distance = ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5
    return distance / (3 ** 0.5)


def point_line_distance(p, a, b):   # distance from point p to line ab
    if a == b:
        return point_point_distance(p, a)
    x1, y1 = a
    x2, y2 = b
    x3, y3 = p
    s = 0.5 * abs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))    # area of pab triangle
    ab = ((x2-x1)**2 + (y2-y1)**2) ** 0.5                       # ab length
    return 2 * s / ab                                           # h = 2S / ab


def is_projection_in_section(h, p, a, b):      # h - max len of projection, p - point, ab - section
    x1, y1 = a
    x2, y2 = b
    x3, y3 = p
    # dot_ab_ap < 0 or dot_ba_pa < 0
    if (x2-x1)*(x3-x1) + (y2-y1)*(y3-y1) < 0 or (x1-x2)*(x3-x2) + (y1-y2)*(y3-y2) < 0:
        return False
    return point_line_distance(p, a, b) <= h


def is_near_section(h, p, a, b):    # checks if p closer to any point of ab section than h
    # near a or b
    if point_point_distance(p, a) <= h or point_point_distance(p, b) <= h:
        return True
    return is_projection_in_section(h, p, a, b)


def cos_abc(a, b, c):       # gets cos of abc angle via vectors
    vector_ba = a[0] - b[0], a[1] - b[1]
    vector_bc = c[0] - b[0], c[1] - b[1]
    dot_ba_bc = vector_ba[0] * vector_bc[0] + vector_ba[1] * vector_bc[1]
    ab_bc = (point_point_distance(a, b) * point_point_distance(b, c))
    return 0 if ab_bc == 0 else dot_ba_bc / ab_bc


if __name__ == '__main__':
    a = (7, 2)
    b = (2, 4)
    c = (9, 7)
    print(point_point_distance(a, b))
    print(point_line_distance(c, a, b))
    print(is_near_section(1, (1, 4), a, b))
    print(is_near_section(1, (1, 5), a, b))
    print(is_near_section(1, (4, 3), a, b))
    print(is_near_section(1, b, a, b))
    print(is_projection_in_section(5, a, a, b))

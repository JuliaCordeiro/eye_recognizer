import numpy as np
from math import hypot


def midpoint(frist_point, second_point):
    x_point = int((frist_point.x + second_point.x) / 2)
    y_point = int((frist_point.y + second_point.y) / 2)
    return x_point, y_point


def eye_center_points(mask, points):
    left_center = (mask.part(points[0]).x, mask.part(points[0]).y)
    right_center = (mask.part(points[3]).x, mask.part(points[3]).y)
    top_center = midpoint(mask.part(points[1]), mask.part(points[2]))
    bottom_center = midpoint(mask.part(points[5]), mask.part(points[4]))
    return [left_center, right_center, top_center, bottom_center]


def blinking_ratio(eye_points):
    horizontal_lenght = hypot((eye_points[0][0] - eye_points[1][0]), (eye_points[0][1] - eye_points[1][1]))
    vertical_lenght = hypot((eye_points[2][0] - eye_points[3][0]), (eye_points[2][1] - eye_points[3][1]))

    ratio = horizontal_lenght / vertical_lenght
    return ratio


def eye_region(mask, points):
    region = np.array([
        (mask.part(points[0]).x, mask.part(points[0]).y),
        (mask.part(points[1]).x, mask.part(points[1]).y),
        (mask.part(points[2]).x, mask.part(points[2]).y),
        (mask.part(points[3]).x, mask.part(points[3]).y),
        (mask.part(points[4]).x, mask.part(points[4]).y),
        (mask.part(points[5]).x, mask.part(points[5]).y)], np.int32)
    return region


def eye_extremes_region(region):
    min_x = np.min(region[:, 0])
    max_x = np.max(region[:, 0])
    min_y = np.min(region[:, 1])
    max_y = np.max(region[:, 1])
    return [min_x, max_x, min_y, max_y]

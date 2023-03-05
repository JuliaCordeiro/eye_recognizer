def midpoint(frist_point, second_point):
    x_point = int((frist_point.x + second_point.x) / 2)
    y_point = int((frist_point.y + second_point.y) / 2)
    return x_point, y_point


def eye_points(mask, points):
    left_center = (mask.part(points[0]).x, mask.part(points[0]).y)
    right_center = (mask.part(points[3]).x, mask.part(points[3]).y)
    top_center = midpoint(mask.part(points[1]), mask.part(points[2]))
    bottom_center = midpoint(mask.part(points[5]), mask.part(points[4]))
    return [left_center, right_center, top_center, bottom_center]

from geoformat_lib.geoprocessing.connectors.operations import segment_to_bbox

# predicate return :
# - a boolean for geometries confrontation
# - or an information about position between a geometry in relation to another

# Return BOOLEAN
# Point vs
# point_intersects_point
# point_intersects_segment
# point_intersects_bbox
#
# segment vs
# segment_intersects_bbox
# segment_intersects_segment
#
# bbox vs
# bbox_intersects_bbox

# Return POSITION
# point_position_segment
# ccw_or_cw_segments


def point_intersects_point(point_a, point_b):
    """
    Return True if point_a and point_b have sames coordinates
    """
    return point_a[0] == point_b[0] and point_a[1] == point_b[1]


def point_intersects_segment(point, segment):
    """
    Test if point intersects a segment
    """
    if point_position_segment(point, segment) == 'ON':
        seg_bbox = segment_to_bbox(segment)
        return point_intersects_bbox(point, seg_bbox)
    else:
        return False


def point_intersects_bbox(point, bbox):
    """
    This function send a boolean (true or false) that indicate if a given point intersect a given bbox

        Input:
            point
            bbox

        Output:
            True or False(boolean)
    """

    (point_x, point_y) = point
    (bbox_x_min, bbox_y_min, bbox_x_max, bbox_y_max) = bbox

    return point_x >= bbox_x_min and point_x <= bbox_x_max and point_y >= bbox_y_min and point_y <= bbox_y_max


def segment_intersects_segment(segment_a, segment_b):
    """"

    """
    (pointA1, pointA2) = segment_a
    (pointB1, pointB2) = segment_b
    segment_a_1 = (pointA2, pointB1)
    segment_a_2 = (pointA2, pointB2)
    segment_b_1 = (pointB2, pointA1)
    segment_b_2 = (pointB2, pointA2)

    (ptAx, ptAy) = segment_a[0]
    (ptBx, ptBy) = segment_a[1]
    (ptCx, ptCy) = segment_a_1[1]

    a = (ptBx - ptAx) * (ptCy - ptAy)
    b = (ptBy - ptAy) * (ptCx - ptAx)
    if a > b:
        ccw_segment_a_1 = 'CCW'
    elif a < b:
        ccw_segment_a_1 = 'CW'
    else:
        ccw_segment_a_1 = False

    (ptCx, ptCy) = segment_a_2[1]

    a = (ptBx - ptAx) * (ptCy - ptAy)
    b = (ptBy - ptAy) * (ptCx - ptAx)
    if a > b:
        ccw_segment_a_2 = 'CCW'
    elif a < b:
        ccw_segment_a_2 = 'CW'
    else:
        ccw_segment_a_2 = False

    (ptAx, ptAy) = segment_b[0]
    (ptBx, ptBy) = segment_b[1]
    (ptCx, ptCy) = segment_b_1[1]

    a = (ptBx - ptAx) * (ptCy - ptAy)
    b = (ptBy - ptAy) * (ptCx - ptAx)
    if a > b:
        ccw_segment_b_1 = 'CCW'
    elif a < b:
        ccw_segment_b_1 = 'CW'
    else:
        ccw_segment_b_1 = False

    (ptCx, ptCy) = segment_b_2[1]

    a = (ptBx - ptAx) * (ptCy - ptAy)
    b = (ptBy - ptAy) * (ptCx - ptAx)
    if a > b:
        ccw_segment_b_2 = 'CCW'
    elif a < b:
        ccw_segment_b_2 = 'CW'
    else:
        ccw_segment_b_2 = False

    # If segments are parallels
    if ccw_segment_a_1 is False and ccw_segment_a_2 is False and ccw_segment_b_1 is False and ccw_segment_b_2 is False:
        segment_a_bbox = segment_to_bbox(segment_a)
        segment_b_bbox = segment_to_bbox(segment_b)
        return bbox_intersects_bbox(segment_a_bbox, segment_b_bbox)
    else:
        if ccw_segment_a_1 != ccw_segment_a_2:
            if ccw_segment_b_1 != ccw_segment_b_2:
                return True
        return False


def segment_intersects_bbox(segment, bbox):
    """

        Output :
            result (boolean) : True or False
    """
    (x_min, y_min, x_max, y_max) = bbox
    # if segment bbox intersect other bbox so segment intersect bbox :)
    segment_side_est = ((x_min, y_min), (x_min, y_max))
    segment_side_north = ((x_min, y_max), (x_max, y_max))
    segment_side_west = ((x_max, y_max), (x_max, y_min))
    segment_side_south = ((x_max, y_min), (x_min, y_min))
    
    side_degments = (segment_side_est, segment_side_north, segment_side_west, segment_side_south)
    for side in side_degments:
        if segment_intersects_segment(segment, side):
            return True

    return False


def bbox_intersects_bbox(bbox_a, bbox_b):
    """
    This function return a Truth Value Testing (True False) that qualifies the rectangle intersection


    True : bbox intersects
    False : bbox doesn't intersects

    The algorithm is inspired from : http://stackoverflow.com/questions/13390333/two-rectangles-intersection
                                    IA  : https://web.archive.org/web/*/http://stackoverflow.com/questions/13390333/two-rectangles-intersection

        Input :
            bbox_a : first boundary box
            bbox_b : second boundary box

        Output :
            result (boolean) : True or False

    """
    (x_min_a, y_min_a, x_max_a, y_max_a) = bbox_a
    (x_min_b, y_min_b, x_max_b, y_max_b) = bbox_b

    return x_min_a <= x_max_b and x_max_a >= x_min_b and y_min_a <= y_max_b and y_max_a >= y_min_b


def ccw_or_cw_segments(segment_a, segment_b):
    """
    Return orientation for two consecutives segments. The second coordinate in segment A must be the same
    that the first segment B coordinate.

    This function is inspired from  : https://www.toptal.com/python/computational-geometry-in-python-from-theory-to-implementation

        Input:
            segment_a(list/tuple) : linestring with two coordinates pairs.
            segment_b(list/tuple) : linestring with two coordinates pairs

        Output:
            sens: 'CCW': counter clock wise / CW: clock wise OR FALSE if segments are parallels
    """

    (pt_a_x, pt_a_y) = segment_a[0]
    (pt_b_x, pt_b_y) = segment_a[1]
    (pt_c_x, pt_c_y) = segment_b[1]

    if (pt_b_x - pt_a_x) * (pt_c_y - pt_a_y) > (pt_b_y - pt_a_y) * (pt_c_x - pt_a_x):
        return 'CCW'
    elif (pt_b_x - pt_a_x) * (pt_c_y - pt_a_y) == (pt_b_y - pt_a_y) * (pt_c_x - pt_a_x):
        return False
    else:
        return 'CW'


def point_position_segment(point, segment):
    """
        Input:

        Output:
            possible values : 'LEFT', 'RIGHT', 'ON'
    """

    segment_b = (segment[1], point)
    orientation = ccw_or_cw_segments(segment, segment_b)
    if orientation:
        if orientation == 'CCW':
            return 'LEFT'
        else:
            return 'RIGHT'
    else:
        return 'ON'
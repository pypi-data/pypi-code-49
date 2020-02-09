# Copyright 2018 - 2019 Ori Ben-Moshe - All rights reserved.
import cv2

from ..math_ import geometry
from .contour_filter import contour_filter


@contour_filter
def distance_sort(contour_list, point):
    """
     Sorts the contours according to their distance from the
    NOTE: it is important to area filter before image_center_sort
    :param contour_list: The list of contours to be sorted
    :type contour_list: List or one contour (numpy array)
    :param point: the point from which the distance of all contours are sorted by
    :return: the sorted contour list
    """
    if type(contour_list) is not list:
        return [contour_list]
    return sorted(contour_list,
                  key=lambda x: geometry.distance_between_points(point, geometry.contour_center(x)))


@contour_filter
def image_center_sort(contour_list, image_dimensions=(320, 240)):
    """
     sorts the contours from the closest to the center to the farthest.
    NOTE: it is important to area filter before image_center_sort
    :param contour_list: list of contours to be sorted
    :type contour_list: List or one contour (numpy array)
    :param image_dimensions: the dimensions of the image
    :return:
    """
    if type(contour_list) is not list:
        return [contour_list]
    image_center = ((image_dimensions[0] - 1) / 2, (image_dimensions[1] - 1) / 2)

    return sorted(contour_list,
                  key=lambda x: geometry.distance_between_points(image_center, geometry.contour_center(x)))


@contour_filter
def dec_area_sort(contour_list):
    """
     sorts the list of contours from the largest to the smallest based on area of the contour
    :param contour_list: List of Contours to be sorted
    :type contour_list: List or one contour (numpy array)
    :return: the contour list sorted.
    """
    if type(contour_list) is not list:
        return [contour_list]
    return sorted(contour_list, key=lambda x: cv2.contourArea(x), reverse=True)


@contour_filter
def inc_area_sort(contour_list):
    """
     sorts the list of contours from the smallest to the largest based on area of the contour
    :param contour_list: List of Contours to filter
    :type contour_list: List or one contour (numpy array)
    :return: the contour list sorted.
    """
    if type(contour_list) is not list:
        return [contour_list]
    return sorted(contour_list, key=lambda x: cv2.contourArea(x))


@contour_filter
def circle_sort(contour_list, area_limit=0.9, radius_limit=0.8):
    """
     sorts the list of contours according to how much they are circle from most similar to least
            using the circle rating function.
    :param contour_list: list of Contours to filter
    :type contour_list: list or one contour(numpy array)
    :param area_limit: The area limit for the circle rating, look at Geometry.circle_rating
    :param radius_limit: the radius limit for the circle rating, look at Geometry.circle_rating
    :return: the list sorted by circle rating
    """
    if type(contour_list) is not list:
        return [contour_list]
    return sorted(contour_list, key=lambda x: geometry.circle_rating(x, area_limit, radius_limit))


@contour_filter
def dec_length_sort(contour_list):
    """
     sorts the list of contours from the largest to the smallest based on area of the contour
    :param contour_list: List of Contours to filter
    :type contour_list: List or one contour (numpy array)
    :return: the contour list sorted.
    """
    if type(contour_list) is not list:
        return [contour_list]
    return sorted(contour_list, key=geometry.open_arc_length).reverse()


@contour_filter
def inc_length_sort(contour_list):
    """
     sorts the list of contours from the smallest to the largest based on area of the contour
    :param contour_list: List of Contours to filter
    :type contour_list: List or one contour (numpy array)
    :return: the contour list sorted.
    """
    if type(contour_list) is not list:
        return [contour_list]
    return sorted(contour_list, key=geometry.open_arc_length)

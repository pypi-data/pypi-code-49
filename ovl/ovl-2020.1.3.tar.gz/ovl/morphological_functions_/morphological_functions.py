import cv2

from ..image_filters_.kernels import rectangle_kernel, is_odd_size
from ..image_filters_.image_filter import image_filter


@image_filter
def erosion(mask, kernel=None, iterations=None, destination=None,
            anchor=None, border_type=None, border_values=None):
    """
     a copy of cv2.erode with default kernel of 5 by 5
    (a logical operation on the binary mask,
    whether every pixel's value should stay as it is based on neighboring pixels,
    which neighbors are chosen by the kernel and its dimensions)
    Erode demands all chosen neighbors must be True (white)
    For more information:
    https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

    :param mask: the binary image where the erosion morphological function should be applied
    :param kernel: the kernel that should be used
    :param iterations: Number of times the function should be applied
    :param destination: where the new image should be saved
    :param anchor: position of the anchor within the element
    :param border_values: border value in case of a constant border
    :param border_type: Pixel extrapolation technique for the border of the image
    see: https://docs.opencv.org/3.4.2/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5
    :return: the eroded binary mask
    """
    kernel = kernel or rectangle_kernel((5, 5))
    if not is_odd_size(kernel):
        raise ValueError("Received an invalid kernel: {} of type {}".format(kernel, type(kernel)))

    return cv2.erode(mask,
                     kernel,
                     dst=destination,
                     anchor=anchor,
                     iterations=iterations,
                     borderValue=border_values,
                     borderType=border_type)


@image_filter
def dilation(mask, kernel=None, iterations=None, destination=None,
             anchor=None, border_type=None, border_values=None):
    """
     a copy of cv2.dilate with default kernel of 5 by 5
    (a logical operation on the binary mask,
    whether every pixel's value should stay as it is based on neighboring pixels,
    which neighbors are chosen by the kernel and its dimensions)
    Dilation demands at least one chosen neighbors must be True (white)
    For more information:
    https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

    :param mask: the binary image where the erosion morphological function should be applied
    :param kernel: the kernel that should be used
    :param iterations: Number of times the function should be applied
    :param destination: where the new image should be saved
    :param anchor: position of the anchor within the element
    :param border_values: border value in case of a constant border
    :param border_type: sets the technique the pixels, that exceed the boundaries of the image for the use
                        of the kernel, are determined with (if they should mirror, copy
    see: https://docs.opencv.org/3.4.2/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5
    :return: the dilated binary mask
    """
    kernel = kernel or rectangle_kernel((5, 5))
    if not is_odd_size(kernel):
        raise ValueError("Received an invalid kernel: {} of type {}".format(kernel, type(kernel)))
    return cv2.dilate(mask,
                      kernel,
                      dst=destination,
                      anchor=anchor,
                      iterations=iterations,
                      borderValue=border_values,
                      borderType=border_type)

# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------
| Date                : August 2018
| Copyright           : (C) 2018 by Tinne Cahy (Geo Solutions) and Ann Crabbé (KU Leuven)
| Email               : tinne.cahy@geosolutions.be, ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from Local Maximum Filter [C++ software]
|                       Ghent University, Laboratory of Forest Management and Spatial Information Techniques
|                       Lieven P.C. Verbeke
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
| License as published by the Free Software Foundation; either version 3 of the License, or any later version.
| ----------------------------------------------------------------------------------------------------------------
"""
import numpy as np  # numpy 2.13 or later


class LocalMaxFilter:
    """
    A window is used to slide over an image and look for maximum reflectance values in the center of that window.
    """

    def __init__(self, window_length):
        """
        The function also determines some derivatives of the input length of the square sliding window to simplify
        the calculations of the other functions in the class.

        :param int window_length: The length of a square window expressed in the number of pixels
        """
        self.window_length = int(window_length)
        self.argcenter = int(self.window_length * self.window_length / 2)
        self.window_half = int(self.window_length/2)
        self.window_shape = (self.window_length, self.window_length)

    def _sliding_window(self, image_array):
        """
        Private helper function of the sliding window yielding for each step the current positions (x, y) and
        the image content of the sliding window. Step size will be set to 1.

        Based on https://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/

        :param ndarray image_array: Numpy array image
        :return:
        """
        # slide a window across the image
        for y in range(0, image_array.shape[0]):
            for x in range(0, image_array.shape[1]):
                # yield the current window
                yield (x, y, image_array[y:y + self.window_length, x:x + self.window_length])

    @staticmethod
    def _eliminate_points(input_dict, snap_distance, geo_transform):
        """
        This SNAP function will remove tree points that are to close to each other. The function will return a mean
        value for those points.

        :param input_dict: dictionary build with the execute function
        :param snap_distance: minimum distance between two points (tree top)
        :param geo_transform: contains the pixel size of the raster
        :return: new_dict: a new dictionary containing the tree location
        """

        pixel_size_x = geo_transform[1]
        pixel_size_y = -geo_transform[5]
        # extract x, y and IR values from the data frame
        xyir = []
        for i in input_dict:
            xyir.append([(i['Pixel']['x']), (i['Pixel']['y']), (i['RasterVal'])])
        xyir = np.array(xyir)

        # create new points based on a buffer with radius = snap_distance
        new_points = []
        # store the points which are not in a pair
        # the distance between two points is defined by the buffer.
        # Because coordinates are set as pixel location on the raster we need to multiply the pixel position with
        #   the pixel width to find distance in meters.

        not_a_pair = []
        for i in range(len(xyir)):
            pairs = []
            for j in range(len(xyir)):
                buffer = (((xyir[j, 0] - xyir[i, 0])*pixel_size_x)**2 + ((xyir[j, 1] - xyir[i, 1])*pixel_size_y)**2)
                if buffer < snap_distance**2:
                    pairs.append(xyir[j, :])
            if len(pairs) < 2:
                not_a_pair.append(xyir[i, :])
            mean = np.mean(pairs, axis=0)
            new_points.append(mean)

        new_points = np.array(new_points)
        new_points = np.unique(new_points, axis=0)
        not_a_pair = np.array(not_a_pair)

        # combine the mean of the pairs and the points which weren't in a pair
        new_dictionary = np.concatenate((not_a_pair, new_points), 0)
        new_dictionary = np.unique(new_dictionary, axis=0)

        new_dict = []
        for i in range(len(new_dictionary)):
            new_dict.append({
                'RasterVal': new_dictionary[i, 2],
                'Pixel': {'x': new_dictionary[i, 0], 'y': new_dictionary[i, 1]}
            })

        return new_dict

    def execute(self, image_array, area_of_interest=None, snap=None, geo_transform=None, p=None):
        """
        The function will return an image containing the reflectance values of the local max of a sliding window
        going over the input image. It is possible to include an area of interest

        :param ndarray image_array: 2D Numpy array image
        :param ndarray area_of_interest: 2D Numpy array image indicating with 0 and 1 the area of interest
        :param snap: defines the snap distance
        :param geo_transform: contains the pixel size of the raster
        :param p: a reference to a function to update the progress bar
        :return: dict: Dictionary containing the reflectance values of the local max together with pixel locations
        """
        if len(image_array.shape) != 2:
            raise Exception("The image array must be 2D.")
        # Area of non interest contains 0 values. Make sure that there are no 0 values left in image_array
        image_array += 1
        image_array = image_array * area_of_interest if area_of_interest is not None else image_array
        local_max_dict = []
        for (x, y, window) in self._sliding_window(image_array):
            if window.shape == self.window_shape and np.all(window):
                if window.max() != window.min() and np.take(window, self.argcenter) == window.max():
                    if window.max() > 0:
                        # first set values back to original and to local_max_array
                        local_max_dict.append({
                            'RasterVal': window.max() - 1,
                            'Pixel': {'x': x + self.window_half, 'y': y + self.window_half}
                        })
            if p:
                p(y/image_array.shape[0]*100)
        if snap:
            local_max_dict = self._eliminate_points(local_max_dict, snap, geo_transform)
        return local_max_dict

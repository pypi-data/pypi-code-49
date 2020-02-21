#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Tuple

import numpy as np


class GisaxsParameters(object):
    def __init__(self, *,
                 image_size: Tuple[int, int] = (1030, 514),
                 beam_center: Tuple[int, int] = (314, 265),
                 wavelength: float = 1.5307,
                 angle_of_incidence_deg: float = 0.1,
                 detector_distance: int = 5292,
                 pixel_size: float = 0.075):
        """

        :param image_size: image size in pixels
        :param beam_center: tuple of beam center pixels coordinates
        :param wavelength: wavelength [A]
        :param angle_of_incidence_deg: [deg]
        :param detector_distance: [mm]
        :param pixel_size: [mm]
        """
        self.size = image_size
        self.beam_center = beam_center
        self.wavelength = wavelength
        self.angle_of_incidence_deg = angle_of_incidence_deg
        self.angle_of_incidence = angle_of_incidence_deg / 180 * np.pi
        self.detector_distance = detector_distance
        self.pixel_size = pixel_size
        self.k0 = 2 * np.pi / self.wavelength

    @classmethod
    def init_from_folder_number(cls, folder_num: int):
        if folder_num <= 42:
            return cls(beam_center=(247, 265))
        else:
            return cls()

    def get_angle_vectors(self, *,
                          flip: bool = True, units: str = 'rad') -> Tuple[np.array, np.array]:
        """
        Returns image axes in provided units (degrees or radians).

        :param flip: if True, flips both axes (True by default)
        :param units: 'rad' or 'deg'
        :return: two numpy arrays of image axes
        """
        if units not in ('rad', 'deg'):
            raise ValueError('Unknown units %s, should be deg or rad' % units)
        x_vector = np.flip(np.linspace(1, self.size[1], self.size[1]) - self.size[1] +
                           self.beam_center[0], axis=0) * self.pixel_size
        y_vector = np.flip(np.linspace(1, self.size[0], self.size[0]) -
                           self.beam_center[1], axis=0) * self.pixel_size - \
                   self.detector_distance * np.tan(
            self.angle_of_incidence)
        angle_x = np.arctan(x_vector / self.detector_distance)
        angle_y = np.arctan(y_vector / self.detector_distance)
        if flip:
            angle_x = np.flip(angle_x, axis=0)
            angle_y = np.flip(angle_y, axis=0)
        if units == 'deg':
            angle_x *= 180 / np.pi
            angle_y *= 180 / np.pi
        return angle_x, angle_y

    def get_q_vectors(self, back_reshape: bool = True):
        angle_xx, angle_yy = self.get_angle_vectors()
        size = len(angle_xx) * len(angle_yy)
        angle_x, angle_y = np.meshgrid(angle_xx, angle_yy)
        angle_x = angle_x.reshape((1, size))[0]
        angle_y = angle_y.reshape((1, size))[0]
        q_xy = self.k0 * np.sign(angle_x) * \
               np.sqrt((np.cos(angle_y) * np.cos(angle_x) - np.cos(self.angle_of_incidence)) ** 2 +
                       (np.cos(angle_y) * np.sin(angle_x)) ** 2)
        q_z = self.k0 * (np.sin(angle_y) + np.sin(self.angle_of_incidence))

        if back_reshape:
            q_xy = self.back_reshape(q_xy)
            q_z = self.back_reshape(q_z)
        return [q_xy, q_z]

    def back_reshape(self, data):
        data = np.reshape(data, (self.size[0], self.size[1]))
        data = np.flip(data, axis=0)
        data = np.rot90(data, k=1)
        data = np.flip(data, axis=1)
        data = np.reshape(data, (1, self.size[1] * self.size[0]))[0]
        return data

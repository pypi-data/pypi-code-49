# -*- coding: utf-8 -*-

from enum import Enum, auto
import numpy as np


class XPCSModes(Enum):
    mean = auto()
    std = auto()


def calculate_2d_corr(intensity_array: np.ndarray,
                      mode: XPCSModes) -> np.ndarray:
    """
    Calculated two-time correlation function from an intensity array
    for two possible modes: mean or std.
    :param intensity_array: A 2-dimensional ndarray with a shape (time_axis, pixel_axis).
    :param mode: a XPCSModes value (XPCSModes.mean or XPCSModes.std).
    :return: A 2-dimensional array with a shape (time_axis, time_axis).
    """
    if mode == XPCSModes.mean:
        intensity_array /= intensity_array.mean(axis=1)[:, np.newaxis]
        return intensity_array.dot(intensity_array.transpose()) / intensity_array.shape[1]
    elif mode == XPCSModes.std:
        std_array = intensity_array.std(axis=1)[:, np.newaxis]
        std_array[std_array == 0] = 1
        intensity_array /= std_array
        res = intensity_array.dot(intensity_array.transpose()) / intensity_array.shape[1]
        i_mean = np.expand_dims(intensity_array.mean(axis=1), axis=1)
        res -= i_mean.dot(i_mean.transpose())
        return res
    else:
        raise ValueError(f'Unknown XPCS mode: {mode}.')


def calculate_1d_corr(intensity_array: np.ndarray) -> np.ndarray:
    """
    Calculates one-time correlation function from an intensity array.
    :param intensity_array: A 2-dimensional ndarray with a shape (time_axis, pixel_axis).
    :return: A 1-dimensional array with a size time_axis.
    """

    norm_constant = intensity_array.mean(axis=1).mean(axis=0) ** 2
    corr_matrix = intensity_array.dot(intensity_array.transpose()) / intensity_array.shape[1]
    corr_function = np.empty(intensity_array.shape[0])

    for t in range(corr_matrix.shape[0]):
        corr_function[t] = corr_matrix.diagonal(t).mean() / norm_constant
    return corr_function

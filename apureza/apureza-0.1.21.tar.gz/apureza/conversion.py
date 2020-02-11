# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

import numpy as np

from rasterio import open as rasterio_open

__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2019, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'


def csv_to_rgb(path_to_csv, out_path):
    """

    :param path_to_csv:
    :param out_path:
    :return:
    """


def rgb_to_csv(path_to_rgb, out_path, delimiter=","):
    """

    :param path_to_rgb:
    :param out_path:
    :param delimiter:
    :return:
    """
    band_images = []
    with rasterio_open(path_to_rgb) as src:
        for band in range(src.count):
            band_images.append([src.read(band + 1).ravel()])

    rgb = np.concatenate(band_images).transpose()
    np.savetxt(out_path, rgb, delimiter=delimiter)

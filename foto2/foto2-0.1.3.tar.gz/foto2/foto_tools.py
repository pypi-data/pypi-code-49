# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""
import warnings

import numpy as np

from itertools import chain, islice

from foto2.exceptions import ImportSklearnWarning

try:
    import sklearn.decomposition
except ModuleNotFoundError:
    SKLEARN_SUPPORT = False
    warnings.warn("No scikit-learn module found, PCA support will be internal", ImportSklearnWarning)
else:
    SKLEARN_SUPPORT = True

__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2019, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'

from numba import jit


def azimuthal_average(psd):
    """ Calculate the azimuthally averaged radial profile.

    :param psd: 2D power spectrum density
    """
    # Get indices
    y, x = np.indices(psd.shape)

    # Get radii as integer
    r = np.sqrt((x - (psd.shape[1] - 1) / 2) ** 2 + (y - (psd.shape[0] - 1) / 2) ** 2).astype(np.int)

    # average radial profile = sums for each radius bin / number of radius bin
    return np.bincount(r.ravel(), psd.ravel()) / np.bincount(r.ravel())


@jit(nopython=True)
def get_block_windows(window_size, raster_x_size, raster_y_size):
    """

    :param window_size:
    :param raster_x_size:
    :param raster_y_size:
    :return:
    """
    for y in range(0, raster_y_size, window_size):
        ysize = min(window_size, raster_y_size - y)
        for x in range(0, raster_x_size, window_size):
            xsize = min(window_size, raster_x_size - x)

            yield x, y, xsize, ysize


@jit(nopython=True)
def get_moving_windows(window_size, raster_x_size, raster_y_size, step=1):
    """

    :param window_size:
    :param raster_x_size:
    :param raster_y_size:
    :param step:
    :return:
    """
    offset = int((window_size - 1) / 2)  # window_size must be an odd number
    # for each pixel, compute indices of the window (all included)
    for y in range(0, raster_y_size, step):
        y1 = max(0, y - offset)
        y2 = min(raster_y_size - 1, y + offset)
        ysize = (y2 - y1) + 1
        for x in range(0, raster_x_size, step):
            x1 = max(0, x - offset)
            x2 = min(raster_x_size - 1, x + offset)
            xsize = (x2 - x1) + 1

            yield x1, y1, xsize, ysize


def pca(data, n_components, sklearn_pca=SKLEARN_SUPPORT):
    """ Principal component analysis

    :param data:
    :param n_components: number of dimensions for PCA
    :param sklearn_pca: use sklearn.decomposition.PCA class
    :return:
    """

    # replace nodata and inf values and standardize
    data = np.nan_to_num(data)
    data -= data.mean(axis=0)
    data /= data.std(axis=0)
    # data = StandardScaler().fit_transform(data)

    if sklearn_pca:
        sk_pca = sklearn.decomposition.PCA(n_components=n_components)
        return sk_pca.fit_transform(data)
    else:
        # get normalized covariance matrix
        c = np.cov(data.T)
        # get the eigenvalues/eigenvectors
        eig_val, eig_vec = np.linalg.eig(c)
        # get sort index of eigenvalues in ascending order
        idx = np.argsort(eig_val)[::-1]
        # sorting the eigenvectors according to the sorted eigenvalues
        eig_vec = eig_vec[:, idx]
        # cutting some PCs if needed
        eig_vec = eig_vec[:, :n_components]
        # return projection of the data in the new space
        return np.dot(data, eig_vec)


def rspectrum(window):
    """ Compute r-spectrum within window

    :param window: window array
    :return:
    """
    # window_center = window - np.nanmean(window)

    # Fast Fourier Transform (FFT) in 2 dims, center fft and then calculate 2D power spectrum density
    ft = np.fft.fft2(window)
    ft = np.fft.fftshift(ft)
    psd = np.abs(ft)**2

    # psd = psd/np.var(data)  Standardize by variance ?

    # Calculate the azimuthally averaged 1D power spectrum (also called radial spectrum)
    return azimuthal_average(psd)


def chunks(iterable, size=10):
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))

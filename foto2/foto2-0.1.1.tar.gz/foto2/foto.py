# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""
import multiprocessing as mp
import warnings

import gdal
from numba import jit
import numpy as np
# from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from utils.check import check_string, lazyproperty

from foto2.exceptions import FotoError, ImportSklearnWarning

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


class Foto:
    """

    """

    _max_sample = 29
    _n_components = 3

    window_size = None
    r_spectra = None
    nb_sample = None
    rgb = None

    def __init__(self, path_to_raster, method="block"):
        """

        :param path_to_raster: path to raster file (must be gdal readable)
        """
        self._dataset = gdal.Open(path_to_raster, gdal.GA_ReadOnly)
        self._image = self._dataset.ReadAsArray()
        self.method = method

    def run(self, window_size, nb_processes=mp.cpu_count(), progress_bar=False):
        """ Run FOTO algorithm

        :param window_size:
        :param nb_processes:
        :param progress_bar: display progress bar (may increase CPU time)
        :return:
        """
        # Get the optimal number of sampled frequencies N/2 (Nyquist frequency), and be in [3, max_sample] range
        self.nb_sample = min(max(int(window_size / 2), 3), self._max_sample)
        self.window_size = window_size
        window_generator = (self._image[w[1]:w[1] + w[3], w[0]:w[0] + w[2]] for w in self.windows)

        # Compute r-spectra
        if progress_bar:
            progress_length = len(list(self.windows))
            with mp.Pool(processes=nb_processes) as pool:
                r_spectra = list(tqdm(pool.imap(rspectrum, window_generator, chunksize=500),
                                      total=progress_length, desc="Compute R-spectra:"))
        else:
            with mp.Pool(processes=nb_processes) as pool:
                r_spectra = pool.map(rspectrum, window_generator)

        if self.method == "block":
            self.r_spectra = np.asarray([r[0:self.nb_sample] for r, w in zip(r_spectra, self.windows)
                                         if w[2] == w[3] == window_size])
        else:
            pass

        # PCA analysis
        rgb = pca(self.r_spectra, self._n_components)

        # RGB _image
        if self.method == "block":
            self.rgb = np.expand_dims(rgb, axis=1).reshape((int(self.height / window_size),
                                                            int(self.width / window_size), 3))
        else:
            pass

    @property
    def image(self):
        return self._image

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        try:
            self._method = check_string(method, {'block', 'moving_window'})
        except ValueError:
            raise FotoError("Method must be either 'block' or 'moving_window'")

    @lazyproperty
    def height(self):
        return self._image.shape[0]

    @lazyproperty
    def width(self):
        return self._image.shape[1]

    @property
    def windows(self):
        if self.method == 'block':
            return get_block_windows(self.window_size, self.width, self.height)
        else:
            return get_moving_windows(self.window_size, self.width, self.height, 5)


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

            yield (x, y, xsize, ysize)


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

            yield (x1, y1, xsize, ysize)


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


if __name__ == "__main__":
    from utils.sys.timer import Timer
    from matplotlib import pyplot as plt
    test = Foto("/home/benjamin/Desktop/APUREZA/FOTO/SUBSET_PLEIADES_20160915_Pan.tif", method="block")
    for w_size in [11]:
        with Timer() as t:
            test.run(w_size, progress_bar=True)
        print("spent time (%d): %s" % (w_size, t))
    plt.imshow(test.rgb)
    plt.show()

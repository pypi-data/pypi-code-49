# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""
import multiprocessing as mp

import gdal
import numpy as np
# from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from utils.check import check_string, lazyproperty

from foto2.exceptions import FotoError


__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2019, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'

from foto2.foto_tools import rspectrum, pca, get_block_windows, get_moving_windows


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
                                      total=progress_length, desc="Compute R-spectra"))
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
            return get_moving_windows(self.window_size, self.width, self.height)


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

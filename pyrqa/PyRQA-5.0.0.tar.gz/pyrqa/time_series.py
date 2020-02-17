#!/usr/bin/env python

"""
Time Series.
"""

import numpy as np

from pyrqa.exceptions import TimeDelayReconstructionNotSupportedException, \
    UnsupportedDataTypeException

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015, 2018, 2019, 2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"

SUPPORTED_DATA_TYPES = (np.dtype('float16'),
                        np.dtype('float32'),
                        np.dtype('float64'))


class TimeSeries(object):
    """
    Time series. The reconstruction of vectors is conducted using the time delay method.
    """
    def __init__(self,
                 data,
                 dtype=np.float32,
                 embedding_dimension=2,
                 time_delay=2):
        self.dtype = dtype
        self.data = data
        self.embedding_dimension = embedding_dimension
        self.time_delay = time_delay

    @property
    def dtype(self):
        return self.__dtype

    @dtype.setter
    def dtype(self,
              dtype):
        if dtype not in SUPPORTED_DATA_TYPES:
            raise UnsupportedDataTypeException("Data type '%s' is not supported. Please select either numpy data type float16, float32 or float64." % dtype)

        self.__dtype = dtype

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,
             data):
        self.__data = np.array(data, dtype=self.dtype)

    @property
    def length(self):
        return len(self.data)

    @property
    def offset(self):
        """
        Time series offset based on embedding dimension and time delay.
        """
        return (self.embedding_dimension - 1) * self.time_delay

    @property
    def number_of_vectors(self):
        if self.length - self.offset < 0:
            return 0

        return self.length - self.offset

    def get_vector(self,
                   idx):

        vector = np.zeros(self.embedding_dimension,
                          dtype=self.dtype)

        for dim in np.arange(self.embedding_dimension):
            vector[dim] = self.data[idx + (dim * self.time_delay)]

        return vector

    def get_vectors(self, start, count):
        recurrence_vectors = []

        for dim in np.arange(self.embedding_dimension):
            offset = dim * self.time_delay
            recurrence_vectors.append(self.data[(start + offset):(start + offset + count)])

        return np.array(recurrence_vectors,
                        dtype=self.dtype).transpose().ravel()

    def get_vectors_iterator(self,
                             start,
                             count):
        """
        Get vectors from the original time series (iterator).

        :param start: Start index within the original time series.
        :param count: Number of vectors to be extracted.
        :returns: Extracted vectors.
        :rtype: 1D array.
        """
        recurrence_vectors = np.zeros(count * self.embedding_dimension,
                                      dtype=self.dtype)

        for dim in np.arange(self.embedding_dimension):
            offset = dim * self.time_delay

            for idx in np.arange(count):
                recurrence_vectors[idx * self.embedding_dimension + dim] = self.data[start + idx + offset]

    def get_vectors_as_2d_array(self,
                                start,
                                count):
        recurrence_vectors = self.get_vectors(start,
                                              count)

        recurrence_vectors.shape = (np.int(recurrence_vectors.size / self.embedding_dimension),
                                    self.embedding_dimension)

        return recurrence_vectors

    def get_sub_series(self, start, count):
        """
        Get sub time series from the original time series.

        :param start: Start index within the original time series.
        :param count: Number of data points to be extracted.
        :returns: Extracted sub time series.
        :rtype: 1D array.
        """
        return self.data[start:start + count + self.offset]

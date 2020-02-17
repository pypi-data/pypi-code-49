#!/usr/bin/env python

"""
Settings
"""

import os

import numpy as np

from pyrqa.analysis_type import Classic
from pyrqa.metric import EuclideanMetric
from pyrqa.neighbourhood import FixedRadius, \
    FAN, \
    RadiusCorridor

from pyrqa.time_series import TimeSeries
from pyrqa.exceptions import InvalidTimeSeriesInputException, \
    DeviatingEmbeddingDimensionException, \
    DeviatingTimeDelayException, \
    DeviatingFloatingPointPrecisionException

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015, 2018, 2019, 2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"

DTYPE_TO_CLASS_MAPPING = {np.dtype('float16'): np.float16,
                          np.dtype('float32'): np.float32,
                          np.dtype('float64'): np.float64}


class Settings(object):
    """
    Settings of recurrence analysis computations.

    :ivar time_series: Time series to be analyzed.
    :ivar analysis_type: Type of recurrence analysis.
    :ivar similarity_measure: Similarity measure, e.g., EuclideanMetric.
    :ivar neighbourhood: Neighbourhood for detecting neighbours, e.g., FixedRadius(1.0).
    :ivar theiler_corrector: Theiler corrector.
    """

    def __init__(self,
                 time_series,
                 analysis_type=Classic,
                 similarity_measure=EuclideanMetric,
                 neighbourhood=FixedRadius(),
                 theiler_corrector=1):
        self.computing_type = analysis_type
        self.similarity_measure = similarity_measure
        self.neighbourhood = neighbourhood
        self.theiler_corrector = theiler_corrector

        self.time_series_x = self.get_time_series(time_series,
                                                  0)

        self.time_series_y = self.get_time_series(time_series,
                                                  1)

    @staticmethod
    def get_time_series(time_series,
                        ind):
        if type(time_series) is TimeSeries:
            return time_series
        if type(time_series) is tuple or type(time_series) is list:
            if len(time_series) == 1:
                return time_series
            elif len(time_series) == 2:
                return time_series[ind]
        else:
            raise InvalidTimeSeriesInputException(
                "Either a single time series or tuple/list of two time series should be passed as argument.")

    @property
    def time_series_x(self):
        try:
            return self.__time_series_x
        except Exception:
            return None

    @time_series_x.setter
    def time_series_x(self,
                      time_series_x):
        if not type(time_series_x) == TimeSeries:
            raise InvalidTimeSeriesInputException("Time series x is not of type TimeSeries.")

        self.__time_series_x = time_series_x

    @property
    def time_series_y(self):
        try:
            return self.__time_series_y
        except Exception:
            return None

    @time_series_y.setter
    def time_series_y(self,
                      time_series_y):
        if not type(time_series_y) == TimeSeries:
            raise InvalidTimeSeriesInputException("Time series y is not of type TimeSeries.")

        self.__time_series_y = time_series_y

    @property
    def embedding_dimension(self):
        if not self.time_series_x.embedding_dimension == self.time_series_y.embedding_dimension:
            raise DeviatingEmbeddingDimensionException(
                "Embedding dimension '%d' of time series x deviates from embedding dimension '%d' of time series y." % (
                    self.time_series_x.embedding_dimension,
                    self.time_series_y.embedding_dimension))

        return self.time_series_x.embedding_dimension

    @property
    def time_delay(self):
        if not self.time_series_x.time_delay == self.time_series_y.time_delay:
            raise DeviatingTimeDelayException(
                "Time delay '%d' of time series x deviates from time delay '%d' of time series y." % (
                    self.time_series_x.time_delay,
                    self.time_series_y.time_delay))

        return self.time_series_x.time_delay

    @property
    def dtype(self):
        if not self.time_series_x.dtype == self.time_series_y.dtype:
            raise DeviatingFloatingPointPrecisionException(
                "Dtype '%s' of time series x deviates from dtype '%s' of time series y." % (self.time_series_x.dtype,
                                                                                            self.time_series_y.dtype))

        return self.time_series_x.dtype

    @property
    def max_number_of_vectors(self):
        if self.time_series_x and self.time_series_y:
            if self.time_series_x.length > self.time_series_y.length:
                return self.time_series_x.number_of_vectors
            else:
                return self.time_series_y.number_of_vectors
        elif not self.time_series_x:
            raise InvalidTimeSeriesInputException("Missing time series x.")
        elif not self.time_series_y:
            raise InvalidTimeSeriesInputException("Missing time series y.")

    @property
    def base_path(self):
        """
        Base path of the project.
        """

        return os.path.dirname(os.path.abspath(__file__))

    @property
    def is_matrix_symmetric(self):
        """
        Is the recurrence matrix symmetric?
        """

        return self.similarity_measure.is_symmetric() and \
            not isinstance(self.neighbourhood, FAN) and \
            self.computing_type is Classic

    @property
    def create_matrix_prefix(self):
        """
        Get prefix of the name of the kernel function to create the recurrence matrix.

        :rtype: String.
        """

        return "create_matrix"

    @property
    def detect_vertical_lines_prefix(self):
        """
        Get prefix of the name of the kernel function to detect vertical lines.

        :rtype: String.
        """

        return "detect_vertical_lines"

    @property
    def detect_diagonal_lines_prefix(self):
        """
        Get prefix of the name of the kernel function to detect diagonal lines.

        :rtype: String.
        """

        if self.is_matrix_symmetric:
            return "detect_diagonal_lines_symmetric"

        return "detect_diagonal_lines"

    @staticmethod
    def get_kernel_function_name(prefix,
                                 suffix):
        """
        Get the full name of the kernel function to select.

        :param prefix: Prefix of the kernel fucntion name.
        :param suffix: Suffix of the kernel fucntion name.
        :rtype: String.
        """

        if suffix:
            return "_".join([prefix,
                             suffix])

        return prefix

    @property
    def create_matrix_kernel_name(self):
        """
        Full name of the kernel function to create the recurrence matrix

        :rtype: String.
        """

        return self.get_kernel_function_name(self.create_matrix_prefix,
                                             self.neighbourhood.name)

    @property
    def detect_vertical_lines_kernel_name(self):
        """
        Full name of the kernel function to detect vertical lines.

        :rtype: String.
        """

        return self.get_kernel_function_name(self.detect_vertical_lines_prefix,
                                             self.neighbourhood.name)

    @property
    def detect_diagonal_lines_kernel_name(self):
        """
        Full name of the kernel function to detect diagonal lines.

        :rtype: String.
        """

        return self.get_kernel_function_name(self.detect_diagonal_lines_prefix,
                                             self.neighbourhood.name)

    @property
    def kernels_sub_dir(self):
        """
        Get the path of the kernel sub directory.

        :rtype: String.
        """

        return self.similarity_measure.name

    @property
    def dtype(self):
        """
        Floating point data type for the time series.
        """

        return DTYPE_TO_CLASS_MAPPING[self.time_series_x.data.dtype]

    @staticmethod
    def clear_buffer_kernel_name(data_type):
        """
        Get name of the kernel function used to clear a buffer.

        :param data_type: Data type that is used to represent the data values.
        :return: Name of clear buffer kernel.
        :rtype: String.
        """

        return "clear_buffer_%s" % data_type.__name__

    def __str__(self):
        return "Recurrence Analysis Settings\n" \
               "----------------------------\n" \
               "Similarity measure: %s\n" \
               "Neighbourhood: %s\n" \
               "Theiler corrector: %d\n" \
               "Matrix symmetry: %r\n" % (self.similarity_measure.__name__,
                                          self.neighbourhood,
                                          self.theiler_corrector,
                                          self.is_matrix_symmetric)

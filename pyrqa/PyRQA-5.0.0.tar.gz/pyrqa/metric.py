#!/usr/bin/env python

"""
Distance metrics
"""

import math

import numpy as np

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015, 2018, 2019, 2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"


class Metric(object):
    """
    Base metric.
    """

    name = 'metric'

    @classmethod
    def is_symmetric(cls):
        """
        Is the metric symmetric?
        """

        return True

    @classmethod
    def get_p(cls):
        """
        Get p value of metric.
        """

        pass

    @classmethod
    def get_distance_time_series(cls,
                                 time_series_x,
                                 time_series_y,
                                 embedding_dimension,
                                 time_delay_x,
                                 time_delay_y,
                                 index_x,
                                 index_y):
        """
        Get distance between two vectors (time series representation).

        :param time_series_x: Time series on X axis.
        :param time_series_y: Time series on Y axis.
        :param embedding_dimension: Embedding dimension.
        :param time_delay_x: Time delay of the time series on the X axis.
        :param time_delay_y: Time delay of the time series on the Y axis.
        :param index_x: Index on X axis.
        :param index_y: Index on Y axis.
        :returns: Distance between two vectors.
        :rtype: Float value.
        """

        pass

    @classmethod
    def get_distance_vectors(cls,
                             vectors_x,
                             vectors_y,
                             embedding_dimension,
                             index_x,
                             index_y):
        """
        Get distance between two vectors (vectors representation).

        :param vectors_x: Vectors on X axis.
        :param vectors_y: Vectors on Y axis.
        :param embedding_dimension: Embedding dimension.
        :param index_x: Index on X axis.
        :param index_y: Index on Y axis.
        :returns: Distance between two vectors.
        :rtype: Float value.
        """

        pass


class TaxicabMetric(Metric):
    """
    Taxicab metric (L_1).
    """

    name = 'taxicab_metric'

    @classmethod
    def get_p(cls):
        return 1.0

    @classmethod
    def get_distance_time_series(cls,
                                 time_series_x,
                                 time_series_y,
                                 embedding_dimension,
                                 time_delay_x,
                                 time_delay_y,
                                 index_x,
                                 index_y):

        distance = 0

        for idx in np.arange(embedding_dimension):
            temp_x = index_x + (idx * time_delay_x)
            temp_y = index_y + (idx * time_delay_y)

            distance += math.fabs(time_series_x[temp_x] - time_series_y[temp_y])

        return distance

    @classmethod
    def get_distance_vectors(cls,
                             vectors_x,
                             vectors_y,
                             embedding_dimension,
                             index_x,
                             index_y):
        distance = 0

        for idx in np.arange(embedding_dimension):
            temp_x = index_x * embedding_dimension + idx
            temp_y = index_y * embedding_dimension + idx

            distance += math.fabs(vectors_x[temp_x] - vectors_y[temp_y])

        return distance


class EuclideanMetric(Metric):
    """
    Euclidean metric (L_2).
    """

    name = 'euclidean_metric'

    @classmethod
    def get_p(cls):
        return 2.0

    @classmethod
    def get_distance_time_series(cls,
                                 time_series_x,
                                 time_series_y,
                                 embedding_dimension,
                                 time_delay_x,
                                 time_delay_y,
                                 index_x,
                                 index_y):
        distance = 0

        for idx in np.arange(embedding_dimension):
            temp_x = index_x + (idx * time_delay_x)
            temp_y = index_y + (idx * time_delay_y)

            distance += math.pow(time_series_x[temp_x] - time_series_y[temp_y], 2)

        return math.sqrt(distance)

    @classmethod
    def get_distance_vectors(cls,
                             vectors_x,
                             vectors_y,
                             embedding_dimension,
                             index_x,
                             index_y):
        distance = 0

        for idx in np.arange(embedding_dimension):
            temp_x = index_x * embedding_dimension + idx
            temp_y = index_y * embedding_dimension + idx

            distance += math.pow(vectors_x[temp_x] - vectors_y[temp_y], 2)

        return math.sqrt(distance)


class MaximumMetric(Metric):
    """
    Maximum metric (L_inf).
    """

    name = 'maximum_metric'

    @classmethod
    def get_p(cls):
        return np.float("inf")

    @classmethod
    def get_distance_time_series(cls,
                                 time_series_x,
                                 time_series_y,
                                 embedding_dimension,
                                 time_delay_x,
                                 time_delay_y,
                                 index_x,
                                 index_y):
        distance = np.finfo(np.float32).min

        for index in np.arange(embedding_dimension):
            temp_x = index_x + (index * time_delay_x)
            temp_y = index_y + (index * time_delay_y)

            value = math.fabs(time_series_x[temp_x] - time_series_y[temp_y])

            if value > distance:
                distance = value

        return distance

    @classmethod
    def get_distance_vectors(cls,
                             vectors_x,
                             vectors_y,
                             embedding_dimension,
                             index_x,
                             index_y):
        distance = np.finfo(np.float32).min

        for idx in np.arange(embedding_dimension):
            temp_x = index_x * embedding_dimension + idx
            temp_y = index_y * embedding_dimension + idx

            value = math.fabs(vectors_x[temp_x] - vectors_y[temp_y])

            if value > distance:
                distance = value

        return distance

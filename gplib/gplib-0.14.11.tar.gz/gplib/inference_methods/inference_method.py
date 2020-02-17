# -*- coding: utf-8 -*-
#
#    Copyright 2019 Ibai Roman
#
#    This file is part of GPlib.
#
#    GPlib is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    GPlib is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with GPlib. If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import scipy.linalg


class InferenceMethod(object):
    """

    """

    def __init__(self, cache_size=10):

        self.gp = None
        self.cache = {
            'size': cache_size,
            'cov_hashes': [],
            'data': [],
            'l_matrices': []
        }

    def set_gp(self, gp):
        """

        :param gp:
        :type gp:
        :return:
        :rtype:
        """
        self.gp = gp

    def marginalize_gp(self, data_x, data_y=None):
        """

        :param data_x:
        :type data_x:
        :param data_y:
        :type data_y:
        :return:
        :rtype:
        """

        raise NotImplementedError("Not Implemented. This is an interface.")

    def loocv(self, data_x, data_y=None):
        """

        :param data_x:
        :type data_x:
        :param data_y:
        :type data_y:
        :return:
        :rtype:
        """

        raise NotImplementedError("Not Implemented. This is an interface.")

    def get_l_matrix(self, data_x):
        """

        :param data_x:
        :type data_x:
        :return:
        :rtype:
        """
        cov_hash = hash(self.gp.covariance_function)

        best_i = None
        best_size_diff = np.inf
        for cache_i in range(len(self.cache['cov_hashes'])):
            cached_cov_hash = self.cache['cov_hashes'][cache_i]
            if cached_cov_hash == cov_hash:
                cached_data = self.cache['data'][cache_i]

                data_size = min(cached_data.shape[0], data_x.shape[0])
                cached_data_hash = hash(cached_data[:data_size, :].tostring())
                data_x_hash = hash(data_x[:data_size, :].tostring())

                size_diff = np.abs(cached_data.shape[0] - data_x.shape[0])

                if cached_data_hash == data_x_hash and \
                        size_diff < best_size_diff:
                    best_i = cache_i
                    best_size_diff = size_diff

        if best_i is not None:
            cached_data = self.cache['data'][best_i]
            cached_l_matrix = self.cache['l_matrices'][best_i]
            if cached_data.shape[0] == data_x.shape[0]:
                return cached_l_matrix
            elif cached_data.shape[0] < data_x.shape[0]:
                covariance = \
                    self.gp.covariance_function.marginalize_covariance(
                        data_x
                    )
                l_matrix = InferenceMethod._update_chol(
                    covariance,
                    cached_l_matrix,
                    offset=0
                )
            else:
                covariance = \
                    self.gp.covariance_function.marginalize_covariance(
                        cached_data
                    )
                l_matrix = InferenceMethod._downdate_chol(
                    covariance,
                    cached_l_matrix,
                    offset=0,
                    size=(cached_data.shape[0] - data_x.shape[0])
                )
        else:
            covariance = self.gp.covariance_function.marginalize_covariance(
                data_x
            )
            l_matrix = InferenceMethod._chol(covariance)

        self.cache['cov_hashes'].append(cov_hash)
        self.cache['data'].append(data_x)
        self.cache['l_matrices'].append(l_matrix)

        if len(self.cache['cov_hashes']) > self.cache['size']:
            del self.cache['cov_hashes'][0]
            del self.cache['data'][0]
            del self.cache['l_matrices'][0]

        return l_matrix

    @staticmethod
    def _chol(k_matrix):
        """
        Compute cholesky decomposition

        :param k_matrix:
        :type k_matrix:
        :return:
        :rtype:
        """
        InferenceMethod._check_k_matrix(k_matrix)

        # Solve cholesky decomposition
        l_matrix = InferenceMethod._jittered_chol(k_matrix)

        InferenceMethod._check_l_matrix(l_matrix, k_matrix)

        return l_matrix

    @staticmethod
    def _update_chol(k_matrix, l_matrix, offset=0):
        """

        :param k_matrix:
        :type k_matrix:
        :param l_matrix:
        :type l_matrix:
        :param offset:
        :type offset:
        :return:
        :rtype:
        """
        InferenceMethod._check_k_matrix(k_matrix)

        b_i = k_matrix.shape[0] - offset
        new_i = l_matrix.shape[0] - offset
        new_l_matrix = np.zeros(k_matrix.shape)
        new_l_matrix[:new_i, :new_i] = l_matrix[:new_i, :new_i]
        new_l_matrix[new_i:b_i:, :new_i] = scipy.linalg.solve_triangular(
            l_matrix[:new_i, :new_i],
            k_matrix[:new_i, new_i:b_i],
            lower=True,
            check_finite=False
        ).T

        new_l_matrix[b_i:, :new_i] = l_matrix[new_i:, :new_i]
        new_l_matrix[new_i:b_i, new_i:b_i] = InferenceMethod._jittered_chol(
            k_matrix[new_i:b_i, new_i:b_i] -
            np.dot(
                new_l_matrix[new_i:b_i:, :new_i],
                new_l_matrix[new_i:b_i:, :new_i].T
            )
        )
        new_l_matrix[b_i:, new_i:b_i] = scipy.linalg.solve_triangular(
            new_l_matrix[new_i:b_i, new_i:b_i],
            k_matrix[b_i:, new_i:b_i].T -
            np.dot(
                new_l_matrix[new_i:b_i:, :new_i],
                new_l_matrix[b_i:, :new_i].T
            ),
            lower=True,
            check_finite=False
        ).T
        new_l_matrix[b_i:, b_i:] = InferenceMethod._jittered_chol(
            np.dot(l_matrix[new_i:, new_i:], l_matrix[new_i:, new_i:].T) -
            np.dot(
                new_l_matrix[b_i:, new_i:b_i],
                new_l_matrix[b_i:, new_i:b_i].T
            )
        )

        InferenceMethod._check_l_matrix(new_l_matrix, k_matrix)

        return new_l_matrix

    @staticmethod
    def _downdate_chol(k_matrix, l_matrix, offset=0, size=0):
        """

        :param k_matrix:
        :type k_matrix:
        :param l_matrix:
        :type l_matrix:
        :param offset:
        :type offset:
        :param size:
        :type size:
        :return:
        :rtype:
        """
        InferenceMethod._check_k_matrix(k_matrix)

        b_i = k_matrix.shape[0] - offset
        new_i = b_i - size
        new_size = k_matrix.shape[0] - size
        new_l_matrix = np.zeros((new_size, new_size))
        new_l_matrix[:new_i, :new_i] = l_matrix[:new_i, :new_i]
        new_l_matrix[new_i:, new_i:] = InferenceMethod._jittered_chol(
            np.dot(l_matrix[b_i:, b_i:], l_matrix[b_i:, b_i:].T) +
            np.dot(l_matrix[b_i:, new_i:b_i], l_matrix[b_i:, new_i:b_i].T)
        )
        new_l_matrix[new_i:, :new_i] = l_matrix[b_i:, :new_i]

        new_k_matrix = np.vstack((
            np.hstack((k_matrix[:new_i, :new_i], k_matrix[:new_i, b_i:])),
            np.hstack((k_matrix[b_i:, :new_i], k_matrix[b_i:, b_i:]))
        ))

        InferenceMethod._check_l_matrix(new_l_matrix, new_k_matrix)

        return new_l_matrix

    @staticmethod
    def _check_k_matrix(k_matrix):
        """

        :param k_matrix:
        :type k_matrix:
        :return:
        :rtype:
        """

        # Empty
        if k_matrix.size == 0:
            return np.empty((0, 0))

        # Non finite values in covariance matrix
        if not np.all(np.isfinite(k_matrix)):
            raise np.linalg.LinAlgError("Non finite values in cov matrix")

        # Covariance matrix is not symmetric
        if np.max(np.abs(k_matrix - k_matrix.T)) > 1e-20:
            raise np.linalg.LinAlgError("Covariance matrix is not symmetric")

    @staticmethod
    def _jittered_chol(k_matrix):
        """

        :param k_matrix:
        :type k_matrix:
        :return:
        :rtype:
        """

        l_matrix = None
        jitter = 1e-30
        max_jitter = 1e-6
        k_corrected = k_matrix
        while l_matrix is None and jitter < max_jitter:
            l_matrix, error = scipy.linalg.lapack.dpotrf(
                np.ascontiguousarray(k_corrected),
                lower=1
            )
            if error != 0:
                l_matrix = None
                k_corrected = k_matrix + jitter * np.eye(k_matrix.shape[0])
                jitter *= 10

        if l_matrix is None:
            raise np.linalg.LinAlgError("Can't compute cholesky decomposition")

        return l_matrix

    @staticmethod
    def _check_l_matrix(l_matrix, k_matrix):
        """

        :param l_matrix:
        :type l_matrix:
        :param k_matrix:
        :type k_matrix:
        :return:
        :rtype:
        """

        # Non finite values in L matrix
        if not np.all(np.isfinite(l_matrix)):
            raise np.linalg.LinAlgError("Non finite values in L matrix")

        # Main diagonal of L not positive
        if np.min(np.diagonal(l_matrix)) <= 0.0:
            raise np.linalg.LinAlgError("Main diagonal of L not positive")

        # Errors in L matrix multiplication
        if np.max(np.abs(k_matrix - np.dot(l_matrix, l_matrix.T))) > 1e-4:
            raise np.linalg.LinAlgError("Errors in L matrix multiplication")

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

import copy

import numpy as np

from .parameters.with_parameters import WithParameters
from .covariance_functions.posterior import Posterior as PosteriorCov
from .mean_functions.posterior import Posterior as PosteriorMean


class GaussianProcess(WithParameters):
    """
    GPlib module for Gaussian Process
    """
    def __init__(self,
                 mean_function,
                 covariance_function,
                 likelihood_function,
                 inference_method):
        self.mean_function = mean_function
        self.covariance_function = covariance_function
        self.likelihood_function = likelihood_function
        self.inference_method = inference_method

        self.likelihood_function.set_gp(self)
        self.inference_method.set_gp(self)

        super(GaussianProcess, self).__init__([
            mean_function, covariance_function
        ])

    def get_posterior(self, data):
        """

        :param data:
        :type data:
        :return:
        :rtype:
        """

        # Create a copy of self to be the prior of the posterior GP

        return GaussianProcess(
            PosteriorMean(self, data),
            PosteriorCov(self, data),
            # Create a copy of the prior to be the likelihood of the posterior
            self.likelihood_function.__class__(),
            # Create a copy of the prior to be the inference of the posterior
            self.inference_method.__class__()
        )

    def sample(self, test_points, n_samples=10):
        """
        Sample the prior of the GP

        :param test_points:
        :type test_points:
        :param n_samples:
        :type n_samples:
        :return:
        :rtype:
        """
        marginal = self.inference_method.marginalize_gp(test_points)
        rnd = np.random.randn(test_points.shape[0], n_samples)

        return marginal['mean'].reshape(-1, 1) + \
            np.dot(marginal['l_matrix'], rnd)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# #########################################################################
# Copyright (c) 2020, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2020. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################

import numpy

from orangecontrib.wonder.fit.parameters.fit_parameter import ParametersList
from orangecontrib.wonder.fit.functions.wppm_functions import \
    Normalization, Distribution, WulffCubeFace, \
    lognormal_distribution, delta_distribution, gamma_distribution, york_distribution, \
    lognormal_average, lognormal_average_surface_weigthed, lognormal_average_volume_weigthed, lognormal_standard_deviation


class SizeDistribution:
    D                      = None
    frequency              = None
    D_min                  = None
    D_max                  = None
    D_avg                  = None
    D_avg_surface_weighted = None
    D_avg_volume_weighted  = None
    standard_deviation     = None


class SizeParameters(ParametersList):

    @classmethod
    def get_parameters_prefix(cls):
        return "size_"

    def __init__(self, shape, distribution, mu, sigma, truncation=0.0, cube_face = WulffCubeFace.HEXAGONAL, add_saxs=False, normalize_to=Normalization.NORMALIZE_TO_N):
        super(SizeParameters, self).__init__()

        self.shape = shape
        self.distribution = distribution
        self.mu = mu
        self.sigma = sigma
        self.truncation = truncation
        self.cube_face = cube_face
        self.add_saxs = add_saxs
        self.normalize_to = normalize_to

    def get_distribution(self, auto=True, D_min=0, D_max=1000):
        if auto:
            D_min = 0
            D_max = 1000

        distribution       = SizeDistribution()
        distribution.D_min = D_min
        distribution.D_max = D_max
        distribution.x     = numpy.arange(start=D_min, stop=D_max, step=(D_max-D_min)/1000)

        self.__populate_stats_on_ditribution(distribution)

        try:
            distribution.y = self.__get_distribution_frequency_values(distribution.x)

            if auto:
                D_min, D_max = self.__get_auto_limits(distribution.x, distribution.y)

                distribution = self.get_distribution(auto=False, D_min=D_min, D_max=D_max)
        except:
            pass

        return distribution

    def __populate_stats_on_ditribution(self, distribution):
        if self.distribution == Distribution.LOGNORMAL:
            distribution.D_avg = lognormal_average(self.mu.value, self.sigma.value)
            distribution.D_avg_surface_weighted = lognormal_average_surface_weigthed(self.mu.value, self.sigma.value)
            distribution.D_avg_volume_weighted = lognormal_average_volume_weigthed(self.mu.value, self.sigma.value)
            distribution.standard_deviation = lognormal_standard_deviation(self.mu.value, self.sigma.value)
        elif self.distribution == Distribution.GAMMA or self.distribution == Distribution.YORK:
            distribution.D_avg = self.mu.value
            distribution.D_avg_surface_weighted = None
            distribution.D_avg_volume_weighted = None
            distribution.standard_deviation = None
        else:
            distribution.D_avg = None
            distribution.D_avg_surface_weighted = None
            distribution.D_avg_volume_weighted = None
            distribution.standard_deviation = None


    def __get_distribution_frequency_values(self, x):
        if self.distribution == Distribution.LOGNORMAL:
            y = lognormal_distribution(self.mu.value, self.sigma.value, x)
        elif self.distribution == Distribution.GAMMA:
            y = gamma_distribution(self.mu.value, self.sigma.value, x)
        elif self.distribution == Distribution.YORK:
            y = york_distribution(self.mu.value, self.sigma.value, x)
        elif self.distribution == Distribution.DELTA:
            y = delta_distribution(self.mu.value, x)
        else:
            y = numpy.zeros(len(x))

        y[numpy.where(numpy.logical_or(numpy.isnan(y), numpy.isinf(y)))] = 0.0

        return y

    def __get_auto_limits(self, x, y):
        good = x[numpy.where(y > 1e-5)]

        D_min = good[0]
        D_max = good[-1]

        if D_min == D_max: D_min = x[0]
        if D_min < 5: D_min = 0.0

        return D_min, D_max

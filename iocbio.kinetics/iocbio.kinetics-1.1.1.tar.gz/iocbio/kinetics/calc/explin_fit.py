# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics

"""Analyzer fitting the data by exponent and linear function"""

import numpy as np
from scipy.optimize import least_squares
from .generic import AnalyzerGeneric, XYData, Stats


class AnalyzerExpLinFit(AnalyzerGeneric):
    """Analyser for data that can be fit by a sum of exponent and linear functions

    Use for data that is best represented by a sum of exponent and
    linear functions.

    The analyzer approximates the data y(t) with:

    y = a*exp(-k*t) + l*t + b

    The calculated constants are all saved in the attributes and in
    `self.stats` under the same names as attributes. Attribute
    `self.calc` contains the best approximation found by the fit after
    fitting.

    See parameters and attributes from the base class: :class:`.generic.AnalyzerGeneric`

    Attributes
    ----------
    
    exponential_amplitude : float
      "a" in the formula
    rate_constant : float
      "k" in the formula
    linear_offset : float
      "b" in the formula
    linear_slope : float
      "l" in the formula

    """

    @staticmethod
    def fit_function(a, k, b, l, t):
        """Calculate fit function"""
        return a*np.exp(-k*t) + l*t + b

    @staticmethod
    def error_function(v, t, y):
        """Calculate fit residual"""
        return y-AnalyzerExpLinFit.fit_function(*v, t)

    def __init__(self, x, y):
        AnalyzerGeneric.__init__(self, x, y)

    def fit(self):
        """Fit the data

        Fit the data stored in `self.experiment`, fill the statistics
        and calculate the best fit approximation.
        """
        t = np.array(self.experiment.x)
        t0 = t[0]
        t = t - t0
        y = np.array(self.experiment.y)

        # first estimate x0 = amp, rate, off, lin
        x0 = [0.2, 0.01, 0.1, -0.0001]
        bounds = ((0, 0, 0, -np.inf),
                  (y.max(), 20, np.inf, 0))

        r = least_squares(self.error_function, x0, args=(t, y), bounds=bounds,
                          loss='soft_l1', f_scale=1, tr_solver='exact',
                          ftol=1.e-10, xtol=1.e-10, max_nfev=100000)

        sol = r.x
        msg = r.message
        s = r.success
        self.exponential_amplitude, self.rate_constant, self.linear_offset, self.linear_slope = sol

        self.calc = XYData(t+t0, self.fit_function(*sol, t))
        self.stats['exponential_amplitude'] = Stats("exponential amplitude", "Abs", self.exponential_amplitude)
        self.stats['rate_constant'] = Stats("rate constant", "1/min", self.rate_constant)
        self.stats['linear_offset'] = Stats("linear offset", "Abs", self.linear_offset)
        self.stats['linear_slope'] = Stats("linear slope", "Abs/min", self.linear_slope)

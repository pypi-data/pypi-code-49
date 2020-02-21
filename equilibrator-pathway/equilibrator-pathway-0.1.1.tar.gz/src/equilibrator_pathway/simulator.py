# The MIT License (MIT)
#
# Copyright (c) 2013 Weizmann Institute of Science
# Copyright (c) 2018-2020 Institute for Molecular Systems Biology,
# ETH Zurich
# Copyright (c) 2018-2020 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import numpy as np
from scipy.integrate import ode

from .errors import ThermodynamicallyInfeasibleError


class EnzymeCostSimulator(object):
    def __init__(self, ecf):
        self.ecf = ecf

    def Simulate(self, lnC0, E, t_max=1000, dt=1, eps=1e-9):
        """
            Find the steady-state solution for the metabolite concentrations
            given the enzyme abundances

            Arguments:
                E    - enzyme abundances [gr]
                y0   - initial concentration of internal metabolites
                       (default: MDF solution)
                eps  - the minimal change under which the simulation will stop

            Returns:
                v    - the steady state flux
                y    - the steady state internal metabolite concentrations
        """
        assert lnC0.shape == (self.ecf.Nc, 1)
        assert E.shape == (self.ecf.Nr,)

        ln_conc_bounds_diff = self.ecf.ln_conc_ub - self.ecf.ln_conc_lb
        idx_fixed = np.where(ln_conc_bounds_diff <= 1e-5)[0].tolist()
        idx_non_fixed = np.where(ln_conc_bounds_diff > 1e-5)[0].tolist()

        def f(t, y):
            # we only care about the time derivatives of the internal
            # metabolites (i.e. the first and last one are assumed to be
            # fixed in time)
            ln_conc = np.log(np.array(y, ndmin=2).T)
            v = self.ecf.GetFluxes(ln_conc, E)
            dy = self.ecf.S @ v
            dy[idx_fixed, :] = 0
            return dy

        if not self.ecf.IsFeasible(lnC0):
            raise ThermodynamicallyInfeasibleError(lnC0)

        v = self.ecf.GetFluxes(lnC0, E)

        T = np.array([0])
        Y = np.exp(lnC0).T
        V = v.T

        r = ode(f)
        r.set_initial_value(Y.T, 0)

        while (
            r.successful()
            and r.t < t_max
            and (
                r.t < 0.05 * t_max
                or (np.abs(self.ecf.S[idx_non_fixed, :] @ v) > eps).any()
            )
        ):
            r.integrate(r.t + dt)
            v = self.ecf.GetFluxes(np.log(r.y), E)

            T = np.hstack([T, r.t])
            Y = np.vstack([Y, r.y.T])
            V = np.vstack([V, v.T])

        if r.t >= t_max:
            v_inf = np.nan
            lnC_inf = np.nan
        else:
            v_inf = V[-1, 0]
            lnC_inf = np.log(Y[-1, :])

        return v_inf, lnC_inf

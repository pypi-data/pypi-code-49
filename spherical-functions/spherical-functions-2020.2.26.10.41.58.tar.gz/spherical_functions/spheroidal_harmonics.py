# Copyright (c) 2016, Michael Boyle
# See LICENSE file for details: <https://github.com/moble/spherical_functions/blob/master/LICENSE>

from __future__ import print_function, division, absolute_import

import math
import cmath

import numpy as np
import quaternion
from quaternion.numba_wrapper import njit, jit, vectorize, int64, float64, xrange
from Wigner3j import clebsch_gordan


@vectorize('int64(int64, int64)')
def _kronecker_delta(a, b):
    if a == b:
        return 1
    else:
        return 0


@vectorize('float64(int64, int64, int64, int64)')
def _moment0(j, l, m, s):
    return _kronecker_delta(j, l)


@vectorize('float64(int64, int64, int64, int64)')
def _moment1(j, l, m, s):
    return np.sqrt((2*l+1)/(2*j+1)) * clebsch_gordan(j, m, 1, 0, l, m) * clebsch_gordan(j, -s, 1, 0, l, -s)


@vectorize('float64(int64, int64, int64, int64)')
def _moment2(j, l, m, s):
    return (_kronecker_delta(j, l)/3.0
            + 2*np.sqrt((2*l+1)/(2*j+1)) * clebsch_gordan(j, m, 2, 0, l, m) * clebsch_gordan(j, -s, 2, 0, l, -s) / 3.0)


def _operator_matrix(m, aomega, s, ell_max):
    # Initialize with empty matrix
    matrix = np.zeros((ell_max+1, ell_max+1), dtype=complex)

    # Set the bands individually
    # 2 above the diagonal:
    ell_range = np.arange(0, ell_max+1-2)
    matrix.flat[2:((ell_max + 1) * (ell_max + 1 - 2)):ell_max + 1 + 1] = (
        aomega**2 * _moment2(ell_range+2, ell_range, m, s)
    )
    # 1 above the diagonal:
    ell_range = np.arange(0, ell_max+1-1)
    matrix.flat[1:((ell_max + 1) * (ell_max + 1 - 1)):ell_max + 1 + 1] = (
        aomega**2 * _moment2(ell_range+1, ell_range, m, s)
        - 2 * aomega * _moment1(ell_range+1, ell_range, m, s)
    )
    # On the diagonal:
    ell_range = np.arange(0, ell_max+1)
    matrix.flat[0:((ell_max + 1) * (ell_max + 1)):ell_max + 1 + 1] = (
        aomega**2 * _moment2(ell_range, ell_range, m, s)
        - 2 * aomega * _moment1(ell_range, ell_range, m, s)
        - ell_range*(ell_range+1)
    )
    # 1 below the diagonal:
    ell_range = np.arange(1, ell_max+1)
    matrix.flat[(ell_max + 1):((ell_max + 1) * (ell_max + 1)):ell_max + 1 + 1] = (
        aomega**2 * _moment2(ell_range-1, ell_range, m, s)
        - 2 * aomega * _moment1(ell_range-1, ell_range, m, s)
    )
    # 2 below the diagonal:
    ell_range = np.arange(2, ell_max+1)
    matrix.flat[2 * (ell_max + 1):((ell_max + 1) * (ell_max + 1)):ell_max + 1 + 1] = (
        aomega**2 * _moment2(ell_range-2, ell_range, m, s)
    )

    return matrix










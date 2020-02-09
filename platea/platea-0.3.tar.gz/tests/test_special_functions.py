import pytest

import numpy as np
from scipy import special
import numpy.testing as npt

from platea import special_functions as sf

################################################################################
# Gamma Function

def test_gamma():
    """
    gamma
    """

    alpha1 = [sf.gamma(i) for i in [0.0, 0.53, 1.0, 5.67, 10.0]]
    beta = [special.gamma(i) for i in [0.0, 0.53, 1.0, 5.67, 10.0]]
    npt.assert_almost_equal(alpha1, beta, decimal=5)

    alpha2 = sf.gamma(np.asarray([0.0, 0.53, 1.0, 5.67, 10.0]))
    npt.assert_almost_equal(alpha2, beta, decimal=5)

    alpha3 = sf.gamma(np.asarray([[0.0, 0.53, 1.0, 5.67, 10.0]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=5)

def test_gammaln():
    """
    gammaln
    """

    alpha1 = [sf.gammaln(i) for i in [0.0, 0.53, 1.0, 5.67, 10.0]]
    beta = [special.gammaln(i) for i in [0.0, 0.53, 1.0, 5.67, 10.0]]
    npt.assert_almost_equal(alpha1, beta, decimal=5)

    alpha2 = sf.gammaln(np.asarray([0.0, 0.53, 1.0, 5.67, 10.0]))
    npt.assert_almost_equal(alpha2, beta, decimal=5)

    alpha3 = sf.gammaln(np.asarray([[0.0, 0.53, 1.0, 5.67, 10.0]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=5)

def test_gammap():
    """
    gammap
    """

    alpha1 = [sf.gammap(1.0, i) for i in [0, 1, 10, 100]]
    beta = [special.gammainc(1.0, i) for i in [0, 1, 10, 100]]
    npt.assert_almost_equal(alpha1, beta, decimal=5)

    alpha2 = sf.gammap(np.ones(4), np.asarray([0, 1, 10, 100]))
    npt.assert_almost_equal(alpha2, beta, decimal=5)

    alpha3 = sf.gammap(np.ones(4).reshape(1, -1), np.asarray([[0, 1, 10, 100]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=5)

def test_gammaq():
    """
    gammaq
    """

    alpha1 = [sf.gammaq(1.0, i) for i in [0, 0.1 ,0.5, 1]]
    beta = [special.gammaincc(1.0, i) for i in [0, 0.1 ,0.5, 1]]
    npt.assert_almost_equal(alpha1, beta, decimal=5)

    alpha2 = sf.gammaq(np.ones(4), np.asarray([0, 0.1 ,0.5, 1]))
    npt.assert_almost_equal(alpha2, beta, decimal=5)

    alpha3 = sf.gammaq(np.ones(4).reshape(1, -1), np.asarray([[0, 0.1 ,0.5, 1]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=5)

################################################################################
# Error Function

def test_erf():
    """
    erf
    """

    alpha1 = [sf.erf(i) for i in [-10, 5, 0, 5, 10]]
    beta = [special.erf(i) for i in [-10, 5, 0, 5, 10]]
    npt.assert_almost_equal(alpha1, beta, decimal=3)

    alpha2 = sf.erf(np.asarray([-10, 5, 0, 5, 10]))
    npt.assert_almost_equal(alpha2, beta, decimal=3)

    alpha3 = sf.erf(np.asarray([[-10, 5, 0, 5, 10]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=3)

def test_erfc():
    """
    erfc
    """

    alpha1 = [sf.erfc(i) for i in [-10, 5, 0, 5, 10]]
    beta = [special.erfc(i) for i in [-10, 5, 0, 5, 10]]
    npt.assert_almost_equal(alpha1, beta, decimal=3)

    alpha2 = sf.erfc(np.asarray([-10, 5, 0, 5, 10]))
    npt.assert_almost_equal(alpha2, beta, decimal=3)

    alpha3 = sf.erfc(np.asarray([[-10, 5, 0, 5, 10]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=3)

def test_erfcc():
    """
    erfcc
    """

    alpha1 = [sf.erfcc(i) for i in [-10, 5, 0, 5, 10]]
    beta = [special.erfc(i) for i in [-10, 5, 0, 5, 10]]
    npt.assert_almost_equal(alpha1, beta, decimal=-1)

    alpha2 = sf.erfcc(np.asarray([-10, 5, 0, 5, 10]))
    npt.assert_almost_equal(alpha2, beta, decimal=-1)

    alpha3 = sf.erfcc(np.asarray([[-10, 5, 0, 5, 10]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=-1)

def test_inverfc():
    """
    inverfc
    """

    alpha1 = [sf.inverfc(i) for i in [0.1, 0.3, 0.5, 0.6, 1.0]]
    beta = [special.erfcinv(i) for i in [0.1, 0.3, 0.5, 0.6, 1.0]]
    npt.assert_almost_equal(alpha1, beta, decimal=3)

    alpha2 = sf.inverfc(np.asarray([0.1, 0.3, 0.5, 0.6, 1.0]))
    npt.assert_almost_equal(alpha2, beta, decimal=3)

    alpha3 = sf.inverfc(np.asarray([[0.1, 0.3, 0.5, 0.6, 1.0]]))
    npt.assert_almost_equal(alpha3[0, :], beta, decimal=3)

################################################################################

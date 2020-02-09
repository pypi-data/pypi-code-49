import pytest

import numpy as np
import numpy.testing as npt

import scipy.stats as st

from platea import distributions as dist

################################################################################
# normal

def test_normal_pdf():
    """
    normal pdf
    """
    pla_dist = dist.Normal(mu=10, sigma=20)
    sp_dist = st.norm(loc=10, scale=20)

    inputs = np.asarray([-90, 5, 10, 15, 100])

    alpha = pla_dist.pdf(inputs)
    beta = sp_dist.pdf(inputs)

    npt.assert_almost_equal(alpha, beta, decimal=10)

def test_normal_cdf():
    """
    normal cdf
    """

    pla_dist = dist.Normal(mu=10, sigma=20)
    sp_dist = st.norm(loc=10, scale=20)

    inputs = np.asarray([-90, 5, 10, 15, 100])

    alpha = pla_dist.cdf(inputs)
    beta = sp_dist.cdf(inputs)

    npt.assert_almost_equal(alpha, beta, decimal=10)

def test_normal_invcdf():
    """
    normal invcdf
    """

    pla_dist = dist.Normal(mu=10, sigma=20)
    sp_dist = st.norm(loc=10, scale=20)

    inputs = np.asarray([0.1, 0.3, 0.5, 0.6, 0.9])

    alpha = pla_dist.invcdf(inputs)
    beta = sp_dist.ppf(inputs)

    npt.assert_almost_equal(alpha, beta, decimal=-1)

def test_normal_draw():
    """
    normal draw
    """

    pla_dist = dist.Normal(mu=10, sigma=20)
    sp_dist = st.norm(loc=10, scale=20)

    alpha = pla_dist.draw(100000)
    beta = sp_dist.rvs(100000)

    test_statistic, p_value = st.ks_2samp(alpha, beta)
    assert p_value >= 0.05, "P value of {}".format(p_value)

################################################################################

import pytest

import numpy as np
import numpy.testing as npt

from statsmodels.tsa.stattools import acf

from platea import random_number_generators as rng

################################################################################

def test_ran0_vec():
    """
    ran0 vectorization test
    """

    seed = -99999
    ran = rng.Ran0(seed=seed)

    sample = ran.draw(n=10)
    assert sample.shape == (10,), "Float arg case failed."

    sample = ran.draw(n=(10))
    assert sample.shape == (10,), "1D tuple arg case failed."

    sample = ran.draw(n=(10, 10))
    assert sample.shape == (10, 10), "Third 2D tuple arg case failed."

def test_ran0_state():
    """
    ran0 state test
    """

    seed = -99999
    ran = rng.Ran0(seed=seed)
    ran.draw(100)

    # check that state system works
    seed = ran.get_state() # get current internal state
    sample_one = ran.draw(10)
    ran.set_state(seed) # reset current internal state
    sample_two = ran.draw(10)
    npt.assert_equal(sample_one, sample_two)

def test_ran0_corr():
    """
    ran0 corr test
    """

    seed = -99999
    ran = rng.Ran0(seed=seed)
    sample = ran.draw(n=1000000)
    auto_corr = acf(sample, fft=True)[1:]
    assert auto_corr.max() < 0.05, "High auto correlation!"
    assert sample.max() <= 1.0, "Sample max value > 1.0!"
    assert sample.min() >= 0.0, "Sample min value < 0.0!"

################################################################################

def test_ran1_vec():
    """
    ran1 vectorization test
    """

    seed = -99999
    ran = rng.Ran1(seed=seed)

    sample = ran.draw(n=10)
    assert sample.shape == (10,), "Float arg case failed."

    sample = ran.draw(n=(10))
    assert sample.shape == (10,), "1D tuple arg case failed."

    sample = ran.draw(n=(10, 10))
    assert sample.shape == (10, 10), "Third 2D tuple arg case failed."

def test_ran1_state():
    """
    ran1 state test
    """

    seed = -99999
    ran = rng.Ran1(seed=seed)
    ran.draw(100)

    # check that state system works
    seed = ran.get_state() # get current internal state
    sample_one = ran.draw(10)
    ran.set_state(seed) # reset current internal state
    sample_two = ran.draw(10)
    npt.assert_equal(sample_one, sample_two)

def test_ran1_corr():
    """
    ran1 corr test
    """

    seed = -99999
    ran = rng.Ran1(seed=seed)
    sample = ran.draw(n=1000000)
    auto_corr = acf(sample, fft=True)[1:]
    assert auto_corr.max() < 0.05, "High auto correlation!"
    assert sample.max() <= 1.0, "Sample max value > 1.0!"
    assert sample.min() >= 0.0, "Sample min value < 0.0!"

################################################################################

def test_ran2_vec():
    """
    ran2 vectorization test
    """

    seed = -99999
    ran = rng.Ran2(seed=seed)

    sample = ran.draw(n=10)
    assert sample.shape == (10,), "Float arg case failed."

    sample = ran.draw(n=(10))
    assert sample.shape == (10,), "1D tuple arg case failed."
    
    sample = ran.draw(n=(10, 10))
    assert sample.shape == (10, 10), "Third 2D tuple arg case failed."

def test_ran2_state():
    """
    ran0 state test
    """

    seed = -99999
    ran = rng.Ran2(seed=seed)
    ran.draw(100)

    # check that state system works
    seed = ran.get_state() # get current internal state
    sample_one = ran.draw(10)
    ran.set_state(seed) # reset current internal state
    sample_two = ran.draw(10)
    npt.assert_equal(sample_one, sample_two)

def test_ran2_corr():
    """
    ran0 corr test
    """

    seed = -99999
    ran = rng.Ran2(seed=seed)
    sample = ran.draw(n=1000000)
    auto_corr = acf(sample, fft=True)[1:]
    assert auto_corr.max() < 0.05, "High auto correlation!"
    assert sample.max() <= 1.0, "Sample max value > 1.0!"
    assert sample.min() >= 0.0, "Sample min value < 0.0!"

################################################################################

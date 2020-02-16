from math import sqrt, log
from pricegen.generator import *
import numpy as np
from numpy.linalg import cholesky
import unittest

class TestGenerator(unittest.TestCase):
    # Assume 252 trading days per year

    def test_random_prices(self):
        # Repeatedly generate a price at 1 year later (time=1.0) with 20% volatility
        prices = [random_price(price=100, sigma=0.20) for _ in range(100000)]

        # Verify the mean and stdev are close enough to the original specification
        self.assertAlmostEqual(np.mean(prices), 100, delta=1.0)
        self.assertAlmostEqual(np.std(prices), 20, delta=1.0)

    def test_price_series(self):
        # Generate a series of daily prices (time=1.0/252 per interval) over 10 years (2520 days)
        prices = list(generate_prices(2520, price=100, sigma=0.20, time=1.0/252))
        logr = [log(j / i) for i, j in zip(prices, prices[1:])]

        # Verify the mean and stdev are close enough to the original specification
        self.assertAlmostEqual(np.mean(logr), 0, delta=0.01)
        self.assertAlmostEqual(np.std(logr), 0.20 / sqrt(252), delta=0.001)

    def test_mean_reversion(self):
        # Generate a series of daily prices, approaching target mean
        prices = list(generate_prices(2520, price=100, sigma=0.20, time=1.0/252, mean=130))
        logr = [log(p1 / p0) for p0, p1 in zip(prices, prices[1:])]

        # Verify the mean and stdev are close enough to the original specification
        self.assertAlmostEqual(np.mean(prices[-252:]), 130, delta=3.0)
        self.assertAlmostEqual(np.mean(logr), 0, delta=0.01)
        self.assertAlmostEqual(np.std(logr), 0.20 / sqrt(252), delta=0.001)

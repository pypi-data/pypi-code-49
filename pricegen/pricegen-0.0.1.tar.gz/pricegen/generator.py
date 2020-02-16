from math import sqrt, log, exp
import numpy as np
from numpy.linalg import cholesky
from random import Random

class PriceGenerator:
    def __init__(self, random=None):
        if random is None:
            random = Random()
        self.random = random

    def next_gauss(self):
        return self.random.gauss(0, 1)

    def random_price(self, price, sigma, time=1.0, drift=0.0, mean=None, theta=None, noise=None):
        if noise is None:
            noise = self.next_gauss()

        if mean is None:
            return price * exp(
                (drift - sigma ** 2 / 2) * time +
                sigma * sqrt(time) * noise)
        else:
            if theta is None:
                theta = - log(0.9) / time
            p = exp(-theta * time)
            frac = (1 - p ** 2) / (2 * theta)
            return exp(
                p * log(price) +
                (1 - p) * log(mean) +
                (drift - sigma ** 2 / 2) * time +
                sigma * sqrt(frac) * noise)

    def generate_prices(self, count, price, sigma, *args, **kwargs):
        for _ in range(count):
            price = self.random_price(price, sigma, *args, **kwargs)
            yield price

default_generator = PriceGenerator()

def random_price(*args, **kwargs):
    return default_generator.random_price(*args, **kwargs)

def generate_prices(*args, **kwargs):
    return default_generator.generate_prices(*args, **kwargs)

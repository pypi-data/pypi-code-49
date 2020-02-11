import numpy as np


def function(x):
    return np.tanh(x)


def derivative(x):
    return 1.0 - np.tanh(x) ** 2

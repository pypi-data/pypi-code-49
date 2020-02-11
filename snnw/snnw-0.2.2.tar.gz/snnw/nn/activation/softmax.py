import numpy as np


def function(x):
    exps = np.exp(x - np.max(x))
    return exps / np.sum(exps)


def derivative(x):
    pass

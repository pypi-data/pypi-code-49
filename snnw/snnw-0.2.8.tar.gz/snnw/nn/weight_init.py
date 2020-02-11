import numpy as np


def kaiming(in_size, out_size):
    return np.random.normal(size=(in_size, out_size)) * np.sqrt(2.0/in_size)

import warnings

import numpy as np


def to_lin(data):
    return 10 ** (data / 10.0)


def from_lin(data):
    return 10 * np.log10(data)


def mean(data, axis=None):
    return from_lin(np.mean(to_lin(data), axis=axis))


def subtract(signal, noise):
    return from_lin(to_lin(signal) - to_lin(noise))


def average(datasets):
    warnings.warn(
        "Use `openqlab.conversion.de.mean` with argument 'axis=-1' instead",
        DeprecationWarning,
    )
    lin = to_lin(datasets)
    average = np.sum(lin, 0) / len(lin)
    return from_lin(average)


def dBm2Vrms(dbm, R=50.0):
    return np.sqrt(0.001 * R) * 10 ** (dbm / 20)

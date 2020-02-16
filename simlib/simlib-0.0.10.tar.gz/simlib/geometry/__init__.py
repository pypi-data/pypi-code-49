"""
geometry.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

import numpy as np
from scipy.spatial.distance import euclidean

__all__ = ['distance']


# Compute the distance between two vectors
# TODO move to module
def distance(x, y=None, method='euclidean'):
    """
    Compute the distance between two vectors

    Parameters
    ----------
    x : ArrayLike

    y : ArrayLike

    method : str
        (Default: 'euclidean')

    Returns
    -------
    float
        Distance
    """

    # If y is not supplied, set to zeros
    if y is None:
        y = np.zeros(x.shape)

    # Return distance
    # return euclidean(x, y)
    return np.sqrt(np.sum(np.square(x - y)))

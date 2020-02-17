""" Provides the repeatedNans and findNans functions

repeatedNans determines the lengths of consecutive nan values in an array.
findNans provides the start and end locations of nans in an array.
"""

import numpy as np


def repeatedNans(array):
    """ Determine the number of repeated nans in a row

    Parameters
    ----------
    array : np.array
        Array containing nan "strings"

    Returns
    -------
    np.array or None
        Array of the lengths of each nan "string"

    """
    idx = findNans(array)
    if idx is not None:
        return idx[1::2] - idx[::2]
    return None


def findNans(array):
    """ Find the start and stop location of nans

    Parameters
    ----------
    array : np.array
        array of data to find nans start/stop locations

    Returns
    -------
    np.array or None
        array of the start and stop locations of each nan "string" or None

    """
    mask = np.concatenate(([False], np.isnan(array), [False]))
    if not mask.any():
        return None
    return np.nonzero(mask[1:] != mask[:-1])[0]

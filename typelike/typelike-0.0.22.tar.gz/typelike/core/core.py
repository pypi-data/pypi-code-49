"""
typelike.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

import numpy as np
import pandas as pd


# A list of types
dtypes = {
    'int': int,
    'float': float,
    'str': str,
    'list': list,
    'tuple': tuple,
    'set': set,
    'dict': dict,
    'numpy': np.ndarray,
    'series': pd.Series,
    'dataframe': pd.DataFrame
}


def infer_type(anything, itemize=True):
    """
    Infer the type of anything

    Applies some logic to parse anything

    Parameters
    ----------
    anything : Anything
        Something of whose type we need to infer
    itemize : bool
        Should we infer the items in lists, tuples? (Default: True)

    Returns
    -------
    object
        Type of `anything`
    """

    # By default, set the type to the type of anything
    # TODO is there a better way to do this?
    dtype = type(anything)

    # We need to correct dtype if it's a type object
    if dtype is type:
        dtype = anything

    # If anything is a string, try to parse
    if isinstance(anything, str):
        dtype = dtypes.get(anything.lower(), dtype)

    # If anything is a tuple or list, parse each element individually
    elif itemize and isinstance(anything, (list, tuple)):
        dtype = []
        for item in anything:
            dtype.append(infer_type(item, itemize=True))
        if isinstance(anything, tuple):
            dtype = tuple(dtype)

    # Return
    return dtype

"""
udf.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

import numpy as np
from refunction import Refunction


# Ensure that pandas DataFrame columns are not changed
def fix_pandas_columns(columns):
    """

    Parameters
    ----------
    columns

    Returns
    -------

    """

    def _fix_pandas_columns(df, columns):
        return np.array_equal(df.columns, columns)
    return Refunction(_fix_pandas_columns, columns=columns)


"""
udf.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

import numpy as np
from refunction import Refunction


# Ensure that pandas DataFrame columns are not changed
def required_dataframe_columns(columns):
    """
    Specify required columns in pandas DataFrames

    Parameters
    ----------
    columns : list of str
        Column names to ensure are represented.

    Returns
    -------
    bool
        Whether or not the requirement columns are in the DataFrame
    """

    def _fix_pandas_columns(df, columns):
        return np.array_equal(df.columns, columns)
    return Refunction(_fix_pandas_columns, columns=columns)


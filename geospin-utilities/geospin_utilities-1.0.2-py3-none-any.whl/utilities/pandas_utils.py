"""Contains help functions for pandas."""

import pandas as pd
import geopandas as gpd
import numpy as np
from shapely import wkt


def read_csv(filename, import_dtypes=True, geometry=None, **kwargs):
    """
    Parses a *.csv file created by utilities.write_csv into a data frame with
    the option of keeping dtypes and converting the geometry column.

    .. note:: Other *.csv files may not be parsed successfully. The format used
        by utilities.write_csv is very specific, e.g. utf-8 encoding, optionally
        column names including '_dtype', an index column specified by 'index'
        and the wkt format being used for geometries in the 'geometry' column.

    :param str filename: File name of *.csv file to be read in.
    :param bool import_dtypes: If True, sets dtypes according to column names.
        These must be specified in the form of 'column_name_dtype' in the *.csv
        file. Subsequently, '_dtype' is removed. If False, pre-existing column
        names (with '_dtype') are kept.
    :param str geometry: Name of column with geometries in wkt format string
        (_object for import_dtypes). The column entries are converted to
        shapely.geometry objects. If None, a pandas.DataFrame is returned,
        otherwise a geopandas.GeoDataFrame.
    :param dict kwargs: Keyword arguments passed on to pandas.read_csv.
    :return: The parsed *.csv file as a data frame. If geometry is None, a
           pandas.DataFrame is returned, otherwise a geopandas.GeoDataFrame.
    :rtype: pandas.DataFrame or geopandas.GeoDataFrame (depending on geometry).
    """
    df = pd.read_csv(filename, encoding='utf-8', **kwargs).set_index('index')

    if import_dtypes:
        assert all('_' in name for name in df.columns)
        names, dtypes = zip(*[name.rsplit('_', 1) for name in df.columns])
        df.columns = names
        df = df.astype(dict(zip(names, dtypes)))

    if geometry is not None:
        df[geometry] = df[geometry].apply(lambda x: wkt.loads(x))
        df = gpd.GeoDataFrame(df, geometry=geometry)

    return df


def write_csv(df, filename, export_dtypes=True, **kwargs):
    """
    Stores a data frame to a *.csv file with the option of preserving column
    dtypes.

    .. note:: shapely.geometry objects are converted to wkt format.

    :param df: A data frame to be stored as *csv.
    :type: pandas.DataFrame or geopandas.GeoDataFrame.
    :param str filename: File name of *.csv file to be created.
    :param bool export_dtypes: If True, the column types are exported using the
        column suffix '_dtype'. If False, column names are not changed.
    :param dict kwargs: Keyword arguments passed on to pandas.to_csv.
    """
    df = df.copy()  # Copy data frame so as to not modify the original.
    if export_dtypes:
        df.columns = ['{}_{}'.format(name, df[name].dtypes) for name in
                      df.columns]
    df.to_csv(filename, encoding='utf-8', index_label='index', **kwargs)


def remove_outliers_percentile(df, column, lower=1, upper=99):
    """
    Remove outliers outside percentiles.

    .. note:: This is a naive approach to remove outliers and might lead to
    the removal of informative data.

    :param pandas.DataFrame df: A data frame.
    :param str column: Name of column whose outliers are to be removed.
    :param int lower: Lower percentile (between 0 and 100).
    :param int upper: Upper percentile (between 0 and 100).
    :return pandas.DataFrame: The data frame with removed outliers.
    """
    percentile_lower = np.percentile(df[column], lower)
    percentile_upper = np.percentile(df[column], upper)
    condition = (
            (df[column] < percentile_upper)
            &
            (df[column] > percentile_lower)
    )
    return df[condition]


def remove_outliers_iqr(df, column):
    """
    Remove outliers outside the interquartile range.

    .. note:: This is a naive approach to remove outliers and might lead
    to the removal of informative data.

    :param pandas.DataFrame df: A data frame.
    :param str column: Name of column whose outliers are to be removed.
    :return pandas.DataFrame: The data frame with removed outliers.
    """
    Q1 = np.percentile(df[column], 25)
    Q3 = np.percentile(df[column], 75)
    IQR = Q3 - Q1  # Inter quartile range
    condition = (
            (df[column].ge(Q1 - 1.5 * IQR))
            &
            (df[column].le(Q3 + 1.5 * IQR))
    )
    return df[condition]

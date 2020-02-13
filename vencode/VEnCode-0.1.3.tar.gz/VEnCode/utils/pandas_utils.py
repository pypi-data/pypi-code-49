#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" pandas_utils.py: utilities module for easier Pandas module integration """

import re
import numpy as np
import pandas as pd


def multi_set_data_frame(data, arrays, set_value):
    """
    Change multiple values on a pandas data frame in one line.
    :param data: pandas DataFrame. Note: must be of the same type as set_value.
            e.g.: DataFrame of "float" type and set_value=2.1.
    :param arrays: arrays of (row, col) directing to the cell to change the value.
    :param set_value: value to change to.
    """
    for i in arrays:
        data.at[i[0], i[1]] = set_value


def df_regex_columns_searcher_list(string, database):
    """ Returns a list containing only the columns of a data frame which contain the string somewhere
    in its label """
    regular = ".*" + string.replace(" ", ".*").replace("+", "%2b") + ".*"
    idx = database.columns.str.contains(regular, flags=re.IGNORECASE, regex=True, na=False)
    regex_filtered_df = database.loc[:, idx]
    regex_filtered = regex_filtered_df.columns.values.tolist()
    return regex_filtered


def df_regex_columns_searcher(string, database):
    """ Returns a df containing only the columns which contain the string somewhere in its label """
    regular = ".*" + string.replace(" ", ".*").replace("+", "%2b").replace(":", "%3a").replace("(",
                                                                                               "%28").replace(
        ")", "%29").replace("/", "%2f") + ".*"  # sets up regex pattern
    idx = database.columns.str.contains(regular, flags=re.IGNORECASE, regex=True, na=False)  # searches cols for str
    regex_filtered_df = database.loc[:, idx]  # cols that are True (have the expression str) remain in data set
    return regex_filtered_df


def df_minimal_regex_columns_searcher(string, database):
    """ Returns a df containing only the columns which contain the string somewhere in its label
    Used for enhancer data set. """
    expression = ".*" + string.replace(" ", ".*").replace("+", "\+") + ".*"  # sets up regex pattern
    idx = database.columns.str.contains(expression, flags=re.IGNORECASE, regex=True, na=False)  # searches cols for str
    regex_filtered_df = database.loc[:, idx]  # cols that are True (have the expression str) remain in data set
    return regex_filtered_df


def df_filter_by_expression(data, codes, expression):
    """ Returns a df containing only the rows which value is >= than expression for all columns in codes """
    if isinstance(codes, (list, tuple, np.ndarray)):
        for item in codes:
            data = data[data[item] >= expression]
    else:
        data = data[data[codes] >= expression]
    return data


def df_percentile_calculator(data_frame, celltype, start_percent, define_percentile=False):
    """
    Returns a df with one extra column containing the value of the data at percentile start_percent and the label
    of such column.
    """
    if define_percentile:
        column_label = "Percentile {}".format(start_percent)
    else:
        column_label = "Percentile_col"
    data_frame[column_label] = np.percentile(data_frame.drop(celltype, axis=1).values, start_percent, axis=1)
    return data_frame, column_label


def df_filter_by_column_value(data_frame, column, value=0):
    """ Returns a df containing only the rows that present a value = x for the column "column" """
    data_filtered = data_frame[data_frame[column] == value]
    return data_filtered


def columns_to_numeric(df, *cols):
    for col in cols:
        df[col] = pd.to_numeric(df[col])


def series_frequency(series, value, percent=True):
    """
    Calculates the frequency of a value in a list.
    :param pd.Series series: the pandas.Series.
    :param value: the value to calculate the frequency
    :return: The frequency of a value in a list
    """
    number_of_value = series.values.tolist().count(value)
    frequency_ = number_of_value/len(series)
    if percent:
        frequency_ *= 100
    return frequency_

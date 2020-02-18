# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:12:18 2020

@author: vincent
"""

# from datetime import datetime, time
import pytz
import datetime as dt
from datetime import time
import pandas as pd
import pyodbc
import os

odbc_driver_template = 'ODBC Driver {} for SQL Server'


def get_pyodbc_sql_server_driver_version():
    pyodbc_drivers = pyodbc.drivers()
    versions = [17, 13.1, 13, 11]  # higher version is better
    for version in versions:
        if 'ODBC Driver {} for SQL Server'.format(version) in pyodbc_drivers:
            return version
    return None


def get_data_from_mssql(formatted_query, database):
    """
    Gets the data from the sql server database
    :param s: required variables
    :param formatted_query: Formatted query
    :param database: Name of the database
    :return: data frame
    """

    driver_ver = get_pyodbc_sql_server_driver_version()
    with pyodbc.connect('DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(odbc_driver_template.format(driver_ver),
                                                                               os.environ['SQL_HOST'],
                                                                               database, os.environ['SQL_USERNAME'],
                                                                               os.environ['SQL_PASSWORD'])) as cursor:
        raw_data = pd.read_sql(formatted_query, cursor)
    return raw_data


def get_apx_spot_prices(startdate_local, enddate_local=None):
    """
    Gets APX spot prices from datahub
    :param startdate_local: startdate (inclusive) of the date range
    :param enddate_local: enddate (inclusive) of the range. If this aruments is omitted than startdate + 23h is taken 
    """
    if not enddate_local:
        enddate_local = dt.datetime.combine(startdate_local, time(23, 00))
    stmt = "SELECT datetime, value_nl FROM spot_prices_data_source " \
           "where datetime >= '{}' and datetime <= '{}'".format(convert_datetime_local_to_str_utc(startdate_local),
                                                                convert_datetime_local_to_str_utc(enddate_local))
    df = get_data_from_mssql(stmt, 'datagenic')
    df = df.set_index(['datetime'])
    df.index = df.index.tz_localize('UTC').tz_convert('Europe/Amsterdam')
    return df


def convert_datetime_local_to_str_utc(datetime_local, tzone='Europe/Amsterdam'):
    """
    Converts local datetime to UTC and then to a string
    """
    tz = pytz.timezone(tzone)
    return tz.localize(datetime_local).astimezone(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")


def resample_hourly_df_to_ptuly(df):
    """
    Converts hourly df to 15min level df
    :param df: df with hourly index
    :return df: dataframe with 15min index
    """
    new_datetime = df.index[-1] + dt.timedelta(hours=1)
    new_data = pd.DataFrame(df[-1:].values, index=[new_datetime], columns=df.columns)
    df_out = df.append(new_data)
    return df_out.resample('15min').pad()[:-1]

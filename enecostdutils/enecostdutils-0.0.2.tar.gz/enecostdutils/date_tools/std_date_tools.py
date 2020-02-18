# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:12:18 2020

@author: vincent
"""

import datetime as dt
import pandas as pd
import pytz
from datetime import time
import numpy as np


def get_num_ptus_on_date(date, tzone='Europe/Amsterdam'):
    """
    Returns the number of ptus on given date.

    :param date: Datetime for which number of ptus we need
    :param tzone: String with datetime, default 'Europe/Amsterdam'

    :return: Int with number of ptus in day (i.e. 96 normal and 100 in Oct)
    """
    tz = pytz.timezone(tzone)
    startdate = tz.localize(dt.datetime.combine(date, time(0, 0)))
    enddate = tz.localize(dt.datetime.combine(date, time(23, 45)))
    num_ptus = len(pd.date_range(startdate, enddate, freq='15min'))
    return num_ptus


def is_date_dst_october(date):
    """
    Checks whether date is dst date in October.
    
    :param date: Datetime to check
    :return: boolean
    """
    if get_num_ptus_on_date(date) == 100:
        is_dst_oct = True
    else:
        is_dst_oct = False
    return is_dst_oct


def is_date_dst_march(date):
    """
    Checks whether date is dst date in March.
    
    :param date: Datetime to check
    :return: boolean
    """
    if get_num_ptus_on_date(date) == 92:
        is_dst_mar = True
    else:
        is_dst_mar = False
    return is_dst_mar


def is_date_dst(date):
    """
    Checks whether date is a dst date.
    
    :param date: Datetime to check
    :return: boolean
    """
    if get_num_ptus_on_date(date) != 96:
        is_dst = True
    else:
        is_dst = False
    return is_dst


def get_dst_dates_oct_in_range(startdate, enddate):
    """
    Calculates all dst dates October in given range.
    
    :param startdate: datetime where range starts
    :param enddate: datetim where range stops
    :return: list with datetimes
    """
    A = pd.date_range(startdate, enddate, freq='D')
    B = list(A)
    C = list(map(is_date_dst_october, B))
    D = np.array(C)
    idx = D == True
    ll = list(A[idx])
    return ll


def get_dst_dates_march_in_range(startdate, enddate):
    """
    Calculates all dst dates March in given range.
    
    :param startdate: datetime where range starts
    :param enddate: datetim where range stops
    :return: list with datetimes
    """
    A = pd.date_range(startdate, enddate, freq='D')
    B = list(A)
    C = list(map(is_date_dst_march, B))
    D = np.array(C)
    idx = D == True
    ll = list(A[idx])
    return ll

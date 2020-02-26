# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 09, 2018
# Modifi: May 09, 2018

MS_PER_SECOND = 1000
MS_PER_MINUTE = 60000
MS_PER_HOUR = 3600000
MS_PER_DAY = 86400000

def current_timestamp(strMessage = None):
    import datetime
    if strMessage is None:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        return "{0} {1}".format(timestamp, strMessage)

def time_since1970():
    import time
    return time.time()
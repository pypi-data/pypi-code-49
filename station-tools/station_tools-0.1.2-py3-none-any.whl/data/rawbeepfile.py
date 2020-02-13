import logging
import pandas as pd
import utm
from . import datafile

class RawBeepFile(datafile.DataFile):
    """sensor station beep file"""
    FILTER_MAX_RSSI = -20

    def __init__(self, filename):
        super(RawBeepFile, self).__init__(filename)

    def _clean(self):
        """convert Time column to datetime

        drop na records
        consistent node id"""
        df = self.df
        df.Time = pd.to_datetime(df.Time)

        # drop na records
        pre_count = df.shape[0]
        df = df.dropna()
        dropped_count = pre_count - df.shape[0]
        if dropped_count > 0:
            logging.error('dropped {:,} n/a records from {:,} records'.format(dropped_count, pre_count))
        df = df.set_index('Time')

        # drop abnormal RSSI values
        df = df[df.TagRSSI < self.FILTER_MAX_RSSI]
        return df

    def beep_count(self):
        return self.df.shape[0]

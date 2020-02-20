# -*- coding: UTF-8 -*-
from datetime import datetime
from StringIO import StringIO
import pandas as pd
from utils import get_station


PARSE_EVENT_CODE = {
    0: [1, 1],
    1: [1, 2],
    2: [1, 3],
    3: [1, 98],
    4: [1, 98],
    5: [4, 1],
    6: [1, 30],
    7: [1, 99],
    8: [1, 99],
    9: [1, 50],
    10: [2, 2],
    11: [2, 3],
    12: [1, 9],
    13: [6, 1],
    14: [1, 98],
    15: [1, 8],
    16: [5, 20],
}


class PlcMeasureEventsParser(object):

    def __init__(self, events_file, cnc_name):
        """Creates a dictionary with data from PLC800"""
        # Support for files or raw string
        if isinstance(events_file, str):
            events_file = StringIO(events_file)
        if not hasattr(events_file, 'read'):
            raise TypeError('Must be file pointer or basestring')
        # read file
        self.cnc_name = cnc_name
        self.df_profiles = pd.read_csv(events_file, header=None, sep=';',
                                       names=['name', 'timestamp', 'event_group', 'event_code_desc'],
                                       dtype={'name': str, 'timestamp': str, 'event_group': int,
                                              'event_code_desc': str})

    @property
    def events(self):
        df = self.df_profiles.copy()
        df['cnc_name'] = self.cnc_name
        df['timestamp'] = df['timestamp'].apply(
            lambda x: datetime.strptime(x, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'))
        df['season'] = df['timestamp'].apply(lambda x: get_station(x))
        df['event_code'] = df['event_group'].apply(lambda x: PARSE_EVENT_CODE.get(x)[1])
        df['event_group'] = df['event_group'].apply(lambda x: PARSE_EVENT_CODE.get(x)[0])
        df['type'] = 'M'
        df['active'] = True
        return df.T.to_dict().values()

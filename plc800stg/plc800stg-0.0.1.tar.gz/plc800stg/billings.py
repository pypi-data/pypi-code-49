# -*- coding: UTF-8 -*-
from StringIO import StringIO
import pandas as pd
from datetime import datetime


class PlcMonthlyBillingsParser(object):
    """PLC Monthly Billings Parser"""

    def __init__(self, billings_file, cnc_name):
        """Creates a dictionary with data from PLC800"""
        # Support for files or raw string
        if isinstance(billings_file, str):
            billings_file = StringIO(billings_file)
        if not hasattr(billings_file, 'read'):
            raise TypeError('Must be file pointer or basestring')
        # read file
        self.cnc_name = cnc_name
        df = pd.read_csv(billings_file, header=None, sep='\n')
        self.df_billings = df[0].str.split(';', expand=True)

    @property
    def billings(self):
        data = []
        for row in self.df_billings.T.to_dict().values():
            num_periods = int(row[2]) + 1
            for period in range(0, num_periods):
                # read row info for each period
                meter_name = row[0]
                contract = int(row[1])
                date_end = datetime.strptime(row[3], '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                date_begin = datetime.strptime(
                    date_end, '%Y-%m-%d %H:%M:%S').replace(day=1).strftime('%Y-%m-%d %H:%M:%S')
                index_activa = 4 + period
                activa_entrante = int(row[index_activa])
                index_inductiva = index_activa + num_periods
                inductiva = int(row[index_inductiva])
                index_capacitativa = index_inductiva + num_periods
                capacitativa = int(row[index_capacitativa])
                index_maxim = index_capacitativa + num_periods
                maxim = float(row[index_maxim])
                billing = {
                    'name': meter_name,
                    'contract': contract,
                    'type': 'month',
                    'value': 'a',
                    'date_begin': date_begin,
                    'date_end': date_end,
                    'period': period,
                    'max': maxim,
                    'date_max': False,
                    'ai': activa_entrante,
                    'ae': 0,
                    'r1': inductiva,
                    'r2': 0,
                    'r3': 0,
                    'r4': capacitativa,
                    'cnc_name': self.cnc_name,
                }
                data.append(billing)
        return data


class PlcDailyBillingsParser(object):
    """PLC Daily Billings Parser"""

    def __init__(self, billings_file, cnc_name):
        """Creates a dictionary with data from PLC800"""
        # Support for files or raw string
        if isinstance(billings_file, str):
            billings_file = StringIO(billings_file)
        if not hasattr(billings_file, 'read'):
            raise TypeError('Must be file pointer or basestring')
        # read file
        self.cnc_name = cnc_name
        self.df_billings = pd.read_csv(billings_file, header=None, sep=';',
                                       names=['name', 'date_end', 'ai', 'ae', 'r1', 'r2', 'r3', 'r4'],
                                       dtype={'name': str, 'date_end': str, 'ai': int, 'ae': int,
                                              'r1': int, 'r2': int, 'r3': int, 'r4': int})

    @property
    def billings(self):
        df = self.df_billings.copy()
        df['contract'] = 1
        df['type'] = 'day'
        df['value'] = 'a'
        df['contract'] = 1
        df['date_end'] = df['date_end'].apply(
            lambda x: datetime.strptime(x, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'))
        df['date_begin'] = df['date_end']
        df['period'] = 0
        df['max'] = 0
        df['date_max'] = False
        df['cnc_name'] = self.cnc_name
        return df.T.to_dict().values()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Create reports from a CSV file.

A simple class to create reports with data from the SWLing
CSV file. Uses `Pandas` data analysis toolkit for importing
and manipulating data. Uses `BeautifulTable` for printing
tabular data in ASCII format.

Example
-------
.. code-block:: python
    :caption: Create an instance using a context manager (recommended)

    with Report(csv_file_full_path) as rpt:
        rpt.create_report(report_name, parameter)

"""

# standard library modules
import os
import sys

# 3rd party modules
import pandas as pd
from beautifultable import BeautifulTable

# local modules
from swtools.constants import FORMATTERS


class Report():
    """A simple class to create reports from a CSV file."""

    def __init__(self, csvfile=None):
        self.data = None
        self.filename = csvfile
        self.bt = None
        self.df = None
        self.report = None
        self.records = None
        self.count = None
        self.columns = None

        # a new BeautifulTable style based on the MySQL style
        # but with no row separators for a more compact display
        self.MySQLCompactStyle = {
            'left_border_char': '|',
            'right_border_char': '|',
            'top_border_char': '-',
            'bottom_border_char': '-',
            'header_separator_char': '-',
            'column_separator_char': '|'
        }

        # replacement values for `NaN` when the CSV file is read
        self.NaValues = {
            'Transmitter': '** No transmitter data **',
            'Target': '** No target area data **'
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.data = None
        self.df = None

    def main(self, report, param=None):
        """Create a report.

        Reads data from the CSV file and then runs the report method.
        Handles the case where the report method is not found or if
        the report has no data. Any parameters are report dependent.

        :param report: A report method name.
        :type time: str

        :param param: A parameter for the report.
        :type param: str
        """

        # read data from the CSV file
        if self.data is None:
            self.read_data()

        # run a report method (a `Pandas` data analysis) using getattr
        self.run_report(report, param)

        # print the results in a `BeautifulTable`
        # if the DataFrame is None, the report (method) does not exist
        # if the DataFrame is empty, there is no data returned
        if self.df is None:
            print('\n Report is not available:', report, '\n')
            sys.exit(0)
        elif self.df.empty is True:
            print('\n There is no data for this report', report, '\n')
            sys.exit(0)
        else:
            self.print_report(self.df, self.MySQLCompactStyle)

    def read_data(self):
        """Read data from the csv file.

        Note: replaces missing values (NaN).
        """
        self.data = pd.read_csv(self.filename, delimiter='|')
        self.data = self.data.fillna(value=self.NaValues)
        return self.data

    def run_report(self, report, param=None):
        """Run the appropriate report method.

        :param report: A report method name.
        :type time: str

        :param param: A parameter for the report.
        :type param: str
        """
        default = "report_stations"
        return getattr(self, report, lambda: default)(param)

    def print_report(self, df, style):
        """Print a beautiful report."""
        self.bt = BeautifulTable(max_width=200)
        self.bt_report_data(self.bt, df)
        self.bt_report_style(self.bt, style)
        self.bt_report_props(self.bt, self.columns)
        wrapper = self.bt_report_wrapper()
        wrapper.append_row([self.bt])
        print('')
        print(wrapper)
        print('', self.records, self.count, '\n')

    def report_transmitters(self, param=None):
        """Transmitters summary report.

        Group and count transmitter occurences to show
        most frequently received transmitter signals.

        Note: For EiBi data, the geolocation is removed for readability.
        """
        # self.data['Transmitter'] = self.data.apply(lambda x: x['Transmitter'][:self.first_digit(x['Transmitter'])], axis=1)
        df = pd.DataFrame(self.data, dtype=str)
        df = df.groupby(['Transmitter', 'Country']).agg(Records=('Transmitter', 'count')).reset_index()
        # df = df.groupby(['Transmitter', 'Country']).agg(Records=('Transmitter', 'count')).reset_index()
        self.df = df.sort_values(by='Records', ascending=False)
        self.report = 'SWLing Summary Report: Transmitters'
        self.records = 'Records: ' + str(df['Records'].sum())
        self.count = 'Transmitters: ' + str(df['Records'].count())
        self.columns = {
            0: BeautifulTable.ALIGN_LEFT,
            # 1: BeautifulTable.ALIGN_LEFT,
            2: BeautifulTable.ALIGN_RIGHT
        }
        return self.df

    def report_stations(self, param=None):
        """Stations summary report.

        Group and count station occurences to show
        most frequently received stations.

        Note: For Aoki data, the station generally includes the scheduled program.
        """
        df = pd.DataFrame(self.data, dtype=str)
        df = df.groupby('Station').agg(Records=('Station', 'count')).reset_index()
        self.df = df.sort_values(by='Records', ascending=False)
        self.report = 'SWLing Summary Report: Stations'
        self.records = 'Records: ' + str(df['Records'].sum())
        self.count = 'Stations: ' + str(df['Records'].count())
        self.columns = {
            0: BeautifulTable.ALIGN_LEFT,
            1: BeautifulTable.ALIGN_RIGHT
        }
        return self.df

    def report_frequencies(self, param=None):
        """Frequencies summary report.

        Group and count frequency occurences to show
        most frequently received frequencies.

        Note: For Aoki data, the same frequency may have more than one station or program.
        """
        df = pd.DataFrame(self.data, dtype=str)
        df = df.groupby(['Freq', 'Station']).agg(Records=('Freq', 'count')).reset_index()
        self.df = df.sort_values(by=['Records', 'Freq'], ascending=[False, True])
        self.report = 'SWLing Summary Report: Frequencies'
        self.records = 'Records: ' + str(df['Records'].sum())
        self.count = 'Frequencies: ' + str(df['Records'].count())
        self.columns = {
            0: BeautifulTable.ALIGN_LEFT,
            1: BeautifulTable.ALIGN_LEFT,
            2: BeautifulTable.ALIGN_RIGHT
        }
        return self.df

    def report_frequency_history(self, freq):
        """Frequency history detail report.

        Count specific frequency occurences to show the most
        frequently received stations and scheduled programs.

        :param param: Frequency
        :type param: int
        """
        self.data['Transmitter'] = self.data.apply(lambda x: x['Transmitter'][:self.first_digit(x['Transmitter'])], axis=1)
        df = pd.DataFrame(self.data, columns=['Date', 'Local', 'UTC', 'Dow', 'Station', 'Lang', 'Transmitter', 'Freq'], dtype=str)
        mask = df['Freq'] == freq
        self.df = df[mask]
        self.df = self.df.sort_values(by=['Date', 'UTC'], ascending=[True, True])
        self.report = 'Shortwave Listening Detail Report for ' + freq + ' kHz'
        self.records = str(self.df['Freq'].count()) + ' occurences'
        self.count = ''
        self.columns = {
            0: BeautifulTable.ALIGN_LEFT,
            1: BeautifulTable.ALIGN_RIGHT,
            2: BeautifulTable.ALIGN_RIGHT
        }
        return self.df

    def bt_report_data(self, bt, df):
        """Add data from the DataFrame to the BeautifulTable."""
        for (index_label, row_series) in df.iterrows():
            bt.append_row(row_series.values.tolist())
        bt.column_headers = list(df.columns.values)
        return bt

    def bt_report_props(self, bt, columns):
        """Set the properties of the BeautifulTable."""
        bt.width_exceed_policy = BeautifulTable.WEP_ELLIPSIS
        for key, value in columns.items():
            bt.column_alignments[key] = value
        return bt

    def bt_report_style(self, bt, style):
        """Set the style attributes of the BeautifulTable."""
        bt.width_exceed_policy = BeautifulTable.WEP_ELLIPSIS
        bt.set_style(BeautifulTable.STYLE_NONE)
        for key, value in style.items():
            bt.__setattr__(key, value)
        return bt

    def bt_report_wrapper(self):
        """Create a wrapper table.

        Note: This simply adds some padding and a heading to the report.
        """
        wrapper = BeautifulTable(max_width=120, default_alignment=BeautifulTable.ALIGN_LEFT)
        wrapper.set_style(BeautifulTable.STYLE_NONE)
        wrapper.column_headers = [self.colorize(self.report, 'yellow')]
        return wrapper

    @staticmethod
    def first_digit(str):
        """Find index of first digit in string."""
        for i, c in enumerate(str):
            if c.isdigit():
                return i
                break

    @staticmethod
    def colorize(string, color):
        """Make a string a certain color."""
        if color not in FORMATTERS:
            return string
        return FORMATTERS[color] + string + '\033[0m'

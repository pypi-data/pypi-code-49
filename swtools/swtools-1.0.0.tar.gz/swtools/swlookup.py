#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Shortwave frequency lookup tool.

Lookup a shortwave frequency by following the
prompts. Local time is optional but recommended for
more accurate results. Type 'q' at any prompt to exit.

Results are displayed in a nicely formatted table.
Users will be asked if they want to save shortwave
listening (SWLing) session data to a CSV file. This
data is used by the `swling` reporting module, a
companion tool to `swlookup`.

Notes
-----
+ Schedule times are displayed in UTC.
+ Days of operation are displayed as numbers where 1 = Sunday.
+ Transmitters show the country code in parentheses if available.

Optional arguments:
    -h, --help     Show this help screen and exit.
    -v, --version  Show program version.

"""

# standard library modules
import sys
import os
import random
import re
import datetime
import csv

# 3rd party modules
from beautifultable import BeautifulTable

# local modules
from swtools.cli import Prompter
from swtools.constants import FORMATTERS, SWLOOKUP, SWLOOKUP_LOGO
from swtools.database import Database
import swtools.functions as tb


def main():
    """Main entry point of the application."""

    # generate an argument parser
    arg_parser = tb.generate_argparser(SWLOOKUP)
    args = arg_parser.parse_args()

    # if the namespace help attribute exists, then
    # show help (the module doctring) and quit
    if hasattr(args, 'help'):
        print(__doc__)
        sys.exit(1)

    # get schedule info from the database, this will appear in the heading
    schedule = lookup_schedule()
    schedule_text = ' {italic}{lightcyan}Schedule ' + schedule + '\n{reset}'

    # print a pretty heading with the logo, the schedule, and quick help
    bad_colors = ['black', 'white', 'darkgrey', 'red', 'bold', 'underline', 'italic' 'reset']
    colors = [FORMATTERS[color] for color in FORMATTERS if color not in bad_colors]
    colored_lines = [random.choice(colors) + line for line in SWLOOKUP_LOGO.split('\n')]
    print('\n'.join(colored_lines), '\033[0m')
    print(schedule_text.format(**FORMATTERS))
    print(' {italic}Please follow the prompts or type \'q\' to quit\n{reset}'.format(**FORMATTERS))

    # create a new instance of the Prompter class
    try:
        with Prompter() as prompt:

            # retrieve the argument for frequency
            frequency = prompt.get_input('frequency', True)

            # retrieve the argument for local broadcast time and convert to UTC (this argument is optional)
            local = prompt.get_input('local', False)
            if local is not None:
                utc = tb.convert_to_utc(local)
            else:
                utc = None

            # get data and print the results
            lookup_frequency(frequency, utc)

            # save SWLing session data to CSV ?
            if local is not None:
                answer = prompt.confirm('save')
                if answer == 'y':
                    # get the database key (this key is in the first column of the lookup results)
                    key = prompt.get_input('key', True)
                    # get the session signal quality (this is a number, wait 60 seconds and take the highest value)
                    dbu = prompt.get_input('dbu', True)
                    # lookup data for key
                    lookup_key(local, utc, key, dbu)

            # view SWLing history for this frequency ?
            view_history = prompt.confirm('history')
            if view_history == 'y':
                lookup_swling(frequency)
            else:
                print('')

    except Exception as error:
        print('\n An error occured:', error, '\n')
        sys.exit(1)

    # quit normally
    sys.exit(0)


def lookup_frequency(frequency, utc):
    """Lookup data for a frequency with optionally a UTC time.

    This lookup queries data to be displayed on screen.

    :param frequency: The frequency to lookup.
    :type frequency: int

    :param utc: The time in UTC format (%H%M) (optional)
    :type time: str
    """

    # base sql statement
    sql = '''
    SELECT
        a.id AS 'Key',
        a.frequency AS 'Freq',
        a.station AS 'Station',
        a.language AS 'Language',
        a.broadcast_time AS 'Schedule',
        a.days_of_operation AS 'Days',
        a.transmitter_location || ' (' || a.transmitter_adm || ')' AS 'Transmitter (Country)',
        CASE
            WHEN a.transmitter_power = '' THEN ''
            ELSE a.transmitter_power || ' KW'
        END AS 'Power'
    FROM aoki_db a
    WHERE (a.frequency = ?)'''

    # tuple for parameters
    params = (frequency,)

    # optional broadcast time in UTC
    # if it's provided, modify the SQL
    # and add to the params tuple
    if utc is not None:
        sql += ' AND (? BETWEEN a.start_time AND a.end_time)'
        params += (utc,)

    # lookup frequency in the database and print the results
    database = os.path.join(os.path.dirname(__file__), 'data/shortwave.sqlite3')
    try:
        with Database(database) as db:
            db.cursor.execute(sql, params)
            print_results(db.cursor, params)
    except Exception as error:
        print('\n An error occured:', error, '\n')
        sys.exit(1)


def lookup_key(local, utc, key, dbu):
    """Lookup data for a specific database key.

    This lookup queries data to be saved to a SWLING CSV file.

    :param local: The time in military (24-hour) format (%H:%M).
    :type local: str

    :param utc: The time in UTC format (%H%M)
    :type utc: str

    :param key: The database key. The key is included in the results.
    :type key: int

    :param dbu: The signal strength expressed as dBu. Use peak value.
    :type dbu: int
    """

    # get the date
    date = datetime.date.today()

    # get the day of the week
    dow = datetime.date.today().strftime('%a')

    # create a dictionary with all the data to pass along for saving the csv
    data = {'local': local, 'utc': utc, 'date': str(date), 'dow': dow, 'key': key, 'dbu': dbu}

    # base SQL statement
    swling = '''
    SELECT
        (SELECT schedule_name FROM schedule) AS Sked,
        a.frequency AS 'Freq',
        IFNULL(b.meter_band, '') AS 'Band',
        a.broadcast_time AS 'Schedule',
        a.days_of_operation  AS 'Days',
        a.transmitter_adm AS 'Country',
        a.station AS 'Station',
        a.language AS 'Lang',
        a.transmitter_location AS 'Transmitter',
        a.remarks AS 'Remarks'
    FROM aoki_db a
    LEFT JOIN meter_bands b ON a.frequency BETWEEN b.frequency_start AND b.frequency_end
    WHERE (a.id = ?)'''

    # lookup key in the database and save the results to CSV file
    database = os.path.join(os.path.dirname(__file__), 'data/shortwave.sqlite3')
    try:
        with Database(database) as db:
            db.cursor.execute(swling, (key,))
            save_results(db.cursor, data)
    except Exception as error:
        print('\n An error occured:', error, '\n')
        sys.exit(1)


def lookup_schedule():
    """Lookup shortwave schedule version information.

    This lookup queries schedule data to be shown in the header.
    """
    schedule = ''
    sql = '''SELECT schedule_season FROM schedule;'''

    # lookup the schedule info from the database
    # return an empty string if an error occurs
    database = os.path.dirname(__file__) + '/data/shortwave.sqlite3'
    try:
        with Database(database) as db:
            db.cursor.execute(sql)
            record = db.cursor.fetchone()
            schedule = record[0]
    except Exception as error:
        print('\n An error occured:', error, '\n')
        sys.exit(1)
    finally:
        return schedule

def print_results(cursor, params):
    """Print frequency lookup results in a `Beautiful Table`.

    :param cursor: A cursor instance with rows returned from the database.
    :type cursor: obj

    :param params: A tuple with the lookup parameters
    :type params: tuple
    """

    # create a beautiful table object with a max width of 120 characters
    table = BeautifulTable(max_width=120)

    # set the table width_exceed_policy to strip to fit column and add an ellipsis
    table.width_exceed_policy = BeautifulTable.WEP_ELLIPSIS  # WEP_WRAP or WEP_ELLIPSIS

    # row counter
    count = 0

    # cursor iterator
    row = None

    # append all rows to the table
    for row in cursor:
        table.append_row(row)
        count = count + 1

    # exit if no rows are returned
    if count == 0:
        msg = '\n {italic}Shortwave Frequency Lookup:  {purple}' + params[0] + ' kHz'
        if len(params) == 2:
            msg += ' @ ' + params[1] + ' UTC'
        msg += '{reset} not found!\n'
        print(msg.format(**FORMATTERS))
        sys.exit(0)

    # get column names for header
    columns = row.keys()

    # add some bold and color formatting to the headers using ansi escape sequences
    for i, s in enumerate(columns):
        columns[i] = '\033[1m\033[32m' + s + '\033[0m'

    # append table header
    table.column_headers = columns

    # left align some longer text columns
    table.column_alignments[2] = BeautifulTable.ALIGN_LEFT
    table.column_alignments[3] = BeautifulTable.ALIGN_LEFT
    table.column_alignments[6] = BeautifulTable.ALIGN_LEFT
    table.column_alignments[7] = BeautifulTable.ALIGN_RIGHT

    # create the table header
    msg = '\n{italic}Shortwave Frequency Lookup Results: {yellow}' + params[0] + ' kHz'
    if len(params) == 2:
        msg += ' @ ' + params[1] + ' UTC (' + tb.convert_to_local(params[1]) + ')'
    msg += '{reset}'

    # create another beautiful table object as a wrapper for the main table
    wrapper = BeautifulTable(max_width=120, default_alignment=BeautifulTable.ALIGN_LEFT)
    wrapper.set_style(BeautifulTable.STYLE_NONE)
    wrapper.column_headers = [msg.format(**FORMATTERS)]
    wrapper.append_row([table])

    # print out full results
    print(wrapper)
    print('')


def save_results(cursor, data):
    """Save SWLing session data to a CSV file.

    :param cursor: A cursor instance with a single row returned from the database.
    :type cursor: obj

    :param data: A dictionary with extra data to save.
    :type data: dict
    """

    # the CSV file name
    filename = os.path.join(os.path.dirname(__file__), 'data/swling.csv')

    try:

        # if the file does not exist yet, create it and add the column headers
        if not os.path.exists(filename):
            with open(filename, mode='w', encoding='UTF-8') as file:
                file.write('Date|Local|UTC|dBu|Dow|Sked|Freq|Band|Broadcast|Days|Country|Station|Lang|Transmitter|Remarks\n')

        # save the data for this key, adding the manual paramaters
        with open(filename, 'a') as f:
            data_row = data['date'] + '|' + data['local'] + '|' + data['utc'] + '|' + data['dbu'] + '|' + data['dow'] + '|'
            for row in cursor:
                for column in row:
                    data_row += str(column) + '|'
                f.write(data_row[0:-1] + '\n')

        # success
        print(' {bold}[{yellow}√{lightgrey}]{reset} Session data saved to CSV file....: √'.format(**FORMATTERS))

    except OSError as error:
        print('\n An error occured:', error, '\n')


def lookup_swling(frequency):
    """Lookup SWLing history data for a frequency.

    :param frequency: The frequency to lookup.
    :type frequency: int
    """

    # the CSV file name
    filename = os.path.join(os.path.dirname(__file__), 'data/swling.csv')

    # if the file does not exist yet, it means we haven't saved anything yet
    if not os.path.exists(filename):
        msg = '\n{italic}{yellow} There are no saved shortwave listening sessions yet!{reset}\n'
        print(msg.format(**FORMATTERS))
        sys.exit(0)

    # process CSV file
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file, delimiter='|')
        try:
            # create a beautiful table object with a max width of 120
            table = BeautifulTable(max_width=120)
            table.width_exceed_policy = BeautifulTable.WEP_ELLIPSIS  # WEP_WRAP or WEP_ELLIPSIS
            table.detect_numerics = False  # Fix for UTC leading zero bug

            count = 0
            row = None

            # append all rows to the table
            # if EiBi use: row['Transmitter'][:first_digit(row['Transmitter'])]
            for row in filter(lambda d: int(d['Freq']) == int(frequency), reader):
                data = (
                    row['Date'],
                    row['Local'],
                    row['UTC'],
                    row['dBu'],
                    row['Dow'],
                    row['Station'],
                    row['Lang'],
                    row['Transmitter'] + ' (' + row['Country'] + ')'
                )
                table.append_row(data)
                count = count + 1

            # exit if no rows are returned
            if count == 0:
                msg = '\n {italic}Shortwave Listening History: No data for frequency {yellow}' + frequency + ' kHz{reset}\n'
                print(msg.format(**FORMATTERS))
                sys.exit(0)

            # column names for header
            columns = ['Date', 'Local', 'UTC', 'dBu', 'Dow', 'Station', 'Language', 'Transmitter (Country)']

            # add some bold and color formatting to the headers using ansi escape sequences
            for i, s in enumerate(columns):
                columns[i] = '\033[1m\033[32m' + s + '\033[0m'

            # append table header
            table.column_headers = columns

            # left align some possibly long text columns
            table.column_alignments[5] = BeautifulTable.ALIGN_LEFT
            table.column_alignments[6] = BeautifulTable.ALIGN_LEFT
            table.column_alignments[7] = BeautifulTable.ALIGN_LEFT

            # print out results
            msg = '\n{italic}Shortwave Listening History: {yellow}' + frequency + ' kHz'

            # create a beautiful table object as a wrapper for the main table
            wrapper = BeautifulTable(max_width=120, default_alignment=BeautifulTable.ALIGN_LEFT)
            wrapper.set_style(BeautifulTable.STYLE_NONE)
            wrapper.column_headers = [msg.format(**FORMATTERS)]
            wrapper.append_row([table])
            print(wrapper, '\n')

        except csv.Error as e:
            error_message = 'file {}, line {}: {}'.format(filename, reader.line_num, e)
            print(error_message)
            sys.exit(1)


if __name__ == "__main__":
    main()

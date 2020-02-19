# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
from sys import version_info
import os, sys

from iocbio.kinetics.io.db import DatabaseInterface

def fetch(s):
    """Query the data from the database

    Perform SQL query from the experiments database using SELECT
    statement.

    Parameters
    ----------

    s : str
      SQL statement as a string

    Returns
    -------
    iterative
      Result of records.query - iterative rows of the results
    """
    slower = s.lower()
    for k in ['insert ', 'create ', 'update ', 'set ', 'delete ']:
        if k in slower.lower():
            print('Not allowed sql commad: %s' % k)
            exit()

    database = DatabaseInterface.get_database()
    records = database.query(s)
    database.close()

    return records


def export_csv(out_file, records):
    """Write results of `fetch` to CSV file

    Parameters
    ----------
    out_file : str
      Filename for the results file. If it does not end on ".csv", extension ".csv" will be appended to the filename
    records : iterative rows
      Result of SQL query as returned by `fetch` function
    """
    if out_file == '-':
        fh = sys.stdout
    else:
        fh = open(out_file if out_file.endswith('.csv') else out_file+'.csv', 'w')
    with fh as result:
        result.write(records.export('csv'))


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Simple tool for fetching data from database',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog = 'To specify database, user name and password, ' + \
                                     'use "iocbio-kinetics --db"')
    parser.add_argument('sql_file', type=str, help='Input SQL query file')
    parser.add_argument('out_file', type=str, help='Output CSV file or - for stdout output')
    args = parser.parse_args()

    # opening sql file
    with open(args.sql_file, 'r') as f:
        s = f.read()

    r = fetch(s)
    export_csv(args.out_file, r)


# if run as a script
if __name__ == '__main__':
    main()

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
#!/usr/bin/env python3
from sys import version_info
import os, sys
import random, string

from iocbio.kinetics.io.db import DatabaseInterface

def tmpname():
    return 'fetch_repeated_' + ''.join(random.choice(string.ascii_uppercase) for _ in range(6))


def fetch_repeated(s, value, tag, cid):
    """Query the data from the database and return in wide format

    Perform SQL query from the experiments database using SELECT
    statement and collect the data corresponding to the same ID on a
    single row.

    Parameters
    ----------

    s : str
      SQL statement as a string
    value : str
      Column name which contains value
    tag : str
      Column name with the tag used for different conditions
    cid : str
      Column name with the ID that is the same for repeated measure
    
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

    extras = []
    for line in s.split('\n'):
        if line.strip().startswith('--#'):
            e = line.split('--#')[1].split('--')[0].strip()
            if len(e) > 0: extras.append(e)

    database = DatabaseInterface.get_database()

    # get all distinct tags
    tags = []
    for r in database.query("SELECT %s FROM (%s) AS foo GROUP BY %s" % (tag, s, tag)):
        t = r[0]
        tags.append(t)
    tags.sort()

    # get extra columns from query
    columns = []
    r = database.query(s + " LIMIT 1").first()
    for k in r.keys():
        if k not in [value, cid, tag]:
            columns.append(k)

    # create temporary table
    Tt = tmpname()
    database.query('CREATE TEMPORARY TABLE ' + Tt + ' AS ' + s)
    database.query('CREATE INDEX ON ' + Tt + '(%s)' % cid)
    database.query('CREATE INDEX ON ' + Tt + '(%s)' % tag)
    database.query('ANALYZE ' + Tt)

    # compose SELECT
    sql = "SELECT *"
    if len(extras) > 0:
        sql += "," + ",".join(extras)

    sql += " FROM (SELECT "
    for c in columns: sql += "t0." + c + ","

    tc = 0
    joiner = None
    cond = "WHERE "
    for t in tags:
        tsane = t.replace(' ', '_').replace('-','m').replace('>','ra').replace('.','p').replace('+','P').replace('/','S')
        sql += "t" + str(tc) + "." + value + " AS " + tsane + ","
        cond += "t%d.%s = '%s' AND " % (tc, tag, t)
        if joiner is None:
            joiner = "FROM %s AS t0" % Tt
        else:
            joiner += " FULL JOIN %s AS t%d ON t0.%s = t%d.%s" % (Tt, tc, cid, tc, cid)
        tc += 1

    sql = sql[:-1] + " " + joiner + " " + cond[:-4] + " ) s"

    # get data
    print("SQL COMMAND:\n\n%s\n\n" % sql)
    records = database.query(sql)
    database.close()

    return records


def export_csv(out_file, records):
    """Write results of `fetch_repeated` to CSV file

    Parameters
    ----------
    out_file : str
      Filename for the results file. If it does not end on ".csv", extension ".csv" will be appended to the filename
    records : iterative rows
      Result of SQL query as returned by `fetch_repeated` function
    """

    if out_file == '-':
        fh = sys.stdout
    else:
        fh = open(out_file if out_file.endswith('.csv') else out_file+'.csv', 'w')
    with fh as result:
        result.write(records.export('csv'))




def main():
    import argparse
    parser = argparse.ArgumentParser(description='Simple tool for fetching data from SysBio database',
                                     epilog = 'To specify database, user name and password, ' + \
                                     'use "iocbio-kinetics --db"',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('sql_file', type=str, help='Input SQL query file')
    parser.add_argument('value', type=str, help='Column name with the value of the measurement')
    parser.add_argument('tag', type=str, help='Column name with the tag used for different conditions (for example, type)')
    parser.add_argument('id', type=str, help='Column name with the ID that is the same for repeated measure (for example, data_id)')
    parser.add_argument('out_file', type=str, help='Output CSV file or - for stdout output')
    args = parser.parse_args()

    # opening sql file
    with open(args.sql_file, 'r') as f:
        s = f.read()

    r = fetch_repeated(s, value=args.value, tag=args.tag, cid=args.id)
    export_csv(args.out_file, r)


# if run as a script
if __name__ == '__main__':
    main()

#!/usr/bin/env python
"""
Show some basic information from IT4I PBS accounting
"""
import argparse
import getpass
import sys
import pycent

from tabulate import tabulate
from .logger import LOGGER
from .config import API_URL
from .config import IT4IFREETOKEN
from .config import CONFIG_FILES
from .jsonlib import jsondata

TABLE_ME_TITLE = 'Projects I am participating in'
TABLE_ME_AS_PI_TITLE = 'Projects I am Primarily Investigating'
TABLE_LEGENDS_TITLE = 'Legend'

def ifpercent(part, whole, percent):
    """
    Return percent if required and it is possible, otherwise return origin number
    """
    if percent:
        try:
            return pycent.percentage(part, whole)
        except ZeroDivisionError:
            raise ZeroDivisionError
    else:
        return part

def main():
    """
    main function
    """

    parser = argparse.ArgumentParser(description="""
The command shows some basic information from IT4I PBS accounting. The
data is related to the current user and to all projects in which user
participates.""",
                                     epilog="""
Columns of "%s":
         PID: Project ID/account string.
   Days left: Days till the given project expires.
       Total: Core-hours allocated to the given project.
        Used: Sum of core-hours used by all project members.
    ...by me: Core-hours used by the current user only.
        Free: Core-hours that haven't yet been utilized.

Columns of "%s" (if present):
         PID: Project ID/account string.
       Login: Project member's login name.
        Used: Project member's used core-hours.
""" % (TABLE_ME_TITLE, TABLE_ME_AS_PI_TITLE),
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-p', '--percent',
                        action='store_true',
                        help="""
show values in percentage. Projects with unlimited resources are not displayed""")

    arguments = parser.parse_args()

    if IT4IFREETOKEN is None:
        LOGGER.error("""Missing or unset configuration option: %s
Suggested paths:
%s
""", "it4ifreetoken", CONFIG_FILES)
        sys.exit(1)

    username = getpass.getuser().strip()
    remote = ('%s/it4ifree/%s' % (API_URL, username))
    data = {'it4ifreetoken' : IT4IFREETOKEN}
    jsonout = jsondata(remote, data)

    table_me = []
    for row in jsonout['me']:
        try:
            table_me.append([row['pid'],
                             row['days_left'],
                             row['total'],
                             ifpercent(row['used'], row['total'], arguments.percent),
                             ifpercent(row['used_with_factor'], row['total'], arguments.percent),
                             ifpercent(row['used_by_me'], row['total'], arguments.percent),
                             ifpercent(row['used_by_me_with_factor'], row['total'], arguments.percent),
                             ifpercent(row['free'], row['total'], arguments.percent)])
        except ZeroDivisionError:
            pass
    table_me_headers = ['PID',
                        'Days left',
                        'Total',
                        'Used WCHs',
                        'Used NCHs',
                        'WCHs by me',
                        'NCHs by me',
                        'Free']

    table_me_as_pi = []
    row_previous = ''
    for row in jsonout['me_as_pi']:
        total = [project['total'] for project in jsonout['me'] if project['pid'] == row['pid']][0]
        try:
            table_me_as_pi.append([row['pid'] if row['pid'] != row_previous else '',
                                   row['login'],
                                   ifpercent(row['core_hours'], total, arguments.percent),
                                   ifpercent(row['core_hours_with_factor'], total, arguments.percent)])
        except ZeroDivisionError:
            pass
        row_previous = row['pid']
    table_me_as_pi_headers = ['PID',
                              'Login',
                              'Used WCHs',
                              'Used NCHs']

    if table_me:
        print >> sys.stdout, '\n%s\n%s' % (TABLE_ME_TITLE,
                                           len(TABLE_ME_TITLE) * '=')
        print tabulate(table_me, table_me_headers)

    if table_me_as_pi:
        print >> sys.stdout, '\n%s\n%s' % (TABLE_ME_AS_PI_TITLE,
                                           len(TABLE_ME_AS_PI_TITLE) * '=')
        print tabulate(table_me_as_pi, table_me_as_pi_headers)

    print >> sys.stdout, '\n%s\n%s' % (TABLE_LEGENDS_TITLE,
                                       len(TABLE_LEGENDS_TITLE) * '=')
    print 'WCH   =    Wall-clock Core-Hour'
    print 'NCH   =    Normalized Core-Hour'

if __name__ == "__main__":
    main()

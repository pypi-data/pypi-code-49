from jezdzenka.console.controllers import create, modify
from jezdzenka.console.shows import show_object
from jezdzenka.console.tables import show_in_table_normal, show_in_table_verbose, info_in_table
from jezdzenka.database.manipulation import move_to_archive, export, remove_elements_by_ids
from jezdzenka.database import collection
import os
import argparse

from jezdzenka.translation import _


def initial():
    parser = argparse.ArgumentParser(prog='jezdzenka',
                                     description=_('initial.description'))
    parser.add_argument('id', nargs='?', help=_('initial.id.help'))
    parser.add_argument('-a', '--all', action='store_true', help=_('initial.all.help'))
    parser.add_argument('-n', '--new', metavar='file', action='store', type=os.path.abspath, help=_('initial.new.help'))
    parser.add_argument('-o', '--outdated', nargs='+', metavar='id', action='store', help=_('initial.outdated.help'))
    parser.add_argument('-m', '--modify', metavar='id', action='store', help=_('initial.modify.help'))
    parser.add_argument('-i', '--info', metavar='id', action='store', help=_('initial.info.help'))
    parser.add_argument('-r', '--remove', nargs='+', metavar='id', action='store', help=_('initial.remove.help'))
    parser.add_argument('-t', '--tag', nargs='+', metavar='tag', action='store', help=_('initial.tag.help'))
    # parser.add_argument('-y', '--year', nargs='+', metavar='year', action='store', help=_('initial.year.help'))
    parser.add_argument('-e', '--export', action='store', help=_('initial.export.help'))
    parser.add_argument('-v', '--verbose', action='store_true', help=_('initial.verbose.help'))
    return parser.parse_args()


def interface_handler(args):
    # Get objects
    rows = collection.get_current()
    if args.all:
        rows = collection.get_all()
    # elif args.year:
    #    rows = collection.get_all_by_year(args.year)
    elif args.tag:
        rows = collection.get_all_by_tag(args.tag)

    # Actual options
    if args.new:
        create(args)
    elif args.modify:
        modify(args)
    elif args.export:
        export(rows, args.export)
    elif args.id:
        show_object(args.id)
    elif args.info:
        info_in_table(args.info)
    elif args.outdated:
        move_to_archive(args.outdated)
    elif args.remove:
        remove_elements_by_ids(args.remove)
    elif args.verbose:
        show_in_table_verbose(rows)
    else:
        show_in_table_normal(rows)
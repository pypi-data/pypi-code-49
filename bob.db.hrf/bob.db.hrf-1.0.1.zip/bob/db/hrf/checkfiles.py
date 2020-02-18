from pathlib import Path
import logging
import bob.extension
from .query import Database

def checkfiles(args):
    """ 
    Check if the local database tree is consistent 
    with the expected structure
    """
    
    db = Database(args.protocol)
    # go through all files, check if they are available on the filesystem
    good = []
    bad = []
    datadir = Path(args.datadir)
    paths = db.paths
    for obj in paths:
        obj = datadir.joinpath(obj)
        if obj.exists():
            good.append(obj)
            logging.info(f'Found file {obj}')
        else:
            bad.append(obj)
            logging.warning(f'Cannot find file {obj}')
    # report
    if bad:
        logging.warning(f'{len(bad)} files (out of {len(paths)}) were not found at "{str(datadir)}" ')
    else:
        print('checkfiles completed sucessfully')

    return 0


def add_command(subparsers):
    """Add specific subcommands that the action "checkfiles" can use"""
    from argparse import SUPPRESS
    parser = subparsers.add_parser('checkfiles', help='Check if the local database tree is consistent with the expected structure')
    parser.add_argument('-D', '--datadir', metavar='DIR', default=bob.extension.rc['bob.db.hrf.datadir'], help='path to HRF dataset, default uses bob config settings (to check use: bob config show).')
    parser.add_argument('-P', '--protocol', metavar='STR', default='default',help='The train/test set protocol to use')
    parser.add_argument('--self-test', dest="selftest", default=False, action='store_true', help=SUPPRESS)
    parser.set_defaults(func=checkfiles) # action
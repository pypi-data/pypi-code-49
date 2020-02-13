import sys
from optparse import OptionParser


def parse_cmd_line():
    parser = OptionParser()
    options, args = parser.parse_args()
    if len(args) < 1:
        print("Usage: {} -- command".format(sys.argv[0]))
        exit(1)
    return options, args

#!/usr/bin/env python
import argparse
from .__version__ import __description__


def cli():
    pass


def main(verbose):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('-v', '--verbose', help='be verbose', action='store_true')
    args = parser.parse_args()
    exit(main(args.verbose))

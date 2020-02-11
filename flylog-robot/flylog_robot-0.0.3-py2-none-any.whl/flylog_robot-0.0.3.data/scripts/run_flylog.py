#!python
# -*- coding: utf-8 -*-

"""
启动 flylog_agent
"""

import types
import argparse
import sys

import flylog
from flylog import Server, constants


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--host', default=constants.HOST, help='bind host', action='store')
    parser.add_argument('-p', '--port', default=constants.PORT, type=int, help='bind port', action='store')
    parser.add_argument('-c', '--config', help='config file', action='store', required=True)
    parser.add_argument('-v', '--version', action='version', version='%s' % flylog.__version__)
    return parser


def load_config(filename):
    d = types.ModuleType('config')
    d.__file__ = filename
    try:
        with open(filename) as config_file:
            exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
    except IOError as e:
        e.strerror = 'Unable to load configuration file (%s)' % e.strerror
        raise
    return d


def main():

    args = build_parser().parse_args()

    app = Server(config=load_config(args.config))

    try:
        app.run(args.host, args.port)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()

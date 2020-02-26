#!/usr/bin/env python3
# coding: utf-8

import argparse
from importlib import import_module

from ifconf.config_print import PrintConfigAction

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('config_function'
                        , nargs='+'
                        , type=str
                        , help='configuration callback methos')
    args = parser.parse_args()
    action = PrintConfigAction(parser, args)
    PrintConfigAction.set_callback_methods([getattr(import_module(f.rsplit('.', 1)[0]), f.rsplit('.', 1)[1]) for f in args.config_function])
    action(parser, args, args.config_function)

if __name__ == "__main__":
    main()

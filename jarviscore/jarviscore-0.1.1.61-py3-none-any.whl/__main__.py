# -*- coding: utf-8 -*-

import argparse
import sys
import platform
from pathlib import Path

import jarviscore

import pkg_resources
import pyodbc
import pymysql
import requests
from .client import Client



def show_version():
    entries = []

    entries.append('- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(sys.version_info))
    version_info = jarviscore.version_info
    entries.append('- jarviscore v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(version_info))
    if version_info.releaselevel != 'final':
        pkg = pkg_resources.get_distribution('jarviscore')
        if pkg:
            entries.append('    - jarviscore pkg_resources: v{0}'.format(pkg.version))

    entries.append('- pyodbc v{0.__version__}'.format(pyodbc))
    entries.append('- pymysql v{0.__version__}'.format(pymysql))
    entries.append('- requests v{0.__version__}'.format(requests))
    uname = platform.uname()
    entries.append('- system info: {0.system} {0.release} {0.version}'.format(uname))
    print('\n'.join(entries))

def core(parser, args):
    if args.version:
        show_version()
    




# def add_newbot_args(subparser):
#     parser = subparser.add_parser('newbot', help='creates a command bot project quickly')
#     parser.set_defaults(func=newbot)

#     parser.add_argument('name', help='the bot project name')
#     parser.add_argument('directory', help='the directory to place it in (default: .)', nargs='?', default=Path.cwd())
#     parser.add_argument('--prefix', help='the bot prefix (default: $)', default='$', metavar='<prefix>')
#     parser.add_argument('--no-git', help='do not create a .gitignore file', action='store_true', dest='no_git')


# def add_newcommand_args(subparser):
#     parser = subparser.add_parser('newcommand', help='creates a new command template quickly')
#     parser.set_defaults(func=newcog)

#     parser.add_argument('name', help='the command name')
#     parser.add_argument('directory', help='the directory to place it in (default: commands)', nargs='?', default=Path('commands'))
#     parser.add_argument('--class-name', help='the class name of the command (default: <name>)', dest='class_name')
#     parser.add_argument('--display-name', help='the command name (default: <name>)')
#     parser.add_argument('--hide-commands', help='whether to hide all commands in the command', action='store_true')
#     parser.add_argument('--full', help='add all special methods as well', action='store_true')



def parse_args():
    parser = argparse.ArgumentParser(prog='jarviscore', description='Tools for helping with jarviscore')
    parser.add_argument('-v', '--version', action='store_true', help='shows the library version')
    parser.set_defaults(func=core)

    #subparser = parser.add_subparsers(dest='subcommand', title='subcommands')
    #add_newbot_args(subparser)
    #add_newcommand_args(subparser)
    return parser, parser.parse_args()


def main():
    parser, args = parse_args()
    args.func(parser, args)

main()
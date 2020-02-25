#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This script defines the clinterfacer's create subparser."""

# standard library(ies)
import argparse
import pathlib as pl
from typing import Any

# local source(s)
from clinterfacer import subparsers
from clinterfacer import cli


def get_default(argument: str, default: Any = None) -> Any:
    return subparsers.get_default(__file__, argument, default)


def existent_folder_path(path: str) -> pl.Path:
    path = pl.Path(path).expanduser().absolute()
    if not path.exists():
        raise argparse.ArgumentTypeError(f'The given path does not exist.')
    return path


def add_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        'create',
        help='This is the create command of the clinterfacer command-line',
        prog='clinterfacer create',
        description='This command is the create one.')
    add_arguments(parser)


def add_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        'path',
        type=existent_folder_path,
        help=(
            'Specifies the path to the module i the package in which the command '
            'will be created. It is expected to exist the \'__main__.py\', '
            '\'commands.__init__.py\' and \'subparsers.__init__.py\' scripts in '
            'the given path. Otherwise, they will be generated as well. The '
            '\'__main__.py\' script is not created if the \'--no-main\' argument '
            'is setted. Similarly, the \'commands.__init__.py\' and '
            '\'subparsers.__init__.py\' scripts are not created if the \'--no-init\''
            ' argument is setted.'
        ),
    )
    parser.add_argument(
        'name',
        help='Specifies the name of the command to be created.',
    )
    parser.add_argument(
        '--no-main',
        help=(
            'Specifies that the \'__main__.py\' script should not be created, '
            'even if it does not exist.'
        ),
        dest='main',
        action='store_false',
    )
    parser.add_argument(
        '--no-init',
        help=(
            'Specifies that the \'commands.__init__.py\' and \'subparsers.__init__.py\' '
            'scripts should not be created, even if they does not exist.'
        ),
        dest='init',
        action='store_false',
    )
    parser.add_argument(
        '-f',
        '--force',
        help='Forces any existent file to be overwritten.',
        action='store_true',
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    add_arguments(parser)
    args = parser.parse_args()
    cli.setup()
    return args

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This python script implements the CommandLineInterface class.
"""

# standard library(ies)
import argparse
import importlib
import os
import typing

# 3rd party packages
import pkgutil

# local source(s)
from clinterfacer import cli


def remove_actions(parser: argparse.ArgumentParser,
                   actions: typing.List[argparse.Action]) -> None:
    for action in parser._actions:
        if action.dest in actions:
            action.container._remove_action(action)


def get_default(argument: str, default: typing.Any = None, key: str = None, f: typing.Callable = None) -> typing.Any:
    """
    This function helps to retrieve the default value of a given parameter.
    It gives an additional flexibility to the command-line interface by 
    loading the defined environment variables related to it.
    
    :param name: [description]
    :type name: str
    :param default: [description]
    :type default: typing.Any
    :param key: [description], defaults to None
    :type key: str, optional
    :param f: [description], defaults to None
    :type f: typing.Callable, optional
    :raises NotImplementedError: [description]
    :return: [description]
    :rtype: typing.Any
    """
    if not key:
        interface = cli.get_name().upper()
        command = cli.get_command_name().replace('-', '_').upper()
        argument = argument.lstrip('-').replace('-', '_').upper()
        key = f'{interface}_{command}_{argument}'
    default = os.environ.get(key, default)
    if not default:
        raise Exception(f'There is no environment variable defined as {key}. The {argument} argument must be given.')
    return f(default) if f else default


class Parser(object):

    def __init__(self, name: str) -> None:
        self.package = importlib.import_module(name)


    def get_commands(self) -> typing.List[str]:
        module = importlib.import_module(f'{self.package.__name__}.subparsers')
        return [name for _, name, _ in pkgutil.iter_modules(module.__path__)]


    def get_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            prog=self.package.__name__,
            description=self.package.__description__,
            epilog=
            f'Visit the project website at {self.package.__url__} for support.',
        )
        self.add_arguments(parser)
        return parser


    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=f'%(prog)s {self.package.__version__}',
        )
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            '-V',
            '--verbose',
            help='Increase the verbosity level.',
            action='store_true',
        )
        group.add_argument(
            '-q',
            '--quiet',
            help='Disable all output text messages.',
            action='store_true',
        )
        module = f'{self.package.__name__}.subparsers'
        module = importlib.import_module(module)
        if hasattr(module, 'add_arguments'):
            module.add_arguments(parser)
        subparsers = parser.add_subparsers(dest='command')
        for command in self.get_commands():
            module = f'{self.package.__name__}.subparsers.{command}'
            module = importlib.import_module(module)
            module.add_parser(subparsers)


    def parse(self,
              args: typing.List[str] = None) -> argparse.Namespace:
        parser = self.get_parser()
        return parser.parse_args(args)


    def print_help(self):
        self.get_parser().print_help()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This python script implements the Parser class.
"""

# standard library(ies)
from argparse import Action, ArgumentParser, Namespace
import importlib as il
import os
from typing import Any, Callable, List

# 3rd party packages
import pkgutil

# local source(s)
from clinterfacer import cli


def remove_actions(parser: ArgumentParser,
                   actions: List[Action]) -> None:
    for action in parser._actions:
        if action.dest in actions:
            action.container._remove_action(action)


def get_default(argument: str, default: Any = None, key: str = None, f: Callable = None) -> Any:
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

    def __init__(self, interface: object) -> None:
        self._interface = interface

    def get_commands(self) -> List[str]:
        module = il.import_module(f'{self._interface}.subparsers')
        return [name for _, name, _ in pkgutil.iter_modules(module.__path__)]

    def get_parser(self) -> ArgumentParser:
        parser = ArgumentParser(
            prog=self._interface.alias,
            description=self._interface.description,
            epilog=f'Visit the project website at {self._interface.url} for support.',
        )
        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=f'%(prog)s {self._interface.version}',
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
        module = f'{self._interface}.subparsers'
        module = il.import_module(module)
        if hasattr(module, 'add_arguments'):
            module.add_arguments(parser)
        subparsers = parser.add_subparsers(dest='command')
        for command in self.get_commands():
            module = f'{self._interface}.subparsers.{command}'
            module = il.import_module(module)
            module.add_parser(subparsers)

    def parse(self, args: List[str] = None) -> Namespace:
        parser = self.get_parser()
        return parser.parse_args(args)

    def print_help(self) -> None:
        self.get_parser().print_help()

    def __str__(self) -> str:
        return str(self._interface)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This python script implements the CommandLineInterface class.
"""

# standard library(ies)
import argparse
import importlib as il
from importlib import util
import inspect
import logging
from logging import config
import pathlib as pl
import typing

# 3rd party package(s)
try:
    import importlib_resources as ilr
    import temppathlib as tpl
except ImportError as e:
    pass

# local source(s)
from clinterfacer.parser import Parser

logger = logging.getLogger(__name__)


def is_root(path: typing.Union[str, pl.Path] = pl.Path.cwd()) -> bool:
    if isinstance(path, str):
        path = pl.Path(path)
    if not path.is_dir():
        return False
    expected_directories = {'commands', 'subparsers'}
    directories = {p.name for p in path.iterdir() if p.is_dir()}
    return (directories & expected_directories) == expected_directories


def find_root(path: typing.Union[str, pl.Path] = pl.Path.cwd()) -> pl.Path:
    if isinstance(path, str):
        path = pl.Path(path)
    while not is_root(path):
        if not len(path.parents):
            raise Exception(
                'The given path is not a child path of a '
                'package in which the clinterfacer is used.'
            )
        path = path.parent
    return path


def is_local_souce(path: typing.Union[str, pl.Path]):
    if isinstance(path, str):
        path = pl.Path(path)
    for p in path.parents:
        if p.is_dir() and p.name == 'clinterfacer':
            return True
    return False


def get_name(frame: object = inspect.currentframe()):
    info = inspect.getframeinfo(frame)
    while not info.filename.endswith('.py') or is_local_souce(info.filename):
        frame = frame.f_back
        info = inspect.getframeinfo(frame)
    return find_root(info.filename).name


def get_command_name(frame: object = inspect.currentframe()):
    raise NotImplementedError('The importlib library is not helping.')
    info = inspect.getframeinfo(frame)
    while not info.filename.endswith('.py') or is_local_souce(info.filename):
        frame = frame.f_back
        info = inspect.getframeinfo(frame)
    return pl.Path(info.filename).name.replace('_', '-') # to be verified


def setup(verbose: bool = False, quiet: bool = False) -> None:
    name = get_name()
    try:
        with ilr.path(f'{name}.resources', 'logging.ini') as path:
            config.fileConfig(path)
    except (ImportError, FileNotFoundError) as e:
        content = ilr.read_text('clinterfacer.resources',
                                'logging.template.ini')
        with tpl.TemporaryDirectory(prefix=name, dont_delete=True) as tmp:
            path = tmp.path / 'logging.ini'
            path.write_text(content.format(package=name))
            config.fileConfig(path)
    logger.debug(f'Loaded logging configuration according to the {path} file.')
    

class CommandLineInterface(object):

    def __init__(self) -> None:
        frame = inspect.currentframe().f_back
        info = inspect.getframeinfo(frame)
        self.function = info.function
        self.name = get_name(frame)
        self.alias = self.name.replace('_', '-')
        #if not util.find_spec(f'{self.name}.commands'):
        #    raise ModuleNotFoundError(f'The \'{self.name}.commands\' module cannot be imported.')
        #if not util.find_spec(f'{self.name}.subparsers'):
        #    raise ModuleNotFoundError(f'The \'{self.name}.subparsers\' module cannot be imported.')
        self.parser = Parser(self.name)
        self.logger = logging.getLogger(__name__)


    def parse(self, args: typing.List[str] = None) -> argparse.Namespace:
        return self.parser.parse(args)


    def main(self, args: typing.List[str] = None) -> int:
        args = self.parse(args)
        self.logger.debug(f'Parser the input arguments as follows: {args}')
        setup(args.verbose, args.quiet)
        module = f'{self.name}.commands'
        if args.command:
            module += f'.{args.command}'.replace('-', '_')
        if not util.find_spec(module):
            self.parser.print_help()
            return 0
        module = il.import_module(module)
        self.logger.debug(
            f'Running the \'{self.function}\' function of the {module} module ...')
        if not hasattr(module, self.function):
            self.parser.print_help()
            self.logger.debug(
                f'Exiting because the {args.command} command does not '
                f'implement the {self.function} function ...'
            )
            return 0
        answer = getattr(module, self.function)(args)
        self.logger.debug(f'Exiting with {answer} ...')
        return answer

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This python script implements the CommandLineInterface class.
"""

# standard library(ies)
from argparse import Namespace
import importlib as il
from importlib import util
import inspect
import logging
from logging import config

from pathlib import Path
import traceback as tb
from typing import List, Union

# 3rd party package(s)
try:
    import importlib_resources as ilr
    from temppathlib import TemporaryDirectory
except ImportError as e:
    pass

# local source(s)
from clinterfacer.parser import Parser

logger = logging.getLogger(__name__)


class Frame(object):

    _not_expected = (
        'clinterfacer/__init__.py',
        'clinterfacer/cli.py',
        'clinterfacer/parser.py',
    )

    def __init__(self, *, info, summary) -> None:
        self._info = info
        self._summary = summary
        self.path = Path(self._summary.filename)
        self.module = self._info.frame.f_globals['__name__']   
        if self.module.endswith('__main__'):
            self.module = self.path.parent.name
        self.package = self._info.frame.f_globals['__package__']
        if not len(self.package):
            self.package = self.path.parent.name
        self.function = self._summary.name

    def __str__(self) -> str:
        return self.module
    
    @staticmethod
    def _match(path: str) -> bool:
        return not path.endswith(Frame._not_expected)

    @staticmethod
    def find():
        stack_summary = tb.extract_stack()
        stack_info = inspect.stack()
        frame_summary = next(f for f in stack_summary[::-1] if Frame._match(f.filename))
        frame_info = next(f for f in stack_info if Frame._match(f.filename))
        return Frame(summary=frame_summary, info=frame_info)


def setup(verbose: bool = False, quiet: bool = False) -> None:
    frame = Frame.find()
    try:
        with ilr.path(f'{frame}.resources', 'logging.ini') as path:
            config.fileConfig(path)
    except (ImportError, FileNotFoundError) as e:
        content = ilr.read_text('clinterfacer.resources',
                                'logging.template.ini')
        with TemporaryDirectory(prefix=frame.package, dont_delete=True) as tmp:
            path = tmp.path / 'logging.ini'
            path.write_text(content.format(package=frame.module))
            config.fileConfig(path)
    logger.debug(f'Loaded logging configuration according to the {path} file.')


class CommandLineInterface(object):

    _expected = {
        'commands', 
        'subparsers',
    }

    def __init__(self) -> None:
        self._frame = Frame.find()
        self.function = self._frame.function
        self.module = self._frame.module
        self.package = il.import_module(self._frame.package)
        self.description = self.package.__description__
        self.version = self.package.__version__
        self.url = self.package.__url__
        self.name = self.module.split('.')[-1]
        self.alias = self.name.replace('_', '-')
        self.path = CommandLineInterface.find(self._frame.path)
        self.parser = Parser(self)
        self.logger = logging.getLogger(__name__)
        #if not util.find_spec(f'{self.name}.commands'):
        #    raise ModuleNotFoundError(f'The \'{self.name}.commands\' module cannot be imported.')
        #if not util.find_spec(f'{self.name}.subparsers'):
        #    raise ModuleNotFoundError(f'The \'{self.name}.subparsers\' module cannot be imported.')

    def parse(self, args: List[str] = None) -> Namespace:
        return self.parser.parse(args)

    def main(self, args: List[str] = None) -> int:
        args = self.parse(args)
        self.logger.debug(f'Parser the input arguments as follows: {args}')
        setup(args.verbose, args.quiet)
        module = f'{self}.commands'
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
                f'Exiting because the {module} module does not '
                f'implement the {self.function} function ...'
            )
            return 0
        answer = getattr(module, self.function)(args)
        self.logger.debug(f'Exiting with {answer} ...')
        return answer

    def __str__(self) -> str:
        return str(self._frame)

    @staticmethod
    def _match(path: Path = Path.cwd()) -> bool:
        if not path.is_dir():
            return False
        directories = {p.name for p in path.iterdir() if p.is_dir()}
        return (directories & CommandLineInterface._expected) == CommandLineInterface._expected

    @staticmethod
    def find(path: Union[str, Path] = Path.cwd()) -> Path:
        if isinstance(path, str):
            path = Path(path)
        while not CommandLineInterface._match(path):
            if not len(path.parents):
                raise Exception(
                    'The given path is not a child path of a '
                    'package in which the clinterfacer is used.'
                )
            path = path.parent
        return path

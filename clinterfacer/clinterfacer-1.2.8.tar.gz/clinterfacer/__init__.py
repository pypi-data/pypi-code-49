#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""__init__.py: This script includes all the project's metadata."""

# standard library(ies)
import pathlib as pl
import typing

# local source(s)
from .cli import CommandLineInterface as CLI


__author__ = (
    'Adriano Henrique Rossette Leite',
)
__email__ = (
    'adrianohrl@gmail.com',
)
__maintainer__ = (
    'Adriano Henrique Rossette Leite',
)
__copyright__ = ''
__credits__ = []
__license__ = ''
__version__ = '1.2.8' # this information should be altered only by the bumpversion tool
__status__ = 'Development' # should typically be one of 'Prototype', 'Development', 
__description__ = 'This framework aims to simplify the creation of Command-Line Interfaces (CLIs) using python.'
__url__ = 'https://gitlab.com/adrianohrl/clinterfacer'
__author__ = ', '.join(__author__)
__email__ = ', '.join(__email__)
__maintainer__ = ', '.join(__maintainer__)
options = [
    'Development',
    'Prototype',
    'Production',
]
if __status__ not in options:
    raise Exception(f'Invalid __status__: {__status__}. It should typically be one of the following: {options}')


def find_console_scripts(
    where: typing.Union[str, pl.Path] = pl.Path.cwd(),
    exclude: typing.Tuple[str] = (),
    include: typing.Tuple[str] = ('*',),
    replace: typing.Tuple[str, str] = ('_', '-'),
    entry_point: str = 'main',
    rename: typing.Dict[str, str] = None
) -> typing.List[str]:
    if isinstance(where, str):
        where = pl.Path(where)
    mandatory = ['commands', 'subparsers', '__main__.py']
    scripts = [{p.parent for p in where.rglob(m)} for m in mandatory]
    scripts = [s.name for s in set.intersection(*scripts)]
    def refactor(s):
        if rename and s in rename:
            s = rename[s]
        if replace:
            return s.replace(*replace)
        return s
    scripts = [(refactor(s), s) for s in scripts]
    # filter only scripts to be included and to be excluded
    return [f'{n} = {p}.__main__:{entry_point}' for n, p in scripts]

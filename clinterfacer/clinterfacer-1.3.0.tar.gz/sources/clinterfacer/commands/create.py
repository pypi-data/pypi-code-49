#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the main script of the clinterfacer's create command."""

# standard library(ies)
from argparse import Namespace
import logging
from pathlib import Path
import sys
import time
from typing import Dict, Tuple

# 3rd party package(s)
import importlib_resources as ilr

# local source(s)
from clinterfacer.subparsers.create import parse_args

logger = logging.getLogger(__name__)


def _prepare(path: Path) -> bool:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        logger.info(f'Created the {path} directory.')
    return path.is_dir()


def _write(path: Path, template: str, fields: Dict[str, str],
           force: bool) -> bool:
    if not _prepare(path.parent):
        logger.error(f'The given path {path} must be a directory.')
        return False
    if path.exists():
        if not force:
            logger.info(f'The {path} file already exists. '
                        'It will not be overwritten!')
            return True
        logger.info(f'Overwriting the {path} file ...')
    logger.info(f'Writing the {path} script ...')
    resources = f'clinterfacer.resources'
    if '/' in template:
        template = template.split('/')
        resources += '.' + '.'.join(template[:-1])
        template = template[-1]
    logger.debug(
        f'Reading the {template} template file located '
        f'in the {resources} module ...')
    template = ilr.read_text(resources, template)
    path.write_text(template.format(**fields))
    logger.info(f'Generated the {path} script.')
    return path.exists()


def _transform(path: Path, template: str,
               **kwargs: Dict[str, str]) -> Dict[Path, str]:
    def key(t: str) -> Path:
        t = t.format(**kwargs)
        return path / t

    def value(t: str) -> str:
        t = t.replace('{', '')
        t = t.replace('}', '')
        return t.replace('.', '.template.')

    return key(template), value(template)


def main(args: Namespace) -> int:
    fields = {
        'package': args.path.name,  # ??
        'module': args.path.name,  # ??
        'alias': args.path.name.replace('_', '-'),  # ??
        'command': args.name,
    }

    def _process(template: str) -> bool:
        path, template = _transform(args.path, template, **fields)
        return _write(path, template, fields, args.force)

    templates = (
        (args.main, '__main__.py'),
        (args.init, 'commands/__init__.py'),
        (True, 'commands/{command}.py'),
        (args.init, 'subparsers/__init__.py'),
        (True, 'subparsers/{command}.py'),
    )
    for check, template in templates:
        if check and not _process(template):
            return 1
    return 0


if __name__ == '__main__':
    start = time.time()
    args = parse_args()
    sys.exit(main(args))
    elapsed_time = (time.time() - start) / 60
    logger.info(f'Elapsed: {elapsed_time:.2f} minutes')
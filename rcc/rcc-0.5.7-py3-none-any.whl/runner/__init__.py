'''rcc main test driver.

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.

# flake8: noqa
'''

from pkgutil import walk_packages

import click
import coloredlogs

LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'
coloredlogs.install(level='WARNING', fmt=LOGGING_FORMAT)


@click.option('--verbose', '-v', envvar='COBRA_VERBOSE', is_flag=True)
@click.group()
@click.version_option()
def main(verbose):
    """\b
RCC

Rcc is a Redis Cluster Client
    """
    if verbose:
        coloredlogs.install(level='INFO', fmt=LOGGING_FORMAT)


for loader, module_name, is_pkg in walk_packages(__path__, __name__ + '.'):
    module = __import__(module_name, globals(), locals(), ['__name__'])
    cmd = getattr(module, module_name.rsplit('.', 1)[-1])
    if isinstance(cmd, click.Command):
        main.add_command(cmd)

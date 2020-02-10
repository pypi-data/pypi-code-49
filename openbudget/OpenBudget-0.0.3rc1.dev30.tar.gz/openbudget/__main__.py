# coding: utf-8

# Simple budget management planner
# Copyright (C) 2019 Yapbreak
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
Main interface
"""
import os
import click

import openbudget
from openbudget.core import logger
from openbudget.core.repositories import memories
import openbudget.cli.shell as cli


@click.command()
@click.option('--shell/--no-shell',
              default=False,
              help='Start interactive shell')
@click.option('--config',
              default=None,
              type=str,
              help='Use provided configuration file')
def main(shell, config):
    """
    Entry point for OpenBudget application
    """
    config_locations = []
    if config is not None:
        config_locations.append(config)
    config_locations.append(os.path.expanduser('~/.openbudgetrc'))
    config_locations.append(os.path.join('etc', 'openbudgetrc'))

    openbudget.__config__.read(config_locations, encoding='utf-8')
    if openbudget.__config__.has_section('logger'):
        logger.configure_logger(dict(openbudget.__config__.items('logger')))

    if shell:
        # Enable repository as singleton
        memories.Memory.shell_mode = True
        cli.shell()


def start():
    """
    Launch Click command from outside
    """
    main()  # pylint: disable=no-value-for-parameter

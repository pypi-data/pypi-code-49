# -*- coding: utf-8 -*-
"""
locale babel manager module.
"""

from pyrin.cli.mixin import CLIMixin
from pyrin.core.context import Manager
from pyrin.globalization.locale.babel.interface import BabelCLIHandlerBase


class LocaleBabelManager(Manager, CLIMixin):
    """
    locale babel manager class.
    """

    _cli_handler_type = BabelCLIHandlerBase

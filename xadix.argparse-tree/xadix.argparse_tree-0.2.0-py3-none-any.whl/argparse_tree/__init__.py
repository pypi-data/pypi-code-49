#!/usr/bin/env python3
# vim: set tw=100 cc=+1:
"""
This package provides a class :py:class:`ArgParseNode` which makes it easier to create complex
nested subcommands with argparse.
"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .argparse_tree import ArgParseNode

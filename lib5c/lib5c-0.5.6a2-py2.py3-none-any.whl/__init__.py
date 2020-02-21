"""
A library for 5C data analysis.

Subpackage structure:

* :mod:`lib5c.algorithms` - main algorithms for analysis
* :mod:`lib5c.contrib` - integrations with third-party packages
* :mod:`lib5c.parsers` - file parsing
* :mod:`lib5c.plotters` - data visualization
* :mod:`lib5c.tools` - command line interface for ``lib5c``
* :mod:`lib5c.util` - various utility functions
* :mod:`lib5c.writers` - file writing

"""

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version


__version__ = version(__name__)

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

The root ``lib5c`` module defines ``lib5c.__version__``, the recommended source
of version information when lib5c is installed. If lib5c is not installed,
``lib5c.__version__`` will be 'unknown'. In this case, consider using
``lib5c._version.get_version()`` as an alternative source of version information
if ``setuptools_scm`` is available.
"""

try:
    try:
        # this works in Python 3.8
        from importlib.metadata import version, PackageNotFoundError
    except ImportError:
        try:
            # this works in Python 2 if lib5c is installed, since it depends on
            # importlib_metadata
            from importlib_metadata import version, PackageNotFoundError
        except ImportError:
            raise
    try:
        # we land here if either importlib.metadata or importlib_metadata
        # is available and lib5c is installed
        __version__ = version(__name__)
    except PackageNotFoundError:
        # we will land here if either importlib.metadata or importlib_metadata
        # is available, but lib5c isn't actually installed
        __version__ = 'unknown'
except ImportError:
    # we land here if neither importlib.metadata nor importlib_metadata are
    # available
    __version__ = 'unknown'

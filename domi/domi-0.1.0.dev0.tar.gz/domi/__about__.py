"""
Description of project with title, state and further constants
"""
import os
__all__ = [
    "__version__",
    "__title__",
    "__summary__",
    "__keywords__",
    "__uri__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
    "__python_requires__",
    "__dependencies__",
    "__classifiers__",
]
__version__ = '0.1.0.dev0'
__title__ = os.path.basename(os.path.abspath('.'))
__summary__ = "Generic framework (gr. domi) for modeling physics environements"
__keywords__ = "environment, forward modeling, graph, node, "
__uri__ = "https://gitlab.mpcdf.mpg.de/dboe/domi"
__author__ = "Daniel Böckenhoff and Anderea Merlo"
__email__ = "dboe@ipp.mpg.de, amerlo@ipp.mpg.de"
__license__ = "Apache Software License"
__copyright__ = "2020 %s" % __author__
__python_requires__ = '>=3.0'
__dependencies__ = [
    'pathlib;python_version>="3.0"',
    'numpy',
]
__classifiers__ = [
    # find the full list of possible classifiers at https://pypi.org/classifiers/
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: {0}'.format(__license__),
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

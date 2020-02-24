import sys

__version__ = "1.0.2"


def verify_version():
    assert sys.version_info >= (3, 6), 'Python version < 3.6 not supported'


verify_version()

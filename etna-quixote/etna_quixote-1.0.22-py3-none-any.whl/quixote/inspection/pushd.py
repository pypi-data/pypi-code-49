from contextlib import contextmanager
import os


@contextmanager
def pushd(path: str):
    """
    Change the current working directory for the duration of a with-block.

    :param path:        the path to the new directory to use as current working directory
    """
    old_wd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_wd)

"""
A module for filesystem utilities.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
from contextlib import contextmanager
import errno
import os
import sys


def remove_file_silent(filename):
    """Removes a file silently even if it does not exist."""
    try:
        os.remove(filename)
    except OSError as e:
        # Re-raise if not expected error
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise


@contextmanager
def unixoutput(filename, **kwargs):
    """Opens filename for output or writes to stdout in a Unix-like manner.

    Command line tools that follow Unix conventions are expected to write to
    standard output (stdout) when an argument '-' is passed to them, otherwise
    the argument filename is opened as normal for output.
    
    Args:
        filename (str): filename for output.
        **kwargs: variable keyword arguments to pass through.

    Returns:
        IO stream object.
    """
    stdout_default = filename is None or filename == '-'
    if not stdout_default:
        stream = open(filename, **kwargs)
    else:
        stream = sys.stdout

    try:
        yield stream
    finally:
        if not stdout_default:
            stream.close()
        else:
            stream.flush()

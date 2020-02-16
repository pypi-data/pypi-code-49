"""Main module."""
from contextlib import contextmanager
from datetime import date
import datetime


def parents(klass):
    """
   Usage: convenience function to find 'bases'
   example:
    in: parents(TypeError)
    out: [Exception, BaseException, object]

   """

    parent_classes = klass.mro()
    parent_classes.remove(klass)

    return parent_classes


@contextmanager
def simple_timer():
    """
   Usage: time a function execution in seconds
   example:
   with simple_timer():
       some_function()
   """
    print("Starting...\n")
    start = datetime.datetime.now()

    try:
        yield
    finally:
        finish = datetime.datetime.now()
        seconds = (finish - start).total_seconds()
        print("\nFinished, took {} seconds".format(seconds))


def readable_datetime(timestamp):
    """
   Usage: convert unix timestamp to human readable
   example: readable_datetime(1581816398)
    """
    print(date.fromtimestamp(timestamp).strftime("%B %d %Y, %I:%M:%S %p"))

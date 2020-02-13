"""
Function decorator caching on disk the result of a function call.

If the cache file 'fpath' is not found, then the decorated function 
is called and its result is saved with pickle on 'fpath', else
the file is loaded and returned, and the function is not executed

Example:

@cache("myfile.pickle")
def foo(args):
    ...
    return result
    
"""

__version__ = "0.1"
__author__ = "Pietro Spadaccino"



import os
import pickle
import functools


def cache(fpath, enabled=True):
    """
    Decorator caching on file `fpath` the result of a function using pickle.
    When `enabled` is False the caching has no effect and the function
    is executed normally. 
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # If not enabled execute func and return
            if not enabled:
                return func(*args, **kwargs)

            # If file is present load it and return its contents
            if os.path.isfile(fpath):
                print({func.__name__}, " result loaded from disk")
                return pickle.load(open(fpath, "rb"))

            # Cache file not present, so execute the function and dump
            # the result on the file. Return then the result
            result = func(*args, **kwargs)
            pickle.dump(result, open(fpath, "wb"))
            return result

        return wrapper

    return decorator



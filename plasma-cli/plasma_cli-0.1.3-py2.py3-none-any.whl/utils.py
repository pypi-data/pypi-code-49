#!/usr/bin/env python

from functools import wraps

def handle_exceptions(f):
    @wraps(f)
    def wrapped_function(*args, **kwargs):
        function_name = f.__name__
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print('Exception | %s | %s |' % (function_name, str(e)))
    return wrapped_function


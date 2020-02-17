from functools import wraps
from time import sleep

import requests

from .exceptions import WaitForProcess

def retry_on_processing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        c = 0
        r = None
        while c < 5:
            try:
                return f(*args, **kwargs)
            except WaitForProcess:
                c += 1
                sleep(1)
        raise requests.exceptions.RetryError("Too many attempts")
    return wrapper


def throw_for(code, exc):
    def wrapped(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            r = f(*args, **kwargs)
            if r.status_code == code:
                raise exc
            return r
        return wrapper
    return wrapped


def returns_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        return r.json()
    return wrapper

def returns_gen(f):
    @wraps(f)
    def wrapper(*args, gen=False, **kwargs):
        g = f(*args, **kwargs)
        return g if gen else list(g)
    return wrapper

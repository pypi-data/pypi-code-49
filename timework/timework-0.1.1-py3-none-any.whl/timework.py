import time
import functools
from threading import Thread
from collections import deque


class ResultHandler:

    def __init__(self, history=None):
        self.value = deque(maxlen=history)

    def log(self, value, *, out=False, method=print, string=""):
        self.value.append(value)
        if out:
            method(string)

    def clean(self):
        self.value.clear()


def timer(handler: ResultHandler, *, out=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()

            used = end - start
            s = "{}: {:g} seconds used".format(func.__name__, used)
            handler.log(used, out=out, method=out, string=s)

        return wrapper

    return decorator


def limit(timeout):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            rc = [Exception('{}: {:g} seconds exceeded'
                            .format(func.__name__, timeout))]

            def new_func():
                try:
                    rc[0] = func(*args, **kwargs)
                except Exception as err_a:
                    rc[0] = err_a

            t = Thread(target=new_func)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as err_b:
                raise err_b

            rt = rc[0]
            if isinstance(rt, BaseException):
                raise rt
            else:
                return rt

        return wrapper

    return decorator


def iterative(handler: ResultHandler, timeout):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            @limit(timeout)
            def iterative_deepening():
                result = None
                max_d = kwargs.pop('max_depth')
                for depth in range(1, max_d + 1):
                    try:
                        result = func(*args, max_depth=depth, **kwargs)
                    except Exception as err_a:
                        result = err_a
                    finally:
                        handler.log(result, out=False)

                return result

            return iterative_deepening()

        return wrapper

    return decorator

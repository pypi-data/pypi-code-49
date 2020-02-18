import time
import functools
from threading import Thread
from collections import deque


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class TimeError(Error):
    def __init__(self, message, result=None, detail=None):
        self.message = message
        self.result = result
        self.detail = detail


def timer(output=None, *, detail=None, timeout=0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if output and detail:
                t = time.asctime(time.localtime(time.time()))
                output('START:  {}'.format(t))
            start = time.time()
            rc = func(*args, **kwargs)
            end = time.time()

            used = end - start
            s = '{}: {:g} seconds used'.format(func.__name__, used)

            if timeout and used > timeout:
                e = TimeError(s, rc, used)
                raise e
            elif output:
                if detail:
                    t = time.asctime(time.localtime(time.time()))
                    output('FINISH: {}\n{}'.format(t, s))
                else:
                    output(s)
            return rc

        return wrapper

    return decorator


def limit(timeout):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            rc = TimeError('{}: {:g} seconds exceeded'
                           .format(func.__name__, timeout))

            def new_func():
                nonlocal rc
                try:
                    rc = func(*args, **kwargs)
                except Exception as err_:
                    rc = err_

            t = Thread(target=new_func)
            t.daemon = True
            t.start()
            t.join(timeout)

            if isinstance(rc, Exception):
                raise rc
            else:
                return rc

        return wrapper

    return decorator


def iterative(timeout, key='max_depth', history=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            @limit(timeout)
            def iterative_deepening():
                result = None
                max_d = kwargs.pop(key)
                for depth in range(1, max_d + 1):
                    try:
                        kwargs[key] = depth
                        result = func(*args, **kwargs)
                    except Exception as err_a:
                        result = err_a
                    finally:
                        handler.append(result)
                return result

            handler = deque(maxlen=history)
            try:
                rc = iterative_deepening()
            except TimeError as e:
                e.message = func.__name__ + '/' + e.message
                e.result = handler[-1]
                e.detail = handler
                raise e
            else:
                return rc

        return wrapper

    return decorator

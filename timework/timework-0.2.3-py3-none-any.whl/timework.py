import time
import functools
from threading import Thread
from collections import deque


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class TimeError(Error):
    """Class for timeout."""

    def __init__(self, message, result=None, detail=None):
        """
        :param message: error message
        :param result: result of the inner function
        :param detail: more information (if have)
        """
        self.message = message
        self.result = result
        self.detail = detail


def timer(output=None, *, detail=False, timeout=0):
    """
    Decorator. Measure the running time.

    :param output: a function object, e.g. print, None to be silent
    :param detail: boolean, True to print start and stop time
    :param timeout: if run time > timeout, then raise error
                     (after inner function finished)
                     0 is never, -1 is always

    :return: result of the inner function

    :exception TimeError object contains timeout message and
                                          the result of the inner function.
    """

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
    """
    Decorator. Limit the running time.

    :param timeout: run time limit (seconds)
    :return: result of the inner function (if finished in time)

    :exception TimeError object contains timeout message.
    """

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
    """
    Decorator. Used to do iterative deepening.
    Notice: please use keyword arguments (at least 'max_depth')
            when calling the inner function.

    :param timeout: run time limit (seconds)
    :param key: variable name of the maximum depth
    :param history: maximum queue length
    :return: result of the inner function (goal node is found)

    :exception: TimeError object contains timeout message,
                                           current result and previous results.
    """

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

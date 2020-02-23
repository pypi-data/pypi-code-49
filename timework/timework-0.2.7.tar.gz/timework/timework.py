import time
import functools
from threading import Thread
from collections import deque


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class TimeError(Error):
    """Class for timeouts."""

    def __init__(self, message, result=None, detail=None):
        """Timeout information.

        Args:
            message: timeout error message
            result: return values of the function that is being decorated
            detail: more information (if have)
        """
        self.message = message
        self.result = result
        self.detail = detail


def timer(output=None, *, detail: bool = False, timeout: float = 0):
    """A Decorator. Measuring the running time.

    The wrapper function measures the running time of the function that is being decorated.
    The output argument is used to log messages, basically the wrapper function will pass
    the start time, end time, and run time message to it as strings. Whether to pass start
    time and end time messages is controlled by detail argument. And timeout argument is
    used to control error messages. The last two arguments must been passed using keywords.

    Typical usage examples:

        @timer(logging.warning)
        def your_function_a():
            ...

        @timer(timeout=5)
        def your_function_b():
            ...


    Args:
        output: A function object that specifies where to log messages.
                For example: print.
        detail: A boolean value, whether to print start and end time.
        timeout: Another optional variable controlling errors,
                 if run_time_after_finished > timeout, then raise TimeError.
                 (0: never, -1: always)

    Returns:
        Exactly the return values of the inner function that is being decorated.
        In this case, the process finishes within [timeout] seconds.

    Raises:
        TimeError: This error does not occur until the inner function
                   terminates, but fails to finish within [timeout] seconds.

                   A TimeError object contains:
                       TimeError.message: timeout message
                       TimeError.result: return values
                       TimeError.detail: used run time
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if output is not None and detail:
                t = time.asctime(time.localtime(time.time()))
                output('START:  {}'.format(t))

            start = time.time()
            rc = func(*args, **kwargs)
            end = time.time()

            used = end - start
            s = '{}: {:g} seconds used'.format(func.__name__, used)

            if timeout != 0 and used > timeout:
                e = TimeError(s, rc, used)
                raise e
            elif output is not None:
                if detail:
                    t = time.asctime(time.localtime(time.time()))
                    output('FINISH: {}\n{}'.format(t, s))
                else:
                    output(s)

            return rc

        return wrapper

    return decorator


def limit(timeout: float):
    """A Decorator. Limiting the running time.

    The wrapper function limits the running time of the function being
    decorated. The timeout argument is used to set timeout (in seconds).
    After that time of processing, raise a TimeError to terminate.

    Typical usage examples:

        @limit(3)
        def your_function():
            ...


    Args:
        timeout: This argument sets the timeout limit of the decorated function.
                 Once the run time of the process reaches [timeout] seconds but
                 not yet finishes, then raise TimeError and stop the inner function.

    Returns:
        Exactly the return values of the inner function that is being decorated.
        In this case, the process finishes within [timeout] seconds.

    Raises:
        TimeError: This error occurs when the inner function runs
                   for [timeout] seconds and still not finishes.

                   A TimeError object contains:
                       TimeError.message: timeout message
                       TimeError.result: None (unused)
                       TimeError.detail: None (unused)
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


def iterative(timeout: float, key: str = 'max_depth', history: int = 1):
    """A Decorator. Used to process iterative deepening.

    The wrapper function is actually doing iterative deepening which is commonly used
    in search algorithms. The wrapper function runs the inner function progressively,
    and stores the return values of each step. Still, the timeout argument is used to
    set timeout (in seconds). The key argument should (and must) set to the name of
    the variable that controls the maximum depth of each search. Since search histories
    are stored in a collections.deque object, the history argument will be directly
    passed to the maxlen argument of the deque.

    Notice:
        Please use keyword arguments when calling the function that is being decorated.

        The max_depth argument of the decorated function should set as maximum depth and
        this wrapper function will try to run the inner function from max_depth=1 until
        max_depth=[your_value] or reaches [timeout] second (can still provide results).

    Typical usage examples:

        @iterative(10)
        def your_function_a(max_depth):
            ...

        @iterative(10, key='depth', history=5)
        def your_function_b(depth):
            ...


    Args:
        timeout: This argument sets the timeout limit of the iterative deepening.
                 Once the run time of the process reaches [timeout] seconds but
                 not yet finishes, then raise TimeError and stop the iteration.
        key: The name of the maximum depth variable of the decorated function.
        history: Maximum queue length, i.e. number of previous results available.
                 (1: only the final result)

    Returns:
        Exactly the return values of the inner function that is being decorated.
        In this case, goal node is found.

    Raises:
        TimeError: This error occurs after [timeout] seconds of running iterative
                   deepening, and not finishes the [max_depth]th level of search.
                   The maximum depth is not set when adding this decorator, but
                   when you make a call to the function that is being decorated.

                   A TimeError object contains:
                       TimeError.message: timeout message
                       TimeError.result: return values of the current level
                       TimeError.detail: collections.deque object containing
                                         return values of the previous levels
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
                e.message = '{}.{}'.format(func.__name__, e.message)
                e.result = handler[-1]
                e.detail = handler
                raise e
            else:
                return rc

        return wrapper

    return decorator

# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""stackdriver logging related helper functions
"""
from functools import wraps
import inspect
import logging
from logging import LoggerAdapter
from timeit import default_timer


class AnnotatedLogger:
    """Contextmanager to temporary annotate the current global logger with extra kwargs.

    Finds a logger by name in the call stack, and replaces it with a LoggerAdapter. On exit the
    logger in the call stack will be reset again to it's original state.

    Args:
        name (str): the (variable) name of the global logger to annotate
        kwargs (dict): the extra k:v pairs to attach to the logger
    """
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.back = 0
        self.logger_orig = None

    def __enter__(self):
        """On entering the context.

        Raises:
            NameError: when the logger is not found.

        Returns:
            LoggerAdapter: the annotated logger
        """
        frame = inspect.currentframe()
        while self.name not in frame.f_globals:
            frame = frame.f_back
            self.back += 1
            if frame is None:
                raise NameError("Could not find logger named '{}'.".format(self.name))
        self.logger_orig = frame.f_globals[self.name]
        adapted_logger = LoggerAdapter(self.logger_orig, self.kwargs)
        # LoggerManager is a bit of a crippled thing, it only partially mimics a regular logger.
        # monkey-patch it so it provides a bit more consistency with logger
        adapted_logger.manager = adapted_logger.logger.manager
        adapted_logger.setLevel = adapted_logger.logger.setLevel
        frame.f_globals[self.name] = adapted_logger
        del frame
        return adapted_logger

    def __exit__(self, *_):
        frame = inspect.currentframe()
        while self.back > 0:
            frame = frame.f_back
            self.back -= 1
        frame.f_globals[self.name] = self.logger_orig
        del frame


def autolog(logger_name='logger', level=logging.DEBUG, log_before=True, log_after=True):
    """Decorate a function for logging candy.

    Decorator to automatically replace the global logger with an AnnotatedLogger, with all the
    the args and kwargs that the decorated function was called with. Options to automatically log
    a starting and a finished message, including the time the decorated function took to execute.

    NB. this is not thread-safe! It temporary changes the global scope of the decorated function; if
    from another thread a function (or class) from the same global scope is called, it will see the
    same modification. If we are going to use this in a threaded environment, we should use
    something like https://github.com/erikrose/stackful.

    Args:
        logger_name (str): the (variable) name of the global logger to use
        level (int): the log level to use for the log_before and log_after messages
        log_before (bool): if True, log a message just before starting the decorated function
        log_after (bool): if True, log a message right after the decorated function finished, using
            a logger annotated with a 'duration' attribute.

    Returns:
        function: the decorator.
    """
    def decorator(function):
        """The decorator

        Args:
            function (function): the function to decorate

        Returns:
            function: the function wrapper.
        """

        @wraps(function)
        def wrapper(*args, **kwargs):
            """The function wrapper.

            Args:
                args (list): decorated function args
                kwargs (dict): decorated function kwargs

            Returns:
                result: the result of the decorated function call
            """
            func_fullname = ".".join([function.__module__, function.__qualname__])
            func_sig = inspect.signature(function)
            bound_args = func_sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            logger_extra = dict(bound_args.arguments)
            # must rename 'args' because logRecord already has an 'args' attribute
            if 'args' in logger_extra:
                logger_extra['function_args'] = logger_extra.pop('args')
            func_kwargs = logger_extra.pop('kwargs', {})
            for key, value in func_kwargs.items():
                logger_extra[key] = value

            with AnnotatedLogger(logger_name, **logger_extra) as logger:

                if log_before:
                    logger.log(level, "Starting %s", func_fullname)

                start = default_timer()

                result = function(*args, **kwargs)

                end = default_timer()

                if log_after:
                    duration = end - start
                    with AnnotatedLogger(logger_name, duration=duration) as logger:
                        logger.log(level, "Finished %s in %s", func_fullname, duration)

            return result

        return wrapper

    return decorator

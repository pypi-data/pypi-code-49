# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""stackdriver logging related helper functions
"""
from datetime import timedelta
from functools import wraps
import inspect
import logging
from logging import LoggerAdapter
import os
from timeit import default_timer

from .logging_handlers import MAGIC_PREFIX


class AnnotatedLogger:
    """Contextmanager to temporary annotate the current global logger with extra kwargs.

    Finds a logger by name in the call stack, and replaces it with a LoggerAdapter. On exit the
    logger in the call stack will be reset again to it's original state. This enables the magic that
    only the 'logger = logging.getLogger(__name__)' at the top of the file is necessary, and an
    adapted logger can be used in other parts of the code without having to add code to either get
    a new logger or to define logger as global.

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
        adapted_logger._log = adapted_logger.logger._log
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
    the args and kwargs that the decorated function was called with as annotation to the logger.
    When used with the StackdriverLoggingHandler, these annotations will automatically end up as
    extra key:value pairs in the 'labels' section.
    Use the log_before and log_after options to automatically log a starting and a finished message,
    including the time the decorated function took to execute.


    NB. this is not thread-safe! It temporary changes the global scope of the decorated function; if
    from another thread a function (or class) from the same global scope is called, it will see the
    same modification. If we are going to use this in a threaded environment, we should use
    something a bit more extensive like https://github.com/erikrose/stackful.

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
            func_file = inspect.getsourcefile(function)
            func_sig = inspect.signature(function)
            bound_args = func_sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            logger_extra = {'arg_{}'.format(k):v for k,v in bound_args.arguments.items()}
            func_kwargs = logger_extra.pop('arg_kwargs', {})
            for key, value in func_kwargs.items():
                logger_extra['arg_{}'.format(key)] = value

            # override some of the logrecord attributes, prepend magic prefix to avoid name clashes
            overrides = dict(
                funcName=func_fullname,
                filename=os.path.basename(func_file),
                module=inspect.getmodule(function).__name__,
                name=function.__name__,
                pathname=func_file,
                lineno=inspect.getsourcelines(function)[-1]
            )
            overrides = {'{}{}'.format(MAGIC_PREFIX, k):v for k,v in overrides.items()}
            logger_extra.update(overrides)

            with AnnotatedLogger(logger_name, **logger_extra) as logger:

                if log_before:
                    logger.log(level, "Starting %s", func_fullname)

                start = default_timer()

                result = function(*args, **kwargs)

                end = default_timer()

                if log_after:
                    duration_seconds = end - start
                    duration_timedelta = timedelta(seconds=duration_seconds)
                    with AnnotatedLogger(
                            logger_name,
                            duration_seconds=duration_seconds,
                            duration=duration_timedelta
                    ) as logger:
                        logger.log(level, "Finished %s in %s", func_fullname, duration_timedelta)

            return result

        return wrapper

    return decorator

"""Provide methods to trace execution."""
import logging
import functools
from typing import Callable, Tuple, Any
import datetime
from dataclasses import dataclass, field


@dataclass
class Invocation:
    """Record an invocation of a function."""

    invocation: Tuple[Callable, Tuple, dict]
    start_time: datetime.datetime

    @classmethod
    def create_from(cls, function: Callable, args: Tuple, kwargs: dict):
        """Record the time when a `function` is called.

        Returns
        -------
        trace: Trace

        """
        return Invocation((function, args, kwargs), datetime.datetime.now())

    def build_start_message(self) -> str:
        """Create a message that represents this invocation."""
        function = self.invocation[0]
        args = self.invocation[1]
        kwargs = self.invocation[2]
        return '%s(%s, %s)' % (function.__name__, args, kwargs)

    def build_end_message(self, return_value: Any) -> str:
        """Create a message that this invocation has ended."""
        start_message = self.build_start_message()
        end_message = '%s -> %s' % (start_message, return_value)
        elapsed_time = self._count_elapsed_time()
        return '[elapsed time: %s milliseconds] %s' \
            % (elapsed_time, end_message)

    def _count_elapsed_time(self) -> float:
        end_time = datetime.datetime.now()
        delta = end_time - self.start_time
        return round(delta.total_seconds() * 1000, 3)


@dataclass
class TraceLevel:
    """Represent logging levels for tracing executions."""

    start_level: int = field(default=logging.DEBUG)
    end_level: int = field(default=logging.DEBUG)

    def start(self, logger: logging.Logger, invocation: Invocation) -> None:
        """Record `trace` with `logger`."""
        message = invocation.build_start_message()
        logger.log(self.start_level, message)

    def end(self,
            logger: logging.Logger,
            invocation: Invocation,
            return_value: Any) -> None:
        """Record that the function has end."""
        message = invocation.build_end_message(return_value)
        logger.log(self.end_level, message)


class Tracer:
    """Record information about a program's execution."""

    def __init__(self,
                 logger: logging.Logger,
                 trace_level: TraceLevel):
        """Take a logger and a logging level."""
        self.logger = logger
        self.trace_level = trace_level

    def trace(self, function: Callable):
        """Provide a function decorator to trace the decorated function."""
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            invocation = Invocation.create_from(function, args, kwargs)
            self.trace_level.start(self.logger, invocation)
            result = function(*args, **kwargs)
            self.trace_level.end(self.logger, invocation, result)
            return result
        return wrapper

    @classmethod
    def create_tracer(
            cls,
            logger_name: str = 'trace',
            format_string: str
            = '%(levelname)s:%(asctime)s:%(name)s:%(message)s',
            level: int = logging.DEBUG,
            trace_level: TraceLevel
            = TraceLevel(logging.DEBUG, logging.DEBUG)):
        """Create a tracer named with `logger_name`.

        Returns
        -------
        tracer: Tracer

        """
        handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(format_string))
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return Tracer(logger, trace_level)

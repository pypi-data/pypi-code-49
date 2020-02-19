# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""logging related helper functions
"""
from logging import LoggerAdapter


def annotate_logger(logger='logger', **kwargs):
    """Annotate a logger with extra info

    Uses a LoggerAdapter to attach any keyword arguments as extra to the logger. Due to how python
    logging works, these will then end up as additional attributes of the __dict__ of the
    logrecord instance. When used together with the StackDriverLoggingHandler, these will then
    automatically be added to the ```labels``` key in the stackdriver record.

    Args:
        logger (object): a logger instance or a string, in which case it will be derived from
                globals()[logger]
        kwargs: anything passed here will be passed as dict to the LoggerAdapter and work as if
                you passed it as ```extra={...}``` to every logging call.

    Returns:
        LoggerAdapter: the annotated logger.
    """
    if isinstance(logger, str):
        # find named logger in higher frames
        frame = inspect.currentframe()
        while logger not in frame.f_globals:
            frame = frame.f_back
            if frame is None:
                raise RuntimeError("Could not find logger named '%s'.", logger)

        logger = frame.f_globals[logger]

    return LoggerAdapter(logger, kwargs)

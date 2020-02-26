"""Logging configuration."""

import logging
from typing import Optional, Union

import structlog
from structlog._config import BoundLoggerLazyProxy

StructLogger = BoundLoggerLazyProxy


def set_log_level(level: Union[str, int]) -> None:
    """Set the log level on the root logger.

    Since the root logger log level is inherited by all the loggers by default,
    this is like setting a default log level.

    Args:
        level: The log level, as documented in the Python standard library.
    """

    root_logger = logging.getLogger()
    root_logger.setLevel(level)


def get_logger(name: str, level: Optional[int] = None) -> BoundLoggerLazyProxy:
    """Wrap the python logger with the default configuration of structlog.

    Args:
        name: Identification name. For module name pass ``name=__name__``.
        level: Threshold for this logger.

    Returns:
        The wrapped python logger with the default configuration of structlog.
    """

    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    formatter: structlog.stdlib.ProcessorFormatter = structlog.stdlib.ProcessorFormatter(
        processor=structlog.processors.JSONRenderer(indent=2, sort_keys=True)
    )

    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger: logging.Logger = logging.getLogger(name)
    logger.addHandler(handler)
    if level is not None:
        logger.setLevel(level)

    return structlog.wrap_logger(logger)

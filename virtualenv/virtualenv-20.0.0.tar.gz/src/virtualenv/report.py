from __future__ import absolute_import, unicode_literals

import logging
import sys

import six

LEVELS = {
    0: logging.CRITICAL,
    1: logging.ERROR,
    2: logging.WARNING,
    3: logging.INFO,
    4: logging.DEBUG,
    5: logging.NOTSET,
}

MAX_LEVEL = max(LEVELS.keys())
LOGGER = logging.getLogger()


def setup_report(verbose, quiet):
    verbosity = max(verbose - quiet, 0)
    _clean_handlers(LOGGER)
    if verbosity > MAX_LEVEL:
        verbosity = MAX_LEVEL  # pragma: no cover
    level = LEVELS[verbosity]
    msg_format = "%(message)s"
    filelock_logger = logging.getLogger("filelock")
    if level <= logging.DEBUG:
        locate = "module"
        msg_format = "%(relativeCreated)d {} [%(levelname)s %({})s:%(lineno)d]".format(msg_format, locate)
        filelock_logger.setLevel(level)
    else:
        filelock_logger.setLevel(logging.WARN)

    formatter = logging.Formatter(six.ensure_str(msg_format))
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(level)
    LOGGER.setLevel(logging.NOTSET)
    stream_handler.setFormatter(formatter)
    LOGGER.addHandler(stream_handler)
    level_name = logging.getLevelName(level)
    logging.debug("setup logging to %s", level_name)
    return verbosity


def _clean_handlers(log):
    for log_handler in list(log.handlers):  # remove handlers of libraries
        log.removeHandler(log_handler)

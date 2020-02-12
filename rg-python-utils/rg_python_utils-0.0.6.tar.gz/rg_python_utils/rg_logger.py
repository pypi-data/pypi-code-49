import logging
import os

from django.conf import settings

logger = logging.getLogger('debug')


def info(msg):
    if settings.DEBUG_FLAG:
        logger.info(msg)


def exception(e, log_message: str = "", can_print_stacktrace: bool = False):
    logger.error(log_message + "%s, ExceptionMessage:%s", log_message, get_exception_msg(e), exc_info=can_print_stacktrace)

    # if can_print_stacktrace:
    #     logger.exception(e)


def get_exception_msg(e) -> str:
    return getattr(e, 'message', repr(e))

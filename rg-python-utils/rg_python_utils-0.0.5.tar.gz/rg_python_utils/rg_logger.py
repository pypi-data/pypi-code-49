import logging
import os

isDebugOn = os.getenv('DEBUG_FLAG', True)

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

if isDebugOn:
    logger = logging.getLogger('debug')
else:
    logger = logging.getLogger('production')


def info(msg):
    if isDebugOn:
        logger.info(msg)


def exception(e, log_message: str = "", can_print_stacktrace: bool = False):
    logger.error(log_message + "%s, ExceptionMessage:%s", log_message, get_exception_msg(e), exc_info=can_print_stacktrace)

    # if can_print_stacktrace:
    #     logger.exception(e)


def get_exception_msg(e) -> str:
    return getattr(e, 'message', repr(e))

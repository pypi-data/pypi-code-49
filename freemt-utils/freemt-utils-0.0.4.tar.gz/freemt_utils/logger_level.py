'''
set logger level of loguru DEBUG INFO
'''
# pylint: disable=broad-except

import sys
from loguru import logger


def logger_level(level: str = 'DEBUG') -> None:
    ''' set logger level'''

    try:
        logger.remove()  # noqa
        logger.add(sys.stderr, level=level.upper())  # noqa
    except Exception:
        print(sys.exc_info()[:2])

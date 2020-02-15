'''
set logger level of loguru DEBUG INFO
'''
# pylint: disable=undefined-variable, broad-except

import sys


def logger_level(level: str = 'DEBUG') -> None:
    ''' set logger level'''
    if 'logger' not in globals():
        print('logger not set.. do: from loguru import logger')
        return

    try:
        logger.remove()  # noqa
        logger.add(sys.stderr, level=level.upper())  # noqa
    except Exception:
        print(sys.exc_info()[:2])

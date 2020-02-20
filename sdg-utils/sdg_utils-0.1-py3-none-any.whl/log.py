import logging
from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG
from time import time

LOG_FRMT = logging.Formatter('%(relativeCreated)04d %(name)-5s %(levelname)s %(message)s')
__flhndlr = None


def log_level_names(levels={CRITICAL: 'C', ERROR: 'E', WARNING: 'W', INFO: '|', DEBUG: ' '}):
    for l, n in levels.items():
        logging.addLevelName(l, n)


def log_open(name=None, level=INFO, frtm=LOG_FRMT):
    logger = logging.getLogger(name)
    logger.setLevel(DEBUG)
    log_level_names()
    hndlr = logging.StreamHandler()
    hndlr.setLevel(level)
    hndlr.setFormatter(frtm)
    logger.addHandler(hndlr)
    return logger


def log_file_open(filename, level=DEBUG, frtm=LOG_FRMT, reset_time=True):
    global __flhndlr
    logger = logging.getLogger()
    logger.setLevel(DEBUG)
    __flhndlr = logging.FileHandler(filename, mode='w')
    __flhndlr.setLevel(level)
    __flhndlr.setFormatter(frtm)
    logger.addHandler(__flhndlr)
    if reset_time:
        logging._startTime = time()
    return logger


def log_file_close():
    global __flhndlr
    if __flhndlr:
        logger = logging.getLogger()
        logger.removeHandler(__flhndlr)
        __flhndlr.close()


def log_starttime():
    try:
        return logging._startTime
    except AttributeError:
        return time()

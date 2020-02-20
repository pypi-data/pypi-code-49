import logging
import os

# https://docs.python.org/3/library/logging.html#logrecord-attributes

logging_levels = { "DEBUG" : logging.DEBUG
                 , "INFO" : logging.INFO
                 , "WARN" : logging.WARN
                 , "ERROR" : logging.ERROR
                 , "CRITICAL" : logging.CRITICAL }

PYLOG = logging.INFO
if os.getenv("PYLOG") is not None:
    PYLOG = logging_levels[os.getenv("PYLOG")]

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(funcName)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(PYLOG)

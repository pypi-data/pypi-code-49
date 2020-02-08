import logging

LEVEL = logging.DEBUG
CORE_LOGGER = logging.getLogger('sptp')
FORMAT = '%(name)-30s:%(levelname)-5s: %(message)s'

def _logger(name):
    return CORE_LOGGER.getChild(name)

def setup_logging():
    CORE_LOGGER.setLevel(LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(FORMAT))
    
    CORE_LOGGER.addHandler(stream_handler)
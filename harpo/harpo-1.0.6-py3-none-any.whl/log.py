import logging

import colorlog


def configure_logging(level=logging.INFO):
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(levelname)s%(reset)s | %(message)s"))
    logger = colorlog.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(level)


def get_logger():
    logger = colorlog.getLogger(__name__)
    return logger

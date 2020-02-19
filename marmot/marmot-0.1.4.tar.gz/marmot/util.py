import logging
from logging import Formatter, FileHandler, StreamHandler


def get_logger(name=None, level=logging.INFO, filename=None):

    if name:
        logger = logging.getLogger("root").getChild(name)
    else:
        logger = logging.getLogger("root")

    logger.setLevel(level)
    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if not len(logger.handlers):
        handler = StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if filename:
            fh = FileHandler(filename=filename)
            fh.setLevel(level)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

    return logger

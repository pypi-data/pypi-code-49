import logging

logging.basicConfig(format='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')


def log(name=None, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

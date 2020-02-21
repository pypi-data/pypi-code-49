import logging


def setup_custom_logger(name):
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger

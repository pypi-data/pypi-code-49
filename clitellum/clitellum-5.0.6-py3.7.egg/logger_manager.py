import logging


def get_logger() -> logging.Logger:
    """
    Devuelve el logger de clitellum
    :return: Logger
    :rtype: logging.Logger
    """
    return logging.getLogger("clitellum")

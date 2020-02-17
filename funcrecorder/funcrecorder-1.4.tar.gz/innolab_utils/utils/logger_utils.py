import logging

import colorlog


def init_logger(name, level=logging.INFO, log_path='report.log', console_enable=True):
    '''
    base on https://docs.python.org/3/howto/logging-cookbook.html
    :param name: logger name
    :param level: logging level
    :param log_path: log file handler default path
    :return:
    '''
    # create logger with 'spam_application'
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(log_path)
    fh.setLevel(level)

    # set file formatter
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    if console_enable:
        # create console handler with a higher log level
        ch = colorlog.StreamHandler()
        ch.setLevel(level)

        # set console formatter
        formatter = colorlog.ColoredFormatter('%(log_color)s[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
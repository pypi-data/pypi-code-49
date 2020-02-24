import datetime
import logging

import pytz


class Logger(object):

    def __init__(self, module=None):
        self.module = module
        self.logger = self
        self.last_msg = None

    def _get_msg(self, *args):
        """
        Build a message string
        :param args: Things to be put together
        :return: Build message
        """
        msg = ' '.join(args)

        if self.module is not None:
            msg = '[{}] {}'.format(self.module.meta['name'], msg)

        return msg

    def _get_logger(self):
        """
        Get the current logger
        :return: Logger
        """
        logger = logging.getLogger('bot')
        if self.module is not None:
            logger = logger.getChild(self.module.meta['name'])

        return logger

    def log(self, *args, level: logging = logging.INFO, **kwargs):
        """
        Log a message
        :param args: Things to be send
        :param level: Log level
        :param kwargs: Other arguments
        :return:
        """
        time_str = datetime.datetime.now(tz=pytz.timezone('UTC')).strftime("%H:%M:%S")
        msg = self._get_msg(*args)
        self.last_msg = msg
        out = '[{}] <{}> {}'.format(time_str, logging.getLevelName(level).upper(), msg)

        if level is None:
            level = logging.INFO

        self._get_logger().log(level, msg, **kwargs)

        print(out)

    def info(self, *args):
        """
        Log at INFO level
        :param args: Things to be send
        """
        self.log(*args, level=logging.INFO)

    def debug(self, *args, **kwargs):
        """
        Log at DEBUG level
        :param args: Things to be send
        :param kwargs: Other arguments
        """
        self.log(*args, level=logging.DEBUG, **kwargs)

    def warn(self, *args):
        """
        Log at WARN level
        :param args: Things to be send
        """
        self.log(*args, level=logging.WARN)

    def error(self, *args):
        """
        Log at ERROR level
        :param args: Things to be send
        """
        self.log(*args, level=logging.ERROR)

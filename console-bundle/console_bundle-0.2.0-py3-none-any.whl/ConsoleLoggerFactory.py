import logging
import colorlog

class ConsoleLoggerFactory:

    def create(self):
        logger = logging.getLogger('console')
        logger.setLevel(logging.DEBUG)

        formatStr = '%(message)s'
        dateFormat = '%H:%M:%S'
        cformat = '%(log_color)s' + formatStr
        formatter = colorlog.ColoredFormatter(cformat, dateFormat)

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        logger.handlers = [streamHandler]

        return logger

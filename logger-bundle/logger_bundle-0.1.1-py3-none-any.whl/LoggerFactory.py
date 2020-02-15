from logging import Handler, getLogger
from typing import List

class LoggerFactory:

    def __init__(
        self,
        defaultLogLevel: int,
        handlers: List[Handler],
    ):
        self.__defaultLogLevel = defaultLogLevel
        self.__handlers = handlers

    def create(self, loggerName: str, logLevel: int = None):
        logger = getLogger(loggerName)
        logger.setLevel(logLevel if logLevel is not None else self.__defaultLogLevel)

        logger.handlers = self.__handlers
        logger.propagate = False

        return logger

from logging import Handler, getLogger
from typing import List

class LoggerFactory:

    def __init__(
        self,
        handlers: List[Handler]
    ):
        self.__handlers = handlers

    def create(self, loggerName: str, logLevel: int):
        logger = getLogger(loggerName)
        logger.setLevel(logLevel)

        logger.handlers = self.__handlers
        logger.propagate = False

        return logger

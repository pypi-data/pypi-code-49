from logging import getLogger
from typing import List
from loggerbundle.handler.HandlerFactoryInterface import HandlerFactoryInterface

class LoggerFactory:

    def __init__(
        self,
        defaultLogLevel: int,
        handlerFactories: List[HandlerFactoryInterface],
    ):
        self.__defaultLogLevel = defaultLogLevel
        self.__handlerFactories = handlerFactories

    def create(self, loggerName: str, logLevel: int = None):
        logger = getLogger(loggerName)
        logger.setLevel(logLevel if logLevel is not None else self.__defaultLogLevel)

        logger.handlers = list(map(lambda handlerFactory: handlerFactory.create(), self.__handlerFactories))
        logger.propagate = False

        return logger

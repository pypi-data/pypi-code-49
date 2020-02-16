from logging import StreamHandler
from loggerbundle.extra.ExtraFieldsFormatter import ExtraFieldsFormatter
from loggerbundle.handler.HandlerFactoryInterface import HandlerFactoryInterface

class StreamHandlerFactory(HandlerFactoryInterface):

    def __init__(
        self,
        formatStr: str,
        dateFormat: str,
    ):
        self.__formatStr = formatStr
        self.__dateFormat = dateFormat

    def create(self):
        cformat = '%(log_color)s' + self.__formatStr
        formatter = ExtraFieldsFormatter(cformat, self.__dateFormat)

        streamHandler = StreamHandler()
        streamHandler.setFormatter(formatter)

        return streamHandler

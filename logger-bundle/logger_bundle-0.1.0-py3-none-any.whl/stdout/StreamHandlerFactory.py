from logging import StreamHandler
from loggerbundle.extra.ExtraFieldsFormatter import ExtraFieldsFormatter
from loggerbundle.handler.LogHandlerInterface import LogHandlerInterface

class StreamHandlerFactory(LogHandlerInterface):

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

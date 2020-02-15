from loggerbundle.azure.AzureLogWithExtraHandler import AzureLogWithExtraHandler
from loggerbundle.handler.LogHandlerInterface import LogHandlerInterface

class AzureLogHandlerFactory(LogHandlerInterface):

    def __init__(
        self,
        instrumentationKey: str,
    ):
        self.__instrumentationKey = instrumentationKey

    def __createAzureLogHandler(self):
        return AzureLogWithExtraHandler(
            connection_string='InstrumentationKey={}'.format(self.__instrumentationKey)
        )

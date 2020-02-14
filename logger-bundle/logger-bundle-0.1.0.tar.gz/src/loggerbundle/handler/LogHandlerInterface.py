from abc import ABC
from logging import Handler

class LogHandlerInterface(ABC):

    def create(self) -> Handler:
        pass

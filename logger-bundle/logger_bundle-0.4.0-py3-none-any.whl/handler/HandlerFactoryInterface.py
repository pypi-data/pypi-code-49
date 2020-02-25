from abc import ABC, abstractmethod
from logging import Handler

class HandlerFactoryInterface(ABC):

    @abstractmethod
    def create(self) -> Handler:
        pass

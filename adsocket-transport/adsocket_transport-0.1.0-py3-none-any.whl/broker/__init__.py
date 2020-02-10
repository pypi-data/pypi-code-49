from abc import ABC, abstractmethod


class BaseBroker(ABC):

    @abstractmethod
    def publish(self, message):
        pass

    @abstractmethod
    def store_credentials(self, key, value, ttl):
        pass

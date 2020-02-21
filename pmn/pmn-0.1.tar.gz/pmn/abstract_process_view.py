from abc import ABC, abstractmethod
from curses import window


class AbstractProcessView(ABC):
    def __init__(self, screen):
        self.screen: window = screen

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def loop(self):
        pass

    @abstractmethod
    def resize(self, h):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def last(self):
        pass

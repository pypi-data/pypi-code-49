"""Implement a wrapper for primitive and strings."""
from dataclasses import dataclass
from typing import Callable
from .typevar import T, S
import abc


@dataclass
class Primitive(metaclass=abc.ABCMeta):
    """Wrapper for primitive and strings."""

    @abc.abstractproperty
    def primitive(self) -> T:
        """Return the raw value."""

    def handle(self, handler: Callable[[T], S]) -> S:
        """Apply a function to :py:meth:`primitive`."""
        return handler(self.primitive)

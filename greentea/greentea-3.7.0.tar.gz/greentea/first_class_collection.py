"""Provide classes that represent first class collections."""
import abc
import contextlib
from typing import Callable, Sequence, Generator, Container
from .typevar import T, S


class FirstClassFileContextManagerProvider(metaclass=abc.ABCMeta):
    """Provide a context manager for the content of :py:attr:`filename`.

    Attributes
    ----------
    filename: str
        The path to a file which :py:meth:`transform` transforms
        each line to an item emitted by :py:meth:`__call__`.

    """

    def __init__(self, filename: str):
        """Take the path to a file to read.

        Parameters
        ----------
        filename: str

        """
        self.filename = filename

    @contextlib.contextmanager
    def __call__(self) -> Generator[T, None, None]:
        """Emit an item transformed t from a line of :py:attr:`filename`."""
        with open(self.filename) as stream:
            yield (self.transform(item.strip()) for item in stream)

    @abc.abstractmethod
    def transform(self, item: str) -> T:
        """Transform each line of :py:attr:`filename`.

        Transform each line of :py:attr:`filename` to an item
        emitted by :py:meth:`__call__`.

        Parameters
        ----------
        item: str
            A line of :py:attr:`filename`.

        """


class FirstClassSequence(metaclass=abc.ABCMeta):
    """An abstract class representing a sequence."""

    @abc.abstractproperty
    def sequence(self) -> Sequence[T]:
        """Return the items."""

    def __getitem__(self, s):
        """Access the specified items."""
        found = self.sequence.__getitem__(s)
        if isinstance(found, type(self.sequence)):
            return self.__class__(found)
        return found

    def __len__(self):
        """Return the size of :py:meth:`sequence`."""
        return len(self.sequence)

    def filter_by_container(self, container: Container[T]) \
            -> Generator[T, None, None]:
        """Return generator that emits items that container contains."""
        return (item for item in self.sequence if item in container)

    def is_empty(self) -> bool:
        """Return `True` if :py:meth:`sequence` is empty."""
        return len(self.sequence) == 0

    def apply_function(self, function: Callable[[T], S]) \
            -> Generator[S, None, None]:
        """Apply `function` to the items, returning the result."""
        return (function(item) for item in self)

    def append(self, other, sequence_type=list):
        """Return a new sequence."""
        return self.__class__(self.sequence + other.sequence)


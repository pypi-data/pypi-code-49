from abc import ABC
from dataclasses import dataclass
from typing import *


from .containers import *
from .monads import *
from .predef import *

class EmptyOption(ValueError):
    pass

T = TypeVar('T')
R = TypeVar('R')
K = TypeVar('K', bound='Monad')
@dataclass(frozen=True, init=False, repr=False)
class _Option(Container['Option[T]', T], Monad['Option[T]', T], Functor['Option[T]', T], Generic[T], ABC):
    
    @classmethod
    def from_optional(cls: Type['Option[T]'], value: Optional[T]) -> 'Option[T]':
        return cls(value)
    
    #region Properties
    @property
    def is_defined(self) -> bool:
        return not self.is_empty
    
    @property
    def non_empty(self) -> bool:
        return self.is_defined
    
    @property
    def get(self) -> T:
        raise NotImplementedError
    
    @property
    def flatten(self) -> T:
        return self.flat_map(identity)
    #endregion
    
    #region Methods
    def get_or_else(self, orElse: T) -> T:
        raise NotImplementedError
    
    def map(self, f: Callable[[T], R]) -> 'Option[R]':
        return self.flat_map(lambda x: Some(f(x)))
    
    def foreach(self, f: Callable[[T], Any]):
        self.map(f)
    #endregion
    
    #region Operators
    def __bool__(self) -> bool:
        return self.is_defined
    
    def __len__(self) -> int:
        return int(self.is_defined)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError
    #endregion
@dataclass(frozen=True, repr=False)
class Option(_Option[T], Generic[T]):
    def __new__(cls, value: Optional[T]):
        if (value is None):
            return OptionNone
        else:
            return Some(value)
    
    def __init__(self, value: Optional[T]):
        pass

@dataclass(frozen=True, repr=False)
class Some(_Option[T], Generic[T]):
    _value: T
    
    #region Properties
    @property
    def is_empty(self):
        return False
    
    @property
    def get(self) -> T:
        return self._value
    # endregion
    
    # region Methods
    def get_or_else(self, orElse: T) -> T:
        return self._value
    
    def flat_map(self, f: Callable[[T], 'Option[R]']) -> 'Option[R]':
        return f(self._value)
    # endregion
    
    # region Operators
    def __repr__(self):
        return f"Some({self._value!r})"
    
    def __iter__(self) -> Iterator[T]:
        yield self._value
    # endregion

@dataclass(frozen=True, repr=False, init=False)
class _OptionNone(_Option[T], Generic[T]):
    # region Properties
    @property
    def is_empty(self):
        return True
    
    @property
    def get(self) -> T:
        raise EmptyOption("Could not get from empty Option")
    # endregion
    
    # region Methods
    def get_or_else(self, orElse: T) -> T:
        return orElse
    
    def flat_map(self, f: Callable[[T], 'Option[R]']) -> 'Option[R]':
        # noinspection PyTypeChecker
        return none
    # endregion
    
    # region Operators
    def __repr__(self):
        return f"None"
    
    def __iter__(self):
        return
        # noinspection PyUnreachableCode
        yield
    # endregion

Option.empty = _OptionNone()
OptionNone = Option.empty
none = Option.empty

__all__ = \
[
    'EmptyOption',
    'Option',
    'Some',
    'OptionNone',
    'none',
]

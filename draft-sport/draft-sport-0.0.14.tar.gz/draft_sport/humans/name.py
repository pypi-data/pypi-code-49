"""
Draft Sport
Name Module
author: hugh@blinkybeach.com
"""
from nozomi import Decodable, Immutable
from typing import TypeVar, Type, Any

T = TypeVar('T', bound='Name')


class Name(Decodable):

    def __init__(
        self,
        first_name: str,
        other_name: str,
        last_name: str
    ) -> None:

        self._first_name = first_name
        self._other_name = other_name
        self._last_name = last_name

        return

    first = Immutable(lambda s: s._first_name)
    other = Immutable(lambda s: s._other_name)
    last = Immutable(lambda s: s._last_name)

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            first_name=data['first_name'],
            other_name=data['other_name'],
            last_name=data['last_name']
        )

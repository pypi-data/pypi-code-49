"""
Draft Sport Python
Fantasy Player Profile Module
author: hugh@blinkybeach.com
"""
from nozomi import Decodable, Immutable
from typing import TypeVar, Type, Any

T = TypeVar('T', bound='Profile')


class Profile(Decodable):

    def __init__(
        self,
        first_name: str,
        last_name: str,
        position_name: str,
        public_id: str,
        team_name: str
    ) -> None:

        self._first_name = first_name
        self._last_name = last_name
        self._position_name = position_name
        self._public_id = public_id
        self._team_name = team_name

        return

    first_name = Immutable(lambda s: s._first_name)
    last_name = Immutable(lambda s: s._last_name)
    public_id = Immutable(lambda s: s._public_id)
    position_name = Immutable(lambda s: s._position_name)
    team_name = Immutable(lambda s: s._team_name)

    full_name = Immutable(lambda s: s._first_name + ' ' + s._last_name)

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            first_name=data['first_name'],
            last_name=data['last_name'],
            position_name=data['position_name'],
            public_id=data['public_id'],
            team_name=data['team_name']
        )

"""
Draft Sport
Team Module
author: hugh@blinkybeach.com
"""
from typing import List, Any, TypeVar, Type, Optional
from nozomi import Immutable, Decodable
from draft_sport.leagues.pick import Pick

T = TypeVar('T', bound='Team')


class Team(Decodable):

    def __init__(
        self,
        league_id: str,
        picks: List[Pick],
        manager_id: str,
        manager_display_name: str,
        name: Optional[str]
    ) -> None:

        self._league_id = league_id
        self._picks = picks
        self._manager_id = manager_id
        self._manager_display_name = manager_display_name
        self._name = name

        return

    league_id = Immutable(lambda s: s._league_id)
    picks = Immutable(lambda s: s._picks)
    manager_id = Immutable(lambda s: s._picks)
    manager_display_name = Immutable(lambda s: s._manager_display_name)
    name = Immutable(lambda s: s._name)

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            league_id=data['league_id'],
            picks=Pick.decode_many(data['picks']),
            manager_id=data['manager_id'],
            manager_display_name=data['manager_display_name'],
            name=data['name']
        )

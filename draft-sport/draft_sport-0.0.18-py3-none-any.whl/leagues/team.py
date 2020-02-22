"""
Draft Sport
Team Module
author: hugh@blinkybeach.com
"""
from typing import List, Any, TypeVar, Type
from nozomi import Immutable, Decodable
from draft_sport.leagues.pick import Pick

T = TypeVar('T', bound='Team')


class Team(Decodable):

    def __init__(
        self,
        league_id: str,
        picks: List[Pick],
        manager_id: str
    ) -> None:

        self._league_id = league_id
        self._picks = picks
        self._manager_id = manager_id

        return

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            league_id=data['league_id'],
            picks=Pick.decode_many(data['picks']),
            manager_id=data['manager_id']
        )

"""
Draft Sport
Pick Module
author: hugh@blinkybeach.com
"""
from draft_sport.fantasy.scores.player.player import Player
from nozomi import Decodable, NozomiTime, Immutable
from typing import TypeVar, Type, Any

T = TypeVar('T', bound='Pick')


class Pick(Decodable):

    def __init__(
        self,
        created: NozomiTime,
        manager_id: str,
        player: Player,
        league_id: str
    ) -> None:

        self._created = created
        self._manager_id = manager_id
        self._player = player
        self._league_id = league_id

        return

    player = Immutable(lambda s: s._player)

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            created=NozomiTime.decode(data['created']),
            manager_id=data['manager_id'],
            player=Player.decode(data['player']),
            league_id=data['league_id']
        )

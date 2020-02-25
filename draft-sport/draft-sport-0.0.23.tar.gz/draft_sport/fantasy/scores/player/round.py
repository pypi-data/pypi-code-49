"""
Draft Sport Python
Player Round Points Module
author: hugh@blinkybeach.com
"""
from draft_sport.fantasy.scores.player.score import Score
from typing import List, TypeVar, Type, Any
from nozomi import Decodable, Immutable

T = TypeVar('T', bound='Round')


class Round(Decodable):
    """Points attributed to a player in a particular round"""

    def __init__(
        self,
        sequence: int,
        scores: List[Score]
    ) -> None:

        self._round_sequence = sequence
        self._scores = scores

        return

    round_sequence = Immutable(lambda s: s._round_sequence)
    scores = Immutable(lambda s: s._scores)

    total_points = Immutable(lambda s: sum([k.value for k in s._scores]))

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            sequence=data['round_sequence'],
            scores=Score.decode_many(data['scores'])
        )

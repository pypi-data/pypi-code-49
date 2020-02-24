"""
Draft Sport Python
Player Points Module
author: hugh@blinkybeach.com
"""
from nozomi import Decodable, Immutable
from draft_sport.fantasy.scores.player.round import Round
from typing import TypeVar, Type, Any, List

T = TypeVar('T', bound='Points')


class Points(Decodable):

    def __init__(
        self,
        average_points: int,
        total_points: int,
        points_last_round: int,
        points_per_minute_played: int,
        rounds: List[Round]
    ) -> None:

        self._average_points = average_points
        self._total_points = total_points
        self._points_last_round = points_last_round
        self._points_per_minute_played = points_per_minute_played
        self._rounds = rounds

        return

    average_points = Immutable(lambda s: s._average_points)
    total_points = Immutable(lambda s: s._total_points)
    points_last_round = Immutable(lambda s: s._points_last_round)
    points_per_minute_played = Immutable(lambda s: s._points_per_minute_played)
    rounds = Immutable(lambda s: s._rounds)

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            points_per_minute_played=data['points_per_minute_played'],
            average_points=data['average_points'],
            total_points=data['total_points'],
            points_last_round=data['points_last_round'],
            rounds=Round.decode_many(data['rounds'])
        )

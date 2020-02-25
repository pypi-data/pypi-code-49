"""
Draft Sport Python
Player Points Module
author: hugh@blinkybeach.com
"""
from nozomi import Decodable, Immutable
from draft_sport.fantasy.scores.player.round import Round
from draft_sport.fantasy.scores.player.score import Score
from typing import TypeVar, Type, Any, List, Dict, Set

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
        self._rounds = sorted(rounds, key=lambda r: r.round_sequence)

        self._cached_flattened_rounds: Optional[Dict[str, List[int]]] = None

        return

    average_points = Immutable(lambda s: s._average_points)
    total_points = Immutable(lambda s: s._total_points)
    points_last_round = Immutable(lambda s: s._points_last_round)
    points_per_minute_played = Immutable(lambda s: s._points_per_minute_played)
    rounds = Immutable(lambda s: s._rounds)

    normalised_rounds = Immutable(lambda s: s._compute_normalised_rounds())
    flattened_rounds = Immutable(lambda s: s._retrieved_flattened_rounds())

    _all_metric_keys = Immutable(lambda s: s._compute_all_metric_keys())

    def _compute_all_metric_keys(self) -> Set[str]:
        keys: Set[str] = set()
        for rou in self._rounds:
            for score in rou.scores:
                keys.add(score.fantasy_metric_name)
        return sorted(keys)

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            points_per_minute_played=data['points_per_minute_played'],
            average_points=data['average_points'],
            total_points=data['total_points'],
            points_last_round=data['points_last_round'],
            rounds=Round.decode_many(data['rounds'])
        )

    def _compute_normalised_rounds(self) -> List[Round]:

        all_keys = self._all_metric_keys

        def _scores_for_round(rou: Round) -> List[Score]:

            scores: List[Score] = list()

            for key in all_keys:

                found = False

                for score in rou.scores:
                    if score.fantasy_metric_name == key:
                        scores.append(score)
                        found = True
                        break
                    
                if found is True:
                    break

                scores.append(Score(
                    fantasy_metric_name=key,
                    score=0
                ))

            return sorted(scores, key=lambda s: s.fantasy_metric_name)

        rounds: List[Round] = list()

        for rou in self._rounds:

            rounds.append(Round(
                sequence=rou.round_sequence,
                scores=_scores_for_round(rou)
            ))

        return sorted(rounds, key=lambda r: r.round_sequence)

    def _retrieved_flattened_rounds(self) -> Dict[str, List[int]]:
        if self._cached_flattened_rounds is None:
            self._cached_flattened_rounds = self._compute_flattened_rounds()
        return self._cached_flattened_rounds

    def _compute_flattened_rounds(self) -> Dict[str, List[int]]:

        flat_rounds: Dict[str, List[int]] = dict()

        for key in self._all_metric_keys:

            metric_stats: List[int] = list()

            for rou in self._rounds:

                found = False
                
                for score in rou.scores:
                    if score.fantasy_metric_name == key:
                        metric_stats.append(score.value)
                        found = True
                        break
                    continue

                if found is True:
                    continue

                metric_stats.append(0)
                continue

            flat_rounds[key] = metric_stats

            continue

        return flat_rounds

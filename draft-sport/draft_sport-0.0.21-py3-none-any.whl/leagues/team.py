"""
Draft Sport
Team Module
author: hugh@blinkybeach.com
"""
from typing import List, Any, TypeVar, Type, Optional
from nozomi import Immutable, Decodable, RequestCredentials, ApiRequest
from nozomi import Configuration, URLParameter, URLParameters, HTTPMethod
from draft_sport.leagues.pick import Pick

T = TypeVar('T', bound='Team')


class Team(Decodable):

    _PATH = '/league/team'

    def __init__(
        self,
        league_id: str,
        picks: List[Pick],
        manager_id: str,
        manager_display_name: str,
        name: Optional[str],
        total_points: int
    ) -> None:

        self._league_id = league_id
        self._picks = picks
        self._manager_id = manager_id
        self._manager_display_name = manager_display_name
        self._name = name
        self._total_points = total_points

        return

    league_id = Immutable(lambda s: s._league_id)
    picks = Immutable(lambda s: s._picks)
    manager_id = Immutable(lambda s: s._manager_id)
    manager_display_name = Immutable(lambda s: s._manager_display_name)
    name = Immutable(lambda s: s._name)
    total_points = Immutable(lambda s: s._total_points)

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            league_id=data['league_id'],
            picks=Pick.decode_many(data['picks']),
            manager_id=data['manager_id'],
            manager_display_name=data['manager_display_name'],
            name=data['name'],
            total_points=data['total_points']
        )

    @classmethod
    def retrieve(
        cls: Type[T],
        league_id: str,
        manager_id: str,
        credentials: RequestCredentials,
        configuration: Configuration
    ) -> Optional[T]:
        """
        Return a Team in the supplied League, managed by the supplied Manager,
        if it exists.
        """

        parameters = URLParameters([
            URLParameter('league', league_id),
            URLParameter('manager', manager_id)
        ])

        request = ApiRequest(
            path=cls._PATH,
            method=HTTPMethod.GET,
            configuration=configuration,
            data=None,
            url_parameters=parameters,
            credentials=credentials
        )

        return cls.optionally_decode(request.response_data)

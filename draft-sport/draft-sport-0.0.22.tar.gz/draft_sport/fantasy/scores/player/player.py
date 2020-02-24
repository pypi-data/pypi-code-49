"""
Draft Sport Python
Fantasy Player Score Module
Author: hugh@blinkybeach.com
"""
from nozomi import Decodable, HTTPMethod, URLParameter, URLParameters
from nozomi import Immutable, ApiRequest, RequestCredentials
from draft_sport.fantasy.player.profile import Profile
from typing import Type, TypeVar, Any, Optional, List
from draft_sport.ancillary.configuration import Configuration
from draft_sport.fantasy.scores.player.order_by import OrderBy
from draft_sport.fantasy.scores.player.points import Points
from draft_sport.data.order import Order

T = TypeVar('T', bound='Player')


class Player(Decodable):

    _PATH = '/fantasy/player'
    _LIST_PATH = '/fantasy/player/list'

    def __init__(
        self,
        profile: Profile,
        limit: int,
        offset: int,
        query_count: int,
        sequence: int,
        requesting_agent_id: str,
        points: Points,
        query_time: int
    ) -> None:

        self._profile = profile
        self._limit = limit
        self._offset = offset
        self._query_count = query_count
        self._sequence = sequence
        self._requesting_agent_id = requesting_agent_id
        self._points = points
        self._query_time = query_time

        return

    public_id = Immutable(lambda s: s._profile.public_id)

    profile = Immutable(lambda s: s._profile)
    limit = Immutable(lambda s: s._limit)
    offset = Immutable(lambda s: s._offset)
    query_count = Immutable(lambda s: s._query_count)
    sequence = Immutable(lambda s: s._sequence)
    requesting_agent_id = Immutable(lambda s: s._requesting_agent_id)
    points = Immutable(lambda s: s._points)
    query_time = Immutable(lambda s: s._query_time)

    query_time_seconds = Immutable(
        lambda s: str(int(s._query_time) / 1000)
    )

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            profile=Profile.decode(data['player']),
            limit=data['limit'],
            offset=data['offset'],
            query_count=data['query_count'],
            sequence=data['sequence'],
            requesting_agent_id=data['requesting_agent_id'],
            points=Points.decode(data['points']),
            query_time=data['query_time']
        )

    @classmethod
    def retrieve(
        cls: Type[T],
        public_id: str,
        season_id: str,
        credentials: Optional[RequestCredentials],
        configuration: Optional[Configuration]
    ) -> Optional[T]:

        parameters = URLParameters([
            URLParameter('public_id', public_id),
            URLParameter('season', season_id)
        ])

        request = ApiRequest(
            path=cls._PATH,
            method=HTTPMethod.GET,
            data=None,
            url_parameters=parameters,
            credentials=credentials,
            configuration=configuration
        )

        return cls.optionally_decode(request.response_data)

    @classmethod
    def retrieve_many(
        cls: Type[T],
        season_id: str,
        offset: int,
        limit: int,
        order_by: OrderBy = OrderBy.TOTAL_SEASON_POINTS,
        order: Order = Order.DESCENDING,
        name_fragment: Optional[str] = None,
        credentials: Optional[RequestCredentials] = None,
        configuration: Optional[Configuration] = None
    ) -> List[T]:

        parameters = URLParameters([
            URLParameter('season', season_id),
            URLParameter('offset', offset),
            URLParameter('limit', limit),
            URLParameter('order_by', order_by.value),
            URLParameter('order', order.value)
        ])

        if name_fragment is not None:
            parameters.append(URLParameter('fragment', name_fragment))

        request = ApiRequest(
            path=cls._LIST_PATH,
            method=HTTPMethod.GET,
            data=None,
            url_parameters=parameters,
            credentials=credentials,
            configuration=configuration
        )

        return cls.optionally_decode_many(
            request.response_data,
            default_to_empty_list=True
        )

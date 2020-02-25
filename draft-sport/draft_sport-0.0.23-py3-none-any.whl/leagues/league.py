"""
Draft Sport
League Module
author: hugh@blinkybeach.com
"""
from nozomi import Immutable, Configuration, RequestCredentials
from nozomi import Decodable, NozomiTime
from typing import Optional, Type, TypeVar, Any, List
from nozomi import URLParameter, URLParameters, HTTPMethod, ApiRequest
from draft_sport.leagues.team import Team

T = TypeVar('T', bound='League')


class League(Decodable):

    _PATH = '/league'

    def __init__(
        self,
        public_id: str,
        teams: List[Team],
        commissioner_id: str,
        name: str,
        created: NozomiTime
    ) -> None:

        self._public_id = public_id
        self._teams = teams
        self._commissioner_id = commissioner_id
        self._name = name
        self._created = created

        return

    name = Immutable(lambda s: s._name)
    public_id = Immutable(lambda s: s._public_id)
    teams = Immutable(lambda s: s._teams)

    @classmethod
    def retrieve(
        cls: Type[T],
        public_id: str,
        credentials: RequestCredentials,
        configuration: Configuration
    ) -> Optional[T]:
        """
        Optionally return a League with the given public ID, if it exists
        """

        assert isinstance(public_id, str)

        parameters = URLParameters([
            URLParameter('league', public_id),
            URLParameter('season', '2020')  # MVP hardcode
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

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        return cls(
            public_id=data['public_id'],
            teams=Team.decode_many(data['teams']),
            commissioner_id=data['commissioner_id'],
            name=data['name'],
            created=NozomiTime.decode(data['created'])
        )

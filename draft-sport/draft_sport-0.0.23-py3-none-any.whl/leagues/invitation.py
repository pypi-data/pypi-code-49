"""
Draft Sport
Invitation Module
author: hugh@blinkybeach.com
"""
from nozomi import Immutable, Configuration, RequestCredentials
from nozomi import Decodable, NozomiTime
from typing import Optional, Type, TypeVar, Any, List
from nozomi import URLParameter, URLParameters, HTTPMethod, ApiRequest
from draft_sport.leagues.team import Team

T = TypeVar('T', bound='Inviation')


class Invitation(Decodable):

    _PATH = '/league/manager/invitation'

    def __init__(
        self,
        created: NozomiTime,
        league_name: str,
        league_id: str,
        token: str,
        invitee_id: Optional[str],
        accepted: bool,
        associated_email: Optional[str]
    ) -> None:

        self._created = created
        self._league_name = league_name
        self._league_id = league_id
        self._token = token
        self._invitee_id = invitee_id
        self._accepted = accepted
        self._associated_email = associated_email

        return

    created = Immutable(lambda s: s._created)
    league_name = Immutable(lambda s: s._league_name)
    league_id = Immutable(lambda s: s._league_id)
    token = Immutable(lambda s: s._token)
    invitee_id = Immutable(lambda s: s._invitee_id)
    has_been_accepted = Immutable(lambda s: s._accepted)
    associated_email = Immutable(lambda s: s._associated_email)

    @classmethod
    def retrieve(
        cls: Type[T],
        token: str,
        credentials: RequestCredentials,
        configuration: Configuration
    ) -> Optional[T]:
        """
        Optionally return an Invitation with the given token if it exists
        """

        assert isinstance(token, str)

        parameters = URLParameters([URLParameter('token', token)])

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
            created=NozomiTime.decode(data['created']),
            token=data['token'],
            league_id=data['league_public_id'],
            league_name=data['league_name'],
            invitee_id=data['invitee_public_id'],
            accepted=data['accepted'],
            associated_email=data['associated_email']
        )

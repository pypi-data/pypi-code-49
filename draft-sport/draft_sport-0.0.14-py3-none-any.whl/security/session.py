"""
Draft Sport Python
Session Module
author: hugh@blinkybeach.com
"""
from nozomi.app import Session as NozomiAppSession
from nozomi import NozomiTime, Immutable, Configuration, Agent
from nozomi import StandaloneAgent, RequestCredentials
from typing import Optional, Type, TypeVar, Any
from draft_sport.security.perspective import Perspective
from nozomi import URLParameter, URLParameters, HTTPMethod, ApiRequest

T = TypeVar('T', bound='Session')


class Session(NozomiAppSession):

    API_PATH = '/session'

    def __init__(
        self,
        session_id: str,
        session_key: str,
        api_key: str,
        agent: Agent,
        created: NozomiTime,
        last_utilised: NozomiTime,
        perspective: Perspective
    ) -> None:

        assert isinstance(session_id, str)
        assert isinstance(session_key, str)
        assert isinstance(api_key, str)
        assert isinstance(agent, Agent)
        assert isinstance(created, NozomiTime)
        assert isinstance(last_utilised, NozomiTime)
        assert isinstance(perspective, Perspective)

        self._session_id = session_id
        self._session_key = session_key
        self._api_key = api_key
        self._agent = agent
        self._created = created
        self._last_utilised = last_utilised
        self._perspective = perspective

        return

    agent: Agent = Immutable(lambda s: s._agent)
    perspective: Perspective = Immutable(lambda s: s._perspective)
    api_key: str = Immutable(lambda s: s._api_key)
    session_id: int = Immutable(lambda s: s._session_id)

    agent_id = Immutable(lambda s: s._agent.agent_id)

    def delete(
        self,
        credentials: RequestCredentials,
        configuration: Configuration
    ) -> None:
        """Delete this Session, AKA logout the user"""
        target = URLParameter('session_id', str(self._session_id))
        parameters = URLParameters([target])

        ApiRequest(
            path=self.API_PATH,
            method=HTTPMethod.DELETE,
            configuration=configuration,
            credentials=credentials,
            data=None,
            url_parameters=parameters
        )
        return None

    @classmethod
    def retrieve(
        cls: Type[T],
        session_id: str,
        credentials: RequestCredentials,
        configuration: Configuration
    ) -> Optional[T]:
        """Return a Session with the given Session ID, if it exists"""

        assert isinstance(session_id, str)

        target = URLParameter('session_id', str(session_id))
        parameters = URLParameters([target])

        request = ApiRequest(
            path=cls.API_PATH,
            method=HTTPMethod.GET,
            configuration=configuration,
            credentials=credentials,
            data=None,
            url_parameters=parameters
        )

        if request.response_data is None:
            return None

        return cls.decode(request.response_data)

    @classmethod
    def create(
        cls: Type[T],
        email: str,
        secret: str,
        configuration: Configuration
    ) -> T:

        data = {
            'email': email,
            'secret': secret
        }

        raise NotImplementedError

    @classmethod
    def decode(cls: Type[T], data: Any) -> T:
        """Return a Session decoded from API response data"""

        return cls(
            data['session_id'],
            data['session_key'],
            data['api_key'],
            StandaloneAgent.decode(data),
            NozomiTime.decode(data['created']),
            NozomiTime.decode(data['last_utilised']),
            Perspective.with_id(data['perspective'])
        )

"""Types for bareASGI and bareClient"""

from abc import ABCMeta, abstractmethod
from typing import (
    AbstractSet,
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Tuple,
    Union
)


class ParseError(Exception):
    """Exception raised on a parse error"""


class HttpInternalError(Exception):
    """Exception raised for an internal error"""


class HttpDisconnectError(Exception):
    """Exception raise on HTTP disconnect"""


class WebSocketInternalError(Exception):
    """Exception raised for a WebSocket internal error"""


Scope = Mapping[str, Any]
Message = Mapping[str, Any]
Context = Optional[Mapping[str, Any]]
Info = Optional[MutableMapping[str, Any]]

Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]

ASGIInstance = Callable[[Receive, Send], Awaitable[None]]
ASGIApp = Callable[[Scope], ASGIInstance]

LifespanHandler = Callable[[Scope, Info, Message], Awaitable[None]]

Header = Tuple[bytes, bytes]
Headers = List[Header]

RouteMatches = Mapping[str, Any]
Content = AsyncIterable[bytes]
PushResponse = Tuple[str, Headers]
PushResponses = Iterable[PushResponse]


class WebSocket(metaclass=ABCMeta):
    """The interface for a server side WebSocket."""

    @abstractmethod
    async def accept(
            self,
            subprotocol: Optional[str] = None,
            headers: Optional[List[Header]] = None
    ) -> None:
        """Accept the socket.

        This must be done before any other action is taken.
        
        Args:
            subprotocol (Optional[str], optional): An optional subprotocol sent
                by the client. Defaults to None.
            headers (Optional[List[Header]], optional): Optional headers to
                send. Defaults to None.
        """

    @abstractmethod
    async def receive(self) -> Optional[Union[bytes, str]]:
        """Receive data from the WebSocket.
        
        Returns:
            Optional[Union[bytes, str]]: Either bytes of a string depending on
                the client.
        """

    @abstractmethod
    async def send(self, content: Union[bytes, str]) -> None:
        """Send data to the client.
        
        Args:
            content (Union[bytes, str]): Either bytes or a string.
        """

    @abstractmethod
    async def close(self, code: int = 1000) -> None:
        """Close the WebSocket.
        
        Args:
            code (int, optional): The reason code. Defaults to 1000.
        """


HttpResponse = Union[
    int,
    Tuple[int, Optional[Headers]],
    Tuple[int, Optional[Headers], Optional[Content]],
    Tuple[int, Optional[Headers], Optional[Content], Optional[PushResponses]]
]
HttpRequestCallback = Callable[[Scope, Info,
                                RouteMatches, Content], Awaitable[HttpResponse]]
WebSocketRequestCallback = Callable[[
    Scope, Info, RouteMatches, WebSocket], Awaitable[None]]
HttpMiddlewareCallback = Callable[[
    Scope, Info, RouteMatches, Content, HttpRequestCallback], Awaitable[HttpResponse]]


class HttpRouter(metaclass=ABCMeta):
    """The interface for an HTTP router"""

    @property  # type: ignore
    @abstractmethod
    def not_found_response(self) -> HttpResponse:
        """The response when a handler could not be found for a method/path
        
        Returns:
            HttpResponse: The response when a route cannot be found.
        """

    @not_found_response.setter  # type: ignore
    @abstractmethod
    def not_found_response(self, value: HttpResponse) -> None:
        ...

    @abstractmethod
    def add(
            self,
            methods: AbstractSet[str],
            path: str,
            callback: HttpRequestCallback
    ) -> None:
        """Add an HTTP request handler
        
        Args:
            methods (AbstractSet[str]): The supported HTTP methods.
            path (str): The path.
            callback (HttpRequestCallback): The request handler.
        """

    @abstractmethod
    def resolve(
            self,
            method: str,
            path: str
    ) -> Tuple[Optional[HttpRequestCallback], Optional[RouteMatches]]:
        """Resolve a request to a handler with the route matches
        
        Args:
            method (str): The HTTP method.
            path (str): The path.
        
        Returns:
            Tuple[Optional[HttpRequestCallback], Optional[RouteMatches]]: A
                handler and the optional route matches.
        """


class WebSocketRouter(metaclass=ABCMeta):
    """The interface for a WebSocket router"""

    @abstractmethod
    def add(
            self,
            path: str,
            callback: WebSocketRequestCallback
    ) -> None:
        """Add the WebSocket handler for a route
        
        Args:
            path (str): The path.
            callback (WebSocketRequestCallback): The handler
        """

    @abstractmethod
    def resolve(
            self,
            path: str
    ) -> Tuple[Optional[HttpRequestCallback], Optional[RouteMatches]]:
        """Resolve a route to a handler
        
        Args:
            path (str): The path
        
        Returns:
            Tuple[Optional[HttpRequestCallback], Optional[RouteMatches]]: A
                handler and possible route matches
        """

"""Session"""

from uuid import uuid4 as uuid

from bareasgi import Application
from baretypes import (
    Scope,
    Info,
    RouteMatches,
    Content,
    HttpRequestCallback,
    HttpResponse
)
from bareutils.cookies import decode_set_cookie
import bareutils.header as header

from .factory import SessionCookieFactory
from .storage import SessionStorage

SESSION_COOKIE_NAME = b'bareASGI-session'
SESSION_COOKIE_KEY = '__bareasgi_session__'


def add_session_middleware(
        app: Application,
        storage: SessionStorage,
        cookie_factory: SessionCookieFactory
) -> None:
    """Add the session middleware

    Args:
        app (Application): The ASGI application
        storage (SessionStorage): The session storage engine
        cookie_factory (SessionCookieFactory): The session cookie factory
    """

    async def _session_middleware(
            scope: Scope,
            info: Info,
            matches: RouteMatches,
            content: Content,
            handler: HttpRequestCallback
    ) -> HttpResponse:
        # Fetch or create the session cookie and add it to info
        cookies = header.cookie(scope['headers'])
        cookie = cookies.get(cookie_factory.name)
        session_key: str = cookie[0].decode('ascii') if cookie else str(uuid())
        info[SESSION_COOKIE_KEY] = await storage.load(session_key)

        # Call the request handler.
        status_code, headers, content, push_responses = await handler(
            scope,
            info,
            matches,
            content
        )

        # Save the cookie data
        await storage.save(session_key, info[SESSION_COOKIE_KEY])

        # Put the set-cookie in the headers
        set_cookie = cookie_factory.create_cookie(session_key)
        set_cookie_header = (b'set-cookie', set_cookie)
        for index, (key, value) in enumerate(headers):
            if key == b'set-cookie':
                candidate = decode_set_cookie(value)
                if candidate['name'] == cookie_factory.name:
                    headers[index] = set_cookie_header
                    break
        else:
            headers.append(set_cookie_header)

        # Return the response.
        return status_code, headers, content, push_responses

    app.middlewares.append(_session_middleware)

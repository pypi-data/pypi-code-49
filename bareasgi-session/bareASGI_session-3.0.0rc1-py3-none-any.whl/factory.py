"""A session cookie factory

Attributes:
    SESSION_COOKIE_NAME (bytes): 'bareASGI-session' - The session cookie name.
    SESSION_COOKIE_EXPIRES (Optional[datetime]): None - The session cookie expiry.
    SESSION_COOKIE_MAX_AGE (Optional[Union[int, timedelta]]): None - The maximum age of the session cookie.
    SESSION_COOKIE_PATH (Optional[bytes]): None - The session cookie path
    SESSION_COOKIE_DOMAIN (Optional[bytes]): None - the session cookie domain
    SESSION_COOKIE_SECURE (bool): False - Indicates whether the session cookie is available to JavaScript.
    SESSION_COOKIE_HTTP_ONLY (bool): False - Indicates whether the session cookie is available to the browser.
    SESSION_COOKIE_SAME_SITE (Optional[bytes]): None - CORS directive.
"""

from datetime import datetime, timedelta
from typing import Optional, Union

from bareutils.cookies import encode_set_cookie

SESSION_COOKIE_NAME: bytes = b'bareASGI-session'
SESSION_COOKIE_EXPIRES: Optional[datetime] = None
SESSION_COOKIE_MAX_AGE: Optional[Union[int, timedelta]] = None
SESSION_COOKIE_PATH: Optional[bytes] = None
SESSION_COOKIE_DOMAIN: Optional[bytes] = None
SESSION_COOKIE_SECURE: bool = False
SESSION_COOKIE_HTTP_ONLY: bool = False
SESSION_COOKIE_SAME_SITE: Optional[bytes] = None


class SessionCookieFactory:
    """Session cookie factory"""

    def __init__(
            self,
            name: bytes = SESSION_COOKIE_NAME,
            expires: Optional[datetime] = SESSION_COOKIE_EXPIRES,
            max_age: Optional[Union[int, timedelta]] = SESSION_COOKIE_MAX_AGE,
            path: Optional[bytes] = SESSION_COOKIE_PATH,
            domain: Optional[bytes] = SESSION_COOKIE_DOMAIN,
            secure: bool = SESSION_COOKIE_SECURE,
            http_only: bool = SESSION_COOKIE_HTTP_ONLY,
            same_site: Optional[bytes] = SESSION_COOKIE_SAME_SITE
    ) -> None:
        """A session cookie factory.

        Args:
            name ([type], optional): The session cookie name. Defaults to
                SESSION_COOKIE_NAME.
            expires (Optional[datetime], optional): The session cookie expiry.
                Defaults to SESSION_COOKIE_EXPIRES.
            max_age (Optional[Union[int, timedelta]], optional): The maximum age
                of the session cookie. Defaults to SESSION_COOKIE_MAX_AGE.
            path (Optional[bytes], optional): The session cookie path. Defaults
                to SESSION_COOKIE_PATH.
            domain (Optional[bytes], optional): The session cookie domain.
                Defaults to SESSION_COOKIE_DOMAIN.
            secure (bool, optional): Indicates whether the cookie should be sent
                over https only. Defaults to SESSION_COOKIE_SECURE.
            http_only (bool, optional): Indicates whether the session cookie is
                available to JavaScript in the browser. Defaults to
                SESSION_COOKIE_HTTP_ONLY.
            same_site (Optional[bytes], optional): CORS directive. Defaults to
                SESSION_COOKIE_SAME_SITE.
        """
        self.name = name
        self.expires = expires
        self.max_age = max_age
        self.path = path
        self.domain = domain
        self.secure = secure
        self.http_only = http_only
        self.same_site = same_site

    def create_cookie(self, key: str) -> bytes:
        """Creates the 'set-cookie' header value

        Args:
            key (str): The session key

        Returns:
            bytes: The set-cookie header value.
        """
        return encode_set_cookie(
            self.name,
            key.encode('ascii'),
            expires=self.expires,
            max_age=self.max_age,
            path=self.path,
            domain=self.domain,
            secure=self.secure,
            http_only=self.http_only,
            same_site=self.same_site
        )

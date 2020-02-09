"""
Draft Sport
API Request Module
author: hugh@blinkybeach.com
"""
from nozomi import HTTPMethod, URLParameters, Immutable
from urllib.request import Request
from urllib.request import urlopen
from draft_sport.security.session import Session
from typing import Any, Optional, TypeVar
from urllib.request import HTTPError
import json
from draft_sport.ancillary.configuration import Configuration

T = TypeVar('T', bound='ApiRequest')


class ApiRequest:
    """A request to a draft_sport-compliant API via HTTP"""

    _DEFAULT_ENDPOINT = 'https://draftrugby.com/api'

    def __init__(
        self,
        path: str,
        method: HTTPMethod,
        data: Optional[Any] = None,
        url_parameters: Optional[URLParameters] = None,
        session: Optional[Session] = None,
        configuration: Optional[Configuration] = None
    ) -> None:

        api_endpoint = self._DEFAULT_ENDPOINT
        if configuration is not None:
            api_endpoint = configuration.api_endpoint

        if not path[0] == '/':
            raise ValueError('Path must begin with \'/\'')
        url = api_endpoint + path
        if url_parameters is not None:
            url = url_parameters.add_to(url)

        headers = session.http_headers if session is not None else dict()

        if data is not None:
            data = json.dumps(data).encode('utf-8')
            headers['content-type'] = 'application/json'

        request = Request(
            url,
            method=method.value,
            data=data,
            headers=headers
        )

        try:
            response = urlopen(request).read()
        except HTTPError as error:
            if error.code == 404:
                self._response_data = None
                return
            raise

        self._response_data = json.loads(response)

        return

    response_data = Immutable(lambda s: s._response_data)

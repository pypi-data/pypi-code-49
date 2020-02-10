"""
REST queries to the backend
"""
import uuid

import requests

from disco.core.exceptions import GraphQLRequestException, TimeOutError, RequestException
from disco.core.exception_factory import ExceptionFactory
from .request_mixin import _RequestsMixin
from .commands import REGISTERED_COMMANDS
from ..core import utils


class RestQuery(_RequestsMixin):
    """Allows submission of REST queries to the backend and then
    either streaming or getting their output.
    """
    RestMethods = {'get', 'post', 'head', 'put', 'options', 'delete'}

    def __init__(
            self,
            url: str,
            data: dict = None,
            params: dict = None,
            method: str = 'get',
            **kwargs
    ):
        """Builds a request to be sent or streamed.

        Args:
            url: Relative url.
            data: Data to be sent.
            params: Parameters to be sent (see: requests package parameters).
            method: Method  to be used.
            skip_authorisation: If set to `True`,
                won't attempt to authorise the request. (used for login).
            request_id: Optional id to attach to the request and response.
                Defaults to GUID.
        """
        assert method in self.RestMethods
        self.url = url
        self.data = data
        self.params = params
        self.method = method
        # implicit request id on Falsy values
        self.request_id = kwargs.get('request_id') or uuid.uuid4().hex
        self.cookies = kwargs.get('cookies') or {}
        self.headers = kwargs.get('headers') or {}

    @property
    def absolute_path(self):
        """Absolute path for the request.

        Returns:
            str: Url for specific REST url.
        """
        return self.get_rest_endpoint(self.url)

    @_RequestsMixin.handle_500_errors
    def _request(self, stream: bool):
        headers = utils.merge_dictionaries(self.headers, self.disco_headers)
        response = requests.request(
            self.method,
            self.absolute_path,
            params=self.params, cookies=self.cookies or None,
            headers=headers, stream=stream, json=self.data)
        response.request_id = self.request_id
        return response

    def stream(self):
        """Stream results rather than getting all at once.

        Returns:
            Raw response bytes.
        """
        ret_data = b''
        with self._request(True) as response:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    ret_data += chunk
        return ret_data

    def send(self):
        """Sends the request to the backend and gets the result json.

        Returns:
            The data portion of the response json.
        """
        response = self._request(False)

        # 504 Gateway Time-out from Nginx
        if response.status_code in [502, 504]:
            raise TimeOutError()
        try:
            json_response = response.json()
        except ValueError:
            raise RequestException()

        if response.content and 'data' in json_response and \
                json_response['data'] is not None:
            return json_response['data']

        if 'error' in json_response:
            raise ExceptionFactory.from_response(json_response)

        if 'errors' in json_response:
            raise GraphQLRequestException('Graphql call returned with errors', json_response['errors'])

        return None

    def __str__(self):
        return f"REST Query: {self.method} {self.url} {self.data}"


class Query(RestQuery):
    """GQL Query.
    The query itself should be stored in `./commands/Q_NAME.gql` and then
    referenced by `Q_NAME` as `operation_name`.
    """
    _rest_properties = {
        'request_id': None
    }

    def __init__(self, operation_name=None, query_string=None, **kwargs):
        """New GQL Query. Only sets up the query but does not execute it.

        Args:
            operation_name: the op_name to be sent and
                the file containing the query itself.
            query_string: optional explicit query string.
                Defaults to the query in the `./commands/operation_name.gql`
            **kwargs: params to be passed as variables to the query.
        """
        base_props = {
            k: kwargs.pop(k, v)
            for k, v in self._rest_properties.items()
        }
        self.operation = operation_name
        self.variables = dict(kwargs)

        self.query_string = query_string
        if self.query_string is None:
            self.query_string = REGISTERED_COMMANDS[operation_name]

        data = utils.filter_nones(
            operationName=self.operation,
            variables=self.variables,
            query=self.query_string
        )
        super().__init__(url='qgl', method='post', data=data, **base_props)

    @property
    def absolute_path(self):
        """Absolute path for the request.

        Returns:
            str: Base url for DISCO GQL requests.
        """
        return self.get_graphql_endpoint()

    def __str__(self):
        return f"GQL Query: " \
            f"{self.operation or self.query_string} " \
            f"{self.variables}"

    def stream(self):
        raise NotImplementedError("Streaming of GQL results is not"
                                  " supported yet")

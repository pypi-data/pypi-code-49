from abc import abstractmethod
from enum import Enum
from functools import partialmethod
from typing import Any

from requests import Session


from trade_common.settings.config import Config


class WithRequestMethods(type):
    """
    This metaclass generates wrapper methods around the request functions for each HTTP action.

    e.g. get, post, patch, put

    These methods just proxy to the class request methods and pass the appropriate request_type
    parameter
    """

    def __init__(cls, *args):
        super().__init__(*args)

        for method in cls.RequestType:
            setattr(cls, f"{method.value}", partialmethod(cls.__request, method))


class ApiClient(metaclass=WithRequestMethods):
    get: Any
    post: Any
    delete: Any
    patch: Any

    class RequestType(Enum):
        GET = "get"
        POST = "post"
        PUT = "put"
        DELETE = "delete"

    def __init__(self, config: Config):
        self.base_url = config.base_url
        self.api_key = config.api_key
        self.api_secret = config.api_secret
        self.__session = Session()

    @abstractmethod
    def __sign_n_encode(self, data):
        raise NotImplementedError

    @abstractmethod
    def __request(self, request_type, path, headers, params=None, data=None):
        raise NotImplementedError

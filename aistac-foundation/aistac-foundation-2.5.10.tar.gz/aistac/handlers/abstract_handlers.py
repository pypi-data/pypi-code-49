import importlib.util
import re
from datetime import datetime
from urllib.parse import parse_qsl, urlparse, urlunparse
from abc import ABC, abstractmethod
from typing import Any

__author__ = 'Darryl Oatridge'


class ConnectorContract(object):
    """ a container class for Connector Contract"""
    uri_raw: str = None
    module_name: str = None
    handler: str = None
    _kwargs: dict = None
    address_raw: str = None
    schema: str = None
    netloc: str = None
    path: str = None
    _params: list = None
    _query: dict = None
    fragment: str = None
    username: str = None
    password: str = None
    hostname: str = None
    port: int = None
    version: str = None

    def __init__(self, uri: str,  module_name: str, handler: str, version: str=None, **kwargs):
        """ initialisation of the Connector Contract. Though not required, the URI can be considered as a
        URL of the form 'scheme://netloc/path;parameters?query#fragment' Following the syntax specifications
        in RFC 1808. This allows the use of the helper method `parse_uri` and static method `parse_params`

        :param uri: A Uniform Resource Identifier that unambiguously identifies a particular resource
        :param module_name: the module or package name where the handler can be found
        :param handler: the handler for retrieving the resource
        :param version: a version number to pass to the connector
        :param kwargs: (optional) key word arguments to be passed to the handler.
        """
        if not isinstance(uri, str) or len(uri) == 0:
            raise ValueError("The uri must be a valid string")
        self.uri_raw = uri
        self.module_name = module_name
        self.handler = handler
        self.version = version if isinstance(version, str) else "v00"
        self._kwargs = kwargs if isinstance(kwargs, dict) else {}
        parse_url = urlparse(self.uri)
        self.address_raw = self.parse_address(uri=uri, with_credentials=True, with_port=True)
        self.schema = parse_url.scheme
        self.netloc = parse_url.netloc
        self.path = parse_url.path
        self._params = parse_url.params.split(sep=';') if len(parse_url.params) > 0 else []
        self._query = dict(parse_qsl(parse_url.query))
        self.fragment = parse_url.fragment
        self.username = parse_url.username
        self.password = parse_url.password
        self.hostname = parse_url.hostname
        self.port = parse_url.port

    @property
    def kwargs(self) -> dict:
        """copy of the private kwargs dictionary"""
        return self._kwargs.copy() if isinstance(self._kwargs, dict) else {}

    @property
    def query(self) -> dict:
        """copy of the private query dictionary"""
        return self._query.copy() if isinstance(self._query, dict) else {}

    @property
    def address(self) -> str:
        return self._format_uri(uri_raw=self.address_raw, version=self.version)

    @property
    def uri(self) -> str:
        return self._format_uri(uri_raw=self.uri_raw, version=self.version)

    @property
    def params(self) -> list:
        """copy of the private params list"""
        return self._params.copy() if isinstance(self._params, list) else []

    def get_key_value(self, key: str, default: Any=None) -> Any:
        """ returns the value for the key in the kwargs or query dictionaries.
        If the key is found in both then the query value is returned

        :param key: the key to look for
        :param default: a default value to return if not found
        :return: the value of the key or the default value if key is not found
        """
        value = self._kwargs.get(key, default)
        return self._query.get(key, value)

    @staticmethod
    def _format_uri(uri_raw: str, version: str):
        """The URI with any modifications"""
        pattern = r'\${([A-Za-z_0-9\-]+)}'
        uri_tags = re.findall(pattern, uri_raw)
        if len(uri_tags) == 0:
            return uri_raw
        tags_dict = ConnectorContract._uri_tag_dict(version)
        pattern = r'\${([A-Za-z_0-9\-]+)}'
        for tag in uri_tags:
            if tag not in tags_dict.keys():
                raise ValueError(
                    f"The URI tag '{tag}' is not recognised, valid tags are {list(tags_dict.keys())}'")
        return re.sub(pattern, lambda m: tags_dict.get(m.group(1), ""), uri_raw)

    @staticmethod
    def _uri_tag_dict(version: str) -> dict:
        """returns a dictionary of URI tags and their substitute"""
        return {'VERSION': f"_{version}",
                'TO_DAYS': datetime.now().strftime("_%Y%m%d"),
                'TO_HOURS': datetime.now().strftime("_%Y%m%d%H"),
                'TO_MINUTES': datetime.now().strftime("_%Y%m%d%H%M"),
                'TO_SECONDS': datetime.now().strftime("_%Y%m%d%H%M%S"),
                'TO_NS': datetime.now().strftime("_%Y%m%d%H%M%S%f")}

    @staticmethod
    def uri_tags() -> list:
        """returns the list of valid uri substitute tags"""
        return list(ConnectorContract._uri_tag_dict(version='').keys())

    @staticmethod
    def parse_address_elements(uri: str, with_credentials: bool=None, with_port: bool=None) -> tuple:
        """ utility method to extract the address elements (schema, netloc, path) from a URI.
        Optionally the credentials and/or port can be excluded from the netloc

        :param uri: the URI to parse
        :param with_credentials: (optional) if to include the credentials. Default is True
        :param with_port: (optional) if to include the port. Default is True
        :return: a tuple of (schema, netloc, path)
        """
        _address = ConnectorContract.parse_address(uri=uri, with_credentials=with_credentials, with_port=with_port)
        parse_address = urlparse(_address)
        return tuple([parse_address.scheme, parse_address.netloc, parse_address.path])

    @staticmethod
    def parse_query(uri: str) -> dict:
        """ utility method to extract the query element from a URI

        :param uri: the URI to parse
        :return:
        """
        parse_url = urlparse(uri)
        _query = dict(parse_qsl(parse_url.query))
        return _query

    @staticmethod
    def parse_address(uri: str, with_credentials: bool=None, with_port: bool=None) -> str:
        """ utility method to extract the address from a URI, removing params, query and fragment. optionally
        the credentials and port can be excluded

        :param uri: the URI to parse
        :param with_credentials: (optional) if to include the credentials. Default is True
        :param with_port: (optional) if to include the port. Default is True
        :return: the full address string
        """
        with_credentials = with_credentials if isinstance(with_credentials, bool) else True
        with_port = with_port if isinstance(with_port, bool) else True
        parse_url = urlparse(uri)
        _netloc = parse_url.hostname
        if with_credentials and isinstance(parse_url.username, str) and isinstance(parse_url.password, str):
            _credentials = ":".join([parse_url.username, parse_url.password])
            _netloc = '@'.join([_credentials, _netloc])
        if with_port and isinstance(parse_url.port, int):
            _netloc = ':'.join([_netloc, str(parse_url.port)])
        return urlunparse((parse_url.scheme, _netloc, parse_url.path, '', '', ''))

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the Connector Contract"""
        uri_dict = {'address': self.address_raw, 'schema': self.schema, 'netloc': self.netloc, 'path': self.path,
                    'params': self.params, 'query': self.query, 'fragment': self.fragment}
        for attr in ['username', 'password', 'hostname', 'port', ]:
            attr_value = eval('self.{}'.format(attr))
            if attr_value is not None:
                uri_dict.update({attr: attr_value})
        rtn_dict = {'uri_raw': self.uri_raw, 'uri_parsed': uri_dict, 'module_name': self.module_name,
                    'handler': self.handler, 'version': self.version, 'kwargs': self.kwargs}
        return rtn_dict

    def __len__(self):
        return self.to_dict().__len__()

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return f"<{self.__class__.__name__} {str(self.to_dict())}"

    def __eq__(self, other):
        return self.to_dict().__eq__(other.to_dict())

    def __setattr__(self, key, value):
        if self.to_dict().get(key, None) is None:
            super().__setattr__(key, value)
        else:
            raise AttributeError("The attribute '{}' is immutable once set and can not be changed".format(key))

    def __delattr__(self, item):
        raise AttributeError("{} is an immutable class and attributes can't be removed".format(self.__class__.__name__))


class AbstractSourceHandler(ABC):

    def __init__(self, connector_contract: ConnectorContract):
        self._contract = connector_contract

    @property
    def connector_contract(self) -> ConnectorContract:
        return self._contract

    def set_connector_contract(self, source_contract: ConnectorContract):
        self._contract = source_contract

    @abstractmethod
    def supported_types(self) -> list:
        pass

    @abstractmethod
    def exists(self) -> bool:
        pass

    @abstractmethod
    def get_modified(self) -> [int, float, str]:
        pass

    @abstractmethod
    def load_canonical(self, **kwargs) -> Any:
        pass


class AbstractPersistHandler(AbstractSourceHandler):

    @abstractmethod
    def persist_canonical(self, canonical: Any, **kwargs) -> bool:
        pass

    @abstractmethod
    def remove_canonical(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def backup_canonical(self, canonical: Any, uri: str, **kwargs) -> bool:
        """ creates a backup of the canonical to an alternative uri

        :param canonical: the canonical to back up
        :param uri: an alternative uri to the one in the ConnectorContract
        :param kwargs: if given, these kwargs are used as a replacement of the connector kwargs
        :return: True if successful
        """
        pass


class HandlerFactory(object):

    @staticmethod
    def instantiate(connector_contract: ConnectorContract) -> [AbstractSourceHandler, AbstractPersistHandler]:
        module_name = connector_contract.module_name
        handler = connector_contract.handler

        # check module
        module_spec = importlib.util.find_spec(module_name)
        if module_spec is None:
            raise ModuleNotFoundError("The module '{}' could not be found".format(module_name))

        # check handler
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        if handler not in dir(module):
            raise ImportError("The handler '{handler}' could not be found in the module '{module_name}'")

        # create instance of handler
        local_kwargs = locals().get('kwargs') if 'kwargs' in locals() else dict()
        local_kwargs['module'] = module
        local_kwargs['connector_contract'] = connector_contract
        instance = eval(f'module.{handler}(connector_contract)', globals(), local_kwargs)
        if not isinstance(instance, (AbstractSourceHandler, AbstractPersistHandler)):
            raise TypeError(f"The handler '{handler}' in package {module_name} could not be instanciated as a handler")
        return instance

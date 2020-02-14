import datetime
import jwt
import requests
import logging
import socket

from pythonjsonlogger.jsonlogger import JsonFormatter
from http.cookiejar import CookiePolicy
from wrapt import ObjectProxy
from http import HTTPStatus
from urllib.parse import urljoin, urlparse, parse_qs, ParseResult
from collections import defaultdict
from requests_toolbelt.adapters import host_header_ssl

from dli import __version__
from dli.analytics import AnalyticsHandler
from dli.siren import siren_to_entity
from dli.client.components.auto_reg_metadata import AutoRegMetadata
from dli.client.components.datafile import Datafile
from dli.client.components.dataset import Dataset, Dictionary
from dli.client.components.me import Me
from dli.client.components.package import Package
from dli.client.components.search import Search
from dli.client.components.accounts import Accounts
from dli.client.exceptions import (
    DatalakeException, InsufficientPrivilegesException,
    InvalidPayloadException, UnAuthorisedAccessException,
    CatalogueEntityNotFoundException, AuthenticationFailure
)

from dli.models import (
    DatasetModel, InstancesCollection as InstancesCollection_,
    InstanceModel, Paginator, FileModel, PackageModel, PackageModule,
    DictionaryModel, DatasetModule)

from dli.siren import PatchedSirenBuilder

class _Environment:

    _catalogue_accounts_environment_map = {
        'catalogue.datalake.ihsmarkit.com': 'accounts.datalake.ihsmarkit.com',
        'catalogue-uat.datalake.ihsmarkit.com': 'accounts-uat.datalake.ihsmarkit.com',
        'catalogue-uat2.datalake.ihsmarkit.com': 'accounts-uat2.datalake.ihsmarkit.com',
        'catalogue-dev.udpmarkit.net': 'accounts-dev.udpmarkit.net',
        'catalogue-qa.udpmarkit.net': 'accounts-qa.udpmarkit.net',
        'catalogue-qa2.udpmarkit.net': 'accounts-qa2.udpmarkit.net',
    }

    _catalogue_consumption_environment_map = {
        'catalogue.datalake.ihsmarkit.com': 'consumption.datalake.ihsmarkit.com',  # noqa
        'catalogue-uat.datalake.ihsmarkit.com': 'consumption-uat.datalake.ihsmarkit.com',  # noqa
        'catalogue-uat2.datalake.ihsmarkit.com': 'consumption-uat2.datalake.ihsmarkit.com',  # noqa
        'catalogue-dev.udpmarkit.net': 'consumption-dev.udpmarkit.net',  # noqa
        'catalogue-qa.udpmarkit.net': 'consumption-qa.udpmarkit.net',  # noqa
        'catalogue-qa2.udpmarkit.net': 'consumption-qa2.udpmarkit.net',  # noqa
    }

    def __init__(self, api_root):
        """
        Class to manage the different endpoints

        :param str root_url: The root url of the catalogue
        """
        catalogue_parse_result = urlparse(api_root)

        self.catalogue = ParseResult(
            catalogue_parse_result.scheme, catalogue_parse_result.netloc,
            '', '', '', ''
        ).geturl()

        accounts_host = self._catalogue_accounts_environment_map.get(
            catalogue_parse_result.netloc
        )

        self.accounts = ParseResult(
            catalogue_parse_result.scheme, accounts_host, '', '', '', ''
        ).geturl()


        consumption_host = self._catalogue_consumption_environment_map.get(
            catalogue_parse_result.netloc
        )

        self.consumption = ParseResult(
            'https', consumption_host, '', '', '', ''
        ).geturl()


class ModelDescriptor:

    def __init__(self, model_cls=None):
        self.model_cls = model_cls

    def __get__(self, instance, owner):
        """Returns a model thats bound to the client instance"""
        return type(
            self.model_cls.__name__, (self.model_cls, ),
            {
                '_client': instance
            }
        )


class DliClient(Accounts, AutoRegMetadata,
                Datafile, Dataset, Dictionary,
                Me, Package, Search):
    """
    Definition of a client. This client mixes in utility functions for
    manipulating packages, datasets and datafiles.
    """

    Dataset = ModelDescriptor(DatasetModel)
    Instance = ModelDescriptor(InstanceModel)
    _InstancesCollection = ModelDescriptor(InstancesCollection_)
    _Pagination = ModelDescriptor(Paginator)
    _File = ModelDescriptor(FileModel)
    _Package = ModelDescriptor(PackageModel)
    _DictionaryV2 = ModelDescriptor(DictionaryModel)

    _packages = ModelDescriptor(PackageModule)
    _datasets = ModelDescriptor(DatasetModule)

    _environment_class = _Environment
    _session = None
    logger = None

    def __init__(self, api_key, api_root, host=None, debug=False):
        self._environment = self._environment_class(api_root)
        self.api_key = api_key
        self.host = host
        self.debug = debug
        self._session = self._new_session()
        self._setup_logging()
        self._analytics_handler = AnalyticsHandler(self)
        self.logger.info(
            'Starting SDK session',
            extra={'jwt': self._session.decoded_token}
        )
        self.packages = self._packages()
        self.datasets = self._datasets()

    def _setup_logging(self):
        # In case there are multiple loggers
        self.logger = logging.getLogger('dli.client_{}'.format(
            self.api_key[:5]
        ))

        # If debug create a log file
        if self.debug:
            json_format = JsonFormatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler = logging.FileHandler(
                'sdk-{}-{}.log'.format(
                    self.api_key[:5],
                    datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
                )
            )

            file_handler.setFormatter(json_format)
            file_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(file_handler)
            self.logger.setLevel(logging.DEBUG)

    def _new_session(self):
        return Session(
            self.api_key,
            self._environment,
            self.host
        )

    @property
    def session(self):
        # if the session expired, then reauth
        # and create a new context
        if self._session.has_expired:
            self._session = self._new_session()
        return self._session


class Response(ObjectProxy):

    def __init__(self, wrapped, builder, *args, **kwargs):
        super(Response, self).__init__(wrapped, *args, **kwargs)
        self.builder = builder

    def to_siren(self):
        # Pypermedias terminology, not mine
        python_object = self.builder._construct_entity(
            self.json()
        ).as_python_object()

        # Keep the response availible
        python_object._raw_response = self

        return python_object

    def to_many_siren(self, relation):
        return [
            siren_to_entity(c) for c in
            self.to_siren().get_entities(rel=relation)
        ]


class BlockAll(CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


class DLIAdapter(host_header_ssl.HostHeaderSSLAdapter):

    def __init__(self, session, *args, **kwargs):
        self.session = session
        super().__init__(*args, **kwargs)

    def add_headers(self, request, **kwargs):
        request.headers["X-Data-Lake-SDK-Version"] = str(__version__)
        # if a host has been provided, then we need to set it on the header
        if self.session.host:
            request.headers['Host'] = self.session.host

        super().add_headers(request, **kwargs)


class DLIBearerAuthAdapter(DLIAdapter):
    def add_headers(self, request, **kwargs):
        super().add_headers(request, **kwargs)
        if self.session.auth_key and 'Authorization' not in request.headers:
            request.headers['Authorization'] = f'Bearer {self.session.auth_key}'


class DLISirenAdapter(DLIAdapter):
    def add_headers(self, request, **kwargs):
        super().add_headers(request, **kwargs)
        request.headers['Content-Type'] = "application/vnd.siren+json"


class DLICookieAuthAdapter(DLIAdapter):
    def add_headers(self, request, **kwargs):
        super().add_headers(request, **kwargs)
        # Accounts V1 authentication is broken, in that it only accepts
        # a cookie rather than an API key.
        request.headers['Cookie'] = f'oidc_id_token={self.session.auth_key}'


class DLIAccountsV1Adapter(DLISirenAdapter, DLICookieAuthAdapter):
    def add_headers(self, request, **kwargs):
        super().add_headers(request, **kwargs)


class DLIInterfaceV1Adapter(DLISirenAdapter, DLIBearerAuthAdapter):
    def add_headers(self, request, **kwargs):
        super().add_headers(request, **kwargs)


class Session(requests.Session):

    def __init__(
        self, api_key, environment, host, auth_key=None
    ):
        super().__init__()
        self.api_key = api_key
        self._environment = environment
        self.host = host
        self.siren_builder = PatchedSirenBuilder()
        self.auth_key = auth_key or self._get_auth_key()
        self.decoded_token = self._get_decoded_token()
        self.token_expires_on = self._get_expiration_date()

        self.mount(
            urljoin(self._environment.catalogue, '__api/'),
            DLIInterfaceV1Adapter(self)
        )

        self.mount(
            urljoin(self._environment.catalogue, '__api_v2/'),
            DLIBearerAuthAdapter(self)
        )

        self.mount(
            self._environment.consumption, DLIBearerAuthAdapter(self)
        )

        self.mount(
            urljoin(self._environment.accounts, '__api/'),
            DLIAccountsV1Adapter(self)
        )

        self.mount(
            urljoin(self._environment.accounts, '__api_v2/'),
            DLIBearerAuthAdapter(self)
        )

        self.mount(
            self._environment.consumption, DLIBearerAuthAdapter(self)
        )

        # Don't allow cookies to be set.
        # The new API will reject requests with both a cookie
        # and a auth header (as there's no predictiable crediential to choose).
        #
        # However the old API, once authenticate using a Bearer token will
        # as a side effect of a request return a oidc_id_token which matches
        # the auth header. This is ignored.
        self.cookies.set_policy(BlockAll())

    def request(self, method, url, *args, **kwargs):
        if not urlparse(url).netloc:
            url = urljoin(self._environment.catalogue, url)

        kwargs.pop('hooks', None)
        hooks = {'response': self._response_hook}

        try:
            return super().request(method, url, hooks=hooks, *args, **kwargs)
        except socket.error as e:
            raise ValueError(
                'Unable to process request due to a networking issue '
                'root cause could be a bad connection, '
                'not being on the correct VPN, '
                'or a network timeout '
            ) from e


    def _get_decoded_token(self):
        return jwt.decode(self.auth_key, verify=False)

    def _get_expiration_date(self):
        default_timeout = (
            datetime.datetime.utcnow() +
            datetime.timedelta(minutes=55)
        )

        if 'exp' not in self.decoded_token:
            return default_timeout

        return datetime.datetime.utcfromtimestamp(
            self.decoded_token['exp']
        ) - datetime.timedelta(minutes=5)

    @property
    def has_expired(self):
        # We subtract timedelta from the expiration time in order to allow a safety window for
        # a code block to execute after a check has been asserted.
        return datetime.datetime.utcnow() > (self.token_expires_on - datetime.timedelta(minutes=1))

    def _response_hook(self, response, *args, **kwargs):
        # Apologies for the ugly code. The startswith siren check
        # is to make this only relevant to the old API.
        response = Response(response, self.siren_builder)

        if not response.ok:
            exceptions = defaultdict(
                lambda: DatalakeException,
                {HTTPStatus.BAD_REQUEST: InvalidPayloadException,
                 HTTPStatus.UNPROCESSABLE_ENTITY: InvalidPayloadException,
                 HTTPStatus.UNAUTHORIZED: UnAuthorisedAccessException,
                 HTTPStatus.FORBIDDEN: InsufficientPrivilegesException,
                 HTTPStatus.NOT_FOUND: CatalogueEntityNotFoundException}
            )

            try:
                message = response.json()
            except ValueError:
                message = response.text

            raise exceptions[response.status_code](
                message=message,
                params=parse_qs(urlparse(response.request.url).query),
                response=response
            )

        return response

    def _get_auth_key(self):
        try:
            response = self.post(
                '/__api/start-session', headers={
                    'Authorization': 'Bearer {}'.format(self.api_key)
                }
            )
        except DatalakeException as e:
            raise AuthenticationFailure(
                message='Could not authenticate API key'
            ) from e

        return response.text

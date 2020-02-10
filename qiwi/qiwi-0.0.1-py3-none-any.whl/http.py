import asyncio
import sys
import json

from typing import Optional, Union, Tuple, Dict

__version__ = '0.0.1'

from urllib.parse import quote

import aiohttp

from senum import Enum

from yarl import URL

from . import utils
from datetime import datetime

from aiohttp import ContentTypeError, BasicAuth


class HTTPMethod(Enum):
    OPTIONS = 'OPTIONS'
    GET = 'GET'
    HEAD = 'HEAD'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    TRACE = 'TRACE'
    CONNECT = 'CONNECT'


class BaseRoute:
    __slots__ = ('_method', '_path', '_url')

    BASE_URL = None

    def __init__(self, method: HTTPMethod, path, **parameters):
        self._method = method
        self._path = path

        if self.BASE_URL is None:
            raise NotImplemented

        self._url = (self.BASE_URL + path).format(
            **{k: quote(v) if isinstance(v, str) else v for k, v in parameters.items()}
        ) if parameters else self.BASE_URL + path

    @property
    def method(self) -> HTTPMethod:
        return self._method

    @property
    def path(self) -> str:
        return self._path

    @property
    def url(self) -> str:
        return self._url


class EdgeRoute(BaseRoute):
    BASE_URL = 'https://edge.qiwi.com/'


class HTTPClient:
    __slots__ = ('_connector', '_token', '_loop', '_session', '_proxy',
                 '_proxy_auth', '_user_agent'
                 )

    def __init__(
            self,
            token: str,
            connector: aiohttp.BaseConnector,
            *,
            proxy: Optional[Union[str, URL]] = None,
            proxy_auth: Optional[BasicAuth] = None,
            loop: Optional[asyncio.AbstractEventLoop] = None
    ):
        self._token = token
        self._connector = connector
        self._loop = loop or asyncio.get_event_loop()
        self._session: Optional[aiohttp.ClientSession] = None

        self._proxy = proxy
        self._proxy_auth = proxy_auth

        self._user_agent = f"AsyncQiwi/{__version__} (https://github.com/xxxcrystalcastles/asyncqiwipy) " \
                           f"Python/{'.'.join(map(str, sys.version_info[0:3]))} aiohttp/{aiohttp.__version__}"

    @property
    def token(self) -> Optional[str]:
        return self._token

    @property
    def proxy(self) -> Optional[Union[str, URL]]:
        return self._proxy

    @proxy.setter
    def proxy(self, proxy: Optional[Union[str, URL]]) -> None:
        self._proxy = proxy

    @property
    def proxy_auth(self) -> Optional[BasicAuth]:
        return self._proxy_auth

    @proxy_auth.setter
    def proxy_auth(self, proxy_auth: Optional[BasicAuth]) -> None:
        self._proxy_auth = proxy_auth

    def recreate(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(connector=self._connector, loop=self._loop)

    async def request(self, route: BaseRoute, **kwargs):
        method = route.method.value
        url = route.url

        headers = {
            'User-Agent': self._user_agent,
            'Accept': '*/*',
            'Content-Type': 'application/json'
        }

        if self._token is not None:
            headers['Authorization'] = f'Bearer {self._token}'

        if 'params' in kwargs:
            kwargs['params'] = utils.resolve_params(kwargs.pop('params'))

        if 'json' in kwargs:
            kwargs['data'] = utils.to_json(kwargs.pop('json'))

        if 'proxy' not in kwargs:
            kwargs['proxy'] = self._proxy

        if 'proxy_auth' not in kwargs:
            kwargs['proxy_auth'] = self._proxy_auth

        async with self._session.request(method, url, headers=headers, **kwargs) as r:
            print(r.real_url)
            try:
                data = await r.json()

            except ContentTypeError:
                data = await r.read()

            return data

    async def close(self):
        if self._session is not None and not self._session.closed:
            await self._session.close()

    async def get_profile(self, auth_info: bool = True, contract_info: bool = True, user_info: bool = True):
        params = {
            'authInfoEnabled': auth_info,
            'contractInfoEnabled': contract_info,
            'userInfoEnabled': user_info
        }

        route = EdgeRoute(HTTPMethod.GET, '/person-profile/v1/profile/current')

        return await self.request(route, params=params)

    async def send_identification_data(self, wallet: Union[int, str],
                                       birth_date: str, first_name: str, middle_name: str, last_name: str,
                                       passport: str, inn: str, snils: str, oms: str):
        params = {
            'birthDate': birth_date,
            'firstName': first_name,
            'middleName': middle_name,
            'lastName': last_name,
            'passport': passport,
            'inn': inn,
            'snils': snils,
            'oms': oms
        }

        route = EdgeRoute(
            HTTPMethod.GET, '/identification/v1/persons/{wallet}/identification', wallet=wallet)

        return await self.request(route, params=params)

    async def get_identification_data(self, wallet: Union[int, str]):
        route = EdgeRoute(
            HTTPMethod.GET, '/identification/v1/persons/{wallet}/identification', wallet=wallet)

        return await self.request(route)

    async def payments_list(self, wallet: Union[int, str],
                            rows: int, operation: str = 'ALL', sources: Tuple[str] = None,
                            start_data: Optional[datetime] = None, end_date: Optional[datetime] = None,
                            next_tx_date: Optional[datetime] = None, next_tx_id: Optional[datetime] = None):
        params = {
            'rows': rows,
            'operation': operation,
            'sources': sources,
            'startDate': start_data,
            'endDate': end_date,
            'nextTxnDate': next_tx_date,
            'nextTxnId': next_tx_id,
        }

        route = EdgeRoute(
            HTTPMethod.GET, '/payment-history/v2/persons/{wallet}/payments', wallet=wallet)

        return await self.request(route, params=params)

    async def payments_stat(self, wallet: Union[int, str],
                            start_data: Optional[datetime] = None, end_date: Optional[datetime] = None,
                            operation: str = 'ALL', sources: Tuple[str] = None):
        params = {
            'startDate': start_data,
            'endDate': end_date,
            'operation': operation,
            'sources': sources,
        }

        route = EdgeRoute(
            HTTPMethod.GET, '/payment-history/v2/persons/{wallet}/payments/total', wallet=wallet)

        return await self.request(route, params=params)

    async def transaction_information(self, transaction_id: int, operation_type: str = None):
        params = {
            'type': operation_type,
        }

        route = EdgeRoute(
            HTTPMethod.GET, '/payment-history/v2/transactions/{transaction_id}',
            transaction_id=transaction_id)

        return await self.request(route, params=params)

    async def payment_receipt(self, transaction_id: int, operation_type: str, file_format: str):
        params = {
            'type': operation_type,
            'format': file_format
        }

        route = EdgeRoute(
            HTTPMethod.GET, '/payment-history/v1/transactions/{transaction_id}/cheque/file',
            transaction_id=transaction_id)

        return await self.request(route, params=params)

    async def accounts_list(self, person_id: int):
        route = EdgeRoute(
            HTTPMethod.GET, '/funding-sources/v2/persons/{person_id}/accounts', person_id=person_id)

        return await self.request(route)

    async def create_an_account(self, person_id: int, alias: str):
        payload = {
            'alias': alias
        }

        route = EdgeRoute(
            HTTPMethod.POST, '/funding-sources/v2/persons/{person_id}/accounts', person_id=person_id)

        return await self.request(route, json=payload)

    async def creatable_accounts_list(self, person_id: int):
        route = EdgeRoute(
            HTTPMethod.GET, '/funding-sources/v2/persons/{person_id}/accounts/offer', person_id=person_id)

        return await self.request(route)

    async def set_default_balance(self, person_id: int, account_alias: str, default_account: bool):
        payload = {
            'defaultAccount': default_account
        }

        route = EdgeRoute(
            HTTPMethod.PATCH, '/funding-sources/v2/persons/{person_id}/accounts/{account_alias}',
            person_id=person_id, account_alias=account_alias)

        return await self.request(route, json=payload)

    async def commission_rates(self, provider_id: int, account: Union[int, str],
                               payment_method_type: str, payment_method_account_id: int,
                               amount: int, currency: str):
        payload = {
            'account': account,
            'paymentMethod': {
                'type': payment_method_type,
                'accountId': payment_method_account_id,
            },
            'purchaseTotals': {
                'total': {
                    'amount': amount,
                    'currency': currency
                }
            }
        }

        route = EdgeRoute(
            HTTPMethod.POST, '/sinap/providers/{provider_id}/onlineCommission', provider_id=provider_id)

        return await self.request(route, json=payload)

    async def transfer_funds(self, provider_id: int, **payload):
        # The same with conversion

        payload['id'] = utils.generate_tx_id()

        route = EdgeRoute(
            HTTPMethod.POST, '/sinap/api/v2/terms/{provider_id}/payments', provider_id=provider_id)

        return await self.request(route, json=payload)

    async def conversion_rates(self):
        route = EdgeRoute(
            HTTPMethod.GET, '/sinap/crossRates')

        return await self.request(route)

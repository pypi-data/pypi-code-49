import asyncio
import inspect
import sys
from itertools import groupby

from asyncqiwi import currencies
from pprint import pprint
from typing import Optional, Dict, Type, List, Union

import aiohttp

from .currencies import try_currency, _Currency as Currency
from .http import HTTPClient
from .http import EdgeRoute, HTTPMethod


class Qiwi:
    def __init__(self, token, connector=None, loop=None):
        self._token = token
        self._loop = loop or asyncio.get_event_loop()
        self._http = HTTPClient(token, connector, loop=loop)
        self._profile: Optional[Dict] = None

    async def profile(self):
        return await self._http.get_profile()

    async def dostup(self):
        if self._profile is None:
            self._profile = await self.profile()

        personId = self._profile['authInfo']['personId']

        return await self._http.request(
            EdgeRoute(HTTPMethod.GET, f'/funding-sources/v2/persons/{personId}/accounts/offer'))

    async def course(self):
        return await self._http.request(EdgeRoute(HTTPMethod.GET, f'/sinap/crossRates'))

    async def balance(self):
        if self._profile is None:
            self._profile = await self.profile()

        personId = self._profile['authInfo']['personId']

        result = await self._http.request(EdgeRoute(HTTPMethod.GET, f'/funding-sources/v2/persons/{personId}/accounts'))

        return result

        balances = result['accounts']

        return [currencies.currency(code, amount) for amount, code in
                (balance['balance'].values() for balance in balances)]

    @classmethod
    async def login(cls, token: str, connector=None, loop=None):
        pass

    async def conversion_rates(self,
                               amount: Union[int, float] = 1,
                               from_currency: Optional[Type[Currency]] = None,
                               to_currency: Optional[Type[Currency]] = None,
                               ) -> Union[Dict[Currency, List[Currency]], List[Currency], Currency]:

        dirty_rates: Dict = await self._http.conversion_rates()

        rates = groupby(
            (
                {
                    k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in d.items()
                } for d in dirty_rates.pop('result')
            ),
            lambda d: d['from']
        )

        constructed_currencies = {
            try_currency(code, amount): [
                try_currency(rate['to'], amount / rate['rate']) for rate in group
            ] for code, group in rates
        }

        if from_currency is None:
            return constructed_currencies

        filtered_currencies = constructed_currencies.get(from_currency(amount))

        if to_currency is None:
            return filtered_currencies

        for currency in filtered_currencies:
            if currency.code == to_currency.code:
                return currency

        raise Exception

    async def convert(self,
                      from_currency: Currency,
                      to_currency: Currency,
                      comment: Optional[str] = None):
        provider_id = 99
        payload = {
            'sum': {
                'amount': to_currency.amount,
                'currency': to_currency.code,
            },
            'paymentMethod': {
                'type': 'Account',
                'accountId': from_currency.code,
            },
            'fields': {
                'account': 79260574395
            }
        }
        if comment is not None:
            payload['comment'] = comment

        return await self._http.transfer_funds(provider_id, **payload)

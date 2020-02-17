import os

from .exceptions import BelvoAPIException
from .http import APISession
from .resources import Accounts, Institutions, Invoices, Links, Owners, TaxReturns, Transactions


class Client:
    def __init__(self, secret_key_id: str, secret_key_password: str, url: str = None) -> None:
        if url is None:
            url = os.getenv("BELVO_API_URL")

        if not url:
            raise BelvoAPIException("You need to provide a URL.")

        self.session = APISession(url)

        if not self.session.login(secret_key_id, secret_key_password):
            raise BelvoAPIException("Login failed.")

        self._links = Links(self.session)
        self._accounts = Accounts(self.session)
        self._transactions = Transactions(self.session)
        self._institutions = Institutions(self.session)
        self._owners = Owners(self.session)
        self._invoices = Invoices(self.session)
        self._tax_returns = TaxReturns(self.session)

    @property
    def Links(self):
        return self._links

    @property
    def Accounts(self):
        return self._accounts

    @property
    def Transactions(self):
        return self._transactions

    @property
    def Institutions(self):
        return self._institutions

    @property
    def Owners(self):
        return self._owners

    @property
    def Invoices(self):
        return self._invoices

    @property
    def TaxReturns(self):
        return self._tax_returns

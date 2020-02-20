from .http_base import HttpClientBase

API_URL = 'https://api.forpay.pro'


def get_url(symbol_url):
    return '{}{}'.format(API_URL, symbol_url)


class ForPayClient(HttpClientBase):
    def get_currencies(self, currency_id=None):
        query_dict = None

        if type(currency_id) != int and currency_id:
            raise TypeError('currency_id\'s type must be int')

        if currency_id:
            query_dict = {"currency_id": currency_id}

        reply, err = self._http_get(get_url('/v1/currencies'), query_dict=query_dict)
        return reply, err

    def sync_user_info(self, user_id: str):
        body_dict = {"user_id": user_id}

        reply, err = self._http_post(get_url('/v1/user_info'), body_dict=body_dict)
        return reply, err

    def get_balance(self, wallet_id: str, currency_id=None):
        # currency_id can be None, otherwise should be given as Type[int]
        query_dict = {"wallet_id": wallet_id}

        if type(currency_id) != int and currency_id:
            raise TypeError('currency_id\'s type must be int')

        if currency_id:
            query_dict.update({"currency_id": currency_id})

        reply, err = self._http_get(get_url('/v1/balance'), query_dict=query_dict)
        return reply, err

    def withdraw(self, wallet_id: str, currency_id: int, client_token: str, amount: str, address: str):
        if float(amount) <= 0:
            raise ValueError('amount\'s value should be greater than 0')

        body_dict = {
            "client_token": client_token,
            "wallet_id": wallet_id,
            "currency_id": currency_id,
            "amount": amount,
            "address": address
        }

        reply, err = self._http_post(get_url('/v1/withdraw'), body_dict=body_dict)
        return reply, err

    def deposit(self, wallet_id: str, currency_id: int, amount: str, client_token: str):
        if float(amount) <= 0:
            raise ValueError('amount\'s value should be greater than 0')

        body_dict = {
            "wallet_id": wallet_id,
            "currency_id": currency_id,
            "amount": amount,
            "client_token": client_token,
        }

        reply, err = self._http_post(get_url('/v1/deposit'), body_dict=body_dict)
        return reply, err

    def deduction(self, wallet_id: str, currency_id: int, amount: str, client_token: str):
        if float(amount) >= 0:
            raise ValueError('amount\'s value should be less than 0')

        body_dict = {
            "wallet_id": wallet_id,
            "currency_id": currency_id,
            "amount": amount,
            "client_token": client_token,
        }

        reply, err = self._http_post(get_url('/v1/deduction'), body_dict=body_dict)
        return reply, err

from .http_base import HttpClientBase

API_URL = 'https://api.forpay.pro'


def get_url(symbol_url):
    return '{}{}'.format(API_URL, symbol_url)


class ForPayClient(HttpClientBase):
    def get_currencies(self, currency_id=None):
        query_dict = None
        if currency_id:
            query_dict = {"currency_id": currency_id}

        reply, err = self._http_get(get_url('/v1/currencies'), query_dict=query_dict)
        return reply, err

    def sync_user_info(self, user_id):
        body_dict = {"user_id": user_id}
        reply, err = self._http_post(get_url('/v1/user_info'), body_dict=body_dict)
        return reply, err

    def get_balance(self, wallet_id, currency_id):
        query_dict = {"wallet_id": wallet_id}
        if currency_id:
            query_dict.update({"currency_id": currency_id})
        reply, err = self._http_get(get_url('/v1/balance'), query_dict=query_dict)
        return reply, err

    def withdraw(self, client_token, wallet_id, currency_id, amount, address):
        body_dict = {
            "client_token": client_token,
            "wallet_id": wallet_id,
            "currency_id": currency_id,
            "amount": amount,
            "address": address
        }
        reply, err = self._http_post(get_url('/v1/withdraw'), body_dict=body_dict)
        return reply, err

    def deposit(self, wallet_id, currency_id, amount, client_token):
        body_dict = {
            "wallet_id": wallet_id,
            "currency_id": currency_id,
            "amount": amount,
            "client_token": client_token,
        }
        reply, err = self._http_post(get_url('/v1/deposit'), body_dict=body_dict)
        return reply, err

    # def cancel_withdraw(self, transaction_id):
    #     body_dict = {
    #         "transaction_id": transaction_id
    #     }
    #     reply, err = self._http_post(get_url('/v1/withdraw/cancel'), body_dict=body_dict)
    #     return reply, err

# coding: utf-8
from broker.base import Request


class FinanceSupportClient(Request):

    def new_order(self, client_order_id, org_id, account_id, symbol, quantity, price, order_side, order_type):
        params = {
            'clientOrderId': client_order_id,
            'orgId': org_id,
            'accountId': account_id,
            'symbol': symbol,
            'side': order_side,
            'type': order_type,
            'quantity': quantity,
            'price': price
        }
        return self._post('finance_support/order', signed=True, params=params, version=None)

    def cancel_order(self, org_id, account_id, order_id='', client_order_id=''):
        params = {
            'orgId': org_id,
            'accountId': account_id,
            'orderId': order_id,
            'clientOrderId': client_order_id
        }
        return self._delete('finance_support/order', signed=True, params=params, version=None)

    def query_order(self, org_id, account_id, order_id='', client_order_id=''):
        params = {
            'orgId': org_id,
            'accountId': account_id,
            'orderId': order_id,
            'clientOrderId': client_order_id
        }
        return self._get('finance_support/order', signed=True, params=params, version=None)

    def get_account_info(self, org_id, account_id):
        params = {
            'orgId': org_id,
            'accountId': account_id
        }
        return self._get('finance_support/account', signed=True, params=params, version=None)

    def create_finance_account(self, org_id):
        params = {
            'orgId': org_id,
        }
        return self._post('finance_support/account', signed=True, params=params, version=None)

    def get_all_finance_accounts(self):
        return self._get('finance_support/accounts', signed=True, params={}, version=None)

    def transfer(self, source_account_id, source_org_id, target_account_id, target_org_id, amount, token_id):
        params = {
            'sourceAccountId': source_account_id,
            'sourceOrgId': source_org_id,
            'targetAccountId': target_account_id,
            'targetOrgId': target_org_id,
            'amount': amount,
            'tokenId': token_id
        }
        return self._post('finance_support/transfer', signed=True, params=params, version=None)


if __name__ == '__main__':
    proxies = {
        "http": '',
        "https": '',
    }
    entry_point = 'https://www.bhex.us/openapi'  # enter your open api entry point
    f = FinanceSupportClient(entry_point,
                             api_key='J3UcHs0mbnMVlBCZLbyGHJsAUI4nfAdspmFaUcz19U42R4AnffXrfX9Jl2fbIgpd',
                             secret='cB0fec8tUk18K3gvpU7387ZJZ4od9NYZbLU4lTJ8HROjku3VSlQgG5bix5BvA6F8',
                             proxies=proxies)
    print(f.get_account_info('6001', '483871630655843584'))

    print(f.get_all_finance_accounts())


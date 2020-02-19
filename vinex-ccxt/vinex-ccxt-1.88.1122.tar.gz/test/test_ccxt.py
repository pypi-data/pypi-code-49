# biki = ccxt.biki()


# biki = ccxt.biki({
#     'apiKey': api_key,
#     'secret': secret,
# })


# for i in range(100):
#     print(biki.fetch_balance().keys())

#
# import os
# import sys
#
#
# # if '__file__' in locals():
# #     BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# #     sys.path.append(BASE_DIR)
# # else:
# sys.path.append('/home/cuongtran/Dev/Python/01-scripts/03-tradebot')
#
# import config_tradebot as config
#
#
# vinex_api = ccxt.vinex(config.api_key['vinex-mm'])
#
# # trades = vinex_api.fetch_my_trades('BTC/USDT', limit=1000000)
# #
# # for trade in trades:
# #     if trade['info']['id'] == 1001092:
# #         print(trade)
# #
# # print(len(trades))
#
# # open_orders = vinex_api.fetch_open_orders('BTC/USDT')
# # print(open_orders)
#
#
# from ccxt.base.errors import OrderNotFound
#
# try:
#     vinex_api.cancel_order(id='anmuifjtcpp8j7bwpk3eamd4t', symbol='BTC/USDT')
# except OrderNotFound as e:
#     print('Order not found')
# except Exception as e:
#     print(e)
#
# vinex_api.fetch_open_orders(limit=1)
#
#
#
#
#
# vinex_api = ccxt.vinex({
#     'proxies': [{
#         'http': 'http://74.126.186.217:5975',
#         'https': 'http://74.126.186.217:5975',
#     }],
# })
#
# vinex_api.urls
#
# vinex_api.urls['api']  = 'https://dev-backend.vinex.network/api/v2'
#
#
# print(vinex_api.fetch_ticker('BTC/USDT'))


# probit_api = ccxt.probit({
#     'proxies': [{
#         'http': 'http://74.126.186.217:5975',
#         'https': 'http://74.126.186.217:5975',
#     }],
# })

# print(probit_api.fetch_ticker('BTC/USDT'))


# import ccxt
#
# user = 'midas'
# password = '21BQG0Z736U7LV24QBY6ENEV'
#
# proxy_path = '196.240.249.5:13555'
#
# http_proxy = f'http://{user}:{password}@{proxy_path}'
#
# proxies = list()
#
# proxies.append({
#     "http": http_proxy,
#     "https": http_proxy,
# })
#
# api = ccxt.vinex({'proxies': proxies})
#
# api.fetch_ticker('BTC/USDT')

# ######################################################

import time

import config

import ccxt

exchange_ids = [
    'whitebit',
    # 'vinex',
]


def test_public_api():
    print('>>>>>>>>>>>> Test public API <<<<<<<<<<<<')

    for exchange_id in exchange_ids:
        exchange_class = getattr(ccxt, exchange_id)

        api = exchange_class()

        print(f'>>> Test exchange: {exchange_id}')

        # 1. Markets
        # print(f"- Markets: {api.fetch_markets()}")

        # 2. Ticker
        # print(f"- Ticker: {api.fetch_ticker('BTC/USDT')}")

        # 3. Order book
        # order_book = api.fetch_order_book('BTC/USDT')
        # print(f"- Order Book: len={len(order_book)}, order_book={order_book}")

        # 4. Trades
        # trades = api.fetch_trades('BTC/USDT')
        # print(f"- Trades: len={len(trades)}, trades={trades}")


def test_private_api():
    print('>>>>>>>>>>>> Test private API <<<<<<<<<<<<')

    for exchange_id in exchange_ids:
        exchange_class = getattr(ccxt, exchange_id)

        # api = exchange_class()

        api_key = config.api_key['whitebit-dev']

        api = exchange_class({
            'apiKey': api_key['apiKey'],
            'secret': api_key['secret'],
        })

        print(f'>>> Test exchange: {exchange_id}')

        # symbol = 'BTC/USDT'
        symbol = 'XST/BTC'

        # 1. Balances
        # balances = api.fetch_balance()['XST']
        # print(f'- Balances: {balances}')

        # 2. List Orders
        # open_orders = api.fetch_open_orders(symbol)
        # print(f'- Open Orders: len={len(open_orders)}, orders={open_orders}')

        # # closed_orders = api.fetch_closed_orders(symbol, since=int(time.time() * 1000))
        # # closed_orders = api.fetch_closed_orders(symbol, limit=1)
        # closed_orders = api.fetch_closed_orders(symbol)
        # print(f'- Open Orders: len={len(closed_orders)}, orders={closed_orders}')

        # # orders = api.fetch_orders()         # Some exchange don't support get orders for all markets
        # orders = api.fetch_orders(symbol)
        # print(f'- Orders: len={len(orders)}, orders={orders}')


        # 2. Create Order
        # order = api.create_order(symbol, 'limit', 'sell', 1, 100)
        # print(f'- Order: {order}')

        # 3. Cancel Order
        order = api.cancel_order(id=193106610, symbol=symbol)
        print(f'- Order: {order}')


if __name__ == '__main__':
    # test_public_api()

    test_private_api()

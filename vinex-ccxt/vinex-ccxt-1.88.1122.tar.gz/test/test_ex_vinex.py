import ccxt
import config

# exchange_id = 'vinex'
# exchange_class = getattr(ccxt, exchange_id)

api = ccxt.vinex()
print(api.fetch_ticker('BTC/USDT'))


api = ccxt.vinex(config.api_key['vinex-test'])

# api.create_order(symbol, 'limit', 'sell', amount, price)
symbol = 'BTC/USDT'
amount = 1
price = 10000

api.create_order(symbol, 'limit', 'sell', amount, price)

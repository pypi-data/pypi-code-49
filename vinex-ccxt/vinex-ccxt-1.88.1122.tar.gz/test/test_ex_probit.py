import ccxt
import config
import time

###############################
# Public
###############################
# api = ccxt.probit()
# print(api.fetch_ticker('BTC/USDT'))


###############################
# Private
###############################
api = ccxt.probit(config.api_key['probit-midas'])

for i in range(20):

    print(f'>>> Turn {i}:', api.fetch_balance())

    time.sleep(1*60)


# # api.create_order(symbol, 'limit', 'sell', amount, price)
# symbol = 'BTC/USDT'
# amount = 1
# price = 10000
#
# api.create_order(symbol, 'limit', 'sell', amount, price)

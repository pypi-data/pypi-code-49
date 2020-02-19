import ccxt

exchange_id = 'vinex'
exchange_class = getattr(ccxt, exchange_id)
print(exchange_class)

vinex = ccxt.vinex()
print(vinex.fetch_ticker('BTC/USDT'))

whitebit = ccxt.whitebit({
    'apiKey': '0c4a235d014e26422894007025f7d9d5',
    'secret': '8d5200182647a76f424e3e2b73eaf703',
})
# print(whitebit.fetch_markets('BTC/USDT'))
symbol = 'BTC/USDT'  # bitcoin contract according to https://github.com/ccxt/ccxt/wiki/Manual#symbols-and-market-ids
type = ''  # or 'Market', or 'Stop' or 'StopLimit'
side = 'sell'  # or 'buy'
amount = 1.0
price = 10000.0  # or None

# extra params and overrides
params = {
    # 'stopPx': 6000.0,  # if needed
}
id = 1000000
# print(whitebit.cancel_order(id,symbol))
print(whitebit.fetch_balance('BTC'))
# print(whitebit.create_order(symbol, type, side, amount, price, params))
# print(whitebit.fetch_balance())



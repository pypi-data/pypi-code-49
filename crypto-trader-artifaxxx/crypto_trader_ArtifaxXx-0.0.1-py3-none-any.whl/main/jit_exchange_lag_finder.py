import asyncio
import ccxt.async_support as ccxt
import time
import os
import sys
from pprint import pprint
import statistics as st
import logging

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

MAIN_EXCHANGES = [
    'binance', 'bitfinex', 'bittrex', 'hitbtc', 'kraken', 'kucoin', 'poloniex', 'bigone', 'gateio', 'bitmart',
]
MAIN_PAIRS = [
    'ETH/BTC',
    'LTC/BTC',
    'XRP/BTC',
    # 'ETC/BTC',
]
S_JIT_THRESHOLD = 0.002
REFRESH_RATE = 15
DEFAULT_FEE = 0.0007
DEFAULT_VOLUME = 5

'''
exchange_markers = 
['_1btcxe', 'acx', 'adara', 'allcoin', 'anxpro', 'bcex', 'bequant', 'bibox', 'bigone', 'binance', 'binanceje', 
 'binanceus', 'bit2c', 'bitbank', 'bitbay', 'bitfinex', 'bitfinex2', 'bitflyer', 'bitforex', 'bithumb', 'bitkk', 
 'bitlish', 'bitmart', 'bitmax', 'bitmex', 'bitso', 'bitstamp', 'bitstamp1', 'bittrex', 'bitz', 'bl3p', 'bleutrade', 
 'braziliex', 'btcalpha', 'btcbox', 'btcchina', 'btcmarkets', 'btctradeim', 'btctradeua', 'btcturk', 'buda', 
 'bytetrade', 'cex', 'chilebit', 'cobinhood', 'coinbase', 'coinbaseprime', 'coinbasepro', 'coincheck', 'coinegg', 
 'coinex', 'coinexchange', 'coinfalcon', 'coinfloor', 'coingi', 'coinmarketcap', 'coinmate', 'coinone', 'coinspot', 
 'cointiger', 'coolcoin', 'coss', 'crex24', 'deribit', 'digifinex', 'dsx', 'dx', 'exmo', 'exx', 'fcoin', 'fcoinjp', 
 'flowbtc', 'foxbit', 'fybse', 'gateio', 'gemini', 'hitbtc', 'hitbtc2', 'huobipro', 'huobiru', 'ice3x', 'idex', 
 'independentreserve', 'indodax', 'itbit', 'kkex', 'kraken', 'kucoin', 'kucoin2', 'kuna', 'lakebtc', 'latoken', 
 'lbank', 'liquid', 'livecoin', 'luno', 'lykke', 'mandala', 'mercado', 'mixcoins', 'negociecoins', 'oceanex', 
 'okcoincny', 'okcoinusd', 'okex', 'okex3', 'paymium', 'poloniex', 'rightbtc', 'southxchange', 'stronghold', 
 'surbitcoin', 'theocean', 'therock', 'tidebit', 'tidex', 'upbit', 'vaultoro', 'vbtc', 'virwox', 'whitebit', 
 'xbtce', 'yobit', 'zaif', 'zb']
'''


async def async_client(exchange, pairs):
    client = getattr(ccxt, exchange)()
    tickers = await client.fetch_tickers(pairs)
    await client.close()
    return {exchange: tickers}


async def multi_tickers(exchanges, pairs):
    input_coroutines = [async_client(exchange, pairs) for exchange in exchanges]
    tickers = await asyncio.gather(*input_coroutines, return_exceptions=True)
    return tickers


def build_matrix(tickers, time=0):
    """
    [pair, exchange, time, ask, bid, last]
    """
    result = []
    for ticker in tickers:
        exchange = [x for x in ticker.keys()][0]
        for pair in MAIN_PAIRS:
            ask = ticker[exchange][pair]['ask']
            bid = ticker[exchange][pair]['bid']
            last = ticker[exchange][pair]['last']
            result.append([pair, exchange, time, ask, bid, last])
    return sorted(result, key=lambda x: x[0])


def stupid_jit_predictor(matrix):
    # analyze deviation
    prediction_pair_list = []
    for pair in MAIN_PAIRS:
        prediction_dict = {'pair': pair}
        last_orders = [x[5] for x in matrix if x[0] == pair]
        prediction_dict['mean'] = st.mean(last_orders)
        prediction_dict['median'] = st.median(last_orders)
        prediction_dict['r_deviation'] = st.stdev(last_orders) / st.median(last_orders)
        prediction_dict['best_candidate_value'] = max(last_orders, key=lambda x: abs(x-st.median(last_orders)))
        prediction_dict['best_candidate_exchange'] = [x[1] for x in matrix if x[5] == prediction_dict['best_candidate_value']][0]
        prediction_dict['best_candidate_ask'] = [x[3] for x in matrix if x[5] == prediction_dict['best_candidate_value']][0]
        prediction_dict['best_candidate_bid'] = [x[4] for x in matrix if x[5] == prediction_dict['best_candidate_value']][0]
        prediction_dict['best_candidate_diff'] = prediction_dict['best_candidate_value'] - prediction_dict['median']
        if prediction_dict['best_candidate_diff'] > 0:  # sell here
            instant_price = prediction_dict['best_candidate_bid']
        else:
            instant_price = prediction_dict['best_candidate_ask']
        potential_profit = abs(instant_price - prediction_dict['best_candidate_value']) - DEFAULT_FEE*2
        prediction_dict['potential_profit'] = potential_profit

        prediction_pair_list.append(prediction_dict)
    return prediction_pair_list


if __name__ == '__main__':
    cycles = 0
    cycle_orders = 0
    r_profit_stats = {}
    for pair in MAIN_PAIRS:
        r_profit_stats[pair] = []

    while cycles < 100:
        tic = time.time()
        tickers = asyncio.get_event_loop().run_until_complete(multi_tickers(MAIN_EXCHANGES, MAIN_PAIRS))
        elapsed = time.time() - tic
        print("Cycle %d async call took: %s" % (cycles, elapsed))
        logging.info("Cycle %d async call took: %s" % (cycles, elapsed))
        logging.info("modified---------------------")
        print("testing new code deployment")
        matrix = build_matrix(tickers)
        res = stupid_jit_predictor(matrix)
        for pair in res:
            if pair['potential_profit'] > 0:
                cycle_orders += 1
                pprint(pair)
                print("%s: Potential Profit: %s" % (pair['pair'], pair['potential_profit']))
                r_profit_stats[pair['pair']].append(pair['potential_profit'])
        cycles += 1
        time.sleep(abs(REFRESH_RATE - elapsed))
    print("Cycle orders: %d" % cycle_orders)
    for pair in MAIN_PAIRS:
        print("%s______________" % pair)
        print("Deviation max: %f" % max(r_profit_stats[pair]))
        print("Deviation avr: %f" % st.mean(r_profit_stats[pair]))


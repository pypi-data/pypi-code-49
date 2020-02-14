from copy import deepcopy
import ccxt


DEPOSIT = 1000  # Money we have in the account
COMMISSION = 0.001  # Fixed exchange commission
BOT_STEP = 0.01  # Casino bot step to create next buy order
INITIAL_COMMITMENT = 1  # Initial bot order size
PROFIT_GAP = 0.01  # Initial profit gap
# Down 10
SCENARIO1_PRICE_LIST = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
# Up 10
SCENARIO2_PRICE_LIST = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
# Down 10 up 10
SCENARIO3_PRICE_LIST = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
# Down 10 up 11
SCENARIO4_PRICE_LIST = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]


def get_binance_history_data(resolution, ticker):

    binance = ccxt.binance()
    if binance.has['fetchOHLCV']:
        candle_close_prices = [x[4] for x in binance.fetch_ohlcv(ticker, resolution)]
        # print(candle_close_prices)
        print("For %s with step = %s we got %s results" % (ticker, resolution, len(candle_close_prices)))
        return candle_close_prices

        # print([datetime.datetime.fromtimestamp(x[5] / 1000.0).strftime("%m/%d/%Y, %H:%M:%S")
        #        for x in binance.fetch_ohlcv('TRX/BNB', resolution)])  # one day


def buy_with_sl(price_list, deposit):
    # buy at arrival
    tokens = (deposit - deposit*COMMISSION) / price_list[0]

    # sell at the end
    base = price_list[-1] * tokens * (1 - COMMISSION)
    return base - deposit


def casino_bot_cycle(price_list, deposit, step, initial_commitment, profit_gap):
    # initial order
    last_order_start_price = price_list[0]
    current_commitment = initial_commitment
    tokens = (initial_commitment - initial_commitment*COMMISSION) / price_list[0]
    deposit -= initial_commitment
    cycle_sell_price = price_list[0]*(1+profit_gap)

    for index, cur_price in enumerate(price_list[1:]):

        # Sell and close cycle
        if cur_price >= cycle_sell_price:
            deposit += cur_price*tokens - cur_price*tokens*COMMISSION
            return deposit, 0, index + 1

        # Threshold surpassed, make new buy order
        elif cur_price <= last_order_start_price * (1-step):
            last_order_start_price = cur_price
            current_commitment *= 2

            # We have no money to continue
            if deposit - current_commitment < 0:
                # SL implementation
                # return deposit + (tokens*cur_price - tokens*cur_price*COMMISSION), 0, index + 1
                return deposit, tokens, index + 1
            tokens += (current_commitment - current_commitment * COMMISSION) / cur_price
            deposit -= current_commitment

    return deposit, tokens, len(price_list) - 1


def bot_strategy(price_list, deposit, step, initial_commitment, profit_gap):
    initial_deposit = deepcopy(deposit)
    simulation_length = len(price_list)
    tokens = 0
    counter = 0
    while counter < simulation_length - 1:
        deposit, token_output, index = casino_bot_cycle(price_list[counter:],
                                                        deposit,
                                                        step,
                                                        initial_commitment,
                                                        profit_gap)
        counter += index
        tokens += token_output

    return (deposit + tokens*price_list[-1]) - initial_deposit


def main():
    print("Buy Scenario 1 profit: %s" % buy_with_sl(SCENARIO1_PRICE_LIST, DEPOSIT))
    print("Bot Scenario 1 profit: %s" % bot_strategy(SCENARIO1_PRICE_LIST, DEPOSIT, BOT_STEP, INITIAL_COMMITMENT,
                                                     PROFIT_GAP))
    print("Buy Scenario 2 profit: %s" % buy_with_sl(SCENARIO2_PRICE_LIST, DEPOSIT))
    print("Bot Scenario 2 profit: %s" % bot_strategy(SCENARIO2_PRICE_LIST, DEPOSIT, BOT_STEP, INITIAL_COMMITMENT,
                                                     PROFIT_GAP))
    print("Buy Scenario 3 profit: %s" % buy_with_sl(SCENARIO3_PRICE_LIST, DEPOSIT))
    print("Bot Scenario 3 profit: %s" % bot_strategy(SCENARIO3_PRICE_LIST, DEPOSIT, BOT_STEP, INITIAL_COMMITMENT,
                                                     PROFIT_GAP))
    print("Buy Scenario 4 profit: %s" % buy_with_sl(SCENARIO4_PRICE_LIST, DEPOSIT))
    print("Bot Scenario 4 profit: %s" % bot_strategy(SCENARIO4_PRICE_LIST, DEPOSIT, BOT_STEP, INITIAL_COMMITMENT,
                                                     PROFIT_GAP))
    print("Buy Scenario 5 profit: %s" % buy_with_sl(get_binance_history_data('1h', 'TRX/BNB'), DEPOSIT))
    print("Bot Scenario 5 profit: %s" % bot_strategy(get_binance_history_data('1h', 'TRX/BNB'), DEPOSIT, BOT_STEP,
                                                     INITIAL_COMMITMENT, PROFIT_GAP))


if __name__ == "__main__":
    main()

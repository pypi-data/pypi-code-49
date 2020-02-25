import yfinance as yf
import pandas as pd
import re
import numpy as np

pd.set_option('display.float_format', '{:,.2f}'.format)


class Symbols:
    def __init__(self, symbols, period='5d',
                 period_start=None, period_end=None):
        self.symbols = [x.upper() for x in re.findall(r"[\w']+", symbols)]
        if period_start and period_end:
            period = {'start': period_start, 'end': period_end}
        else:
            period = {'period': period}
        self.__period = period
        columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        self.__data = yf.download(' '.join(self.symbols),
                                  **self.__period)[columns]

    def __repr__(self):
        return "Market data for the following symbol(s): {}". \
            format(' '.join(self.symbols))

    @property
    def quotes(self):
        data = self.__data.copy()
        if len(self.symbols) == 1:
            return data
        else:
            data.columns = data.columns.swaplevel(0, 1)
            return data.sort_index(axis=1, level=0)

    @property
    def quotes_t(self):
        data = self.__data.copy()
        if len(self.symbols) == 1:
            return data.T
        else:
            return data.T.swaplevel().sort_index(axis=0, level=0)

    def __beta(self, market='SPY'):
        market_close = yf.Ticker(market).history(**self.__period)['Close']
        market_return = market_close.pct_change()[1:]
        beta_values = []
        for symbol in self.symbols:
            stock_return = self.quotes[symbol]['Close'].pct_change()[1:]
            sm_cov = np.cov(stock_return, market_return)[0][1]
            market_var = np.var(market_return)
            beta_values.append(sm_cov / market_var)
        return pd.DataFrame({'Beta': beta_values}, index=self.symbols)

    @property
    def __avg_day_dollar_trd_volume(self):
        addtv = []
        for symbol in self.symbols:
            avg_quotes = self.quotes[symbol].mean()
            addtv_tmp = (avg_quotes['Open'] + avg_quotes['High'] +
                         avg_quotes['Low'] + avg_quotes['Close']) / 4 * avg_quotes['Volume']
            addtv.append(addtv_tmp)
        return pd.DataFrame({'Avg Day Dollar Trd Vol': addtv}, index=self.symbols)

    @property
    def metrics(self):
        df = pd.DataFrame(self.__data.T.loc['Close'].mean(axis=1),
                          columns=['Average Close'])
        volume = pd.DataFrame(self.__data.T.loc['Volume'].mean(axis=1),
                              columns=['Average Vol'])
        df = df.join(volume)
        df = df.join(self.__avg_day_dollar_trd_volume)
        try:
            df = df.join(self.__beta())
        except (AttributeError, ValueError):
            print("Attention: Not enough data to calculate Beta for {} time interval".format(self.__period['period']))
        return df
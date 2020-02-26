"""
This library will allow you to perform the following actions:
- Fetch market data for a specified list of tickers and time interval.
Available data points: Open, High, Low, Close,Volume

- Time interval can be set in two ways:
-- period like 1d, 5d, 1mo, 3mo, 1y, 2y, 5y, 10y, ytd, etc.
1mo is used by default.
-- period specified by start and end dates in format "YYYY-MM-DD".
The second option has a higher priority if specified.

- Get the fetched data as a Pandas Dataframe. Two view modes are available:
-- Regular (index consists of dates and columns are represented as two levels -
symbols and data points). Used by default.
-- Transposed (columns are represented as dates and index
consists of two levels -symbol and data points).

- Calculate the following date points: Average Close Price, Average Volume,
Average Daily Dollar Trade Volume, Beta-coefficient
"""

from typing import Optional, Dict, Union, List, Any
import re
from pandas import DataFrame, Series
import yfinance as yf
import pandas as pd
import numpy as np

pd.set_option('display.float_format', '{:,.2f}'.format)


class Symbols:
    """
    Symbols object has the following public attributes:
    - symbols
    - quotes
    - quotes_t (transposed view)
    - metrics
    """

    symbols: List[Any]
    __period: Union[Dict[str, Optional[str]], Dict[str, str]]
    __data: DataFrame

    def __init__(self, symbols: str, period: str = '5d',
                 period_start: str = None, period_end: str = None) -> None:
        """
        Symbols class constructor.

        :type symbols: str
        :type period: str
        :type period_start: str
        :type period_end: str
        """

        self.symbols = [x.upper() for x in re.findall(r"[\w']+", symbols)]
        if period_start and period_end:
            period = {'start': period_start, 'end': period_end}
        else:
            period = {'period': period}
        self.__period = period
        columns: List[str] = ['Open', 'High', 'Low', 'Close', 'Volume']
        self.__data = yf.download(' '.join(self.symbols),
                                  **self.__period)[columns]

    def __repr__(self) -> str:
        return "Market data for {}". \
            format(' '.join(self.symbols))

    @property
    def quotes(self) -> DataFrame:
        """Returns fetched data as a Pandas Dataframe where index consists of dates and
        the columns have two levels: symbols and data points

        :rtype: object"""

        data: DataFrame = self.__data.copy()
        if len(self.symbols) == 1:
            return data
        data.columns = data.columns.swaplevel(0, 1)
        return data.sort_index(axis=1, level=0)

    @property
    def quotes_t(self) -> DataFrame:
        """
        Returns fetched data as a transposed Pandas Dataframe. As result,
        columns consist of dates and the index has two levels: symbols and
        data points. The data is groupped by symbols.

        :rtype: DataFrame
        """

        data: DataFrame = self.__data.copy()
        if len(self.symbols) == 1:
            return data.T
        return data.T.swaplevel().sort_index(axis=0, level=0)

    def __beta(self, market: str = 'SPY') -> DataFrame:
        """
        Receives a symbols against which Beta coefficient should be calculated
        for all symbols in the class instance. SPY is used by default.

        Beta is calculated as follows:
        Beta= Covariance(s, m) / Variance(m), where:
        - Covariance(s, m) = Measure of a stock’s return relative
        to that of the market
        - Variance(m) = Measure of how the market moves relative to its mean

        :type market: str
        :rtype: DataFrame
        """

        market_close: Series = yf.Ticker(market).history(**self.__period)['Close']
        market_return: Series = market_close.pct_change()[1:]
        beta_values: list = []
        for symbol in self.symbols:
            stock_return: Series = self.quotes[symbol]['Close'].pct_change()[1:]
            sm_cov: float = np.cov(stock_return, market_return)[0][1]
            market_var: float = np.var(market_return)
            beta_values.append(sm_cov / market_var)
        return pd.DataFrame({'Beta': beta_values}, index=self.symbols)

    @property
    def __avg_day_dollar_trd_volume(self) -> DataFrame:
        """
        Calculates Average Daily Dollar Trading Volume value for each
        symbols in the class instance within the period specified.
        Calculated as the product of the daily trading volume of the Common
        Stock as reported by Bloomberg on such Trading Day and the Weighted
        Average Price of the Common Stock on such Trading Day.

        NOTE: since weighted average price cannot be calculated based on the
        data available, the average price is calculated as follows:
        (open + high + low + close) / 4.

        :rtype: DataFrame
        """

        def day_doll_trd_vol(row: Series) -> float:
            """
            Receives a Pandas Series containing Open, High, Low, Close, Volume
            values and returns Daily Dollar Trading Value.

            :rtype: float
            """

            return (row['Close'] + row['High'] + row['Low'] + row['Open']) / 4 * row['Volume']

        addtv: list = []
        for symbol in self.symbols:
            addtv_tmp = self.quotes[symbol].apply(day_doll_trd_vol, axis=1).mean()
            addtv.append(addtv_tmp)
        return pd.DataFrame({'Avg Day Dollar Trd Vol': addtv}, index=self.symbols)

    @property
    def metrics(self) -> DataFrame:
        """
        Returns calculated metrics for all symbols of the class instance within
        the time period specified. Available metrics:
        - Average Close Price
        - Average Volume
        - Average Daily Dollar Trade Volume
        - Beta-coefficient

        :rtype: DataFrame
        """

        metrics: DataFrame = pd.DataFrame(self.__data.T.loc['Close'].mean(axis=1),
                                          columns=['Average Close'])
        volume: DataFrame = pd.DataFrame(self.__data.T.loc['Volume'].mean(axis=1),
                                         columns=['Average Vol'])
        metrics = metrics.join(volume)
        metrics = metrics.join(self.__avg_day_dollar_trd_volume)
        try:
            metrics = metrics.join(self.__beta())
        except (AttributeError, ValueError):
            print("Attention: Not enough data to calculate Beta for {} time \
                interval".format(self.__period['period']))
        return metrics

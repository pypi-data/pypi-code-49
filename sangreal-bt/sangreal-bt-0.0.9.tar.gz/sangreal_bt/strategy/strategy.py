import datetime as dt
import os

import attr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dateutil.parser import parse

from sangreal_bt.commons import Commons
from sangreal_bt.datafeed.datafeed import DataBase


@attr.s(
    hash=True,
    cmp=False,
)
class Strategy:
    """
    从sangreal_bt包中导入 sangreal_bt
        初始化新类中支持参数

    begin_dt: 回测开始日期
    end_dt: 回测结束日期


    matching_type: 有两种撮合方式， 分别为
        next_bar：第二天开盘价撮合
        current_bar：当天收盘价撮合
        默认next_bar

    commission: 股票手续费 默认(0, 0) 分别为（做多，做空）
    fcommission: 股指期货手续费 默认(0, 0) 分别为（做多，做空）
    """

    # 日期函数转化工具
    def dt_converter(value):
        return pd.to_datetime(value)

    begin_dt = attr.ib(
        default=pd.to_datetime('20010101'),
        repr=True,
        converter=dt_converter,
    )
    end_dt = attr.ib(
        default=pd.to_datetime(dt.date.today()),
        repr=True,
        converter=dt_converter,
    )

    matching_type = attr.ib(default="next_bar")

    benchmark = attr.ib(default="")

    commission = attr.ib(default=(0, 0), converter=tuple)

    @commission.validator
    def check_commission(self, attribute, value):
        if len(value) != 2:
            raise ValueError('commission must be tuple like (0.1, 0.1)!')

    fcommission = attr.ib(default=(0, 0), converter=tuple)

    @fcommission.validator
    def check_fcommission(self, attribute, value):
        if len(value) != 2:
            raise ValueError('fcommission must be tuple like (0.1, 0.1)!')

    @matching_type.validator
    def check_match(self, attribute, value):
        if value not in ('next_bar', 'current_bar'):
            raise ValueError('matching_type must be next_bar or current_bar')

    def __attrs_post_init__(self):
        self._open = None
        self._close = None
        self._signal = None

    # 注入信号
    def addsignal(self, signal):
        if not isinstance(signal, pd.DataFrame):
            raise TypeError('The data must be a DataFrame!')
        signal = signal.copy()
        # 三列模式
        if isinstance(signal.index[0], int):
            signal.columns = [c.lower() for c in signal.columns]
            columns = {'date', 'stockid', 'weight'}
            assert columns.issubset(signal), f"signal must contain {columns}"
            signal.rename({'date': 'trade_dt', 'stockid': 'sid'},
                          axis=1, inplace=True)
            signal['trade_dt'] = pd.to_datetime(signal['trade_dt'])
            # 股指期货端
            signal_future = signal[signal['sid'].str.contains(
                Commons.INDEX_FUTURE)].copy()
            signal_future = signal_future.pivot(
                values='weight', index='trade_dt', columns='sid')

            # 多头资产端
            signal_asset = signal[~signal['sid'].str.contains(
                Commons.INDEX_FUTURE)].copy()
            signal_asset = signal_asset.pivot(
                values='weight', index='trade_dt', columns='sid')

        # pivot table 模式
        else:
            signal.index = pd.to_datetime(signal.index)
            signal_column = signal.columns
            asset_columns = signal_column[~signal_column.str.contains(
                Commons.INDEX_FUTURE)]
            future_columns = signal_column[signal_column.str.contains(
                Commons.INDEX_FUTURE)]
            signal_future = signal[future_columns].copy()
            signal_asset = signal[asset_columns].copy()

        # 加入现金权重
        _s0 = signal_asset.sum(axis=1)
        _s1 = signal_future.sum(axis=1)
        signal_asset['cash'] = 1 * np.sign(_s0) - _s0
        signal_future['cash'] = 1 * np.sign(_s1) - _s1

        # 第二天开盘价买入
        if self.matching_type == 'next_bar':
            signal_asset.index = signal_asset.index + Commons.SHIFT_TIME
            signal_future.index = signal_future.index + Commons.SHIFT_TIME
        self._signal = {'asset': signal_asset, 'future': signal_future}
        return

    # 注入回测数据
    def adddata(self, data):
        if not isinstance(data, DataBase):
            raise TypeError('The data must be a handle with datafreed class!')
        self._open = data.open.copy()
        self._close = data.close.copy()
        # 对开始及结束日期进行修正
        self.begin_dt = max(self.begin_dt, self._open.index[0])
        self.end_dt = min(self.end_dt, self._open.index[-1])

        # 重新设置开始结束data日期
        self._open = self._open.loc[self.begin_dt:self.end_dt].copy()
        # open的日期进行处理前移
        self._open = self._open.shift(-1)
        self._open.index = self._open.index + Commons.SHIFT_TIME
        self._close = self._close.loc[self.begin_dt:self.end_dt].copy()
        # 加入现金项
        self._open['cash'] = 1.0
        self._close['cash'] = 1.0

    def setcommission(self, commission):
        if len(commission) != 2:
            raise ValueError('commission must be tuple like (0.1, 0.1)!')
        self.commission = tuple(commission)

    def setfcommission(self, commission):
        if len(commission) != 2:
            raise ValueError('commission must be tuple like (0.1, 0.1)!')
        self.fcommission = tuple(commission)

    def setbenchmark(self, benchmark):
        self.benchmark = benchmark

    def _get_universe_value(self, signal):
        """[获取资产池内收益，得到每个信号bar后一个bar的收益，并前移至该bar]

        Arguments:
            signal {[pd.DataFrame]} -- [处理好的signal]

        Returns:
            [type] -- [description]
        """
        df = self._close.reindex(signal.columns, axis=1)
        if self.matching_type == 'next_bar':
            df_c = df.copy()
            df_o = self._open.reindex(
                signal.columns, axis=1).reindex(signal.index)
            df = pd.concat([df_c, df_o], axis=0, sort=False)
            df.sort_index(inplace=True)
        # =======================================
        df = df.pct_change()
        df = df.shift(-1).fillna(0)
        return df

    def _get_ret(self, signal, commission_factor):
        """
        向量化计算收益
        信号 手续费 tuple
        返回，多空，多头，空头累计收益
        """
        # 对应universe每天收益（pct_change)

        u_value = self._get_universe_value(signal)
        # =============================================
        trade_dt_list = u_value.index
        # =============信号处理====================
        # 初始信号
        signal_tmp = signal.fillna(0)
        # ================================================
        _weight = np.exp(np.log1p(u_value.shift(1).fillna(0)).cumsum())
        signal_all = signal_tmp.reindex(index=trade_dt_list).ffill()

        # 更新持仓期间权重，但是每期初期权重仍未改变到初始状态
        signal_all = signal_all * _weight
        # 得到每期的初始持仓权重 因子
        weight_factor = _weight.reindex(signal_tmp.index).reindex(
            signal_all.index).ffill()
        # 得到修正后的每期持仓信号（包含权重变化）
        signal_all = signal_all / weight_factor

        # 归一化
        signal_all = signal_all.div(signal_all.sum(axis=1).abs(), axis='index')

        # ============计算收益=================
        _shift = 1
        ret_all = (signal_all * u_value).sum(axis=1)
        ret_all = ret_all.shift(_shift).fillna(0)

        # ===================考虑手续费==========================
        # 手续费修正
        tmp_diff = signal_all.fillna(0).diff().reindex(signal_tmp.index)
        # 做多方向
        tmp_long_diff = (tmp_diff + tmp_diff.abs()) / 2
        # 做空方向
        tmp_short_diff = (tmp_diff.abs() - tmp_diff) / 2

        # =======手续费=====================
        commission_all = (-1 * (tmp_long_diff).sum(axis=1) * commission_factor[0] -
                          (tmp_short_diff).sum(axis=1) * commission_factor[1]).fillna(0)
        commission_all = commission_all.reindex(
            trade_dt_list).fillna(0)
        ret_all = ret_all + commission_all
        ret_all = np.exp(np.log1p(ret_all).cumsum())
        # ======================
        ret_all = ret_all[ret_all.index.hour != 12]
        return ret_all

    def _hedge_ret(self, long_ret, short_ret):
        '''
        计算对冲后收益
        '''
        # 如果空头为空
        if short_ret.empty:
            short_ret = long_ret.copy()
            short_ret.iloc[:] = 1

        # 如果多头为空
        if long_ret.empty:
            long_ret = short_ret.copy()
            long_ret.iloc[:] = 1

        trades_dt = self._signal['asset'].index
        if self.matching_type == 'next_bar':
            trades_dt -= Commons.SHIFT_TIME
        trades_dt = trades_dt[trades_dt <= self.end_dt]
        long_adjust_factor = (long_ret.loc[trades_dt].reindex(
            long_ret.index)).ffill().fillna(1)
        short_adjust_factor = (short_ret.loc[trades_dt].reindex(
            short_ret.index)).ffill().fillna(1)
        # 对每期初始资金作调整，此时净值有跳跃
        long_adjust = long_ret / long_adjust_factor
        short_adjust = short_ret / short_adjust_factor
        ratio = (short_adjust / long_adjust).shift(1)
        long_short_ret = (long_ret.pct_change() + short_ret.pct_change() *
                          ratio) / (1 + ratio - 1 / long_adjust.shift(1))
        long_short_ret = (1 + long_short_ret).fillna(1).cumprod()
        return long_short_ret

    def run(self):
        if not all([isinstance(self._open, pd.DataFrame), isinstance(self._close, pd.DataFrame), isinstance(self._signal, dict)]):
            raise ValueError('Please add signal and data!')
        # 保证回测数据有足够的品种
        assert (set(self._signal['asset'].columns) | set(self._signal['future'])).issubset(
            self._open.columns), 'Please check data stock range!'

        # 对信号进行修正
        self._signal['asset'] = self._signal['asset'].loc[self.begin_dt:self.end_dt].copy()
        self._signal['future'] = self._signal['future'].loc[self.begin_dt:self.end_dt].copy()

        ret_asset = self._get_ret(self._signal['asset'], self.commission)
        ret_future = self._get_ret(self._signal['future'], self.fcommission)
        ret_hedge = self._hedge_ret(ret_asset, ret_future)

        ret_all = pd.concat([ret_asset.to_frame('asset'), ret_future.to_frame(
            'future'), ret_hedge.to_frame('hedge')], axis=1, sort=False)
        if self.benchmark:
            benchmark = self._close.reindex([self.benchmark], axis=1)
            if benchmark.empty:
                raise ValueError('请输入正确的基准代码!')
            ret_all = ret_all.join(benchmark)
            ret_all[self.benchmark] = ret_all[self.benchmark] / \
                ret_all[self.benchmark].dropna().iloc[0]
        self.result = ret_all

    def plot(self, *args, **kwargs):
        # 对数收益
        np.log(self.result).plot(*args, **kwargs)
        plt.show()


if __name__ == "__main__":
    pass

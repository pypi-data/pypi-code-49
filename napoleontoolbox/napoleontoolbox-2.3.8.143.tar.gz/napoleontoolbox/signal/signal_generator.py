#!/usr/bin/env python
# coding: utf-8

import numpy as np
import numpy.ma as ma

from napoleontoolbox.tools.analyze_tools import roll_corr

def compute_correlation(col_one, col_two):
    a = ma.masked_invalid(col_one)
    b = ma.masked_invalid(col_two)
    msk = (~a.mask & ~b.mask)
    correlation_matrix = ma.corrcoef(col_one[msk], col_two[msk])
    correlation_coefficient = correlation_matrix[0][1]
    return correlation_coefficient

# zura kakushade alphas
def alpha_2(data = None,  contravariant = -1., **kwargs):
    data['log_vol'] = np.log(data['volumefrom'])
    correlation_coefficient = compute_correlation(data.log_vol.diff(2).rank(pct=True), (data.close - data.open)/data.open)
    return contravariant*correlation_coefficient

def alpha_3(data = None, contravariant = -1., **kwargs):
    correlation_coefficient = compute_correlation(data.open.rank(pct = True), data.volumefrom.rank(pct = True))
    return contravariant*correlation_coefficient

def alpha_5(data = None, contravariant = -1., **kwargs):
    data['volu_close'] = data['volumefrom']*data['close']
    vwap = data['volu_close'].sum() / data['volumefrom'].sum()
    data['open_minus_vwap'] = data.open - vwap
    data['close_minus_vwap'] = data.close - vwap
    correlation_coefficient = compute_correlation(data['open_minus_vwap'].rank(pct = True), data['close_minus_vwap'].rank(pct = True))
    return contravariant*correlation_coefficient

def alpha_6(data = None, contravariant = -1., **kwargs):
    correlation_coefficient = compute_correlation(data['open'], data['volumefrom'])
    return contravariant*correlation_coefficient

def alpha_6_rank(data = None, contravariant = -1., **kwargs):
    correlation_coefficient = compute_correlation(data['open'].rank(pct = True), data['volumefrom'].rank(pct = True))
    return contravariant*correlation_coefficient

def alpha_8(data = None, contravariant = -1 , lag=5, **kwargs):
    data['close_return']=data['close'].pct_change()
    col1 = (data['open']*data['close_return'])
    col2 = (data['open']*data['close_return']).shift(lag)
    correlation_coefficient = compute_correlation(col1, col2)
    return contravariant*correlation_coefficient

# Alpha  # 12: (sign(delta(volume, 1)) * (-1 * delta(close, 1)))
def alpha_12(data = None, contravariant = -1., **kwargs):
    signals = np.sign(data['volumefrom'].diff() * data['close'].diff())
    return signals[-1]*contravariant

def alpha_13(data = None, contravariant = -1., lag = 5,  **kwargs):
    to_roll =  data[['close','volumefrom']]
    to_roll = to_roll.reset_index(drop = True)
    result_df = roll_corr(to_roll, window=lag)
    result_df = result_df.dropna()
    result_df = result_df.rank(pct = True)
    return contravariant*result_df.iloc[-1,0]

#Alpha#14: ((-1 * rank(delta(returns, 3))) * correlation(open, volume, 10))
def alpha_14(data = None, contravariant = -1., lag = 3, **kwargs):
    correlation_coefficient = compute_correlation(data['open'],data['volumefrom'])
    returns = data['close'].pct_change().diff(lag)
    returns=returns.to_frame()
    return returns.iloc[-1,0]*correlation_coefficient*contravariant

# Alpha#15: (-1 * sum(rank(correlation(rank(high), rank(volume), 3)), 3))
def alpha_15(data = None, contravariant = -1., lag = 3, **kwargs):
    data['high_rank'] = data['high'].rank(pct=True)
    data['volume_rank'] = data['volumefrom'].rank(pct=True)
    to_roll =  data[['high_rank','volume_rank']]
    to_roll = to_roll.reset_index(drop = True)
    result_df = roll_corr(to_roll, window=lag)
    result_df = result_df.dropna()
    result_df = result_df.rank(pct = True)
    return contravariant*result_df[-lag:].mean().iloc[0]

# #Alpha#16: (-1 * rank(covariance(rank(high), rank(volume), 5)))
def alpha_16(data = None, contravariant = -1., lag = 5, **kwargs):
    data['high_rank'] = data['high'].rank(pct=True)
    data['volume_rank'] = data['volumefrom'].rank(pct=True)
    to_roll =  data[['high_rank','volume_rank']]
    to_roll = to_roll.reset_index(drop = True)
    result_df = roll_corr(to_roll, window=lag)
    result_df = result_df.rank(pct = True)
    return result_df.iloc[-1,0]

def counting_candles(data= None, threshold = 1., contravariant = -1, **kwargs):
    me_values = (data.close.diff() >= 0.).astype(float).value_counts()
    try:
        one_count = me_values[1.]
    except KeyError:
        one_count = 0
    try:
        zero_count = me_values[0.]
    except KeyError:
        zero_count = None
    if zero_count is not None:
        ratio = one_count/zero_count
        if ratio >= threshold:
            return -contravariant
        else:
            return contravariant
    else :
        return -contravariant

def dd_threshold(data = None, threshold=1., contravariant = -1., **kwargs):
    ratio = data['high'][-1]/data['high'][0]
    if ratio > threshold:
        return contravariant
    else :
        return -contravariant

def lead_lag_indicator(data = None, lead=3, lag=5, contravariant = -1., **kwargs):
    output_sma_lead = data.close[-lead:].mean()
    output_sma_lag = data.close[-lag:].mean()
    if output_sma_lead > output_sma_lag:
        return -contravariant
    else :
        return contravariant

def volume_weighted_high_low_vol(data = None , vol_threshold = 0.05, up_trend_threshold=1e-4, low_trend_threshold=1e-4, contravariant = 1., display = False, **kwargs):
    trend = ((data['close'][-1]-data['close'][0])/data['close'][0])/data['close'][0]
    data['hl'] = (data['high'] - data['low'])/data['low']
    data['volu_hi_low'] = data['volumefrom']*data['hl']
    weighted_volu_hi_low = data['volu_hi_low'].sum() / data['volumefrom'].sum()
    if display:
        print('weighted_volu_hi_low :' + str(weighted_volu_hi_low))
        print('trend :'+str(trend))
        print('vol_threshold :'+str(vol_threshold))
        print('up_trend_threshold :'+str(up_trend_threshold))
        print('low_trend_threshold :'+str(low_trend_threshold))
    if weighted_volu_hi_low > vol_threshold:
        if trend > up_trend_threshold:
            return contravariant
        elif trend < -low_trend_threshold:
            return -contravariant
        else:
            return np.nan
    else :
        return np.nan


def volume_weighted_high_low_vol_long_only(data = None , vol_threshold = 0.05, up_trend_threshold=1e-4, low_trend_threshold=1e-4, contravariant = 1., display = False, **kwargs):
    trend = ((data['close'][-1]-data['close'][0])/data['close'][0])/data['close'][0]
    data['hl'] = (data['high'] - data['low'])/data['low']
    data['volu_hi_low'] = data['volumefrom']*data['hl']
    weighted_volu_hi_low = data['volu_hi_low'].sum() / data['volumefrom'].sum()
    if display:
        print('weighted_volu_hi_low :' + str(weighted_volu_hi_low))
        print('trend :'+str(trend))
        print('vol_threshold :'+str(vol_threshold))
        print('up_trend_threshold :'+str(up_trend_threshold))
        print('low_trend_threshold :'+str(low_trend_threshold))
    if weighted_volu_hi_low > vol_threshold:
        if trend > up_trend_threshold:
            return contravariant
        elif trend < -low_trend_threshold:
            return 0
        else:
            return np.nan
    else :
        return np.nan
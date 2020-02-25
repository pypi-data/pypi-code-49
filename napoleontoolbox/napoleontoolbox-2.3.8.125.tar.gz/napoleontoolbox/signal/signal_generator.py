#!/usr/bin/env python
# coding: utf-8

import numpy as np


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


def dd_threshold(data = None, threshold=1., contravariant = -1, **kwargs):
    ratio = data['high'][-1]/data['high'][0]
    if ratio > threshold:
        return contravariant
    else :
        return -contravariant

def lead_lag_indicator(data = None, lead=3, lag=5, contravariant = -1, **kwargs):
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
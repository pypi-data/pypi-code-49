#!/usr/bin/env python
# coding: utf-8

import talib
import numpy as np

def dd_threshold(data = None, threshold=1., contravariant = -1, **kwargs):
    ratio = data['high'][-1]/data['high'][0]
    if ratio > threshold:
        return contravariant
    else :
        return -contravariant

def lead_lag_indicator(data = None, lead=3, lag=5, contravariant = -1, **kwargs):
    output_sma_lead = talib.SMA(data.close, timeperiod=lead)
    output_sma_lag = talib.SMA(data.close, timeperiod=lag)
    if output_sma_lead[-1] > output_sma_lag[-1]:
        return -contravariant
    else :
        return contravariant

def volume_weighted_high_low_vol(data = None , vol_threshold = 0.005, trend_threshold=0.005, contravariant = 1., display = False, **kwargs):
    trend = ((data['close'][-1]-data['close'][0])/data['close'][0])/data['close'][0]
    data['hl'] = (data['high'] - data['low'])/data['low']
    data['volu_hi_low'] = data['volumefrom']*data['hl']
    weighted_volu_hi_low = data['volu_hi_low'].sum() / data['volumefrom'].sum()
    if display:
        print('weighted_volu_hi_low :' + str(weighted_volu_hi_low))
        print('trend :'+str(trend))
        print('vol_threshold :'+str(vol_threshold))
        print('trend_threshold :'+str(trend_threshold))
    if weighted_volu_hi_low > vol_threshold:
        if trend > trend_threshold:
            return contravariant
        elif trend < -trend_threshold:
            return -contravariant
        else:
            return np.nan
    else :
        return np.nan
#!/usr/bin/env python
# coding: utf-8

import talib

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

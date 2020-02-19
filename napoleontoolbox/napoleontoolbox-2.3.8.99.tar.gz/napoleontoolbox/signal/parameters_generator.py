#!/usr/bin/env python
# coding: utf-8

def generate_lead_lag(lookback_windows, contravariants):
    parameters = []
    lookback_window = max(lookback_windows)
    for contravariant in contravariants:
        for lag in range(3, lookback_window):
            for lead in range(2, lag):
                parameters.append({
                    'lead':lead,
                    'lag':lag,
                    'lookback_window':lookback_window,
                    'contravariant':contravariant
                })
    return parameters

def generate_dd_threshold(lookback_windows, thresholds, contravariants):
    parameters = []
    for lookback_window in lookback_windows:
        for contravariant in contravariants:
            for threshold in thresholds:
                parameters.append({
                    'lookback_window':lookback_window,
                    'contravariant':contravariant,
                    'threshold':threshold
                })
    return parameters

def generate_volume_weighted_high_low_vol(lookback_windows, vol_thresholds, trend_thresholds, contravariants, display):
    parameters = []
    for lookback_window in lookback_windows:
        for contravariant in contravariants:
            for vol_threshold in vol_thresholds:
                for trend_threshold in trend_thresholds:
                    parameters.append({
                        'lookback_window':lookback_window,
                        'contravariant':contravariant,
                        'vol_threshold':vol_threshold,
                        'trend_threshold':trend_threshold,
                        'display' : display
                    })
    return parameters
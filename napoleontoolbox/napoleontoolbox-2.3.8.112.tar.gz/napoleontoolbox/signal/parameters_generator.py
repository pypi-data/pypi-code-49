#!/usr/bin/env python
# coding: utf-8

def generate_lead_lag(lookback_windows, contravariants, ranging_stride):
    parameters = []
    lookback_window = max(lookback_windows)
    for contravariant in contravariants:
        for lag in range(3, lookback_window, ranging_stride):
            for lead in range(2, lag, ranging_stride):
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

def generate_volume_weighted_high_low_vol(lookback_windows, vol_thresholds, up_trend_thresholds,  low_trend_thresholds, contravariants, display):
    parameters = []
    for lookback_window in lookback_windows:
        for contravariant in contravariants:
            for vol_threshold in vol_thresholds:
                for up_trend_threshold in up_trend_thresholds:
                    for low_trend_threshold in low_trend_thresholds:
                        parameters.append({
                            'lookback_window':lookback_window,
                            'contravariant':contravariant,
                            'vol_threshold':vol_threshold,
                            'up_trend_threshold':up_trend_threshold,
                            'low_trend_threshold': low_trend_threshold,
                            'display' : display
                        })
    return parameters
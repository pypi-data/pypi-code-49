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

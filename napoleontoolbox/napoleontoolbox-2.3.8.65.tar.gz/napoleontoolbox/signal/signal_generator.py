#!/usr/bin/env python
# coding: utf-8



def dd_threshold(data = None, threshold=1., contravariant = -1, **kwargs):
    ratio = data['high'][-1]/data['high'][0]
    if ratio > threshold:
        return contravariant
    else :
        return -contravariant



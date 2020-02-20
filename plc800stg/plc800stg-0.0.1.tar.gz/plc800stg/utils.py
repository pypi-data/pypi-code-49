#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from pytz import timezone


def get_station(dt_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    if not dt.tzinfo:
        dt = timezone('Europe/Madrid').localize(dt)
    if timezone('Europe/Madrid').normalize(dt).dst():
        return 'S'
    else:
        return 'W'


def assert_list_dict_eq(list_dict_a, list_dict_b, sorting_key):
    """ Asserts that two lists of dicts are equal sorting by key """
    if len(list_dict_a) != len(list_dict_b):
        raise AssertionError()
    list_dict_a_sorted = sorted(list_dict_a, key=lambda k: k[sorting_key])
    list_dict_b_sorted = sorted(list_dict_b, key=lambda k: k[sorting_key])
    for index_dict in range(0, len(list_dict_a_sorted)):
        if list_dict_a_sorted[index_dict] != list_dict_b_sorted[index_dict]:
            raise AssertionError()


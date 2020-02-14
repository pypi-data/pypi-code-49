"""
A type module for combining item information with account names.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
from collections import namedtuple
from itertools import chain

from . import possessions
from .utils._i18n import n_

AccountItemRecord = namedtuple(
    'AccountItemRecord', 
    list(chain([n_('account')], possessions.ItemRecord._fields)))
"""Data type for the raw item data, including account name."""
# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .configuration import ConfigurationDefaultAccount, Configuration
from .account import AgedBalanceContext


def register():
    Pool.register(
        Configuration,
        ConfigurationDefaultAccount,
        AgedBalanceContext,
        module='account_aged_balance_defaults', type_='model')

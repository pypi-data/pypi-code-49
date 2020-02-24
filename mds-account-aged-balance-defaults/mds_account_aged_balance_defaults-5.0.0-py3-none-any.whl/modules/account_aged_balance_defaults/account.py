# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelView
from trytond.pool import Pool


__all__ = ['AgedBalanceContext']


class AgedBalanceContext(ModelView):
    'Aged Balance Context'
    __name__ = 'account.aged_balance.context'

    @staticmethod
    def default_term1():
        """ load value from config
        """
        AccountConfig = Pool().get('account.configuration')
        
        config1 = AccountConfig.get_singleton()
        if not isinstance(config1.agedbal_term1, type(1)):
            return 30
        else :
            return config1.agedbal_term1

    @staticmethod
    def default_term2():
        """ load value from config
        """
        AccountConfig = Pool().get('account.configuration')
        
        config1 = AccountConfig.get_singleton()
        if not isinstance(config1.agedbal_term2, type(1)):
            return 60
        else :
            return config1.agedbal_term2

    @staticmethod
    def default_term3():
        """ load value from config
        """
        AccountConfig = Pool().get('account.configuration')
        
        config1 = AccountConfig.get_singleton()
        if not isinstance(config1.agedbal_term3, type(1)):
            return 90
        else :
            return config1.agedbal_term3

# end AgedBalanceContext

# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.transaction import Transaction
from trytond.modules.company.model import (
    CompanyMultiValueMixin, CompanyValueMixin)


__all__ = ['Configuration', 'ConfigurationDefaultAccount']


agedbal_term1 = fields.Integer(string='Term 1', 
    help="Number of days above the due date for term 1.", required=True)
agedbal_term2 = fields.Integer(string='Term 2', 
    help="Number of days above the due date for term 2.", required=True)
agedbal_term3 = fields.Integer(string='Term 3', 
    help="Number of days above the due date for term 3.", required=True)



class Configuration(ModelSingleton, ModelSQL, ModelView, CompanyMultiValueMixin):
    'Account Configuration'
    __name__ = 'account.configuration'
    
    agedbal_term1 = fields.MultiValue(agedbal_term1)
    agedbal_term2 = fields.MultiValue(agedbal_term2)
    agedbal_term3 = fields.MultiValue(agedbal_term3)
    
    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field in {'agedbal_term1', 'agedbal_term2', 'agedbal_term3'}:
            return pool.get('account.configuration.default_account')
        return super(Configuration, cls).multivalue_model(field)

# end Configuration


class ConfigurationDefaultAccount(ModelSQL, CompanyValueMixin):
    "Account Configuration Default Account"
    __name__ = 'account.configuration.default_account'
    
    agedbal_term1 = agedbal_term1
    agedbal_term2 = agedbal_term2
    agedbal_term3 = agedbal_term3
    
    @classmethod
    def default_agedbal_term1(cls):
        return 30

    @classmethod
    def default_agedbal_term2(cls):
        return 60

    @classmethod
    def default_agedbal_term3(cls):
        return 90
    
    
# end ConfigurationDefaultAccount

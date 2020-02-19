# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.pyson import Eval

__all__ = ['SaleLine']


class SaleLine(ModelSQL, ModelView):
    'Sale Line'
    __name__ = 'sale.line'

    desctitle = fields.Text(string='Title', size=None,
        states={
            'readonly': Eval('sale_state') != 'draft',
            },
        depends=['sale_state'])

    @classmethod
    def __setup__(cls):
        super(SaleLine, cls).__setup__()
        
        # add line-type 'twocolumn'
        cls.type.selection.append(('twocolumn', 'Two Columns'))

    @classmethod
    def view_attributes(cls):
        return [
            ('/form//group[@id="grptwocols1"]', 'states', 
                {'invisible': Eval('type') == 'twocolumn'}),
            ('/form//group[@id="grptwocols2"]', 'states', 
                {'invisible': Eval('type') != 'twocolumn'}),
            ]

# end SaleLine

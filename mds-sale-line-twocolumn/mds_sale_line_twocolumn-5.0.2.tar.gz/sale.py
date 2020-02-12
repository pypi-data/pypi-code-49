# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Sale']


class Sale(ModelSQL, ModelView):
    'Sale'
    __name__ = 'sale.sale'

    def create_invoice(self):
        invoice = super(Sale, self).create_invoice()
        for i in invoice.lines:
            if i.type == 'twocolumn':
                if not isinstance(i.origin, type(None)):
                    if hasattr(i.origin, 'desctitle'):
                        i.desctitle = i.origin.desctitle
                        i.save()
        return invoice
        
# end Sale

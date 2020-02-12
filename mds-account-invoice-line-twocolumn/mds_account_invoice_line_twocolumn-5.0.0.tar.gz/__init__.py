# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .invoiceline import InvoiceLine


def register():
    Pool.register(
        InvoiceLine,
        module='account_invoice_line_twocolumn', type_='model')

# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .saleline import SaleLine
from .sale import Sale


def register():
    Pool.register(
        Sale,
        SaleLine,
        module='sale_line_twocolumn', type_='model')

# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import trytond.tests.test_tryton
import unittest

from trytond.modules.sale_line_twocolumn.tests.test_sale import SaleLineTestCase

__all__ = ['suite']


class SaleTestCase(\
            SaleLineTestCase,
    ):
    'Test two-columns module'
    module = 'sale_line_twocolumn'

#end OrderProcessTestCase


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SaleTestCase))
    return suite

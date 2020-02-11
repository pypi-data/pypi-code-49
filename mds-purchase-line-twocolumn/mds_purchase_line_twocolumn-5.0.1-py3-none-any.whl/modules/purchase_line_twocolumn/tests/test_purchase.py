# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.exceptions import UserError
from trytond.modules.company.tests import create_company, set_company
from trytond.modules.account.tests import create_chart


class PurchaseLineTestCase(ModuleTestCase):
    'Test sale-line module'
    module = 'sale_line_twocolumn'

    @with_transaction()
    def test_purchaseline_(self):
        """ test: add sale-line, fill both columns
        """
        pool = Pool()
        Party = pool.get('party.party')
        Address = pool.get('party.address')
        Contact = pool.get('party.contact_mechanism')
        Purchase = pool.get('purchase.purchase')
        PurchaseLine = pool.get('purchase.line')
        PaymentTerm = pool.get('account.invoice.payment_term')
        PaymentTermLine = pool.get('account.invoice.payment_term.line')
        PaymentTermDeltas = pool.get('account.invoice.payment_term.line.delta')

        company1 = create_company('m-ds')
        
        with set_company(company1):
            with Transaction().set_context({'company': company1.id}):
                chart1 = create_chart(company = company1, tax = True)
        
                # payment term
                pay1 = PaymentTerm(
                        name = '14 days',
                        lines = [
                            PaymentTermLine(
                                    type = 'remainder',
                                    relativedeltas = [
                                        PaymentTermDeltas(days = 14),
                                        ],
                                ),
                            ],
                    )
                pay1.save()

                party1 = Party(name = 'Party 1',
                    customer_payment_term = pay1,
                    supplier_payment_term = pay1,
                    addresses=[
                        Address(
                            zip='12345', 
                            city='Town', 
                            street='Street 1', 
                            invoice=True,
                            delivery = True,
                        ),
                    ],
                    contact_mechanisms = [
                        Contact(type='phone', value='0123456'),
                    ],
                )
                party1.save()

                pur1 = Purchase(
                        company = Purchase.default_company(),
                        party = party1,
                    )
                pur1.on_change_party()
                pur1.save()
                
                pur1.lines = [
                        PurchaseLine(
                            type='twocolumn',
                            desctitle = 'left column',
                            description = 'right column'
                        ),
                    ]
                pur1.save()
                
                pur_lst = Purchase.search([])
                self.assertEqual(len(pur_lst), 1)
                self.assertEqual(len(pur_lst[0].lines), 1)
                self.assertEqual(pur_lst[0].lines[0].type, 'twocolumn')
                self.assertEqual(pur_lst[0].lines[0].desctitle, 'left column')
                self.assertEqual(pur_lst[0].lines[0].description, 'right column')

# end PurchaseLineTestCase

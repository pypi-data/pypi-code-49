# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.exceptions import UserError
from trytond.modules.company.tests import create_company, set_company
from trytond.modules.account.tests import create_chart
# create_fiscalyear, , create_tax, create_tax_code


# from account.tests.tools
def get_accounts(company, config=None):
    "Return accounts per kind"
    
    Account = Pool().get('account.account')

    accounts = Account.search([
            ('kind', 'in', ['receivable', 'payable', 'revenue', 'expense']),
            ('company', '=', company.id),
            ])
    accounts = {a.kind: a for a in accounts}
    cash, = Account.search([
            ('kind', '=', 'other'),
            ('company', '=', company.id),
            ('name', '=', 'Main Cash'),
            ])
    accounts['cash'] = cash
    tax, = Account.search([
            ('kind', '=', 'other'),
            ('company', '=', company.id),
            ('name', '=', 'Main Tax'),
            ])
    accounts['tax'] = tax
    return accounts


class InvoiceLineTestCase(ModuleTestCase):
    'Test invoice-line module'
    module = 'account_invoice_line_twocolumn'

    @with_transaction()
    def test_invoiceline_(self):
        """ test: add invoice-line, fill both columns
        """
        pool = Pool()
        Party = pool.get('party.party')
        Address = pool.get('party.address')
        Contact = pool.get('party.contact_mechanism')
        Invoice = pool.get('account.invoice')
        InvoiceLine = pool.get('account.invoice.line')
        PaymentTerm = pool.get('account.invoice.payment_term')
        PaymentTermLine = pool.get('account.invoice.payment_term.line')
        PaymentTermDeltas = pool.get('account.invoice.payment_term.line.delta')
        Journal = pool.get('account.journal')
        PaymentMethod = pool.get('account.invoice.payment.method')
        Sequence = pool.get('ir.sequence')

        company1 = create_company('m-ds')
        
        with set_company(company1):
            with Transaction().set_context({'company': company1.id}):
                chart1 = create_chart(company = company1, tax = True)
        
                accounts = get_accounts(company1)
                receivable = accounts['receivable']
                revenue = accounts['revenue']
                expense = accounts['expense']
                account_tax = accounts['tax']
                account_cash = accounts['cash']
        
                journal_cash, = Journal.search([('type', '=', 'cash')])
                payment_method = PaymentMethod()
                payment_method.name = 'Cash'
                payment_method.journal = journal_cash
                payment_method.credit_account = account_cash
                payment_method.debit_account = account_cash
                payment_method.save()

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

                inv1 = Invoice(
                        company = Invoice.default_company(),
                        party = party1,
                        type = 'out',
                        payment_term = pay1,
                    )
                inv1.on_change_type()
                inv1.on_change_party()
                inv1.save()
                
                inv1.lines = [
                        InvoiceLine(
                            type='twocolumn',
                            desctitle = 'left column',
                            description = 'right column'
                        ),
                    ]
                inv1.save()
                
                inv_lst = Invoice.search([])
                self.assertEqual(len(inv_lst), 1)
                self.assertEqual(len(inv_lst[0].lines), 1)
                self.assertEqual(inv_lst[0].lines[0].type, 'twocolumn')
                self.assertEqual(inv_lst[0].lines[0].desctitle, 'left column')
                self.assertEqual(inv_lst[0].lines[0].description, 'right column')

# end InvoiceLineTestCase

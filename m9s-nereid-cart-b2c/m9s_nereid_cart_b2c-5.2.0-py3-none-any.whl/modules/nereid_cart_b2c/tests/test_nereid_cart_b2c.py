# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import json
import pycountry
import datetime

from decimal import Decimal
from dateutil.relativedelta import relativedelta

from trytond.tests.test_tryton import suite as test_suite
from trytond.tests.test_tryton import with_transaction, USER
from trytond.pool import Pool
from trytond.exceptions import UserError
from trytond.transaction import Transaction

from werkzeug.datastructures import Headers

from nereid.testing import NereidModuleTestCase
from nereid import current_user, current_website

from trytond.modules.company.tests import create_company, set_company
from trytond.modules.nereid.tests.test_common import (create_website_locale,
    create_static_file)
from trytond.modules.payment_gateway.tests import (create_payment_gateway,
    create_payment_profile)
from trytond.modules.sale_channel.tests import (create_sale_channels,
    create_channel_sale)

from trytond.config import config
config.set('database', 'path', '/tmp')


def create_website(name='localhost', locales=[], default_locale=None):
    """
    Creates the website for testing
    """
    pool = Pool()
    Website = pool.get('nereid.website')
    Party = pool.get('party.party')
    User = pool.get('res.user')
    NereidUser = pool.get('nereid.user')
    Company = pool.get('company.company')
    SaleChannel = pool.get('sale.channel')
    Location = pool.get('stock.location')
    Currency = pool.get('currency.currency')

    websites = Website.search([('name', '=', name)])
    if websites:
        return websites[0]

    companies = Company.search([])
    if companies:
        company = companies[0]
    else:
        company = create_company()

    User.write(
        [User(USER)], {
            'main_company': company.id,
            'company': company.id,
            })

    Transaction().context.update(
        User.get_preferences(context_only=True))

    create_sale_channels(company)
    channel1, channel2, channel3, channel4 = SaleChannel.search(
        [], order=[('code', 'ASC')])

    User.set_preferences({'current_channel': channel1})
    channel_price_list, user_price_list = create_pricelists()

    warehouse, = Location.search([
            ('type', '=', 'warehouse'),
            ])
    with Transaction().set_context(company=company.id):
        channel1.price_list = channel_price_list
        channel1.invoice_method = 'order'
        channel1.shipment_method = 'order'
        channel1.source = 'webshop'
        channel1.create_users = [USER]
        channel1.warehouse = warehouse
        channel1.save()

        usd, = Currency.create([{
                    'name': 'US Dollar',
                    'code': 'USD',
                    'symbol': '$',
                    }])
    party1, = Party.create([{
        'name': 'Guest User',
    }])
    party2, = Party.create([{
        'name': 'Registered User 1',
        'sale_price_list': user_price_list,
        'addresses': [('create', [{
            'name': 'Address1',
        }])],
    }])
    party3, = Party.create([{
        'name': 'Registered User 2',
    }])

    guest_user, = NereidUser.create([{
        'party': party1.id,
        'name': 'Guest User',
        'email': 'guest@m9s.biz',
        'password': 'password',
        'company': company.id,
    }])
    registered_user, = NereidUser.create([{
        'party': party2.id,
        'name': 'Registered User',
        'email': 'email@example.com',
        'password': 'password',
        'company': company.id,
    }])
    registered_user2, = NereidUser.create([{
        'party': party3.id,
        'name': 'Registered User 2',
        'email': 'email2@example.com',
        'password': 'password2',
        'company': company.id,
    }])

    if not locales:
        locale = create_website_locale()
        locales = [locale.id]
        default_locale = locale
    else:
        locales = [l for l in locales]

    if default_locale is None:
        default_locale = locales[0]

    website = Website()
    website.name = name
    website.company = company
    website.application_user = USER
    website.default_locale = default_locale
    website.locales = locales
    website.guest_user = guest_user
    website.channel = channel1
    website.currencies = [usd]
    return website


def create_countries(count=5):
    """
    Create some sample countries and subdivisions
    """
    pool = Pool()
    Subdivision = pool.get('country.subdivision')
    Country = pool.get('country.country')

    for country in list(pycountry.countries)[0:count]:
        countries = Country.create([{
            'name': country.name,
            'code': country.alpha_2,
        }])
        try:
            divisions = pycountry.subdivisions.get(
                country_code=country.alpha_2
            )
        except KeyError:
            pass
        else:
            for subdivision in list(divisions)[0:count]:
                Subdivision.create([{
                    'country': countries[0].id,
                    'name': subdivision.name,
                    'code': subdivision.code,
                    'type': subdivision.type.lower(),
                }])


def create_pricelists(party_pl_margin=None, guest_pl_margin=None):
    """
    Create the pricelists
    """
    pool = Pool()
    PriceList = pool.get('product.price_list')
    Company = pool.get('company.company')

    if party_pl_margin is None:
        party_pl_margin = Decimal('1.10')
    if guest_pl_margin is None:
        guest_pl_margin = Decimal('1.20')
    # Setup the pricelists
    company, = Company.search([])
    user_price_list, = PriceList.create([{
        'name': 'PL 1',
        'company': company.id,
        'lines': [
            ('create', [{
                'formula': 'unit_price * %s' % party_pl_margin
            }])
        ],
    }])
    guest_price_list, = PriceList.create([{
        'name': 'PL 2',
        'company': company.id,
        'lines': [
            ('create', [{
                'formula': 'unit_price * %s' % guest_pl_margin
            }])
        ],
    }])
    return guest_price_list.id, user_price_list.id


def create_product_template(name, vlist, uri, uom='Unit'):
    """
    Create a product template with products and return its ID

    :param name: Name of the product
    :param vlist: List of dictionaries of values to create
    :param uri: uri of product template
    :param uom: Note it is the name of UOM (not symbol or code)
    """
    pool = Pool()
    Template = pool.get('product.template')
    Category = pool.get('product.category')
    Uom = pool.get('product.uom')
    Account = pool.get('account.account')
    Company = pool.get('company.company')

    company, = Company.search([])
    with set_company(company):
        revenue, = Account.search([
                ('type.revenue', '=', True),
                ])
        expense, = Account.search([
                ('type.expense', '=', True),
                ])

    with Transaction().set_context(company=company.id):
        category = Category()
        category.name = 'Account category'
        category.account_revenue = revenue
        category.account_expense = expense
        category.accounting = True
        category.save()

    uom, = Uom.search([('name', '=', uom)])
    for values in vlist:
        values['name'] = name
        values['default_uom'] = uom
        values['sale_uom'] = uom
        values['account_category'] = category
        values['products'] = [
            ('create', [{
                'uri': uri,
                'displayed_on_eshop': True,
                'cost_price': Decimal('5'),
            }])
        ]
    return Template.create(vlist)


class NereidCartB2CTestCase(NereidModuleTestCase):
    'Test Nereid Cart B2C module'
    module = 'nereid_cart_b2c'

    def setUp(self):
        self.templates = {
            'home.jinja': '{{get_flashed_messages()}}',
            'login.jinja':
                '{{ login_form.errors }} {{get_flashed_messages()}}',
            'shopping-cart.jinja':
                'Cart:{{ cart.id }},{{get_cart_size()|round|int}},'
                '{{cart.sale.total_amount}}',
            'product.jinja':
                '{{ product.sale_price(product.id) }}',
            }

    @with_transaction()
    def test_0005_user_status(self):
        """
        Test that `_user_status()` returns a dictionary
        with correct params.
        """
        pool = Pool()
        Company = pool.get('company.company')
        SaleLine = pool.get('sale.line')
        Channel = pool.get('sale.channel')
        Product = pool.get('product.product')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )

        app = self.get_app()
        with app.test_client() as c:
            response = c.post(
                '/en/login',
                data={
                    'email': 'email@example.com',
                    'password': 'password',
                    }
                )
            self.assertEqual(response.status_code, 302)  # Login success

            product, = Product.search([('name', '=', 'product-1')])

            rv = c.post(
                '/en/cart/add',
                data={
                    'product': product.id, 'quantity': 7
                }
            )
            self.assertEqual(rv.status_code, 302)

            results = c.get('/en/user_status')
            data = json.loads(results.data)
            lines = data['status']['cart']['lines']

            self.assertEqual(len(lines), 1)
            line, = SaleLine.search([])
            self.assertEqual(line.serialize('cart'), lines[0])

    @with_transaction()
    def test_0010_test_guest_price(self):
        """
        Test the pricelist lookup algorithm

        We are not logged in, the pricelist of the channel is used.
        """
        pool = Pool()
        Company = pool.get('company.company')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )
        template2, = create_product_template(
            'product-2',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('15'),
            }],
            uri='product-2',
        )

        party_pl_margin = Decimal('1.10')
        guest_pl_margin = Decimal('1.20')

        app = self.get_app()
        with app.test_client() as c:
            rv = c.get('/en/product/product-1')
            self.assertEqual(
                Decimal(rv.data.decode('utf-8')),
                Decimal('10') * guest_pl_margin)

            rv = c.get('/en/product/product-2')
            self.assertEqual(
                Decimal(rv.data.decode('utf-8')),
                Decimal('15') * guest_pl_margin)



    @with_transaction()
    def test_0020_test_party_price(self):
        """
        Test the pricelist lookup algorithm when a price is defined on party
        """
        pool = Pool()
        Company = pool.get('company.company')
        SaleLine = pool.get('sale.line')
        Channel = pool.get('sale.channel')
        Product = pool.get('product.product')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )
        template2, = create_product_template(
            'product-2',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('15'),
            }],
            uri='product-2',
        )

        party_pl_margin = Decimal('1.10')
        guest_pl_margin = Decimal('1.20')

        app = self.get_app()
        with app.test_client() as c:
            response = c.post(
                '/en/login',
                data={
                    'email': 'email@example.com',
                    'password': 'password',
                    }
                )
            self.assertEqual(response.status_code, 302)  # Login success

            rv = c.get('/en/product/product-1')
            self.assertEqual(
                Decimal(rv.data.decode('utf-8')), Decimal('10') * party_pl_margin
            )
            rv = c.get('/en/product/product-2')
            self.assertEqual(
                Decimal(rv.data.decode('utf-8')), Decimal('15') * party_pl_margin
            )

    @with_transaction()
    def test_0030_test_guest_price_fallback(self):
        """
        Test the pricelist lookup algorithm if it falls back to guest pricing
        if a price is NOT specified for a party.
        """
        pool = Pool()
        Company = pool.get('company.company')
        SaleLine = pool.get('sale.line')
        Channel = pool.get('sale.channel')
        Product = pool.get('product.product')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )
        template2, = create_product_template(
            'product-2',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('15'),
            }],
            uri='product-2',
        )

        party_pl_margin = Decimal('1.10')
        guest_pl_margin = Decimal('1.20')

        app = self.get_app()
        with app.test_client() as c:
            response = c.post(
                '/en/login',
                data={
                    'email': 'email2@example.com',
                    'password': 'password2',
                    }
                )
            self.assertEqual(response.status_code, 302)  # Login success

            rv = c.get('/en/product/product-1')
            self.assertEqual(
                Decimal(rv.data.decode('utf-8')), Decimal('10') * guest_pl_margin
            )
            rv = c.get('/en/product/product-2')
            self.assertEqual(
                Decimal(rv.data.decode('utf-8')), Decimal('15') * guest_pl_margin
            )

    @with_transaction()
    def test_0040_availability(self):
        """
        Test the availability returned for the products
        """
        pool = Pool()
        Company = pool.get('company.company')
        StockMove = pool.get('stock.move')
        Location = pool.get('stock.location')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )
        template2, = create_product_template(
            'product-2',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('15'),
            }],
            uri='product-2',
        )

        product1 = template1.products[0]
        product2 = template2.products[0]
        party_pl_margin = Decimal('1.10')
        guest_pl_margin = Decimal('1.20')

        app = self.get_app()
        with app.test_client() as c:
            rv = c.get('/en/product-availability/product-1')
            availability = json.loads(rv.data)
            self.assertEqual(availability['quantity'], 0.00)
            self.assertEqual(availability['forecast_quantity'], 0.00)

        supplier, = Location.search([('code', '=', 'SUP')])
        stock1, = StockMove.create([{
            'product': product1.id,
            'uom': template1.sale_uom.id,
            'quantity': 10,
            'from_location': supplier,
            'to_location': website.stock_location.id,
            'company': website.company.id,
            'unit_price': Decimal('1'),
            'currency': website.currencies[0].id,
            'planned_date': datetime.date.today(),
            'effective_date': datetime.date.today(),
            'state': 'draft',
        }])
        stock2, = StockMove.create([{
            'product': product1.id,
            'uom': template1.sale_uom.id,
            'quantity': 10,
            'from_location': supplier,
            'to_location': website.stock_location.id,
            'company': website.company.id,
            'unit_price': Decimal('1'),
            'currency': website.currencies[0].id,
            'planned_date': datetime.date.today() + relativedelta(days=1),
            'effective_date': datetime.date.today() + relativedelta(days=1),
            'state': 'draft'
        }])
        StockMove.write([stock1], {
            'state': 'done'
        })

        locations = Location.search([('type', '=', 'storage')])

        with app.test_client() as c:
            with Transaction().set_context(
                    {'locations': list(map(int, locations))}):
                rv = c.get('/en/product-availability/product-1')
                availability = json.loads(rv.data)
                self.assertEqual(availability['forecast_quantity'], 20.00)
                self.assertEqual(availability['quantity'], 10.00)

    @with_transaction()
    def test_0050_product_serialize(self):
        """
        Test the serialize() method.
        """
        pool = Pool()
        Company = pool.get('company.company')
        StockMove = pool.get('stock.move')
        Location = pool.get('stock.location')
        Uom = pool.get('product.uom')
        Media = pool.get('product.media')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])
        uom, = Uom.search([], limit=1)

        file_memoryview = memoryview(b'test')
        file1 = create_static_file(file_memoryview, name='test.png')
        file_memoryview = memoryview(b'test-again')
        file2 = create_static_file(file_memoryview, name='test-again.png')


        template, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )
        product = template.products[0]

        product_media1 = Media(**{
            'static_file': file1.id,
            'product': product.id,
        })
        product_media1.save()
        template.media = [product_media1]
        template.save()

        product_media2 = Media(**{
            'static_file': file2.id,
            'product': product.id,
        })
        product_media2.save()

        qty = 7

        app = self.get_app()
        # Without login
        with app.test_client() as c:
            c.post(
                '/en/cart/add',
                data={
                    'product': product.id,
                    'quantity': qty,
                }
            )
            rv = c.get('/en/user_status')
            data = json.loads(rv.data)

            lines = data['status']['cart']['lines']

            self.assertEqual(lines[0]['product']['id'], product.id)
            self.assertTrue(lines[0]['product']['image'] is not None)
            self.assertEqual(
                lines[0]['display_name'], product.name
            )

        # With login
        with app.test_client() as c:
            response = c.post(
                '/en/login',
                data={
                    'email': 'email@example.com',
                    'password': 'password',
                    }
                )
            self.assertEqual(response.status_code, 302)  # Login success
            c.post(
                '/en/cart/add',
                data={
                    'product': product.id,
                    'quantity': qty,
                }
            )
            rv = c.get('/en/user_status')
            data = json.loads(rv.data)

            lines = data['status']['cart']['lines']

            self.assertEqual(lines[0]['product']['id'], product.id)
            self.assertTrue(lines[0]['product']['image'] is not None)
            self.assertEqual(
                lines[0]['url'],
                product.get_absolute_url(_external=True)
            )
            self.assertEqual(
                lines[0]['display_name'], product.name
            )

    @with_transaction()
    def test_0060_warehouse_quantity(self):
        """
        Test that the sale of a product is affected by availability
        and warehouse quantity.
        """
        pool = Pool()
        Company = pool.get('company.company')
        StockMove = pool.get('stock.move')
        Location = pool.get('stock.location')
        SaleLine = pool.get('sale.line')

        # Setup defaults
        # A gateway sets up a lot of configuration stuff (fiscalyear, chart,
        # etc.)
        website = create_website()
        website.save()
        gateway = create_payment_gateway()
        gateway.save()
        company, = Company.search([])

        # Create product templates with products
        template1, = create_product_template(
            'product-1',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('10'),
            }],
            uri='product-1',
        )
        template2, = create_product_template(
            'product-2',
            [{
                'type': 'goods',
                'salable': True,
                'list_price': Decimal('15'),
            }],
            uri='product-2',
        )

        product1 = template1.products[0]
        product2 = template2.products[0]
        party_pl_margin = Decimal('1.10')
        guest_pl_margin = Decimal('1.20')

        app = self.get_app()
        with app.test_client() as c:
            rv = c.get('/en/product-availability/product-1')
            availability = json.loads(rv.data)
            self.assertEqual(availability['quantity'], 0.00)
            self.assertEqual(availability['forecast_quantity'], 0.00)

        supplier, = Location.search([('code', '=', 'SUP')])
        stock1, = StockMove.create([{
            'product': product1.id,
            'uom': template1.sale_uom.id,
            'quantity': 10,
            'from_location': supplier,
            'to_location': website.stock_location.id,
            'company': website.company.id,
            'unit_price': Decimal('1'),
            'currency': website.currencies[0].id,
            'planned_date': datetime.date.today(),
            'effective_date': datetime.date.today(),
            'state': 'draft',
        }])
        StockMove.write([stock1], {
            'state': 'done'
        })

        headers = Headers([('Referer', '/')])

        self.assertEqual(product1.is_backorder, True)

        # Set product warehouse quantity
        product1.min_warehouse_quantity = 11
        product1.save()

        self.assertEqual(product1.is_backorder, False)

        with app.test_client() as c:
            response = c.post(
                '/en/login',
                data={
                    'email': 'email@example.com',
                    'password': 'password',
                    }
                )
            self.assertEqual(response.status_code, 302)  # Login success

            rv = c.post(
                '/en/cart/add',
                data={
                    'product': product1.id, 'quantity': 5
                },
                headers=headers
            )
            # Cannot add to cart, available quantity < warehouse quantity
            self.assertTrue(rv.location.endswith('/'))
            self.assertEqual(rv.status_code, 302)
            self.assertEqual(SaleLine.search([], count=True), 0)

        # Try a service product
        product1.template.type = 'service'
        product1.template.save()

        with app.test_client() as c:
            response = c.post(
                '/en/login',
                data={
                    'email': 'email@example.com',
                    'password': 'password',
                    }
                )
            self.assertEqual(response.status_code, 302)  # Login success

            rv = c.post(
                '/en/cart/add',
                data={
                    'product': product1.id, 'quantity': 5
                },
            )
            # Add to cart proceeds normally
            self.assertTrue(rv.location.endswith('/cart'))
            self.assertEqual(rv.status_code, 302)
            self.assertEqual(SaleLine.search([], count=True), 1)


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            NereidCartB2CTestCase))
    return suite

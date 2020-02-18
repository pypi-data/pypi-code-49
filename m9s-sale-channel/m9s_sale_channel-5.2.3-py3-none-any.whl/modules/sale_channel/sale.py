# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, Unique
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval, Or, Bool, If

from trytond.i18n import gettext
from trytond.exceptions import UserError


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    #: A many2one field decides to which channel this sale
    #: belongs to. This helps filling lot of default values on sale.
    channel = fields.Many2One(
        'sale.channel', 'Channel', required=True, select=True, domain=[
            ('id', 'in', If(
                Eval('id', 0) > 0,
                Eval('context', {}).get('allowed_read_channels', []),
                Eval('context', {}).get('allowed_create_channels', [])
            )),
        ],
        states={
            'readonly': Or(
                (Eval('id', 0) > 0),
                Bool(Eval('lines', [])),
            )
        }, depends=['id']
    )

    #: Function field which return source of the channel this sale belongs
    #: to.
    channel_type = fields.Function(
        fields.Char('Channel Type'), 'on_change_with_channel_type'
    )

    #: Boolean function field returns true if sale has any exception.
    has_channel_exception = fields.Function(
        fields.Boolean('Has Channel Exception ?'), 'get_has_channel_exception',
        searcher='search_has_channel_exception'
    )

    #: One2Many to channel exception, lists all the exceptions.
    exceptions = fields.One2Many(
        "channel.exception", "origin", "Exceptions"
    )

    # XXX: to identify sale order in external channel
    channel_identifier = fields.Char(
        'Channel Identifier', readonly=True, select=True
    )

    @classmethod
    def __setup__(cls):
        super(Sale, cls).__setup__()
        table = cls.__table__()
        cls._sql_constraints += [(
            'origin_channel_identifier',
            Unique(table, table.channel, table.channel_identifier),
            'Channel identifier for a channel should be unique'
        )]
        cls.payment_authorize_on.states = cls.channel.states
        cls.payment_capture_on.states = cls.channel.states

    @classmethod
    def default_payment_authorize_on(cls):
        pool = Pool()
        Channel = pool.get('sale.channel')
        if Transaction().context.get('current_channel'):
            channel = Channel(Transaction().context['current_channel'])
            if channel.payment_authorize_on:
                return channel.payment_authorize_on
        return super(Sale, cls).default_payment_authorize_on()

    @classmethod
    def default_payment_capture_on(cls):
        pool = Pool()
        Channel = pool.get('sale.channel')
        if Transaction().context.get('current_channel'):
            channel = Channel(Transaction().context['current_channel'])
            if channel.payment_capture_on:
                return channel.payment_capture_on
        return super(Sale, cls).default_payment_capture_on()

    @classmethod
    def view_attributes(cls):
        return super(Sale, cls).view_attributes() + [
            ('//page[@name="exceptions"]', 'states', {
                    'invisible': Eval('channel_type') == 'manual',
                    })]

    @classmethod
    def search_has_channel_exception(cls, name, clause):
        """
        Returns domain for sale with exceptions
        """
        if clause[2]:
            return [('exceptions.is_resolved', '=', False)]
        else:
            return [
                'OR',
                [('exceptions', '=', None)],
                [('exceptions.is_resolved', '=', True)],
            ]

    def get_channel_exceptions(self, name=None):
        pool = Pool()
        ChannelException = pool.get('channel.exception')

        return list(map(
            int, ChannelException.search([
                ('origin', '=', '%s,%s' % (self.__name__, self.id)),
                ('channel', '=', self.channel.id),
            ], order=[('is_resolved', 'desc')])
        ))

    @classmethod
    def set_channel_exceptions(cls, exceptions, name, value):
        pass

    def get_has_channel_exception(self, name):
        """
        Returs True if sale has exception
        """
        pool = Pool()
        ChannelException = pool.get('channel.exception')

        return bool(
            ChannelException.search([
                ('origin', '=', '%s,%s' % (self.__name__, self.id)),
                ('channel', '=', self.channel.id),
                ('is_resolved', '=', False)
            ])
        )

    @classmethod
    def default_channel(cls):
        pool = Pool()
        User = pool.get('res.user')

        user = User(Transaction().user)
        channel_id = Transaction().context.get('current_channel')
        if channel_id:
            return channel_id
        return user.current_channel and \
            user.current_channel.id  # pragma: nocover

    @staticmethod
    def default_company():
        pool = Pool()
        Sale = pool.get('sale.sale')
        Channel = pool.get('sale.channel')

        channel_id = Sale.default_channel()
        if channel_id:
            return Channel(channel_id).company.id

        return Transaction().context.get('company')  # pragma: nocover

    @staticmethod
    def default_invoice_method():
        pool = Pool()
        Sale = pool.get('sale.sale')
        Channel = pool.get('sale.channel')
        Config = pool.get('sale.configuration')

        channel_id = Sale.default_channel()
        if not channel_id:  # pragma: nocover
            config = Config(1)
            return config.sale_invoice_method

        return Channel(channel_id).invoice_method

    @staticmethod
    def default_shipment_method():
        pool = Pool()
        Sale = pool.get('sale.sale')
        Channel = pool.get('sale.channel')
        Config = pool.get('sale.configuration')

        channel_id = Sale.default_channel()
        if not channel_id:  # pragma: nocover
            config = Config(1)
            return config.sale_invoice_method

        return Channel(channel_id).shipment_method

    @staticmethod
    def default_warehouse():
        pool = Pool()
        Sale = pool.get('sale.sale')
        Channel = pool.get('sale.channel')
        Location = pool.get('stock.location')

        channel_id = Sale.default_channel()
        if not channel_id:  # pragma: nocover
            return Location.search([('type', '=', 'warehouse')], limit=1)[0].id
        else:
            return Channel(channel_id).warehouse.id

    @staticmethod
    def default_price_list():
        pool = Pool()
        Sale = pool.get('sale.sale')
        Channel = pool.get('sale.channel')

        channel_id = Sale.default_channel()
        if channel_id:
            return Channel(channel_id).price_list.id
        return None  # pragma: nocover

    @staticmethod
    def default_payment_term():
        pool = Pool()
        Sale = pool.get('sale.sale')
        Channel = pool.get('sale.channel')

        channel_id = Sale.default_channel()
        if channel_id:
            return Channel(channel_id).payment_term.id
        return None  # pragma: nocover

    @fields.depends(
        'channel', 'party', 'company', 'currency', 'payment_term', 'warehouse'
    )
    def on_change_channel(self):
        pool = Pool()
        SaleConfiguration = pool.get('sale.configuration')

        if not self.channel:
            return

        for fname in ('company', 'warehouse', 'currency', 'payment_term'):
            setattr(self, fname, getattr(self.channel, fname))

        if (not self.party or not self.party.sale_price_list):
            self.price_list = self.channel.price_list.id  # pragma: nocover
        if self.channel.invoice_method:
            self.invoice_method = self.channel.invoice_method
        if self.channel.shipment_method:
            self.shipment_method = self.channel.shipment_method
        if self.channel.payment_authorize_on:
            self.payment_authorize_on = self.channel.payment_authorize_on
        else:
            self.payment_authorize_on = \
                SaleConfiguration(1).payment_authorize_on
        if self.channel.payment_capture_on:
            self.payment_capture_on = self.channel.payment_capture_on
        else:
            self.payment_capture_on = SaleConfiguration(1).payment_capture_on

    @fields.depends('channel')
    def on_change_party(self):  # pragma: nocover
        super(Sale, self).on_change_party()
        if self.channel:
            if not self.price_list and self.invoice_address:
                self.price_list = self.channel.price_list.id
                self.price_list.rec_name = self.channel.price_list.rec_name
            if not self.payment_term and self.invoice_address:
                self.payment_term = self.channel.payment_term.id

    @fields.depends('channel')
    def on_change_with_channel_type(self, name=None):
        """
        Returns the source of the channel
        """
        if self.channel:
            return self.channel.source

    @classmethod
    def validate(cls, sales):
        super(Sale, cls).validate(sales)
        for sale in sales:
            sale.check_create_access()

    def check_create_access(self, silent=False):
        """
            Check sale creation in channel
        """
        pool = Pool()
        User = pool.get('res.user')
        user = User(Transaction().user)

        if user.id == 0:
            return  # pragma: nocover
        if self.channel not in user.allowed_create_channels:
            if silent:
                return False
            raise UserError(gettext('sale_channel.channel_not_allowed'))
        if self.channel and not self.__class__.default_channel():
                raise UserError(gettext('sale_channel.channel_missing',
                        user.rec_name))
        return True

    @classmethod
    def copy(cls, sales, default=None):
        """
        Duplicating records
        """
        if default is None:
            default = {}

        for sale in sales:
            if not sale.check_create_access(True):
                default['channel'] = cls.default_channel()

        default['channel_identifier'] = None
        default['exceptions'] = None

        return super(Sale, cls).copy(sales, default=default)


    def process_to_channel_state(self, channel_state):
        """
        Process the sale in tryton based on the state of order
        when its imported from channel.

        :param channel_state: State on external channel the order was imported.
        """
        pool = Pool()
        Sale = pool.get('sale.sale')
        Payment = pool.get('sale.payment')

        data = self.channel.get_tryton_action(channel_state)

        if self.state == 'draft':
            self.invoice_method = data['invoice_method']
            self.shipment_method = data['shipment_method']
            self.save()

        if data['action'] in ['process_manually', 'process_automatically']:
            if self.state == 'draft':
                Sale.quote([self])
            if self.state == 'quotation':
                Sale.confirm([self])

        if data['action'] == 'process_automatically' and \
                self.state == 'confirmed':
            Sale.process([self])

        if data['action'] == 'import_as_past' and self.state == 'draft':
            Payment.delete(self.payments)
            # XXX: mark past orders as completed
            self.state = 'done'
            self.save()
            # Update cached values
            Sale.store_cache([self])


class SaleLine(metaclass=PoolMeta):
    "Sale Line"
    __name__ = 'sale.line'

    # XXX: to identify sale order item in external channel
    channel_identifier = fields.Char('Channel Identifier', readonly=True)

    def create_payment_from(self, payment_data):
        """
        Create sale payment using given data.

        Since external channels are implemented by downstream modules, it is
        the responsibility of those channels to reuse this method.

        :param payment_data: Dictionary which must have at least one key-value
                                pair for 'code'
        """
        raise NotImplementedError(
            "This feature has not been implemented for %s channel yet."
            % self.source)

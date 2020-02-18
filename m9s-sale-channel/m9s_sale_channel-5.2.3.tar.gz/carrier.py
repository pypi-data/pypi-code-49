# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval


class SaleChannelCarrier(ModelSQL, ModelView):
    """
    Shipping Carriers

    This model stores the carriers / shipping methods, each record
    here can be mapped to a carrier in tryton which will then be
    used for managing export of tracking info.
    """
    __name__ = 'sale.channel.carrier'
    _rec_name = 'name'

    name = fields.Char('Name')
    code = fields.Char("Code")
    carrier = fields.Many2One('carrier', 'Carrier')
    carrier_service = fields.Many2One(
        'carrier.service', 'Service', domain=[(
            ('id', 'in', Eval('available_carrier_services'))
        )],
        depends=['available_carrier_services']
    )
    available_carrier_services = fields.Function(
        fields.One2Many("carrier.service", None, 'Available Carrier Services'),
        getter="on_change_with_available_carrier_services"
    )
    channel = fields.Many2One(
        'sale.channel', 'Channel', readonly=True
    )

    @fields.depends('carrier')
    def on_change_with_available_carrier_services(self, name=None):
        if self.carrier:
            return [s.id for s in self.carrier.services]
        return []

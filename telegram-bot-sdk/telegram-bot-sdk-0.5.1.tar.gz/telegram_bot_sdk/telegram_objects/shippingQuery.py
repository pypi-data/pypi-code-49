from telegram_bot_sdk.telegram_objects.shippingAddress import ShippingAddress
from telegram_bot_sdk.telegram_objects.user import User


class ShippingQuery:
    """This class contains information about an incoming shipping query

    :param id_unique: Unique query identifier
    :type id_unique: str
    :param from_user: User who sent the query
    :type from_user: :ref:`object_user`
    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: str
    :param shipping_address: User specified shipping address
    :type shipping_address: :ref:`object_shipping_address`
    """
    def __init__(self, *, id_unique=None, from_user=None, invoice_payload=None, shipping_address=None):
        self.id_unique = id_unique
        self.from_user = User(**from_user) if from_user else None
        self.invoice_payload = invoice_payload
        self.shipping_address = ShippingAddress(**shipping_address) if shipping_address else None

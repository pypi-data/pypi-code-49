from telegram_bot_sdk.telegram_objects.shippingAddress import ShippingAddress


class OrderInfo:
    """This class represents information about an order

    :param name: Optional: User name
    :type name: str
    :param phone_number: Optional: User's phone number
    :type phone_number: str
    :param email: Optional: User email
    :type email: str
    :param shipping_address: Optional: User shipping address
    :type shipping_address: :ref:`object_shipping_address`
    """
    def __init__(self, *, name=None, phone_number=None, email=None, shipping_address=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = ShippingAddress(**shipping_address) if shipping_address else None

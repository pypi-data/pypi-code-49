from telegram_bot_sdk.telegram_objects.orderInfo import OrderInfo
from telegram_bot_sdk.telegram_objects.user import User


class PreCheckoutQuery:
    """This class contains information about an incoming pre-checkout query

    :param id_unique: Unique query identifier
    :type id_unique: str
    :param from_user: User who sent the query
    :type from_user: :ref:`object_user`
    :param currency: Three-letter ISO 4217 currency code
    :type currency: str
    :param total_amount: Total price in the smallest units of the currency (int not float/double)
    :type total_amount: int
    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: str
    :param shipping_option_id: Optional: Identifier of the shipping option chosen by the user
    :type shipping_option_id: str
    :param order_info: Optional: Order info provided by the user
    :type order_info: :ref:`object_order_info`
    """
    def __init__(self, *, id_unique=None, from_user=None, currency=None, total_amount=None, invoice_payload=None,
                 shipping_option_id=None, order_info=None):
        self.id_unique = id_unique
        self.from_user = User(**from_user) if from_user else None
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = OrderInfo(**order_info) if order_info else None

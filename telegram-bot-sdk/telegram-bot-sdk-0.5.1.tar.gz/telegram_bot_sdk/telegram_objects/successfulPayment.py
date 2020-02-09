from telegram_bot_sdk.telegram_objects.orderInfo import OrderInfo


class SuccessfulPayment:
    """This class contains basic information about a successful payment

    :param currency: Three-letter ISO 4217 currency code
    :type currency: str
    :param total_amount: Total price in the smallest units of the currency (int not float/double)
    :type total_amount: int
    :param invoice_payload: Bot specified invoice payload
    :type invoice_payload: str
    :param telegram_payment_charge_id: Telegram payment identifier
    :type telegram_payment_charge_id: str
    :param provider_payment_charge_id: Provider payment identifier
    :type provider_payment_charge_id: str
    :param shipping_option_id: Optional: Identifier of the shipping option chosen by the user
    :type shipping_option_id: str
    :param order_info: Optional: Order info provided by the user
    :type order_info: :ref:`object_order_info`
    """
    def __init__(self, currency, total_amount, invoice_payload, telegram_payment_charge_id,
                 provider_payment_charge_id=None, shipping_option_id=None, order_info=None):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        self.shipping_option_id = shipping_option_id
        self.order_info = OrderInfo(**order_info) if order_info else None

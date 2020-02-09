from telegram_bot_sdk.telegram_objects.callbackQuery import CallbackQuery
from telegram_bot_sdk.telegram_objects.message import Message
from telegram_bot_sdk.telegram_objects.inlineQuery import InlineQuery
from telegram_bot_sdk.telegram_objects.chosenInlineResult import ChosenInlineResult
from telegram_bot_sdk.telegram_objects.poll import Poll
from telegram_bot_sdk.telegram_objects.preCheckoutQuery import PreCheckoutQuery
from telegram_bot_sdk.telegram_objects.shippingQuery import ShippingQuery


class Update:
    """This class represents an incoming update
    
    :param update_id: The update's unique identifier. Update identifiers start from a certain positive number \
    and increase sequentially. If there are no new updates for at least a week, then identifier of the next update \
    will be chosen randomly instead of sequentially.
    :type update_id: int
    :param message: Optional: New incoming message of any kind
    :type message: :ref:`object_message`
    :param edited_message: Optional: New version of a message that is known to the bot and was edited
    :type edited_message: :ref:`object_message`
    :param channel_post: Optional: New incoming channel post of any kind
    :type channel_post: :ref:`object_message`
    :param edited_channel_post: Optional: New version of a channel post that is known to the bot and was edited
    :type edited_channel_post: :ref:`object_message`
    :param inline_query: Optional: New incoming query
    :type inline_query: :ref:`object_inline_query`
    :param chosen_inline_result: Optional: The result of an inline query that was chosen by a user and sent to their \
    chat partner
    :type chosen_inline_result: :ref:`object_chosen_inline_result`
    :param callback_query: Optional: New incoming callback query
    :type callback_query: :ref:`object_callback_query`
    :param shipping_query: Optional: New incoming shipping query. Only for invoices with flexible price
    :type shipping_query: :ref:`object_shipping_query`
    :param pre_checkout_query: Optional: New incoming pre-checkout query. Contains full information about checkout
    :type pre_checkout_query: :ref:`object_pre_checkout_query`
    :param poll: Optional: New poll state. Bots receive only updates about stopped polls and polls, which are sent \
    by the bot
    :type poll: :ref:`object_poll`
    """
    def __init__(self, *, update_id, message=None, edited_message=None, channel_post=None,
                 edited_channel_post=None, inline_query=None, chosen_inline_result=None, callback_query=None,
                 shipping_query=None, pre_checkout_query=None, poll=None):
        self.update_id = update_id
        self.message = Message(**message) if message else None
        self.edited_message = Message(**edited_message) if edited_message else None
        self.channel_post = Message(**channel_post) if channel_post else None
        self.edited_channel_post = Message(**edited_channel_post) if edited_channel_post else None
        self.inline_query = InlineQuery(**inline_query) if inline_query else None
        self.chosen_inline_result = ChosenInlineResult(**chosen_inline_result) if chosen_inline_result else None
        self.callback_query = CallbackQuery(**callback_query) if callback_query else None
        self.shipping_query = ShippingQuery(**shipping_query) if shipping_query else None
        self.pre_checkout_query = PreCheckoutQuery(**pre_checkout_query) if pre_checkout_query else None
        self.poll = Poll(**poll) if poll else None

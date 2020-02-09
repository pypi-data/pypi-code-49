from telegram_bot_sdk.telegram_objects.inlineKeyboardButton import InlineKeyboardButton


class InlineKeyboardMarkup:
    """This class represents an inline keyboard that appears right next to the message it belongs to

    :param inline_keyboard: List of button rows, each represented by a list of :ref:`object_inline_keyboard_button` \
    objects
    :type inline_keyboard: list of list of :ref:`object_inline_keyboard_button`
    """
    def __init__(self, *, inline_keyboard):
        self.inline_keyboard = [InlineKeyboardButton(**y) for y in [x for x in inline_keyboard]]

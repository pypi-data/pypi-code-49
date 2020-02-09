from telegram_bot_sdk.telegram_objects.callbackGame import CallbackGame
from telegram_bot_sdk.telegram_objects.loginUrl import LoginUrl


class InlineKeyboardButton:
    """This class represents one button of an inline keyboard. You *must* use exactly one of the optional fields

    :param text: Label text on the button
    :type text:
    :param url: Optional: HTTP or tg:// url to be opened when button is pressed
    :type url: str
    :param login_url: Optional: An HTTP URL user to automatically authorize the user
    :type login_url: :ref:`object_login_url`
    :param callback_data: Optional: Data to be sent in a :ref:`object_callback_query` to the bot when button is \
    pressed, 1-64 bytes
    :type callback_data: str
    :param switch_inline_query: Optional: If set, pressing the button will prompt the user to select one of their \
    chats, open that chat and insert the bot‘s username and the specified inline query in the input field. Can be \
    empty, in which case just the bot’s username will be inserted.
    :type switch_inline_query: str
    :param switch_inline_query_current_chat: Optional: If set, pressing the button will insert the bot's username \
    and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's \
    username will be inserted.
    :type switch_inline_query_current_chat: str
    :param callback_game: Optional: Description if the game that will be launched when the user presses the button. \
    *Note:* This button *must* be always be the first button in the first row
    :type callback_game: :ref:`object_callback_game`
    :param pay: Optional: Specify True, to send a Pay Button
    :type pay: bool
    """
    def __init__(self, *, text, url=None, login_url=None, callback_data=None, switch_inline_query=None,
                 switch_inline_query_current_chat=None, callback_game=None, pay=None):
        self.text = text
        self.url = url
        self.login_url = LoginUrl(**login_url) if login_url else None
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = CallbackGame() if callback_game else None
        self.pay = pay

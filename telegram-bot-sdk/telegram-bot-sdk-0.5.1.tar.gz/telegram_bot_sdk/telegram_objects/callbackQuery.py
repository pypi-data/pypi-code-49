from telegram_bot_sdk.telegram_objects.message import Message
from telegram_bot_sdk.telegram_objects.user import User


class CallbackQuery:
    """This object represents an incoming callback query from a callback button in an inline keyboard.
    * If the button that originated the query was attached to a message sent by the bot, the field message will be \
    present.
    * If the button was attached to a message sent via the bot the field inline_message_id will be present
    * Exactly one of the field data or game_short_name will be present

    :param id_unique: Unique identifier for this query
    :type id_unique: str
    :param from_user: Specifies the sender
    :type from_user: :ref:`object_user`
    :param message: Optional: Message with the callback button that originated the query
    :type message: :ref:`object_message`
    :param inline_message_id: Optional: Identifier of the message sent via the bot in inline mode, that originated the \
    query
    :type inline_message_id: str
    :param chat_instance: Optional: Global identifier, uniquely corresponding to the chat which the message with the \
    callback button was sent
    :type chat_instance: str
    :param data: Optional: Data associated with the callback button.
    :type data: str
    :param game_short_name: Optional: Short name of a :ref:`object_game` to be returned, serves as the unique \
    identifier for the game
    :type game_short_name: str
    """
    def __init__(self, *, id_unique, from_user, message=None, inline_message_id=None, chat_instance=None, data=None,
                 game_short_name=None):
        self.id_unique = id_unique
        self.from_user = User(**from_user)
        self.message = Message(**message) if message else None
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

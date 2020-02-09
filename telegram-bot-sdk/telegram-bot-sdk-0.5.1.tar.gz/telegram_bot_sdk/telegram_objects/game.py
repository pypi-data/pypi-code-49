from telegram_bot_sdk.telegram_objects.animation import Animation
from telegram_bot_sdk.telegram_objects.messageEntity import MessageEntity
from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class Game:
    """This class represents a game. Use the Botfather to create and edit games, their short names, will act as unique
    identifier

    :param title: Title of the game
    :type title: str
    :param description: Description of the game
    :type description: str
    :param photo: Photo that will be displayed in the game message in chats
    :type photo: list of :ref:`object_photo_size`
    :param text: Optional: Brief description of the game or high scores included in the game message. 0-4096 Characters
    :type text: str
    :param text_entities: Optional: Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    :type text_entities: list of :ref:`object_message_entity`
    :param animation: Optional: Animation that will be displayed in the game message in chats. Upload via the Botfather
    :type animation: :ref:`object_animation`
    """
    def __init__(self, *, title=None, description=None, photo=None, text=None, text_entities=None, animation=None):
        self.title = title
        self.description = description
        self.photo = [PhotoSize(**x) for x in photo] if photo else None
        self.text = text
        self.text_entities = [MessageEntity(**x) for x in text_entities] if text_entities else None
        self.animation = Animation(**animation) if animation else None

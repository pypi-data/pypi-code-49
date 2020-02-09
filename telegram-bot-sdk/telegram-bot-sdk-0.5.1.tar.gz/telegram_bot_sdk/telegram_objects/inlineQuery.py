from telegram_bot_sdk.telegram_objects.location import Location
from telegram_bot_sdk.telegram_objects.user import User


class InlineQuery:
    """This class represents an incoming inline query

    :param id_unique: Unique identifier for this query
    :type id_unique: str
    :param from_user: Sender from which query came from
    :type from_user: :ref:`object_user`
    :param location: Optional: Sender location, only for bots that request user location
    :type location: :ref:`object_location`
    :param query: Text of the query (up to 512 characters)
    :type query: str
    :param offset: Offset of the results to be returned, can be controlled by the bot
    :type offset: str
    """
    def __init__(self, *, id_unique, from_user, location=None, query, offset):
        self.id_unique = id_unique
        self.from_user = User(**from_user) if from_user else None
        self.location = Location(**location) if location else None
        self.query = query
        self.offset = offset

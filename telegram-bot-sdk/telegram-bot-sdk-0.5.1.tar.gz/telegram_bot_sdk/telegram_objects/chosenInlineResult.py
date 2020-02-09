from telegram_bot_sdk.telegram_objects.location import Location
from telegram_bot_sdk.telegram_objects.user import User


class ChosenInlineResult:
    """This class represents a result of an inline query that was chosen by the user and sent to their chat partner
    It is necessary to enable inline feedback via the Botfather to receive this objects in updates

    :param query: The query that was used to obtain the result
    :type query: str
    :param result_id: The unique identifier for the result that was chosen
    :type result_id: str
    :param from_user: The user that chose the result
    :type from_user: :ref:`object_user`
    :param location: Optional: Sender locations, only for bots that require user location
    :type location: :ref:`object_location`
    :param inline_message_id: Optional: Identifier of the sent inline message
    :type inline_message_id: str
    """
    def __init__(self, *, query, result_id=None, from_user=None, location=None, inline_message_id=None):
        self.query = query
        self.result_id = result_id
        self.from_user = User(**from_user) if from_user else None
        self.location = Location(**location) if location else None
        self.inline_message_id = inline_message_id

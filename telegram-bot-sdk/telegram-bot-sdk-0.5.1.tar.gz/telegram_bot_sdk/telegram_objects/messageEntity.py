from telegram_bot_sdk.telegram_objects.user import User


class MessageEntity:
    """This class represents one special entity in a text message

    :param type_result: Type of the entity. Can be _mention_(@username), **hashtag**, **cashtag**, **bot_command**, \
    **url**, **email**, **phone_number**, **bold**, **italic**, **code**, **pre**, **text_link** or **text_mention**
    :type type_result: str
    :param offset: Offset in UTF-16 code units to the start of the entity
    :type offset: int
    :param length: Length oh the entity in UTF-16 code units
    :type length: int
    :param url: Optional: For **text_link** only, url that will be opened after user taps on the text
    :type url: str
    :param user: Optional: for **text_mention** only, the mentioned user
    :type user: :ref:`object_user`
    """
    def __init__(self, *, type_result, offset, length, url=None, user=None):
        self.type_result = type_result
        self.offset = offset
        self.length = length
        self.url = url
        self.user = User(**user) if user else None

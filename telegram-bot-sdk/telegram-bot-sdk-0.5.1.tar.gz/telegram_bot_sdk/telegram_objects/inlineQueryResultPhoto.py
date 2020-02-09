from telegram_bot_sdk.telegram_objects.inlineKeyboardMarkup import InlineKeyboardMarkup
from telegram_bot_sdk.telegram_objects.inlineQueryResult import InlineQueryResult
from telegram_bot_sdk.telegram_objects.inputMessageContent import InputMessageContent


class InlineQueryResultPhoto(InlineQueryResult):
    """This class represents a link to a photo. By default, this photo will be sent by the user with optional caption. \
     Alternatively, you can use input_message_content to send a message with the specified content instead of the photo

    :param type_result: Type of the result, must be _photo_
    :type type_result: str
    :param id_unique: Unique identifier for this result, 1-64 Bytes
    :type id_unique: str
    :param photo_url: A valid URL of the photo. Photo must be in *jpeg* format. Photo size must not exceed 5 MB
    :type photo_url: str
    :param thumb_url: URL of the thumbnail for the photo
    :type thumb_url: str
    :param photo_width: Optional: Width of the photo
    :type photo_width: int
    :param photo_height: Optional: Height of the photo
    :type photo_height: int
    :param title: Optional: Title for the result
    :type title: str
    :param description: Optional: Short description of the result
    :type description: str
    :param caption: Optional: Caption of the photo to be sent, 0-1024 characters
    :type caption: str
    :param parse_mode: Optional: Send *Markdown* or *HTML*, if you want Telegram apps to show bold, italic, fixed-width\
    text or inline URLs in the media caption
    :type parse_mode: str
    :param reply_markup: Optional: Inline keyboard attached to the message
    :type reply_markup: :ref:`object_inline_keyboard_markup`
    :param input_message_content: Optional: Content of the message to be sent instead of the photo
    :type input_message_content: :ref:`object_input_message_content`
    """
    def __init__(self, *, type_result, id_unique, photo_url, thumb_url, photo_width=None, photo_height=None, title=None,
                 description=None, caption=None, parse_mode=None, reply_markup=None, input_message_content=None):
        super().__init__()
        self.type_result = type_result
        self.id_unique = id_unique
        self.photo_url = photo_url
        self.thumb_url = thumb_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        self.input_message_content = InputMessageContent(**input_message_content) if input_message_content else None

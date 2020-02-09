from telegram_bot_sdk.telegram_objects.inlineKeyboardMarkup import InlineKeyboardMarkup
from telegram_bot_sdk.telegram_objects.inlineQueryResult import InlineQueryResult
from telegram_bot_sdk.telegram_objects.inputMessageContent import InputMessageContent


class InlineQueryResultArticle(InlineQueryResult):
    """This class represents a link to an article or web page

    :param type_result: Type of the result, must be _article_
    :type type_result: str
    :param id_unique: Unique identifier for the result, 1-64 Bytes
    :type id_unique: str
    :param title: Title of the result
    :type title: str
    :param input_message_content: Content of the message to be sent
    :type input_message_content: :ref:`object_input_message_content`
    :param reply_markup: Optional: Inline keyboard attached to the message
    :type reply_markup: :ref:`object_inline_keyboard_markup`
    :param url: Optional: URL of the result
    :type url: str
    :param hide_url: Pass True, if you don't want the URL to be shown in the message
    :type hide_url: bool
    :param description: Optional: Short description of the result
    :type description: str
    :param thumb_url: Optional: URL of the thumbnail for the result
    :type thumb_url: str
    :param thumb_width: Thumbnail width
    :type thumb_width: str
    :param thumb_height: Thumbnail height
    :type thumb_height: str
    """
    def __init__(self, *, type_result, id_unique, title, input_message_content, reply_markup=None, url=None,
                 hide_url=None, description=None, thumb_url=None, thumb_width=None, thumb_height=None):
        super().__init__()
        self.type_result = type_result
        self.id_unique = id_unique
        self.title = title
        self.input_message_content = InputMessageContent(**input_message_content) if input_message_content else None
        self.reply_markup = InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

from telegram_bot_sdk.telegram_objects.inputMessageContent import InputMessageContent


class InputTextMessageContent(InputMessageContent):
    """This class represents the content of a text message to be sent as the result of an inline query

    :param message_text: Text of the message to be sent, 1-4096 characters
    :type message_text: str
    :param parse_mode: Optional: Send *Markdown* or *HTML*, if oyu want Telegram apps to show bold, italic, fixed-width\
    text or inline URLs in you bot's message
    :type parse_mode: str
    :param disable_web_page_preview: Optional: Disables link preview for links in the sent message
    :type disable_web_page_preview: bool
    """
    def __init__(self, *, message_text, parse_mode=None, disable_web_page_preview=None):
        super().__init__()
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview

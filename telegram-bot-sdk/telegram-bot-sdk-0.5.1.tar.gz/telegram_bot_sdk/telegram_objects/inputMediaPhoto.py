from telegram_bot_sdk.telegram_objects import inputMedia


class InputMediaPhoto(inputMedia):
    """This class represents a photo to be sent

    :param type_result: Type of the result, must be **photo**
    :type type_result: str
    :param media: File to send. Pass a file_id to send a file that exists on that Telegram servers (recommended), pass \
    an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one\
    using multipart/form-data under <file_attach_name>
    :type media: str
    :param caption: Optional: Caption of the audio to be sent, 0-1024 characters
    :type caption: str
    :param parse_mode: Optional: Send *Markdown* or *HTML*, if you want Telegram apps to show bold, italic, fixed-width\
    text or inline URLs in the media caption
    :type parse_mode: str
    """
    def __init__(self, *, type_result, media, caption=None, parse_mode=None):
        self.type_result = type_result
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode

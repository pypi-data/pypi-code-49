from telegram_bot_sdk.telegram_objects import inputMedia


class InputMediaVideo(inputMedia):
    """This class represents a video to be sent

    :param type_result: Type of the result, must be **video**
    :type type_result: str
    :param media: File to send. Pass a file_id to send a file that exists on that Telegram servers (recommended), pass \
    an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one\
    using multipart/form-data under <file_attach_name>
    :type media: str
    :param thumb: Optional: Thumbnail of the file sent
    :type thumb: :ref:`object_input_file` or str
    :param caption: Optional: Caption of the audio to be sent, 0-1024 characters
    :type caption: str
    :param parse_mode: Optional: Send *Markdown* or *HTML*, if you want Telegram apps to show bold, italic, fixed-width\
    text or inline URLs in the media caption
    :type parse_mode: str
    :param width: Optional: Video width
    :type width: int
    :param height: Optional: Video height
    :type height: int
    :param duration: Optional: Video duration
    :type duration: int
    :param supports_streaming: Optional: Pass True, if the uploaded video is suitable for streaming
    :type supports_streaming: bool
    """
    def __init__(self, *, type_result, media, thumb=None, caption=None, parse_mode=None, width=None, height=None,
                 duration=None, supports_streaming=None):
        self.type_result = type_result
        self.media = media
        if type(thumb).__name__ is 'InputFile':
            self.thumb = thumb
        else:
            self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming

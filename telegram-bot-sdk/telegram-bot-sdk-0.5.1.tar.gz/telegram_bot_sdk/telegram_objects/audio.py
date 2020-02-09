from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class Audio:
    """This objects represents an audio file to be treated as music by the Telegram client

    :param file_id: Identifier for this file
    :type file_id: str
    :param duration: Duration of the audio in seconds as defined by sender
    :type duration: int
    :param performer: Optional: Performer of the audio as defined by sender or by audio tags
    :type performer: str
    :param title: Optional: Title of the audio as defined by sender or by audio tags
    :type title: str
    :param mime_type: Optional: MIME type of the file as defined by sender
    :type mime_type: str
    :param file_size: Optional: Size of the file
    :type file_size: int
    :param thumb: Optional: Thumbnail of the album cover to which the music belongs
    :type thumb: :ref:`object_photo_size`
    """
    def __init__(self, *, file_id, duration, performer=None, title=None, mime_type=None, file_size=None, thumb=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = PhotoSize(**thumb) if thumb else None

from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class VideoNote:
    """This class represents a video message

    :param file_id: Identifier for this file
    :type file_id: str
    :param length: Video width and height as defined by sender
    :type length: int
    :param duration: Duration of the video in seconds as defined by sender
    :type duration: int
    :param thumb: Optional: Video thumbnail
    :type thumb: :ref:`object_photo_size`
    :param file_size: Optional: Size of file
    :type file_size: int
    """
    def __init__(self, *, file_id, length, duration, thumb=None, file_size=None):
        self.file_id = file_id
        self.length = length
        self.duration = duration
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.file_size = file_size

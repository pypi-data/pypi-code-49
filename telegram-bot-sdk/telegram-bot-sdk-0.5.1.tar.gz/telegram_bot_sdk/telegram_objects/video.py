from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class Video:
    """This class represents a video file

    :param file_id: Identifier for this file
    :type file_id: str
    :param width: Video width as defined by sender
    :type width: int
    :param height: Video height as defined by sender
    :type height: int
    :param duration: Duration of the video in seconds defined by sender
    :type duration: int
    :param thumb: Optional: Video thumbnail
    :type thumb: :ref:`object_photo_size`
    :param mime_type: Optional: MIME type of a file as defined by sender
    :type mime_type: str
    :param file_size: Optional: Size of file
    :type file_size: int
    """
    def __init__(self, *, file_id, width, height, duration, thumb=None, mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.mime_type = mime_type
        self.file_size = file_size

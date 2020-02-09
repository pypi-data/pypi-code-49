from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class Animation:
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).


        :param file_id: Identifier for this file
        :type file_id: str
        :param width: Video width as defined by sender
        :type width: int
        :param height: Video height as defined by sender
        :type height: int
        :param duration: Duration of the video in seconds as defined by sender
        :type duration: int
        :param thumb: Optional: Animation thumbnail as defined by sender
        :type thumb: :ref:`object_photo_size`
        :param file_name: Optional: Original animation filename as defined by sender
        :type file_name: str
        :param mime_type: MIME type of the file as defined by sender
        :type mime_type: str
        :param file_size: Size of the file
        :type file_size: int
    """
    def __init__(self, *, file_id, width, height, duration, thumb=None, file_name=None, mime_type=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

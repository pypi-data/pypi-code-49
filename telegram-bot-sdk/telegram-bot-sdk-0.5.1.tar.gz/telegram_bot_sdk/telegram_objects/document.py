from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class Document:
    """This class represents a general file

    :param file_id: Identifier for this file
    :type file_id: str
    :param thumb: Optional: Document thumbnail as defined by sender
    :type thumb: :ref:`object_photo_size`
    :param file_name: Optional: Original filename as defined by sender
    :type file_name: str
    :param mime_type: Optional: MIME type of the file as defined by sender
    :type mime_type: str
    :param file_size: Size of the file
    :type file_size: int
    """
    def __init__(self, *, file_id, thumb=None, file_name=None, mime_type=None, file_size=None):
        self.file_id = file_id
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

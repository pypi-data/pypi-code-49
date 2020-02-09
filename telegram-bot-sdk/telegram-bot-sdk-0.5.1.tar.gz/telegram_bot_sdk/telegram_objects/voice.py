class Voice:
    """This class represents a voice note

    :param file_id: Identifier for this file
    :type file_id: str
    :param duration: Duration of the audio in seconds as defined by sender
    :type duration: int
    :param mime_type: MIME type of the file as defined by sender
    :type mime_type: int
    :param file_size: Size of file
    :type file_size: str
    """
    def __init__(self, *, file_id, duration, mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

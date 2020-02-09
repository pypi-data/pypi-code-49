class File:
    """This class represents a file ready to be downloaded. The file can be downloaded via the link
    https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1
    hour. When the link expires, a new one can be requested by calling :ref:`method_get_file`

    :param file_id: Identifier for this file
    :type file_id: str
    :param file_size: Optional: Size of the file
    :type file_size: int
    :param file_path: Optional: File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    :type file_path: str
    """
    def __init__(self, *, file_id, file_size=None, file_path=None):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path

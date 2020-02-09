class PassportFile:
    """This class represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG \
    format when decrypted and don't exceed 10 MB

    :param file_id: Identifier for this file
    :type file_id: str
    :param file_size: Size of file
    :type file_size: int
    :param file_date: Unix time when the file was uploaded
    :type file_date: int
    """
    def __init__(self, *, file_id, file_size, file_date):
        self.file_id = file_id
        self.file_size = file_size
        self.file_date = file_date

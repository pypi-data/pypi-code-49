class PhotoSize:
    """This class represents one size of a photo or a file / sticker thumbnail

    :param file_id: Identifier for the file
    :type file_id: int
    :param width: Width of the photo
    :type width: int
    :param height: Height of the photo
    :type height: int
    :param file_size: Optional: Size of the file
    :type file_size: int
    """
    def __init__(self, *, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

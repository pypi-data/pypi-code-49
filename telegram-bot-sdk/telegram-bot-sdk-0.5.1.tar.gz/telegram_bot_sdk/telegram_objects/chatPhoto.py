class ChatPhoto:
    """This class represents a chat photo

    :param small_file_id: File identifier of small (160x160) chat photo
    :type small_file_id: str
    :param big_file_id: File identifier of big (640x640) chat photo
    :type big_file_id: str
    """
    def __init__(self, *, small_file_id, big_file_id):
        self.small_file_id = small_file_id
        self.big_file_id = big_file_id

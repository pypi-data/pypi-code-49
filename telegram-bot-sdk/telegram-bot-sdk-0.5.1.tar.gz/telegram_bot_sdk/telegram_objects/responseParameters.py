class ResponseParameters:
    """This class contains information about why a request was unsuccessful

    :param migrate_to_chat_id: Optional: The group has been migrated to a supergroup with the specified identifier
    :type migrate_to_chat_id: int
    :param retry_after: Optional: In case of exceeding flood control, the number of seconds left to wait before the \
    request can be repeated
    :type retry_after: int
    """
    def __init__(self, *, migrate_to_chat_id=None, retry_after=None):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after

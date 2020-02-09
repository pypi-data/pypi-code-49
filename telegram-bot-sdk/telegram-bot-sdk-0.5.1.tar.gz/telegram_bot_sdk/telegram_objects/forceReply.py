class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user \
    (act as if the user has selected the bot‘s message and tapped ’Reply').

    :param force_reply: Returns True, if the reply was successfully
    :type force_reply: bool
    :param selective: Optional: Use this parameter if you want to force reply from specific users only
    :type selective: bool
    """
    def __init__(self, *, force_reply, selective=None):
        self.force_reply = force_reply
        self.selective = selective

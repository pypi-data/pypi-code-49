class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display \
    the default letter-keyboard

    :param remove_keyboard: Requests clients to remove the custom keyboard
    :type remove_keyboard: bool
    :param selective: Optional: Use this parameter if you want to remove the keyboard for specific users only
    :type selective: bool
    """
    def __init__(self, *, remove_keyboard, selective=None):
        self.remove_keyboard = remove_keyboard
        self.selective = selective

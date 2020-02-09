class ReplyKeyboardMarkup:
    """This class represents a custom keyboard with reply options

    :param keyboard: List of button rows, each represented by an list of :ref:`object_keyboard_button` objects
    :type keyboard: list of list of :ref:`object_keyboard_button`
    :param resize_keyboard: Optional: Requests clients to resize the keyboard vertically for optimal fit. Defaults to \
    false, in which case the custom keyboard is always of the same height as the apps's standard keyboard
    :type resize_keyboard: bool
    :param one_time_keyboard: Optional: Requests client to hide the keyboard as soon as it's been used. The \
    keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - \
    the user can press a special button in the input field to see the custom keyboard again
    :type one_time_keyboard: bool
    :param selective: Optional: Use this parameter if you want to show the keyboard to specific users only
    :type selective: bool
    """
    def __init__(self, *, keyboard, resize_keyboard=None, one_time_keyboard=None, selective=None):
        self.keyboard = [ReplyKeyboardMarkup(**x) for x in keyboard]
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

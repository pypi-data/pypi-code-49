class KeyboardButton:
    """This class represents one button of the reply keyboard

    :param text: Text of the button. If none of the optional fields are used, it will be sent as a message, when \
    the button is pressed
    :type text: str
    :param request_contact: Optional: If True, the user's phone number will be sent as a contact when the button is \
    pressed. Available in private chats only
    :type request_contact: bool
    :param request_location: Optional: If True, the user's current location will be sent when the button is pressed. \
    Available in private chats only
    :type request_location: bool
    """
    def __init__(self, *, text, request_contact=None, request_location=None):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location

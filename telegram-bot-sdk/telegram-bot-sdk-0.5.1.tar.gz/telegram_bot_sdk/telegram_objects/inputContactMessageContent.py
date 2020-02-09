class InputContactMessageContent:
    """This class represents the content of a contact message to be sent as the result of an inline query

    :param phone_number: Contact's phone number
    :type phone_number: str
    :param first_name: Contact's first name
    :type first_name: str
    :param last_name: Optional: Contact's last name
    :type last_name: str
    :param vcard: Optional: Additional data about the contact in the form of a vCard, 0-2048 Bytes
    :type vcard: str
    """
    def __init__(self, *, phone_number, first_name, last_name=None, vcard=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

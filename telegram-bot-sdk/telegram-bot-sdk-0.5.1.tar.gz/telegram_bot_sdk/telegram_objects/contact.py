class Contact:
    """This class represents a contact information

    :param phone_number: Contact's phone number
    :type phone_number: str
    :param first_name: Contact's first name
    :type first_name: str
    :param last_name: Optional: Contact's last name
    :type last_name: str
    :param user_id: Optional: Contact's user identifier in Telegram
    :type user_id: str
    :param vcard: Optional: Additional data about the contact in form of a vCard
    :type vcard: str
    """
    def __init__(self, *, phone_number, first_name, last_name=None, user_id=None, vcard=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

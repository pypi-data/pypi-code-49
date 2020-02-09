class ChatPermissions:
    """This class describes actions that a non-administrator user is allowed to take in a chat

    :param can_send_messages: Optional: True, if the user is allowed to send text messages, contacts, locations and \
    venues
    :type can_send_messages: bool
    :param can_send_media_messages: Optional: True, if the user is allowed to send audios, documents, photos, videos,\
    video notes and voice notes, implies can_send_messages
    :type can_send_media_messages: bool
    :param can_send_polls: Optional: True, if the user is allowed to send polls, implies can_send_messages
    :type can_send_polls: bool
    :param can_send_other_messages: Optional: True, if the user is allowed to send animations, games, stickers and use\
    inline bots, implies can_send_media_messages
    :type can_send_other_messages: bool
    :param can_add_web_page_previews: Optional: True, if the user is allowed to add web page previews to their\
    messages, implies can_send_media_messages
    :type can_add_web_page_previews: bool
    :param can_change_info: Optional: True, if the user is allowed to change the chat title, photo and other settings. \
    Ignored in public supergroups
    :type can_change_info: bool
    :param can_invite_users: Optional: True, if the user is allowed to invite new users to the chat
    :type can_invite_users: bool
    :param can_pin_messages: Optional: True, if the user is allowed to pin messages. Ignored in public supergroups
    :type can_pin_messages: bool
    """
    def __init__(self, *, can_send_messages=None, can_send_media_messages=None, can_send_polls=None,
                 can_send_other_messages=None, can_add_web_page_previews=None, can_change_info=None,
                 can_invite_users=None, can_pin_messages=None):
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages

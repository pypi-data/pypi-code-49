from telegram_bot_sdk.telegram_objects.user import User


class ChatMember:
    """This object contains information about one member of a chat

    :param user: Information about the user
    :type user: :ref:`object_user`
    :param status: The member's status in the chat. Can be "creator", "administrator", "member", "restricted", "left" \
    or "kicked"
    :type status: str
    :param until_date: Optional: Restricted and kicked only. Date when restriction will be lifted for this user, unix \
    time
    :type until_date: int
    :param can_be_edited: Optional: Administrators only. True, if the bot is allowed to edit administrator privileges \
    of that user
    :type can_be_edited: bool
    :param can_post_messages: Optional: Administrators only. True, if the administrator can post in the channel; \
    channels only
    :type can_post_messages: bool
    :param can_edit_messages: Optional: Administrators only. True, if the administrator can edit messages of other \
    users and can pin messages; channels only
    :type can_edit_messages: bool
    :param can_delete_messages: Optional: Administrators only. True, if the administrator can delete messages of other \
    user
    :type can_delete_messages: bool
    :param can_restrict_members: Optional: Administrators only. True, if the administrator can restrict, ban or unban \
    chat members
    :type can_restrict_members: bool
    :param can_promote_members: Optional: Administrators only. True, if the administrator can add new administrators \
    with a subset of his own privileges or demote administrators that he has promoted
    :type can_promote_members: bool
    :param can_change_info: Optional: Administrators and restricted only. True, if the user is allowed to change the \
    chat title, photo and other settings
    :type can_change_info: bool
    :param can_invite_users: Optional: Administrators and restricted only. True, if the user is allowed to invite new \
    users to the chat
    :type can_invite_users: bool
    :param can_pin_messages: Optional: Administrators and restricted only. True, if the user is allowed to pin \
    messages; groups and supergroups only
    :type can_pin_messages: bool
    :param is_member: Optional: Restricted only. True, if the user is a member of the chat at the moment of the request
    :type is_member: bool
    :param can_send_messages: Optional: Restricted only. True, if the user is allowed to send text messages, contacts, \
    locations and venues
    :type can_send_messages: bool
    :param can_send_media_messages: Optional: Restricted only. True, if the user is allowed to send audios, documents, \
    photos, videos, video notes and voice messages
    :type can_send_media_messages: bool
    :param can_send_polls: Optional: Restricted only. True, if the user is allowed to send polls
    :type can_send_polls: bool
    :param can_send_other_messages: Optional: Restricted only. True, if the user is allowed to send animations, games, \
    stickers and use inline bots
    :type can_send_other_messages: bool
    :param can_add_web_page_previews: Optional: Restricted only. True, if the user is allowed to add web page preview \
    to their messages
    :type can_add_web_page_previews: bool
    """
    def __init__(self, *, user, status, until_date=None, can_be_edited=None, can_post_messages=None,
                 can_edit_messages=None, can_delete_messages=None, can_restrict_members=None, can_promote_members=None,
                 can_change_info=None, can_invite_users=None, can_pin_messages=None, is_member=None,
                 can_send_messages=None, can_send_media_messages=None, can_send_polls=None,
                 can_send_other_messages=None, can_add_web_page_previews=None):
        self.user = User(**user)
        self.status = status
        self.until_date = until_date
        self.can_be_edited = can_be_edited
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews

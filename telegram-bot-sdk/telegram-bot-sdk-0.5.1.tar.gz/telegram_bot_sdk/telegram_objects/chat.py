from telegram_bot_sdk.telegram_objects.chatPermissions import ChatPermissions
from telegram_bot_sdk.telegram_objects.chatPhoto import ChatPhoto


class Chat:
    """This object represents a chat

        :param id_unique: Unique identifier for the chat
        :type id_unique: int
        :param type_result: Type of chat, can be either "private", "group", "supergroup" or "channel"
        :type type_result: str
        :param title: Optional: Title, for supergroups, channels and group chats
        :type title: str
        :param username: Optional: Username, for private chats, supergroups and channel is available
        :type username: str
        :param first_name: Optional: First name of the other party in a private chat
        :type first_name: str
        :param last_name: Optional: Last name of the other party in a private chat
        :type last_name: str
        :param photo: Optional: Chat photo. Returned only in :ref:`get_chat<method_get_chat>`
        :type photo: :ref:`object_chat_photo`
        :param description: Optional: Description, for groups, supergroups and channel chats. Returned only in \
        :ref:`get_chat<method_get_chat>`
        :type description: str
        :param invite_link: Optional: Chat invite link, for groups, supergroups and channel chats. Returned only in \
        :ref:`get_chat<method_get_chat>`
        :type invite_link: str
        :param pinned_message: Optional: Pinned message, for groups, supergroups and channels. Returned only in \
        :ref:`get_chat<method_get_chat>`
        :type pinned_message: :ref:`object_message`
        :param permissions: Optional: Default chat member permissions. Returned only in :ref:`get_chat<method_get_chat>`
        :type permissions: :ref:`object_chat_permissions`
        :param sticker_set_name: Optional: Name of sticker set for supergroups. Returned only in \
        :ref:`get_chat<method_get_chat>`
        :type sticker_set_name: str
        :param can_set_sticker_set: Optional: True if the bot can change the supergroup set. Returned only in \
        :ref:`get_chat<method_get_chat>`
        :type can_set_sticker_set: bool
    """
    def __init__(self, *, id_unique, type_result, title=None, username=None, first_name=None, last_name=None,
                 photo=None, description=None, invite_link=None, pinned_message=None, permissions=None,
                 sticker_set_name=None, can_set_sticker_set=None):
        self.id_unique = id_unique
        self.type_result = type_result
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.photo = ChatPhoto(**photo) if photo else None
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = ChatPermissions(**permissions) if permissions else None
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set

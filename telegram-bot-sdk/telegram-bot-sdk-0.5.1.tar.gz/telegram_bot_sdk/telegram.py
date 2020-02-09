from typing import Union

from httpx import ConnectTimeout

from telegram_bot_sdk.config import Config
from telegram_bot_sdk.helper.util import check_locals
from telegram_bot_sdk.network import network
from telegram_bot_sdk.network.network import HttpVerbs
from telegram_bot_sdk.telegram_objects.chat import Chat
from telegram_bot_sdk.telegram_objects.chatMember import ChatMember
from telegram_bot_sdk.telegram_objects.file import File
from telegram_bot_sdk.telegram_objects.inputFile import InputFile
from telegram_bot_sdk.telegram_objects.message import Message
from telegram_bot_sdk.telegram_objects.poll import Poll
from telegram_bot_sdk.telegram_objects.stickerSet import StickerSet
from telegram_bot_sdk.telegram_objects.user import User
from telegram_bot_sdk.telegram_objects.userProfilePhotos import UserProfilePhotos
from telegram_bot_sdk.telegram_objects.update import Update


class TelegramBot:
    """The base class to interact with the Telegram SDK

    :param bot_token: Insert here the bot token received by the Botfather
    :type bot_token: String
    """

    def __init__(self, bot_token):
        self.config = Config()
        self.config.vars = {"URL": "https://api.telegram.org/bot" + bot_token + "/"}
        self.my_network = network.Network(self.config)
        self.check_for_updates = False

    def set_callback_method(self, method):
        """This method is used to define the callback method to handle incoming updates

        :param method: Method to call
        :type method: method
        """
        self.check_for_updates = True
        self._check_for_updates(method)

    def _check_for_updates(self, method):
        """This method is used internally to check for updates

        :param method: Method to call
        :type method: method
        """
        data_dict = {"offset": 0,
                     "timeout": ""}
        while self.check_for_updates:
            try:
                update_list = self.my_network.make_request(verb=HttpVerbs.POST, call="getUpdates", data=data_dict)
                for update in update_list:
                    update = Update(**update)
                    data_dict["offset"] = update.update_id + 1
                    method(update)
            except ConnectTimeout:
                continue

    def get_updates(self, *, offset=None, limit=None, timeout=None, allowed_updates=None) -> list:
        """Call this method to receive Messages

        :param offset: Optional: Only updates with an id greater or equal the offset are returned
        :type offset: int
        :param limit: Optional: Set a limit how many Updates are returned
        :type limit: int
        :param timeout: Optional: Set the timeout for long polling
        :type timeout: int
        :param allowed_updates: Optional: Specify the type of updates that are allowed to returned
        :type allowed_updates: list of str

        :return: Returns list of Updates
        :rtype: list of :ref:`object_update`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getUpdates", data=data_dict)
        return [Update(**x) for x in response]

    def get_me(self) -> User:
        """Get information about the bot

        :return: Returns an user instance which holds the information about the bot
        :rtype: :ref:`object_user`
        """
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getMe")
        return User(**response)

    def get_user_profile_photos(self, *, user_id, offset=None, limit=None) -> UserProfilePhotos:
        """Get a list of profile pictures for a user

        :param user_id: Unique id of the target
        :type user_id: int
        :param offset: Optional: Sequential number of the first photo to be returned. By default, all photos are \
        returned
        :type offset: int
        :param limit: Optional: Limits the number of photos to be retrieved. Values between 1 and 100 are accepted.\
        Defaults to 100
        :type limit: int

        :return: Returns an UserProfilePhotos object
        :rtype: :ref:`object_user_profile_photos`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.GET, call="getUserProfilePhotos", data=data_dict)
        return UserProfilePhotos(**response)

    def send_message(self, *, chat_id, text, parse_mode=None, disable_web_page_preview=None,
                     disable_notification=None, reply_to_message_id=None, reply_markup=None) -> Message:
        """This method is used to send messages.

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param text: Text of the message to be sent
        :type text: str
        :param parse_mode: Optional: "Markdown" or "HTML" to use the Markdown or HTML parser
        :type parse_mode: str
        :param disable_web_page_preview: Optional: Disables link previews for links in this message
        :type disable_web_page_preview: bool
        :param disable_notification: Optional: Sends the message silently
        :type disable_notification: bool
        :param reply_to_message_id: ID of the original message if message is a reply
        :type reply_to_message_id: int
        :param reply_markup: Additional interface options. A JSON-Serialized object.
        :type reply_markup: :ref:`object_inline_keyboard_markup` or :ref:`object_reply_keyboard_markup` or \
        :ref:`object_reply_keyboard_remove` or :ref:`object_force_reply`

        :return: On success, the send Message is returned
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.GET, call="sendMessage", params=data_dict)
        return Message(**response)

    def send_location(self, *, chat_id, latitude, longitude, live_period=None, disable_notification=None,
                      reply_to_message_id=None, reply_markup=None) -> Message:
        """This method is used to send locations

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param latitude: Latitude of the location
        :type latitude: float
        :param longitude: Longitude of the location
        :type longitude: float
        :param live_period: Optional: Period in seconds for which the location will be updated, should be between \
        60-864000
        :type live_period: int
        :param disable_notification: Optional: Sends the message silently
        :type disable_notification: bool
        :param reply_to_message_id: Optional: If the message is a reply, ID of the original message
        :type reply_to_message_id: int
        :param reply_markup: Additional interface options
        :type reply_markup: :ref:`object_inline_keyboard_markup` or :ref:`object_reply_keyboard_markup` or \
        :ref:`object_reply_keyboard_remove` or :ref:`object_force_reply`

        :return: On success the sent message is returned
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="sendLocation", data=data_dict)
        return Message(**response)

    def send_venue(self, *, chat_id, latitude, longitude, title, address, foursquare_id=None,
                   foursquare_type=None, disable_notification=None, reply_to_message_id=None,
                   reply_markup=None) -> Message:
        """This method is user to send information about a venue

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param latitude: Latitude of the venue
        :type latitude: float
        :param longitude: Longitude of the venue
        :type longitude: float
        :param title: Name of the venue
        :type title: str
        :param address: Address of the venue
        :type address: str
        :param foursquare_id: Optional: Foursquare identifier of the venue
        :type foursquare_id: str
        :param foursquare_type: Optional: Foursquare type of the venue
        :type foursquare_type: str
        :param disable_notification: Optional: Sends the message silently
        :type disable_notification: bool
        :param reply_to_message_id: Optional: If the message is a reply, ID of the original message
        :type reply_to_message_id: int
        :param reply_markup: Additional interface options
        :type reply_markup: :ref:`object_inline_keyboard_markup` or `object_reply_keyboard_markup` or \
        :ref:`object_reply_keyboard_remove` or :ref:`object_force_reply`

        :return: On success the sent message is returned
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="sendVenue", data=data_dict)
        return Message(**response)

    def send_audio(self, *, chat_id, audio, caption=None, parse_mode=None, duration=None, disable_notification=None,
                   reply_to_message_id=None, reply_markup=None) -> Message:
        """This method is used to send audio messages

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param audio: Audio file to send, path to the file
        :type audio: :ref:`object_input_file`: or str
        :param caption: Voice message caption, 0-1024 characters
        :type caption: str
        :param parse_mode: Send *Markdown* or *HTML*, if you want Telegram apps to show bold, italic, fixed-width, \
        text or inline URLs in the media caption
        :type parse_mode: str
        :param duration: Duration of the voice message in seconds
        :type duration: int
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: bool
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :type reply_to_message_id: int
        :param reply_markup: Additional interface options
        :type reply_markup: :ref:`object_inline_keyboard_markup` or `object_reply_keyboard_markup` or \
        :ref:`object_reply_keyboard_remove` or :ref:`object_force_reply`

        :return: On success the sent message is returned
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        files = {}
        del data_dict["audio"]
        files["audio"] = (audio.file_name, audio.file_data, audio.mime_type)
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="sendAudio", data=data_dict, files=audio)
        return Message(**response)

    def send_contact(self, *, chat_id, phone_number, first_name, last_name=None, vcard=None,
                     disable_notification=None, reply_to_message_id=None, reply_markup=None) -> Message:
        """This method is used to send phone contacts

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param phone_number: Contact's phone number
        :type phone_number: str
        :param first_name: Contact's first name
        :type first_name: str
        :param last_name: Optional: Contact's last name
        :type last_name: str
        :param vcard: Optional: Additional data about the contact in the form of a vCard, 0-2048
        :type vcard: str
        :param disable_notification: Optional: Sends the message silently
        :type disable_notification: bool
        :param reply_to_message_id: Optional: If the message is a reply, ID of the original message
        :type reply_to_message_id: int
        :param reply_markup: Optional: Additional interface options
        :type reply_markup: :ref:`object_inline_keyboard_markup` or `object_reply_keyboard_markup` or \
        :ref:`object_reply_keyboard_remove` or :ref:`object_force_reply`

        :return: On success the sent message is returned
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="sendContact", data=data_dict)
        return Message(**response)

    def send_poll(self, *, chat_id, question, options, disable_notification=None,
                  reply_to_message_id=None, reply_markup=None) -> Message:
        """This message is used to send a native poll. A native poll can't be send to a private chat.

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param question: Poll question, 1-255 characters
        :type question: str
        :param options: List of answer options, 2-10 strings 1-100 characters each
        :type options: list of str
        :param disable_notification: Optional: Sends the message silently
        :type disable_notification: bool
        :param reply_to_message_id: Optional: If the message is a reply, ID of the original message
        :type reply_to_message_id: int
        :param reply_markup: Optional: Additional interface
        :type reply_markup: :ref:`object_inline_keyboard_markup` or `object_reply_keyboard_markup` or \
        :ref:`object_reply_keyboard_remove` or :ref:`object_force_reply`

        :return: On success the sent message is returned
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(call=HttpVerbs.POST, verb="sendPoll", data=data_dict)
        return Message(**response)

    def send_chat_action(self, *, chat_id, action) -> bool:
        """This method is used to send chat action

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param action: Type of action to broadcast. Options: **typing**, **upload_photo**, **record_video** or \
        **upload_video**, **record_audio** or **upload_audio**, **upload_document**, **find_location**, \
        **record_video_note** or **upload_video_note**
        :type action: str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="sendChatAction", data=data_dict)
        return response

    def get_file(self, file_id) -> File:
        """This method is used to get basic information about a file and prepare it for downloading

        :param file_id: File identifier to get info about

        :return: Returns File object on success
        :rtype: :ref:`object_file`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getFile", data=data_dict)
        return File(**response)

    def kick_chat_member(self, *, chat_id, user_id, until_date=None) -> bool:
        """This method is used to kick a user from a group, a supergroup or a channel

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel \
        (format @channelusername)
        :type chat_id: int or str
        :param user_id: Unique identifier of the target user
        :type user_id: int
        :param until_date: Optional: Date when the user will be banned, unix time. If the user is banned for more \
        than 366 days or less than 30 seconds from the current time they are considered to be banned forever
        :type until_date: int

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="kickChatMember", data=data_dict)
        return response

    def unban_chat_member(self, *, chat_id, user_id) -> bool:
        """This method is used to unban a previously kicked user in a supergroup or channel

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel (format \
        @username)
        :type chat_id: int or str
        :param user_id: Unique identifier of the target user
        :type user_id: int

        :return: Returns true on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="unbanChatMember", data=data_dict)
        return response

    def restrict_chat_member(self, *, chat_id, user_id, permissions, until_date=None) -> bool:
        """This method is used to restrict a user in a supergroup

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (format \
        @supergroupname)
        :type chat_id: int or str
        :param user_id: Unique identifier of the target user
        :type user_id: int
        :param permissions: New user permissions
        :type permissions: :ref:`object_chat_permissions`
        :param until_date: Optional: Date when restrictions will be lifted for the user, unix time. If the user is \
        restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be \
        restricted forever

        :return: Return True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="restrictChatMember", data=data_dict)
        return response

    def promote_chat_member(self, *, chat_id, user_id, can_change_info=None, can_post_messages=None,
                            can_edit_messages=None, can_delete_messages=None, can_invite_users=None,
                            can_restrict_members=None, can_pin_messages=None, can_promote_members=None) -> bool:
        """This method is used to promote or demote a user in a supergroup or a channel

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param user_id: Unique identifier of the target user
        :type user_id: int
        :param can_change_info: Optional: Pass True, if the administrator can change title, photo and other settings
        :type can_change_info: bool
        :param can_post_messages: Optional: Pass True, if the administrator can create channel posts, channels only
        :type can_post_messages: bool
        :param can_edit_messages: Optional: Pass True, if the administrator can edit messages of other users and \
        can pin messages, channels only
        :type can_edit_messages: bool
        :param can_delete_messages: Optional: Pass True, if the administrator can delete messages of other users
        :type can_delete_messages: bool
        :param can_invite_users: Optional: Pass True, if the administrator can invite new users to the chat
        :type can_invite_users: bool
        :param can_restrict_members: Optional: Pass True, if the administrator can restrict, ban or unban chat \
        chat members
        :type can_restrict_members: bool:
        :param can_pin_messages: Optional: Pass True, if the administrator can pin messages, supergroups only
        :type can_pin_messages: bool
        :param can_promote_members: Optional: Pass True, if the administrator can add new administrators with a subset \
        of his own privileges or demote administrators that he has promoted (directly or indirectly)
        :type can_promote_members: bool

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="promoteChatMember", data=data_dict)
        return response

    def set_chat_permissions(self, *, chat_id, permissions=None) -> bool:
        """This method is used to set default chat permissions for all members

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (format \
        @supergroupname)
        :type chat_id: int or str
        :param permissions: New default chat permissions
        :type permissions: :ref:`object_chat_permissions`

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="setChatPermissions", data=data_dict)
        return response

    def export_chat_invite_link(self, chat_id) -> bool:
        """This method is used to generate a new invite link for a chat; revokes any previously generated link

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Return the new link on success
        :rtype: str
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="exportChatInviteLink", data=data_dict)
        return response

    def set_chat_photo(self, *, chat_id, photo) -> bool:
        """This method is used to set a new profile photo for the chat

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param photo: New chat photo
        :type photo: :ref:`object_input_file`

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="setChatPhoto", data=data_dict)
        return response

    def delete_chat_photo(self, chat_id) -> bool:
        """This method is used to delete a chat photo

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="deleteChatPhoto", data=data_dict)
        return response

    def set_chat_title(self, *, chat_id, title) -> bool:
        """This method is used to change the title of a chat

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param title: New chat title, 1-255 characters
        :type title: str

        :return: Return True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="setChatTitle", data=data_dict)
        return response

    def set_chat_description(self, *, chat_id, description=None) -> bool:
        """This method is used to change the description of a group, a supergroup or a channel

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param description: New chat description, 0-255 characters

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="setChatDescription", data=data_dict)
        return response

    def pin_chat_message(self, *, chat_id, message_id, disable_notification=None) -> bool:
        """This method is used to pin a message in a group, a supergroup or in a channel

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param message_id: Identifier of a message to pin
        :type message_id: int
        :param disable_notification: Optional: Pass True, if it is not necessary to send a notification to all chat \
        members about the new pinned message
        :type disable_notification: bool

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="pinChatMessage", data=data_dict)
        return response

    def unpin_chat_message(self, chat_id) -> bool:
        """This method is used to unpin a message in a group, supergroup or channel

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="unpinChatMessage", data=data_dict)
        return response

    def leave_chat(self, chat_id) -> Chat:
        """This method is used to leave a group, supergroup or channel

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="leaveChat", data=data_dict)
        return Chat(**response)

    def get_chat(self, chat_id) -> Chat:
        """Use this method to get information about a chat

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Chat object
        :rtype: :ref:`object_chat`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getChat", data=data_dict)
        return Chat(**response)

    def get_chat_administrators(self, chat_id) -> list:
        """This method is used to get a list of administrators of a chat

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Returns a list of :ref:`object_chat_member` objects that contains information about all chat \
        administrators except other bots
        :rtype: list of :ref:`object_chat_member`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getChatAdministrators", data=data_dict)
        return [ChatMember(**response)]

    def get_chat_members_counter(self, chat_id) -> int:
        """This method is used to get the number of members in a chat

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Returns the count on success
        :rtype: int
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getChatMembersCount", data=data_dict)
        return response

    def get_chat_member(self, *, chat_id, user_id) -> ChatMember:
        """This method is used to get information about a member of a chat

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param user_id: Unique identifier of the target user
        :type user_id: int

        :return: Returns a :ref:`object_chat_member` object on success
        :rtype: :ref:`object_chat_member`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getChatMember", data=data_dict)
        return ChatMember(**response)

    def set_chat_sticker_set(self, *, chat_id, sticker_set_name) -> bool:
        """This method is used to set a new group sticker set for a supergroup

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param sticker_set_name: Name of the sticker set to be set as the group sticker set
        :type sticker_set_name: str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="setChatStickerSet", data=data_dict)
        return response

    def delete_chat_sticker_set(self, chat_id) -> bool:
        """This method is used to delete a group sticker set from a supergroup

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="deleteChatStickerSet", data=data_dict)
        return response

    def answer_callback_query(self, *, callback_query_id, text=None, show_alert=None, url=None,
                              cache_time=None) -> bool:
        """This method is used to send answers to callback queries sent from inline keyboards

        :param callback_query_id: Unique identifier for the query to be answered
        :type callback_query_id: str
        :param text: Optional: Text of the notification. If not specified, nothing will be shown to the user. 0-200 \
        characters
        :type text: str
        :param show_alert: Optional: If True, an alert will be shown by the client instead of a notification at the \
        top of the chat screen. Defaults to false
        :type show_alert: bool
        :param url: Optional: URL that will be opened by the user's client
        :type url: str
        :param cache_time: Optional: The maximum amount of time in seconds that the result of the callback query may \
        be cached client-side. Defaults to 0
        :type cache_time: int

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="answerCallbackQuery", data=data_dict)
        return response

    def edit_message_text(self, *, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,
                          disable_web_page_preview=None, reply_markup=None) -> Union[bool, Message]:
        """This method is used to edit text and game messages

        :param text: New text of the message
        :type text: str
        :param chat_id: Optional: Required if *inline_message_id* is not specified. Unique identifier for the \
        target chat or username of the target chat or username of the target channel (format @channelusername)
        :type chat_id: int or str
        :param message_id: Optional: Required if *inline_message_id* is not specified, Identifier of the message to \
        edit
        :type message_id: int
        :param inline_message_id: Optional: Required if *chat_id* and *message_id* are not specified
        :type inline_message_id: str
        :param parse_mode: Optional: Send **Markdown** or **HTML**, if you want Telegram apps to show bold, italic, \
        fixed-width text or inline URLs in your bot's message
        :type parse_mode: str
        :param disable_web_page_preview: Optional: Disables link previews for links in this message
        :type disable_web_page_preview: bool
        :param reply_markup: A JSON serialized object for an inline keyboard
        :type reply_markup: :ref:`object_inline_keyboard_markup`

        :return: Returns the edited Message, if the edited message is sent by the bot, otherwise True
        :rtype: bool or :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageText", data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    def edit_message_caption(self, *, chat_id=None, message_id=None, inline_message_id=None, caption=None,
                             parse_mode=None, reply_markup=None) -> Union[bool, Message]:
        """This method is used to edit the caption of a message

        :param chat_id: Optional: Required if *inline_message_id* is not specified. Unique identifier for the target \
        chat or username of the target channel (format @channelusername)
        :type chat_id: int or str
        :param message_id: Optional: Required if *inline_message_id* is not specified. Identifier of the message to edit
        :type message_id: int
        :param inline_message_id: Optional: Required if *chat_id* and *message_id* are not specified. Identifier of \
        the inline message
        :type inline_message_id: str
        :param caption: Optional: New caption of the message
        :type caption: str
        :param parse_mode: Optional: Send *Markdown* or *HTML*, if you want Telegram apps to show bold, italic, fixed-\
        width text or inline URLs in the message caption.
        :type parse_mode: str
        :param reply_markup: Optional: A JSON-serialized object for an inline keyboard
        :type reply_markup: :ref:`object_inline_keyboard_markup`

        :return: Return the edited Message, if the edited message is sent by the bot, otherwise True
        :rtype: bool or :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageCaption", data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    def edit_message_media(self, *, media, chat_id=None, message_id=None, inline_message_id=None,
                           reply_markup=None) -> Union[bool, Message]:
        """This method is used to edit animation, audio, document, photo or video messages. If a message is a part of \
        a message album, then it can be edited only to a photo or a video. Otherwise, message type can be changed \
        arbitrarily. When inline message is edited, new file can't be uploaded. Use previously uploaded file via \
        its file_id or specify a URL.

        :param media: A JSON-serialized object for a new media content of the message
        :type media: :ref:`object_input_media`
        :param chat_id: Optional: Required if *inline_message_id* is not specified. Unique identifier for the target \
        chat or username of the target channel (format @channelusername)
        :type chat_id: int or str
        :param message_id: Optional: Optional: Required if *inline_message_id* is not specified. Identifier of the \
        message to edit
        :type message_id: int
        :param inline_message_id: Optional: Required if *chat_id* and *message_id* are not specified. Identifier of \
        the inline message.
        :type inline_message_id: str
        :param reply_markup: Optional: A JSON-serialized object for a new media content of the message
        :type reply_markup: :ref:`object_inline_keyboard_markup`

        :return: Return the edited message, if the edited message is sent by the bot, otherwise True
        :rtype: bool or :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageMedia", data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    def edit_message_reply_markup(self, *, chat_id=None, message_id=None, inline_message_id=None,
                                  reply_markup=None) -> Union[bool, Message]:
        """This method is used to edit only the reply markup of messages

        :param chat_id: Optional: Required if *inline_message_id* is not specified. Unique identifier for the \
        target chat or username of the target channel (format @channlerusername)
        :type chat_id: int or str
        :param message_id: Optional: Required if *inline_message_id* is not specified. Identifier of the message to edit
        :type message_id: int
        :param inline_message_id: Optional: Required if *chat_id* and *message_id* are not specified. Identifier of \
        the inline message
        :type inline_message_id: str
        :param reply_markup: Optional: A JSON-serialized object for an inline keyboard
        :type reply_markup: :ref:`object_inline_keyboard_markup`

        :return: Return the edited message, if the edited message is sent by the bot, otherwise True
        :rtype: bool or :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageReplyMarkup", data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    def stop_poll(self, *, chat_id, message_id, reply_markup=None) -> Poll:
        """This method is used to stop a poll which was sent by the bot

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param message_id: Identifier of the original message with the poll
        :type message_id: int
        :param reply_markup: Optional: A JSON-serialized object for a new message inline keyboard
        :type :ref:`object_inline_keyboard_markup`

        :return: Returns the stopped poll on success
        :rtype: :ref:`object_poll`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="stopPoll", data=data_dict)
        return Poll(**response)

    def delete_message(self, *, chat_id, message_id) -> bool:
        """This method is used to delete a message, including service messages, with the following limitations:
        * A message can only be deleted if it was sent less than 48 hours ago.
        * Bots can delete outgoing messages in private chats, groups, and supergroups.
        * Bots can delete incoming messages in private chats.
        * Bots granted *can_post_messages* permissions can delete outgoing messages in channels.
        * If the bot is an administrator of a group, it can delete any message there.
        * If the bot has *can_delete_messages* permission in a supergroup or a channel, it can delete any message there.

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param message_id: Identifier of the message to delete
        :type message_id: int

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="deleteMessage", data=data_dict)
        return response

    def send_sticker(self, *, chat_id, sticker, disable_notification=None, reply_to_message_id=None,
                     reply_markup=None) -> Message:
        """This method is used to send static .WEBP or animated .TGS stickers

        :param chat_id: Unique identifier for the target chat or username of the target channel (format \
        @channelusername)
        :type chat_id: int or str
        :param sticker: Sticker to send. Pass a file_id as str to send a file that exists on the Telegram servers \
        (recommended), pass a HTTP URL as a str for Telegram to get .webp file from the internet or upload a new \
        one using multipart/form-data
        :type sticker: :ref:`object_input_file` or str
        :param disable_notification: Optional: Sends the message silently. Users will receive a notification with \
        no sound
        :type disable_notification: bool
        :param reply_to_message_id: Optional: If the message is a reply, ID of the original message
        :type reply_to_message_id: int
        :param reply_markup: Optional: Additional interface options. A JSON-serialized object for an inline keyboard, \
        custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user
        :type reply_markup: Optional: :ref:`object_inline_keyboard_markup` or :ref:`object_reply_keyboard_markup` or \
        :ref:`object_reply_keyboard_remove` or :ref:`object_force_reply`

        :return: Returns the sent message on success
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getSticker", data=data_dict)
        return Message(**response)

    def get_sticker_set(self, name) -> StickerSet:
        """This method is used to get a sticker set

        :param name: Name of the sticker set
        :type name: str

        :return: Returns a sticker set
        :rtype: :ref:`object_sticker_set`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="getStickerSet", data=data_dict)
        return StickerSet(**response)

    def upload_sticker_file(self, *, user_id, png_sticker) -> File:
        """This method is used to upload .png file with a sticker for later use in \
        :ref:`method_create_new_sticker_set` and :ref:`method_add_sticker_set` methods

        :param user_id: User identifier of sticker file owner
        :type user_id: int
        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not \
        exceed 512px, and either width or height must be exactly 512px
        :type png_sticker: :ref:`object_input_file`

        :return: Returns the uploaded file
        :rtype: :ref:`object_file`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="uploadStickerFile", data=data_dict)
        return File(**response)

    def create_new_sticker_set(self, *, user_id, name, title, png_sticker, emojis, contains_mask=None,
                               mask_position=None) -> bool:
        """This method is used to create a new sticker set owned by a user. The bot will be able to edit the created \
        sticker set

        :param user_id: User identifier of created sticker set owner
        :type user_id: int
        :param name: Short name of sticker set, to be used in ``t.me/addstickers/``URLs. Can contain only english \
        letters, digits and undersocres. Must begin with a leeter, can't contain consecutive underscores and must end \
        in "_by_<bot_username>". <bot_username> is case insensitive. 1-64 characters
        :type name: str
        :param title: Sticker set title, 1-64 characters
        :type title: str
        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not \
        exceed 512px, and either width or height must be exactly 512px. Pass a *file_id* as a str to send a file that \
        already exists on the Telegram servers, pass a HTTP URL as a str for Telegram to get a file from the Internet, \
        or upload a new one using multipart/form-data
        :type png_sticker: :ref:`object_input_file` or str
        :param emojis: One or more emoji corresponding to the sticker
        :type emojis: str
        :param contains_mask: Optional: Pass True, if a set of mask stickers should be created
        :type contains_mask: bool
        :param mask_position: Optional: A JSON.serialized object for position where the mask should be played on faces
        :type mask_position: :ref:`object_mask_position`

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="createNewStickerSet", data=data_dict)
        return response

    def add_sticker_to_set(self, user_id, name, png_sticker, emojis, mask_position=None) -> bool:
        """This method is used to add a set created by the bot

        :param user_id: User identifier of sticker set owner
        :type user_id: int
        :param name: Sticker set name
        :type name: str
        :param png_sticker: PNG image with the sticker, must be up to 512 kb in size, dimensions must not exceed 512px \
        and either width or height must exactly 512px. Pass a  *file_id* as a str to send a file that already \
        exists on the telegram servers, pass an HTTP URL as a str for telegram to get a file from the internet or \
        upload a new one using multipart/form-data
        :type png_sticker: str or :ref:`object_input_file`
        :param emojis: One or more emoji corresponding to the sticker
        :type emojis: str
        :param mask_position: Optional: A JSON-serialized object for position where the mask should be placed on faces
        :type mask_position: :ref:`object_mask_position`

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="addStickerToSet", data=data_dict)
        return response

    def set_sticker_position_in_set(self, *, sticker, position) -> bool:
        """This method is used to move a sticker in a set created by the bot to a specific position

        :param sticker: File identifier for the sticker
        :type sticker: str
        :param position: New sticker position in the set, zero based
        :type position: int

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="setStickerPositionInSet", data=data_dict)
        return response

    def delete_sticker_from_set(self, sticker) -> bool:
        """This method is used to delete a sticker from a set created by the bot

        :param sticker: File identifier for sticker
        :type sticker: str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="deleteStickerFromSet", data=data_dict)
        return response

    def answer_inline_query(self, *, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                            switch_pm_text=None, switch_pm_parameter=None) -> bool:
        """This method is used to send answers to an inline query

        :param inline_query_id: Unique identifier for the answered query
        :type inline_query_id: str
        :param results: A JSON-serialized array of results for the inline query
        :type results: list of :ref:`object_inline_query_result`
        :param cache_time: Optional: The maximum amount of time in seconds that the result of the inline query may be \
        cached on the server Defaults to 300
        :type cache_time: int
        :param is_personal: Optional: Pass True, if results may be cached on the server side only for the user that \
        sent the query. By default, results may be returned to any user who sends the same query
        :type is_personal: bool
        :param next_offset: Optional: Pass the offset that a client should send in the next query with the same text \
        to receive more results. Pass an empty string ig there are no more results or if you don't support pagination. \
        Offset length can't exceed 64 bytes
        :type next_offset: str
        :param switch_pm_text: Optional: If passed, clients will display a button with specified text that switches \
        the user to a private chat with the bot and sends the bot a start message with the parameter \
        *switch_pm_parameter*
        :type switch_pm_text: str
        :param switch_pm_parameter: Optional: Deep-linking parameter for the /start message sent to the bot when user \
        presses the switch button. 1-64 characters, only ``A-Z``, ``a-z``, ``0-9``, ``_``and ``-`` are allowed
        :type switch_pm_parameter: str

        :return: Returns True on success
        :rtype: bool
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="answerInlineQuery", data=data_dict)
        return response

    def send_invoice(self, *, chat_id, title, description, payload, provider_token, start_parameter, currency,
                     prices, provider_data=None, photo_url=None, photo_size=None, photo_width=None, photo_height=None,
                     need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None,
                     send_phone_number_to_provider=None, send_email_to_provider=None, is_flexible=None,
                     disable_notification=None, reply_to_message_id=None, reply_markup=None) -> Message:
        """This method is used to send invoices

        :param chat_id: Unique identifier for the target private chat
        :type chat_id: int
        :param title: Product name, 1-32 characters
        :type title: str
        :param description: Product description, 1-255 characters
        :type description: str
        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your \
        internal processes
        :type payload: str
        :param provider_token: Payments provider token, obtained via Botfather
        :type provider_token: str
        :param start_parameter: Unique deep-linking parameter that can be used to generate this invoice when used as a \
        start parameter
        :type start_parameter:str
        :param currency: Three-letter ISO 4217 currency code
        :type currency: str
        :param prices: Price breakdown, a list of components
        :type prices: list of :ref:`object_labeled_price`
        :param provider_data: Optional: JSON-encoded data about the invoice, which will be shared with the payment \
        provider
        :type provider_data: str
        :param photo_url: Optional: URL of the product photo for the invoice. Can be a photo of the goods or a \
        marketing image for a service
        :type photo_url: str
        :param photo_size: Optional: Photo size
        :type photo_size: str
        :param photo_width: Optional: Photo width
        :type photo_width: int
        :param photo_height: Optional: Photo height
        :type photo_height: int
        :param need_name: Optional: Pass True, if you require the user's full name to complete the order
        :type need_name: bool
        :param need_phone_number: Optional: Pass True, if you require the user's phone number to complete the order
        :type need_phone_number: bool
        :param need_email: Optional:  Pass True, if user's email address to complete the order
        :type need_email: bool
        :param need_shipping_address: Optional:  Pass True, if you require the user's shipping address to complete the \
        order
        :type need_shipping_address: bool
        :param send_phone_number_to_provider: Optional: Pass True, if user's phone number should be sent to provider
        :type send_phone_number_to_provider: bool
        :param send_email_to_provider: Optional: Pass True, if user's email address should be sent to provider
        :type send_email_to_provider: bool
        :param is_flexible: Optional: Pass True, if the final price depends on the shipping method
        :type is_flexible: bool
        :param disable_notification: Optional: Sends the message silently. Users will receive a notification with \
        no sound
        :type disable_notification: bool
        :param reply_to_message_id: Optional: If the message is a reply, ID of the original message
        :type reply_to_message_id: int
        :param reply_markup: Optional: A JSON-serialized object for an inline keyboard. If empty, one \
        'Pay ``total price``' button will be shown. If not empty, the first button must be a Pay button
        :type reply_markup: :ref:`object_inline_keyboard_markup`

        :return: Returns the sent message on success
        :rtype: :ref:`object_message`
        """
        data_dict = check_locals(**locals())
        response = self.my_network.make_request(verb=HttpVerbs.POST, call="sendInvoice", data=data_dict)
        return Message(**response)


class TelegramBotAsync:
    """The base class to interact with the Telegram SDK asynchronously. For the further documentation, see \
    :ref:`class_telegram_bot`

    :param bot_token: Insert here the bot token received by the Botfather
    :type bot_token: String
    """

    def __init__(self, bot_token):
        self.config = Config()
        self.config.vars = {"URL": "https://api.telegram.org/bot" + bot_token + "/"}
        self.my_network = network.NetworkAsync(self.config)

    async def get_updates(self, *, offset=None, limit=None, timeout=None, allowed_updates=None) -> list:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getUpdates", data=data_dict)
        return [Update(**x) for x in response]

    async def get_me(self) -> User:
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getMe")
        return User(**response)

    async def get_user_profile_photos(self, *, user_id, offset=None, limit=None) -> UserProfilePhotos:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.GET, call="getUserProfilePhotos", data=data_dict)
        return UserProfilePhotos(**response)

    async def send_message(self, *, chat_id, text, parse_mode=None, disable_web_page_preview=None,
                           disable_notification=None, reply_to_message_id=None, reply_markup=None) -> Message:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.GET, call="sendMessage", params=data_dict)
        return Message(**response)

    async def send_location(self, *, chat_id, latitude, longitude, live_period=None, disable_notification=None,
                            reply_to_message_id=None, reply_markup=None) -> Message:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="sendLocation", data=data_dict)
        return Message(**response)

    async def send_venue(self, *, chat_id, latitude, longitude, title, address, foursquare_id=None,
                         foursquare_type=None, disable_notification=None, reply_to_message_id=None,
                         reply_markup=None) -> Message:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="sendVenue", data=data_dict)
        return Message(**response)

    async def send_contact(self, *, chat_id, phone_number, first_name, last_name=None, vcard=None,
                           disable_notification=None, reply_to_message_id=None, reply_markup=None) -> Message:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="sendContact", data=data_dict)
        return Message(**response)

    async def send_poll(self, *, chat_id, question, options, disable_notification=None,
                        reply_to_message_id=None, reply_markup=None) -> Message:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(call=HttpVerbs.POST, verb="sendPoll", data=data_dict)
        return Message(**response)

    async def send_chat_action(self, *, chat_id, action) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="sendChatAction", data=data_dict)
        return response

    async def get_file(self, file_id) -> File:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getFile", data=data_dict)
        return File(**response)

    async def kick_chat_member(self, *, chat_id, user_id, until_date=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="kickChatMember", data=data_dict)
        return response

    async def unban_chat_member(self, *, chat_id, user_id) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="unbanChatMember", data=data_dict)
        return response

    async def restrict_chat_member(self, *, chat_id, user_id, permissions, until_date=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="restrictChatMember", data=data_dict)
        return response

    async def promote_chat_member(self, *, chat_id, user_id, can_change_info=None, can_post_messages=None,
                                  can_edit_messages=None, can_delete_messages=None, can_invite_users=None,
                                  can_restrict_members=None, can_pin_messages=None, can_promote_members=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="promoteChatMember", data=data_dict)
        return response

    async def set_chat_permissions(self, *, chat_id, permissions=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="setChatPermissions", data=data_dict)
        return response

    async def export_chat_invite_link(self, chat_id) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="exportChatInviteLink", data=data_dict)
        return response

    async def set_chat_photo(self, *, chat_id, photo) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="setChatPhoto", data=data_dict)
        return response

    async def delete_chat_photo(self, chat_id) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="deleteChatPhoto", data=data_dict)
        return response

    async def set_chat_title(self, chat_id) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="setChatTitle", data=data_dict)
        return response

    async def set_chat_description(self, *, chat_id, description=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="setChatDescription", data=data_dict)
        return response

    async def pin_chat_message(self, *, chat_id, message_id, disable_notification=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="pinChatMessage", data=data_dict)
        return response

    async def unpin_chat_message(self, chat_id) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="unpinChatMessage", data=data_dict)
        return response

    async def leave_chat(self, chat_id) -> Chat:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="leaveChat", data=data_dict)
        return Chat(**response)

    async def get_chat(self, chat_id) -> Chat:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getChat", data=data_dict)
        return Chat(**response)

    async def get_chat_administrators(self, chat_id) -> list:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getChatAdministrators", data=data_dict)
        return [ChatMember(**response)]

    async def get_chat_members_counter(self, chat_id) -> int:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getChatMembersCount", data=data_dict)
        return response

    async def get_chat_member(self, *, chat_id, user_id) -> ChatMember:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getChatMember", data=data_dict)
        return ChatMember(**response)

    async def set_chat_sticker_set(self, *, chat_id, sticker_set_name) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="setChatStickerSet", data=data_dict)
        return response

    async def delete_chat_sticker_set(self, chat_id) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="deleteChatStickerSet", data=data_dict)
        return response

    async def answer_callback_query(self, *, callback_query_id, text=None, show_alert=None, url=None,
                                    cache_time=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="answerCallbackQuery", data=data_dict)
        return response

    async def edit_message_text(self, *, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,
                                disable_web_page_preview=None, reply_markup=None) -> Union[bool, Message]:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageText", data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    async def edit_message_caption(self, *, chat_id=None, message_id=None, inline_message_id=None, caption=None,
                                   parse_mode=None, reply_markup=None) -> Union[bool, Message]:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageCaption", data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    async def edit_message_media(self, *, media, chat_id=None, message_id=None, inline_message_id=None,
                                 reply_markup=None) -> Union[bool, Message]:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageMedia", data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    async def edit_message_reply_markup(self, *, chat_id=None, message_id=None, inline_message_id=None,
                                        reply_markup=None) -> Union[bool, Message]:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="editMessageReplyMarkup",
                                                      data=data_dict)
        if not isinstance(response, bool):
            return Message(**response)
        return response

    async def stop_poll(self, *, chat_id, message_id, reply_markup=None) -> Poll:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="stopPoll", data=data_dict)
        return Poll(**response)

    async def delete_message(self, *, chat_id, message_id) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="deleteMessage", data=data_dict)
        return response

    async def get_sticker(self, *, chat_id, sticker, disable_notification=None, reply_to_message_id=None,
                          reply_markup=None) -> Message:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getSticker", data=data_dict)
        return Message(**response)

    async def get_sticker_set(self, name) -> StickerSet:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="getStickerSet", data=data_dict)
        return StickerSet(**response)

    async def upload_sticker_file(self, *, user_id, png_sticker) -> File:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="uploadStickerFile", data=data_dict)
        return File(**response)

    async def create_new_sticker_set(self, *, user_id, name, title, png_sticker, emojis, contains_mask=None,
                                     mask_position=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="createNewStickerSet", data=data_dict)
        return response

    async def add_sticker_to_set(self, user_id, name, png_sticker, emojis, mask_position=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="addStickerToSet", data=data_dict)
        return response

    async def set_sticker_position_in_set(self, *, sticker, position) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="setStickerPositionInSet",
                                                      data=data_dict)
        return response

    async def delete_sticker_from_set(self, sticker) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="deleteStickerFromSet", data=data_dict)
        return response

    async def answer_inline_query(self, *, inline_query_id, results, cache_time=None, is_personal=None,
                                  next_offset=None, switch_pm_text=None, switch_pm_parameter=None) -> bool:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="answerInlineQuery", data=data_dict)
        return response

    async def send_invoice(self, *, chat_id, title, description, payload, provider_token, start_parameter, currency,
                           prices, provider_data=None, photo_url=None, photo_size=None, photo_width=None,
                           photo_height=None, need_name=None, need_phone_number=None, need_email=None,
                           need_shipping_address=None, send_phone_number_to_provider=None, send_email_to_provider=None,
                           is_flexible=None, disable_notification=None, reply_to_message_id=None,
                           reply_markup=None) -> Message:
        data_dict = check_locals(**locals())
        response = await self.my_network.make_request(verb=HttpVerbs.POST, call="sendInvoice", data=data_dict)
        return Message(**response)


class TestBot:
    def __init__(self):
        self.telebot = TelegramBot("951769475:AAFjUgldVr-phYMp_0chJ57CNAs-Deg53zw")
        self.telebot.set_callback_method(self.on_update)

    def on_update(self, update):
        self.telebot.send_audio(chat_id=update.message.chat.id_unique,
                                audio=InputFile("/home/omikron/Dokumente/Python/WololoBot/taunt/01.mp3"))


def main():
    TestBot()


if __name__ == '__main__':
    main()

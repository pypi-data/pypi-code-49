from telegram_bot_sdk.telegram_objects.animation import Animation
from telegram_bot_sdk.telegram_objects.audio import Audio
from telegram_bot_sdk.telegram_objects.chat import Chat
from telegram_bot_sdk.telegram_objects.contact import Contact
from telegram_bot_sdk.telegram_objects.document import Document
from telegram_bot_sdk.telegram_objects.game import Game
from telegram_bot_sdk.telegram_objects.inlineKeyboardMarkup import InlineKeyboardMarkup
from telegram_bot_sdk.telegram_objects.invoice import Invoice
from telegram_bot_sdk.telegram_objects.location import Location
from telegram_bot_sdk.telegram_objects.messageEntity import MessageEntity
from telegram_bot_sdk.telegram_objects.passportData import PassportData
from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize
from telegram_bot_sdk.telegram_objects.poll import Poll
from telegram_bot_sdk.telegram_objects.sticker import Sticker
from telegram_bot_sdk.telegram_objects.successfulPayment import SuccessfulPayment
from telegram_bot_sdk.telegram_objects.user import User
from telegram_bot_sdk.telegram_objects.venue import Venue
from telegram_bot_sdk.telegram_objects.video import Video
from telegram_bot_sdk.telegram_objects.videoNote import VideoNote
from telegram_bot_sdk.telegram_objects.voice import Voice


class Message:
    """This class represents a message

    :param message_id: Unique message identifier
    :type message_id: int
    :param from_user: Optional: User from which the message is from. Empty for messages sent to channels
    :type from_user: :ref:`object_user`
    :param date: Date the message was sent in Unix time
    :type date: int
    :param chat: Optional: Conversation the message belongs to
    :type chat: :ref:`object_chat`
    :param forward_from: Optional: For forwarded messages, sender of the original messages
    :type forward_from: :ref:`object_user`
    :param forward_from_chat: Optional: For messages forwarded from channels, information about the original channel
    :type forward_from_chat: :ref:`object_chat`
    :param forward_from_message_id: Optional: For messages forwarded from channels, identifier of the original message \
    in the channel
    :type forward_from_message_id: int
    :param forward_signature: Optional: For messages forwarded from channels, signature of the post author if present
    :type forward_signature: str
    :param forward_sender_name: Optional: Sender's name for messages forwarded from users who disallow adding a link \
    to their account in forwarded messages
    :type forward_sender_name: str
    :param forward_date: Optional: For forwarded messages, date the original message was sent in Unix time
    :type forward_date: int,
    :param reply_to_message: Optional: For replies, the original message
    :type reply_to_message: :ref:`object_message`
    :param edit_date: Optional: Date the message was last edited in Unix time
    :type edit_date: int
    :param media_group_id: Optional: The unique identifier of a media message group this message belongs to
    :type media_group_id: str
    :param author_signature: Optional: Signature of the post author for messages in channels
    :type author_signature: str
    :param text: Optional: For text messages, the actual UTF-8 text of the message, 0-4096 characters.
    :type text: str
    :param entities: Optional: For text messages, special entities like usernames, URLs, bot commands, etc. that \
    appear in the text
    :type entities: list of :ref:`object_message_entity`
    :param caption_entities: Optional: For messages with a caption, special entities like usernames, URLs, bot \
    commands, etc. that appear in the caption
    :type caption_entities: list of :ref:`object_message_entity`
    :param audio: Optional: If the message is an audio file, information about the file
    :type audio: :ref:`object_audio`
    :param document: Optional: If the message is a general file, information about the file
    :type document: :ref:`object_document`
    :param animation: Optional: If the message is an animation, information about the animation. For backward \
    compatibility, when this field is set, the document field will also be set
    :type animation: :ref:`object_animation`
    :param game: Optional: If the message is a game, information about the game.
    :type game: :ref:`object_game`
    :param photo: Optional: If the message is a photo, available sizes of the photo
    :type photo: list of :ref:`object_photo_size`
    :param sticker: Optional: If the message is a sticker, information about the sticker.
    :type sticker: :ref:`object_sticker`
    :param video: Optional: If the message is a video, information about the video.
    :type video: :ref:`object_video`
    :param voice: Optional: If the message is a voice message, information about the voice message
    :type voice: :ref:`object_voice`
    :param video_note: Optional: If the message ia a video note, information about the video message
    :type video_note: :ref:`object_video_note`,
    :param caption: Optional: Caption for the animation, audio, document, photo, video or voice, 0-1024 Characters
    :type caption: str
    :param contact: Optional: If the message is a shared contact, information about the contact
    :type contact: :ref:`object_contact`
    :param location: Optional: If the message is a shared location information about the location
    :type location: :ref:`object_location`
    :param venue: Optional: If the message is a venue, information, about the venue
    :type venue: :ref:`object_venue`
    :param poll: Optional: If the message is a native poll, information about the poll
    :type poll: :ref:`object_poll`
    :param new_chat_members: Optional: New members that were added to the group or supergroup and information about them
    :type new_chat_members: list of :ref:`object_user`
    :param left_chat_member: Optional: Information about a member, who was removed from the group
    :type left_chat_member: :ref:`object_user`

    :param new_chat_member: Optional: Information about a user, who was added to the group
    :type new_chat_member: :ref:`object_user`
    :param new_chat_participant: Optional: Information about a new chat participant, who was added to the group
    :type new_chat_participant: :ref:`object_user`

    :param new_chat_title: Optional: New chat title
    :type new_chat_title: str
    :param new_chat_photo: Optional: New chat photo
    :type new_chat_photo: list of :ref:`object_photo_size`
    :param delete_chat_photo: Optional: Service Message: The chat photo was deleted
    :type delete_chat_photo: bool
    :param group_chat_created: Optional: Service Message: The group has been created
    :type group_chat_created: bool
    :param supergroup_chat_created: Optional: Service message: The supergroup has been created. For more information, \
    see https://core.telegram.org/bots/api#message
    :type supergroup_chat_created: bool
    :param channel_chat_created: Optional: Service message: the channel has been created. For more information, \
    see https://core.telegram.org/bots/api#message
    :type channel_chat_created: bool
    :param migrate_to_chat_id: Optional: The group has been migrated to a supergroup with the specified identifier
    :type migrate_to_chat_id: int
    :param migrate_from_chat_id: Optional: The supergroup has been migrated from a group with the specified identifier
    :type migrate_from_chat_id: int
    :param pinned_message: Optional: Specified message was pinned
    :type pinned_message: :ref:`object_message`
    :param invoice: Optional: If the message is a invoice for payment, information about the invoice
    :type invoice: :ref:`object_invoice`
    :param successful_payment: Optional: If the message is a service message about a successful payment, information \
    about the payment
    :type successful_payment: :ref:`object_successful_payment`
    :param connected_website: Optional: The domain name of the website on which the user has logged in
    :type connected_website: str
    :param passport_data: Optional: Telegram Passport data
    :type passport_data: :ref:`object_passport_data`
    :param reply_markup: Optional: Inline keyboard attached to the message
    :type reply_markup: :ref:`object_inline_keyboard_markup`
    """
    def __init__(self, *, message_id, from_user=None, date, chat=None, forward_from=None,
                 forward_from_chat=None, forward_from_message_id=None, forward_signature=None, forward_sender_name=None,
                 forward_date=None, reply_to_message=None, edit_date=None, media_group_id=None, author_signature=None,
                 text=None, entities=None, caption_entities=None, audio=None, document=None, animation=None, game=None,
                 photo=None, sticker=None, video=None, voice=None, video_note=None, caption=None, contact=None,
                 location=None, venue=None, poll=None, new_chat_members=None, left_chat_member=None,
                 new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None,
                 supergroup_chat_created=None, channel_chat_created=None, migrate_to_chat_id=None,
                 migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None,
                 connected_website=None, passport_data=None, reply_markup=None, new_chat_member=None,
                 new_chat_participant=None):

        if "pinned_message" in chat:
            chat["pinned_message"] = Message(**chat["pinned_message"])

        self.message_id = message_id
        self.from_user = User(**from_user) if from_user else None
        self.date = date
        self.chat = Chat(**chat) if chat else None
        self.forward_from = User(**forward_from) if forward_from else None
        self.forward_from_chat = Chat(**forward_from_chat) if forward_from_chat else None
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.reply_to_message = Message(**reply_to_message) if reply_to_message else None
        self.edit_date = edit_date
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = [MessageEntity(**x) for x in entities] if entities else None
        self.caption_entities = [MessageEntity(**x) for x in caption_entities] if caption_entities else None
        self.audio = Audio(**audio) if audio else None
        self.document = Document(**document) if document else None
        self.animation = Animation(**animation) if animation else None
        self.game = Game(**game) if game else None
        self.photo = [PhotoSize(**x) for x in photo] if photo else None
        self.sticker = Sticker(**sticker) if sticker else None
        self.video = Video(**video) if video else None
        self.voice = Voice(**voice) if voice else None
        self.video_note = VideoNote(**video_note) if video_note else None
        self.caption = caption
        self.contact = Contact(**contact) if contact else None
        self.location = Location(**location) if location else None
        self.venue = Venue(**venue) if venue else None
        self.poll = Poll(**poll) if poll else None
        self.new_chat_member = [User(**x) for x in new_chat_members] if new_chat_members else None
        self.left_chat_member = User(**left_chat_member) if left_chat_member else None
        self.new_chat_title = new_chat_title
        self.new_chat_photo = [PhotoSize(**x) for x in new_chat_photo] if new_chat_photo else None
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = Message(**pinned_message) if pinned_message else None
        self.invoice = Invoice(**invoice) if invoice else None
        self.successful_payment = SuccessfulPayment(**successful_payment) if successful_payment else None
        self.connected_website = connected_website
        self.passport_data = PassportData(**passport_data) if passport_data else None
        self.reply_markup = InlineKeyboardMarkup(**reply_markup) if reply_markup else None

        self.new_chat_participant = User(**new_chat_participant) if new_chat_participant else None
        self.new_chat_member = User(**new_chat_member) if new_chat_member else None

from telegram_bot_sdk.telegram_objects.maskPosition import MaskPosition
from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class Sticker:
    """This class represents a sticker

    :param file_id: Identifier for this file
    :type file_id: str
    :param width: Sticker width
    :type width: int
    :param height: Sticker height
    :type height: int
    :param is_animated: True, if the sticker is animated
    :type is_animated: bool
    :param thumb: Optional: Sticker thumbnail in the .webp or .jpg format
    :type thumb: :ref:`object_photo_size`
    :param emoji: Optional: Emoji associated with the sticker
    :type emoji: str
    :param set_name: Optional: Name of the sticker set to which the sticker belongs
    :type set_name: str
    :param mask_position: Optional: For mask stickers, the position where the mask should be placed
    :type mask_position: :ref:`object_mask_position`
    :param file_size: Optional: Size of the file
    :type file_size: int
    """
    def __init__(self, *, file_id=None, width=None, height=None, is_animated=None, thumb=None, emoji=None,
                 set_name=None, mask_position=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.emoji = emoji
        self.set_name = set_name
        self.mask_position = MaskPosition(**mask_position) if mask_position else None
        self.file_size = file_size

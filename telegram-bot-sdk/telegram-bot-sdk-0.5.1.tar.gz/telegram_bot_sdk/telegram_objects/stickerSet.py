from telegram_bot_sdk.telegram_objects.sticker import Sticker


class StickerSet:
    """This class represents a sticker set

    :param name: Sticker set name
    :type name: str
    :param title: Sticker set title
    :type title: str
    :param is_animated: True, if the sticker set contains animated stickers
    :type is_animated: bool
    :param contains_masks: True, if the sticker set contains masks
    :type contains_masks: bool
    :param stickers: List of all set stickers
    :type stickers: list of :ref:`object_stickers`
    """
    def __init__(self, *, name, title, is_animated, contains_masks, stickers):
        self.name = name
        self.title = title
        self.is_animated = is_animated
        self.contains_masks = contains_masks
        self.stickers = [Sticker(**x) for x in stickers] if stickers else None

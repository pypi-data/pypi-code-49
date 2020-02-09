from telegram_bot_sdk.telegram_objects.photoSize import PhotoSize


class UserProfilePhotos:
    """Represents a list of profile photos

    :param total_count: Total number of profile pictures the target user has
    :type total_count: int
    :param photos: List of profile pictures
    :type photos: list of list of :ref:`object_photo_size`
    """
    def __init__(self, *, total_count, photos):
        self.total_count = total_count
        self.photos = [PhotoSize(**y) for y in [x for x in photos]] if photos else None

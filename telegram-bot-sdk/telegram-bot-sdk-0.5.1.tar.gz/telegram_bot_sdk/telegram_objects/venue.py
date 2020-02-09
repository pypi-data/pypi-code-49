from telegram_bot_sdk.telegram_objects.location import Location


class Venue:
    """This class represents a venue

    :param location: Venue location
    :type location: :ref:`object_location`
    :param title: Name of the venue
    :type title: str
    :param address: Address of the venue
    :type address: str
    :param foursquare_id: Optional: Foursquare identifier of the venue
    :type foursquare_id: str
    :param foursquare_type: Optional: Foursquare type of the venue
    :type foursquare_type: str
    """
    def __init__(self, *, location, title, address, foursquare_id=None, foursquare_type=None):
        self.location = Location(**location)
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type

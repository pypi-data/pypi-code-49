class InputVenueMessageContent:
    """This class represents the content of a venue message to be sent as the result of an inline query

    :param latitude: Latitude of the venue in degrees
    :type latitude: float
    :param longitude: Longitude of the venue in degrees
    :type longitude: float
    :param title: Name of the venue
    :type title: str
    :param address: Address of the venue
    :type address: str
    :param foursquare_id: Optional: Foursquare identifier of the venue
    :type foursquare_id: str
    :param foursquare_type: Optional: Foursquare type of the venue
    :type foursquare_type: str
    """
    def __init__(self, *, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type

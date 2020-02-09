class InputLocationMessageContent:
    """This class represents the content of a location message to be sent as the result of an inline query

    :param latitude: Latitude of the location in degrees
    :type latitude: float
    :param longitude: Longitude of the location in degrees
    :type longitude: float
    :param live_period: Optional: Period in seconds for which the location can be updated, should be between 60 and \
    86400
    :type live_period: int
    """
    def __init__(self, *, latitude, longitude, live_period):
        self.latitude = latitude
        self.longitude = longitude
        self.live_period = live_period

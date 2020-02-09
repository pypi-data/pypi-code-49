class Location:
    """This class represents a point on the map

    :param longitude: Longitude as defined by the sender
    :type longitude: float
    :param latitude: Latitude as defined by the sender
    :type latitude: float
    """
    def __init__(self, *, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

class ShippingAddress:
    """This class represents a shipping address

    :param country_code: USI 3166-1 alpha-2 country code
    :type country_code: str
    :param state: State, if applicable
    :type state: str
    :param city: City
    :type city: str
    :param street_line1: First line for the address
    :type street_line1: str
    :param street_line2: Second line for the address
    :type street_line2: str
    :param post_code: Address post code
    :type post_code: str
    """
    def __init__(self, *, country_code=None, state=None, city=None, street_line1=None,
                 street_line2=None, post_code=None):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

from enum import Enum, unique

__all__ = ['InvalidDNSType', 'DNSType']


class InvalidDNSType(Exception):

    def __init__(self, dns_type):
        self.message = f"{repr(dns_type)} is not a valid DNS type."

    def __str__(self):
        return self.message


@unique
class DNSType(Enum):
    """
    Enum of all the different record types

    Type IDs are not used in this program but its keeps naming inline with the RFCs:

    Reference: https://en.wikipedia.org/wiki/List_of_DNS_record_types#Resource_records
    """
    A = 1
    AAAA = 28
    CNAME = 5
    MX = 15
    NS = 2
    PTR = 12
    SRV = 33
    SOA = 6
    TXT = 16
    ANY = 255

    @classmethod
    def get(self, dns_type):
        """
        Returns the enum from a string or int
        """

        # We are already an enum so nothing more to do
        if isinstance(dns_type, self):
            return dns_type

        # Try and find the enum by the string value
        try:
            return self[dns_type.upper()]
        except (KeyError, AttributeError):
            pass

        # Try and find the enum by record type id
        try:
            return self(dns_type)
        except ValueError:
            pass

        # This is the exception we raise if the dns_type isn't valid
        raise InvalidDNSType(dns_type)

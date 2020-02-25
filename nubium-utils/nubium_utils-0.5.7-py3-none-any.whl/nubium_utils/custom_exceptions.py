
class NoMessageError(Exception):
    """
    No message was returned when consuming from the broker
    """
    pass


class NetworkError(Exception):
    """
    Generic network errors
    """
    pass


class ConsumeMessageError(Exception):
    """
    Non-trivial errors when consuming from the broker
    """
    pass


class MessageValueException(Exception):
    """
    Represents a significant error in the value of the message
    """
    pass


class ProduceHeadersException(Exception):
    """
    Represents a significant error in the value of the message
    """
    pass
class PassportElementErrorUnspecified:
    """This class represents an issue in an unspecified place. The error is considered resolved when new data is added

    :param source: Error source, must be **unspecified**
    :type source: str
    :param type_result: Type of element of the user's Telegram Passport which has the issue
    :type type_result: str
    :param element_hash: Base64 encoded element hash
    :type element_hash: str
    :param message: Error message
    :type message: str
    """
    def __init__(self, *, source, type_result, element_hash, message):
        self.source = source
        self.type_result = type_result
        self.element_hash = element_hash
        self.message = message

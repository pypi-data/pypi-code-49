class ClientAuthError(Exception):
    def __init__(self, message, errors=None):
        self.message = message
        self.errors = errors
        super().__init__(f"message: {self.message}, errors: {self.errors}")


class ClientValidationError(Exception):
    def __init__(self, message, errors=None):
        self.message = message
        self.errors = errors
        super().__init__(f"message: {self.message}, errors: {self.errors}")

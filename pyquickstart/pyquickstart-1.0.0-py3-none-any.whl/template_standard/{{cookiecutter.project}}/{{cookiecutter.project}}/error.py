class BaseError(Exception):
    """Basic exception for errors raised by pyquickstart"""
    pass


class ConfigurationError(BaseError):
    """Exception for misconfigurations"""
    def __init__(self, message):
        self.message = message

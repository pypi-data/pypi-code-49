class Settings:
    """ A static class containing settings for all Config children. """
    
    frozen: bool = False
    """ Represents if a config should be frozen or not. """
    
    def __new__(cls, *args, **kwargs):
        raise ValueError("Cannot instantiate the Settings")

__all__ = \
[
    'Settings',
]

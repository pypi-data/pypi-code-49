from ._JSONPropertyError import JSONPropertyError


class OptionalDisallowed(JSONPropertyError):
    """
    Error type for when trying to set a property as optional,
    but it is not allowed.
    """
    pass

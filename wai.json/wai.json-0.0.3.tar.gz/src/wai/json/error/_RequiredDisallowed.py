from ._JSONPropertyError import JSONPropertyError


class RequiredDisallowed(JSONPropertyError):
    """
    Error type for when trying to set a property as required,
    but it is not allowed.
    """
    pass

from ._JSONPropertyError import JSONPropertyError


class OfPropertySelectionError(JSONPropertyError):
    """
    Error for when an of-property (any-of, one-of, all-of) can't
    select a sub-property to match a value.
    """
    pass

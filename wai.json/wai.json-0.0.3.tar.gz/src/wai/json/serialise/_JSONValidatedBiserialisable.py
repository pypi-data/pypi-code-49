from abc import ABC

from ..validator import JSONValidator
from ._JSONBiserialisable import JSONBiserialisable, SelfType


class JSONValidatedBiserialisable(JSONValidator, JSONBiserialisable[SelfType], ABC):
    """
    Utility interface that specifies that a class is both biserialisable
    with JSON and that that JSON is validated.
    """
    pass

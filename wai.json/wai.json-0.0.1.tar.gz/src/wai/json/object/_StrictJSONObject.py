from typing import TypeVar

from ._JSONObject import JSONObject

SelfType = TypeVar("SelfType", bound='StrictJSONObject')


class StrictJSONObject(JSONObject[SelfType]):
    """
    Base class for JSON objects which don't support additional
    properties by default.
    """
    @classmethod
    def _additional_properties_validation(cls):
        return None

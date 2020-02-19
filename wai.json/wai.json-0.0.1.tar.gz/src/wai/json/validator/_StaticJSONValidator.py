from abc import ABC
from functools import lru_cache

from wai.common.meta import instanceoptionalmethod

from ..schema import JSONSchema
from ._JSONValidator import JSONValidator


class StaticJSONValidator(JSONValidator, ABC):
    """
    Base class for JSON validators whose schema is
    constant for the lifetime of the class/object.
    """
    @instanceoptionalmethod
    @lru_cache(maxsize=None)
    def get_json_validation_schema(self) -> JSONSchema:
        return super().get_json_validation_schema()

    @instanceoptionalmethod
    @lru_cache(maxsize=None)
    def get_validator(self):
        return super().get_validator()

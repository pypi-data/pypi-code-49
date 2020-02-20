from abc import ABC

from wai.common.meta import instanceoptionalmethod

from ..schema import JSONSchema
from ._JSONValidator import JSONValidator


class StaticJSONValidator(JSONValidator, ABC):
    """
    Base class for JSON validators whose schema is
    constant for the lifetime of the class/object.
    """
    @instanceoptionalmethod
    def get_json_validation_schema(self) -> JSONSchema:
        if not hasattr(self, "__json_validation_schema"):
            setattr(self, "__json_validation_schema", super().get_json_validation_schema())

        return getattr(self, "__json_validation_schema")

    @instanceoptionalmethod
    def get_validator(self):
        if not hasattr(self, "__validator"):
            setattr(self, "__validator", super().get_validator())

        return getattr(self, "__validator")

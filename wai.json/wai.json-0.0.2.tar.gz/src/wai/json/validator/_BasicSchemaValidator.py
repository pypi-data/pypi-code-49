from ..schema import JSONSchema
from ._JSONValidator import JSONValidator


class BasicSchemaValidator(JSONValidator):
    """
    Basic wrapper for a JSON schema which presents it as a validator.
    """
    def __init__(self, schema: JSONSchema):
        self._schema = schema

    def _get_json_validation_schema(self) -> JSONSchema:
        return self._schema

from typing import Optional, Any

from ...schema import JSONSchema, TRIVIALLY_FAIL_SCHEMA
from .._typing import PropertyValueType
from ._Property import Property


class RawProperty(Property):
    """
    Property which takes raw JSON values. Uses a schema for validation.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 *,
                 schema: JSONSchema = TRIVIALLY_FAIL_SCHEMA,
                 optional: bool = False):
        super().__init__(name, optional=optional)

        self._schema = schema

    def _get_json_validation_schema(self) -> JSONSchema:
        return self._schema

    def _validate_value(self, value: Any) -> PropertyValueType:
        # Perform schema validation
        self.validate_raw_json(value)

        return value

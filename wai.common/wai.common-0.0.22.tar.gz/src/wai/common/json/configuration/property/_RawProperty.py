from ...schema import JSONSchema, TRIVIALLY_FAIL_SCHEMA
from ..._typing import RawJSONElement
from ._Property import Property


class RawProperty(Property):
    """
    Property which takes raw JSON values. Uses a schema for validation.
    """
    def __init__(self,
                 name: str = "",
                 schema: JSONSchema = TRIVIALLY_FAIL_SCHEMA,
                 *,
                 optional: bool = False):
        super().__init__(name, optional=optional)

        self.__schema = schema

    def get_json_validation_schema(self) -> JSONSchema:
        return self.__schema

    def _value_as_raw_json(self, instance, value) -> RawJSONElement:
        # Raw properties store raw JSON already, so just return it
        return value

    def validate_value(self, instance, value):
        # Validate the raw JSON with our schema
        try:
            self.validate_raw_json(value)
            return value
        except Exception as e:
            raise ValueError(f"{value} failed schema validation") from e

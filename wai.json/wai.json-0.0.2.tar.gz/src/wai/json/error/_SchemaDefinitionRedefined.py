from ._JSONSchemaError import JSONSchemaError


class SchemaDefinitionRedefined(JSONSchemaError):
    """
    Error for when consolidating schema definitions and
    an attempt is made to redefine a definition.
    """
    def __init__(self, definition_name: str, original_definition, new_definition):
        super().__init__(f"Attempted to redefine JSON schema definition '{definition_name}': "
                         f"from {original_definition} to {new_definition}")

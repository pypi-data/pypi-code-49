class InvalidGraphObject(Exception):

    def __init__(self, object_type, required_fields, missing_key):
        self._object_type = object_type
        self._required_fields = required_fields
        self._missing_key = missing_key

    def __str__(self):
        return f"""
                {self._object_type} object instantiation failed - Invalid mapping object:
                Must contain the following keys: {self._required_fields}

                {self._missing_key} is missing.
                """


class SchemaRegistryError(Exception):

    def __init__(self, mesg):
        self._mesg = mesg

    def __str__(self):
        return f"""
                Schema registry error:
                {self._mesg}
                """


class SQLQueryInvalid(Exception):

    def __init__(self, schema):
        self._schema = schema

    def __str__(self):
        return f"""
                Schema placeholder not found:
                {self._schema}
                """

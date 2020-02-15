from .schema_validation import SchemaValidation


class ProjectDatasetSchema():
    '''

    '''

    def __init__(self, client, schema=None, columnOverrides=None, metadata=None, schemaValidation={}):
        self.client = client
        self.id = schema
        self.schema = schema
        self.column_overrides = columnOverrides
        self.metadata = metadata
        self.schema_validation = SchemaValidation(
            client, **schemaValidation) if schemaValidation else None

    def __repr__(self):
        return f"ProjectDatasetSchema(schema={repr(self.schema)}, column_overrides={repr(self.column_overrides)}, metadata={repr(self.metadata)}, schema_validation={repr(self.schema_validation)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'schema': self.schema, 'column_overrides': self.column_overrides, 'metadata': self.metadata, 'schema_validation': self.schema_validation.to_dict() if self.schema_validation else None}

    def refresh(self):
        self = self.describe()
        return self

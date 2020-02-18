"""Provides the SubjectMap class."""

import json

from ....util import custom_json_serializer


class SubjectMap:

    """Represents a single subject map entry

    Attributes:
        ingest_id (int): The id of the ingest operation this belongs to
        subject_id (int): Increamental, number only subject id
        subject_code (str): The formatted subject code
        field_values (list): List of field values
    """

    def __init__(self, ingest_id=None, subject_id=None, subject_code=None, field_values=None):
        self.ingest_id = ingest_id
        self.subject_id = subject_id
        self.subject_code = subject_code
        self.field_values = field_values

    @staticmethod
    def map_field(key, value):
        """Convert from object to map for serialization"""
        if key == "field_values":
            if isinstance(value, list):
                return json.dumps(value, default=custom_json_serializer)
            return value

        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into SubjectMap

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            SubjectMap: The deserialized ingest item
        """
        result = SubjectMap(**kwargs)
        for attr in ["field_values"]:
            value = getattr(result, attr, None)
            if value is not None:
                setattr(result, attr, json.loads(value))

        return result

    def __repr__(self):
        return f"SubjectMap(ingest_id={self.ingest_id},subject_code={self.subject_code})"

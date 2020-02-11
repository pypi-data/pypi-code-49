"""Provides the DeidLog class."""

import json

from ....util import custom_json_serializer


class DeidLog:

    """Represents a single deid log entry

    Attributes:
        ingest_id (int): The id of the ingest operation this belongs to
        path (int): File path
        log_type (str): Field values before or after
        field_values (dict): List of field values
        created (datetime): The timestamp when the log was created
    """

    def __init__(self, ingest_id=None, path=None, log_type=None, field_values=None, created=None):
        self.ingest_id = ingest_id
        self.path = path
        self.log_type = log_type
        self.field_values = field_values
        self.created = created

    @staticmethod
    def map_field(key, value):
        """Convert from object to map for serialization"""
        if key == "field_values":
            if isinstance(value, dict):
                return json.dumps(value, default=custom_json_serializer)
            return value

        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into DeidLog

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            DeidLog: The deserialized ingest item
        """
        result = DeidLog(**kwargs)
        for attr in ["field_values"]:
            value = getattr(result, attr, None)
            if value is not None:
                setattr(result, attr, json.loads(value))

        return result

    def __repr__(self):
        return f"DeidLog(ingest_id={self.ingest_id},path={self.path})"

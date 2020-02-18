"""Provides IngestItem model class."""

import json

from ....util import custom_json_serializer


class IngestItem:
    """Represents an ingest item.

    Attributes:
        item_id (int): The unique ID of this item.
        ingest_id (int): The ID of the ingest operation this belongs to.
        subdir (str): The common subdirectory for files to be processed.
        files (list): The list of files to be processed, discovered during scanning.
        item_type (str): The type of task this is (e.g. file, packfile, metadata).
        context (dict): The free-form context for this ingest item
        mtime (datetime): The most recent modified time for any of the files
        warnings (list): Any warnings that were encountered.
        errors (list): Any errors that were encountered.

    """

    def __init__(self, item_id=None, ingest_id=None, subdir=None, files=None,  # pylint: disable=too-many-arguments
                 item_type=None, context=None, size=None, mtime=None, warnings=None, errors=None):
        """Create an IngestItem"""
        self.item_id = item_id
        self.ingest_id = ingest_id
        self.subdir = subdir
        self.files = files
        self.item_type = item_type
        self.context = context
        self.size = size
        self.mtime = mtime
        self.warnings = warnings
        self.errors = errors

    @staticmethod
    def map_field(key, value):
        """Convert from object to map for serialization"""
        if key == "context" and value is not None:
            if isinstance(value, dict):
                return json.dumps(value, default=custom_json_serializer)
            return value
        if key in ["files", "warnings", "errors"] and value is not None:
            if isinstance(value, list):
                return json.dumps(value, default=custom_json_serializer)
            return value
        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into IngestItem.

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            IngestItem: The deserialized ingest item
        """
        result = IngestItem(**kwargs)
        for attr in ["context", "files", "warnings", "errors"]:
            value = getattr(result, attr, None)
            if value is not None:
                setattr(result, attr, json.loads(value))

        return result

    def __repr__(self):
        return f"IngestItem(item_id={self.item_id},ingest_id={self.ingest_id},item_type={self.item_type},subdir={self.subdir})"

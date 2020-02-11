"""Provides the IngestOperation and IngestStage classes."""

import json
from enum import Enum

from ....util import custom_json_serializer


class IngestStage(Enum):
    """Represents the possible values for IngestStage"""
    scan = 'scan'
    review = 'review'
    processing = 'processing'
    complete = 'complete'
    aborted = 'aborted'


class IngestOperation:
    """Represents a single IngestOperation.

    Attributes:
        ingest_id (int): The unique id of the ingest
        name (str): A unique name for the ingest (collected at start time)
        created (datetime): The timestamp when the ingest was created
        fs_path (str): The filesystem path (e.g. s3://bucket-name or /mnt/share)
        config (str): The entire materialized configuration for the import, includes device/api key
        stage (str): The current stage of the import
        version (str): The product version - workers should not start if this is a mismatch
    """
    # pylint: disable=too-many-arguments

    def __init__(self, ingest_id=None, name=None, created=None, fs_path=None, config=None,
                 stage=None, version=None, processing_start=None, processing_end=None):

        """Creates a new IngestOperation"""
        self.ingest_id = ingest_id
        self.name = name
        self.created = created
        self.fs_path = fs_path
        self.config = config
        self.stage = stage
        self.version = version
        self.processing_start = processing_start
        self.processing_end = processing_end

    @staticmethod
    def map_field(key, value):
        """Convert from object to map for serialization"""
        if key == 'config' and value is not None:
            if isinstance(value, dict):
                return json.dumps(value, default=custom_json_serializer)
        if key == 'stage' and isinstance(value, IngestStage):
            return value.value
        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into IngestOperation.

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            IngestOperation: The deserialized ingest operation
        """
        result = IngestOperation(**kwargs)
        if result.config is not None:
            result.config = json.loads(result.config)
        if result.stage is not None:
            result.stage = IngestStage(result.stage)

        return result

    def __repr__(self):
        return f"IngestOperation(ingest_id={self.ingest_id},name={self.name},fs_path={self.fs_path})"

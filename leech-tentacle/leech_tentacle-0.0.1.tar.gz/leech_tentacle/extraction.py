from typing import Iterable

from algernon import AlgObject

from leech_tentacle.extraction_config import ExtractionConfig


class ExtractedData(AlgObject):
    def __init__(
            self,
            extraction_type: str,
            capture_timestamp: float,
            object_type: str,
            id_source: str,
            source_name: str,
            extracted_data: object
    ):
        self._extraction_type = extraction_type
        self._capture_timestamp = capture_timestamp
        self._object_type = object_type
        self._id_source = id_source
        self._source_name = source_name
        self._extracted_data = extracted_data

    @classmethod
    def parse_json(cls, json_dict):
        return cls(
            capture_timestamp=json_dict['capture_timestamp'],
            extraction_type=json_dict['extraction_type'],
            object_type=json_dict['object_type'],
            id_source=json_dict['id_source'],
            source_name=json_dict['source_name'],
            extracted_data=json_dict['extracted_data']
        )

    @classmethod
    def from_extraction_config(
            cls,
            extraction_config: ExtractionConfig,
            capture_timestamp: float,
            extracted_data: object
    ):
        return cls(
            extraction_type=extraction_config.extraction_type,
            object_type=extraction_config.extracted_object_type,
            id_source=extraction_config.id_source,
            source_name=extraction_config.source_name,
            extracted_data=extracted_data,
            capture_timestamp=capture_timestamp
        )

    @property
    def extraction_type(self) -> str:
        return self._extraction_type

    @property
    def object_type(self) -> str:
        return self._object_type

    @property
    def id_source(self) -> str:
        return self._id_source

    @property
    def source_name(self) -> str:
        return self._source_name

    @property
    def extracted_data(self) -> object:
        return self._extracted_data

    @property
    def capture_timestamp(self) -> float:
        return self._capture_timestamp


class ProcessedExtraction(AlgObject):
    def __init__(
            self,
            id_source: str,
            source_name: str,
            capture_timestamp: float,
            extracted_object_type: str,
            processed_data: Iterable[object]
    ):
        self._id_source = id_source
        self._source_name = source_name
        self._capture_timestamp = capture_timestamp
        self._extracted_object_type = extracted_object_type
        self._processed_data = processed_data

    @classmethod
    def parse_json(cls, json_dict):
        return cls(
            id_source=json_dict['id_source'],
            source_name=json_dict['source_name'],
            capture_timestamp=json_dict['capture_timestamp'],
            extracted_object_type=json_dict['extracted_object_type'],
            processed_data=json_dict['processed_data']
        )

    @property
    def id_source(self) -> str:
        return self._id_source

    @property
    def source_name(self) -> str:
        return self._source_name

    @property
    def capture_timestamp(self) -> float:
        return self._capture_timestamp

    @property
    def extracted_object_type(self) -> str:
        return self._extracted_object_type

    @property
    def processed_data(self) -> Iterable[object]:
        return self._processed_data


class DataAsset:
    def __init__(self, id_source: str, source_name: str, capture_timestamp: float, asset_type: str, asset_data):
        self._id_source = id_source
        self._source_name = source_name
        self._capture_timestamp = capture_timestamp
        self._asset_type = asset_type
        self._asset_data = asset_data

    @property
    def id_source(self):
        return self._id_source

    @property
    def source_name(self):
        return self._source_name

    @property
    def capture_timestamp(self):
        return self._capture_timestamp

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def asset_data(self):
        return self._asset_data

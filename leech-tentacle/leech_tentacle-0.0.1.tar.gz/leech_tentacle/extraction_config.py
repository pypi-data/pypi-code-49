from algernon import AlgObject


class ExtractionConfig(AlgObject):
    def __init__(
            self,
            id_source: str,
            source_name: str,
            extraction_type: str,
            extractor_class: str,
            extractor_params: str,
            processor_class: str,
            processor_params,
            extracted_object_type: str,
            extraction_params
    ):
        self._id_source = id_source
        self._source_name = source_name
        self._extraction_type = extraction_type
        self._extractor_class = extractor_class
        self._extractor_params = extractor_params
        self._processor_class = processor_class
        self._processor_params = processor_params
        self._extracted_object_type = extracted_object_type
        self._extraction_params = extraction_params

    @classmethod
    def parse_json(cls, json_dict):
        return cls(
            id_source=json_dict['id_source'],
            source_name=json_dict['source_name'],
            extraction_type=json_dict['extraction_type'],
            extractor_class=json_dict['extractor_class'],
            extractor_params=json_dict['extractor_params'],
            processor_class=json_dict['processor_class'],
            processor_params=json_dict['processor_params'],
            extracted_object_type=json_dict['extracted_object_type'],
            extraction_params=json_dict['extraction_params']
        )

    @property
    def id_source(self):
        return self._id_source

    @property
    def source_name(self):
        return self._source_name

    @property
    def extraction_type(self) -> str:
        return self._extraction_type

    @property
    def extractor_class(self) -> str:
        return self._extractor_class

    @property
    def extractor_params(self):
        return self._extractor_params

    @property
    def processor_class(self) -> str:
        return self._processor_class

    @property
    def processor_params(self):
        return self._processor_params

    @property
    def extracted_object_type(self) -> str:
        return self._extracted_object_type

    @property
    def extraction_params(self):
        return self._extraction_params

from __future__ import annotations
from leech_tentacle.extraction import ExtractedData
from leech_tentacle.extraction_config import ExtractionConfig


class Extractor:
    @classmethod
    def generate(cls, extraction_config: ExtractionConfig) -> Extractor:
        raise NotImplementedError()

    def perform_extraction(self, extraction_config: ExtractionConfig) -> ExtractedData:
        raise NotImplementedError()

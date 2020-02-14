from __future__ import annotations

from leech_tentacle.extraction import ExtractedData, ProcessedExtraction
from leech_tentacle.extraction_config import ExtractionConfig


class Processor:
    @classmethod
    def generate(cls, extraction_config: ExtractionConfig) -> Processor:
        raise NotImplementedError()

    def process(self, extraction: ExtractedData) -> ProcessedExtraction:
        raise NotImplementedError()

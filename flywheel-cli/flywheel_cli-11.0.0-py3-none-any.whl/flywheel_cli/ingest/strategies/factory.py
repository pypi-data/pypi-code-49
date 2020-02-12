"""Provides factory method to create ingest strategy"""
from .dicom import DicomIngestStrategy
from .folder import FolderIngestStrategy
from .template import TemplateIngestStrategy

STRATEGIES_MAP = {
    "dicom": DicomIngestStrategy,
    "folder": FolderIngestStrategy,
    "template": TemplateIngestStrategy,
}


def create_ingest_strategy(strategy, config):
    """Create an ingest strategy instance"""
    strategy_cls = STRATEGIES_MAP.get(strategy, config)
    return strategy_cls(config)

"""Provides factory method to create importers"""
from .dicom import DicomImporter
from .folder import FolderImporter
from .template import TemplateImporter

IMPORTER_MAP = {
    'dicom': DicomImporter,
    'folder': FolderImporter,
    'template': TemplateImporter,
}


def create_importer(config):
    """Create an importer instance from dict"""
    importer_cls = IMPORTER_MAP.get(config.importer_type)
    return importer_cls(config)

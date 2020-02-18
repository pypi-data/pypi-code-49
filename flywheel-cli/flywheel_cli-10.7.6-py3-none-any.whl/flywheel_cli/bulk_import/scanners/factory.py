"""Provides factory method to create scanner instances"""
from .dicom import DicomScanner

SCANNER_MAP = {
    "dicom": DicomScanner
}


def create_scanner_task(scan_task, factory, config):
    """Initialite a given type of scanner."""
    scanner_cls = SCANNER_MAP.get(scan_task.scanner_type)
    if not scanner_cls:
        raise Exception(f"Unknown scanner type: {scan_task.scanner_type}")
    return scanner_cls(scan_task, factory, config)

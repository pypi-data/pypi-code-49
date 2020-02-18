import pytest

from flywheel_cli.bulk_import.db import create_ingest_factory


def test_bulk_import_ingest_factory_invalid_provider():
    with pytest.raises(Exception):
        create_ingest_factory("unknown")

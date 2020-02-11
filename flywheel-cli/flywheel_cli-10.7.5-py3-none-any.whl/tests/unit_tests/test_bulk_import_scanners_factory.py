import copy

import pytest

from flywheel_cli.bulk_import.db.models import ScanTask, TaskStatus
from flywheel_cli.bulk_import.scanners.factory import create_scanner_task

MOCK_TASK_REC = ScanTask(
    ingest_id=1,
    path="/test/folder",
    context={"foo": "bar"},
    scanner_type="dicom",
    actor_id="actor_1",
    status=TaskStatus.waiting,
)


def test_scanners_factory_type_is_invalid(ingest_factory):
    item = copy.copy(MOCK_TASK_REC)
    item.scanner_type = "foo"
    with pytest.raises(Exception):
        scanner_task = create_scanner_task(item, ingest_factory, None)

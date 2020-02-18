import copy

import pytest

from flywheel_cli.bulk_import.db.models import WorkTask, TaskStatus

MOCK_REC = WorkTask(
    ingest_id=1,
    item_id=2,
    status=TaskStatus.waiting,
)


def test_bulk_import_work_queue_create(db_type, ingest_factory):
    factory = ingest_factory(db_type)

    queue = factory.create_work_queue_mapper()
    assert queue is not None

    queue.initialize()
    queue.initialize()  # Idempotent


def test_bulk_import_work_queue_insert(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    queue = factory.create_work_queue_mapper()

    queue.initialize()

    rowid = queue.insert(MOCK_REC)
    assert rowid is not None

    # Verify existence
    item = queue.find(rowid)
    assert item
    assert item.task_id == rowid
    assert item.status == TaskStatus.waiting


def test_bulk_import_work_queue_get(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    queue = factory.create_work_queue_mapper()

    # Insert 1 item into the queue
    queue.initialize()
    rowid = queue.insert(MOCK_REC)

    # Take one item from the queue
    item = queue.get("actor_1")
    assert item is not None
    assert item.task_id == rowid
    assert item.status == TaskStatus.processing
    assert item.actor_id == "actor_1"

    # Verify that it was updated in the database
    item = queue.find(rowid)
    assert item.status == TaskStatus.processing
    assert item.actor_id == "actor_1"

    # Verify that the next take returns nothing
    item = queue.get("actor_1")
    assert item is None


def test_bulk_import_work_queue_update(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    queue = factory.create_work_queue_mapper()

    # Insert 1 item into the queue
    queue.initialize()
    rowid = queue.insert(MOCK_REC)

    with pytest.raises(Exception):
        queue.update(rowid, foo="bar")

    queue.update(rowid, status="complete")
    item = queue.find(rowid)
    assert item.status == TaskStatus.complete

    # Test JSON in context
    queue.update(rowid, context={"foo": "bar"})
    item = queue.find(rowid)
    assert item.context == {"foo": "bar"}


def test_bulk_import_work_queue_is_complete(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    queue = factory.create_work_queue_mapper()

    queue.initialize()

    assert queue.is_complete()

    queue.insert(MOCK_REC)
    assert not queue.is_complete()


def test_bulk_import_work_queue_is_complete_ingest(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    queue = factory.create_work_queue_mapper()

    queue.initialize()

    assert queue.is_complete_ingest(1)

    mock_rec = copy.copy(MOCK_REC)
    mock_rec.ingest_id = 1
    queue.insert(mock_rec)
    assert not queue.is_complete_ingest(1)

import copy
import datetime

import pytest

from flywheel_cli.bulk_import.db.models import IngestItem

MOCK_MODIFIED_DATE = datetime.datetime.now()
MOCK_REC = IngestItem(
    ingest_id=1,
    subdir="/test/folder",
    files=["file_1.txt"],
    item_type="file",
    context={"foo": "bar"},
    mtime=MOCK_MODIFIED_DATE,
)


def test_ingest_items_mapper_create(db_type, ingest_factory):
    factory = ingest_factory(db_type)

    mapper = factory.create_ingest_items_mapper()
    assert mapper is not None

    mapper.initialize()
    mapper.initialize()  # Idempotent


def test_ingest_items_mapper_insert(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    mapper = factory.create_ingest_items_mapper()

    mapper.initialize()

    # Insert
    rowid = mapper.insert(MOCK_REC)

    # Retrieve by id
    rec = mapper.find(rowid)
    assert rec is not None
    assert rec.item_id == rowid
    assert rec.ingest_id == 1
    assert rec.subdir == "/test/folder"
    assert rec.files == ["file_1.txt"]
    assert rec.item_type == "file"
    assert rec.context == {"foo": "bar"}
    assert rec.mtime == MOCK_MODIFIED_DATE


def test_ingest_mapper_update(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    mapper = factory.create_ingest_items_mapper()

    mapper.initialize()

    # Insert
    rowid = mapper.insert(MOCK_REC)
    mtime = datetime.datetime.now()
    # Update
    mapper.update(rowid, context={"bar": "foo"}, mtime=mtime)

    # Retrieve by id
    rec = mapper.find(rowid)
    assert rec is not None
    assert rec.item_id == rowid
    assert rec.ingest_id == 1
    assert rec.subdir == "/test/folder"
    assert rec.files == ["file_1.txt"]
    assert rec.item_type == "file"
    assert rec.context == {"bar": "foo"}
    assert rec.mtime == mtime

def test_ingest_mapper_update_invalid_key(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    mapper = factory.create_ingest_items_mapper()

    mapper.initialize()

    # Update
    with pytest.raises(Exception):
        mapper.update(1, invalid={"bar": "foo"})


def test_ingest_mapper_get_all_item_for_ingest(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    mapper = factory.create_ingest_items_mapper()
    mapper.initialize()

    rowid = mapper.insert(MOCK_REC)
    item_2_rec = copy.copy(MOCK_REC)
    item_2_rec.ingest_id = 2
    rowid = mapper.insert(item_2_rec)

    items = list(mapper.get_all_item_for_ingest(1))
    assert len(items) == 1
    item = items[0]
    assert item.ingest_id == 1

def test_ingest_mapper__find_one_stop_iter(db_type, ingest_factory):
    factory = ingest_factory(db_type)
    mapper = factory.create_ingest_items_mapper()
    mapper.initialize()

    rowid = mapper.insert(MOCK_REC)

    command = "SELECT * FROM ingest_items WHERE item_id = 5"
    item = mapper._find_one(command)
    assert item is None


def test_ingest_item_repr():
    rec = copy.copy(MOCK_REC)
    rec.item_id = 1
    assert str(rec) == "IngestItem(item_id=1,ingest_id=1,item_type=file,subdir=/test/folder)"

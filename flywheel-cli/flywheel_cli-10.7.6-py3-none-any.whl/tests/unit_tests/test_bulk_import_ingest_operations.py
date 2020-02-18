import copy
import datetime

from flywheel_cli.bulk_import.db.models import IngestOperation, IngestStage

MOCK_START_DATE = datetime.datetime.now()
MOCK_REC = IngestOperation(
    name="Test Ingest",
    created=MOCK_START_DATE,
    fs_path="osfs:///tmp/import",
    config={"foo": "bar"},
    stage="scan",
    version="1.0.0-dev.1",
)


def test_ingest_mapper_create(db_type, ingest_factory):
    factory = ingest_factory(db_type)

    mapper = factory.create_mapper()
    assert mapper is not None

    mapper.initialize()
    mapper.initialize()  # Idempotent


def test_ingest_mapper_insert(db_type, ingest_factory):
    factory = ingest_factory(db_type)

    mapper = factory.create_mapper()
    assert mapper is not None

    mapper.initialize()

    # Insert
    rowid = mapper.insert(MOCK_REC)

    # Retrieve by id
    rec = mapper.find(rowid)
    assert rec is not None
    assert rec.ingest_id == rowid
    assert rec.name == "Test Ingest"
    assert rec.created == MOCK_START_DATE
    assert rec.fs_path == "osfs:///tmp/import"
    assert rec.config == {"foo": "bar"}
    assert rec.stage == IngestStage.scan
    assert rec.version == "1.0.0-dev.1"


def test_ingest_mapper_update(db_type, ingest_factory):
    factory = ingest_factory(db_type)

    mapper = factory.create_mapper()
    assert mapper is not None

    mapper.initialize()

    # Insert
    rowid = mapper.insert(MOCK_REC)

    # Update
    mapper.update(rowid, stage=IngestStage.review, config={"bar": "foo"})

    # Retrieve by id
    rec = mapper.find(rowid)
    assert rec is not None
    assert rec.ingest_id == rowid
    assert rec.name == "Test Ingest"
    assert rec.created == MOCK_START_DATE
    assert rec.fs_path == "osfs:///tmp/import"
    assert rec.config == {"bar": "foo"}
    assert rec.stage == IngestStage.review
    assert rec.version == "1.0.0-dev.1"


def test_ingest_operation_repr():
    rec = copy.copy(MOCK_REC)
    rec.ingest_id = 1
    assert str(rec) == "IngestOperation(ingest_id=1,name=Test Ingest,fs_path=osfs:///tmp/import)"

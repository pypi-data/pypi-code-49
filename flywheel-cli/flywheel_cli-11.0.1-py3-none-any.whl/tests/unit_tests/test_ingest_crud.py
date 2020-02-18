import datetime
from uuid import UUID, uuid4

import pytest
from sqlalchemy.orm.exc import NoResultFound

from flywheel_cli.ingest import crud, models, schemas, utils


def test_create_ingest(db):
    ingest = crud.create_ingest(db, schemas.IngestIn(
        src_fs  = "/tmp",
        config  = {},
        label   = "label",
        api_key = "api_key",
        fw_host = "flywheel.test",
        fw_user = "test@flywheel.test",
    ))

    assert isinstance(ingest, schemas.IngestOut)
    assert isinstance(ingest.id, UUID)
    assert isinstance(ingest.created, datetime.datetime)
    assert ingest.status  == "created"
    assert ingest.src_fs  == "/tmp"
    assert ingest.config  == {}
    assert ingest.label   == "label"
    assert ingest.api_key == "api_key"
    assert ingest.fw_host == "flywheel.test"
    assert ingest.fw_user == "test@flywheel.test"

    db_ingest = db.query(models.Ingest).filter_by(id=ingest.id).one()
    assert db_ingest.schema() == ingest


def test_get_ingests_empty(db):
    ingests = crud.get_ingests(db)
    assert ingests == []


def test_get_ingests(db, data):
    ingest_id_1 = data.create("Ingest")
    ingest_id_2 = data.create("Ingest")

    ingests = crud.get_ingests(db)
    assert len(ingests) == 2
    assert {ingest.id for ingest in ingests} == {ingest_id_1, ingest_id_2}


def test_get_ingest_nonexistent_id(db):
    with pytest.raises(NoResultFound):
        crud.get_ingest(db, uuid4())


def test_get_ingest(db, data):
    ingest_id = data.create("Ingest")

    ingest = crud.get_ingest(db, ingest_id)
    assert ingest.id == ingest_id


def test_start_ingest(db, data):
    ingest_id = data.create("Ingest")

    ingest = crud.start_ingest(db, ingest_id)
    assert ingest.status == "scanning"
    assert db.query(models.Task).filter_by(
        ingest_id = ingest_id,
        type      = "scan",
        status    = "pending",
    ).count() == 1


def test_set_ingest_status(db, data):
    ingest_id = data.create("Ingest")
    ingest = crud.set_ingest_status(db, ingest_id, "scanning")
    assert ingest.status == "scanning"
    ingest = crud.set_ingest_status(db, ingest_id, "failed")
    assert ingest.status == "failed"
    ingest = crud.set_ingest_status(db, ingest_id, "resolving")
    assert ingest.status == "failed"


def test_abort_ingest(db, data):
    ingest_id = data.create("Ingest")
    ingest = crud.abort_ingest(db, ingest_id)
    assert ingest.status == "aborted"
    last_history = ingest.history[-1]
    assert last_history[0] == "aborted"
    # abort idempotent
    ingest = crud.abort_ingest(db, ingest_id)
    assert last_history == ingest.history[-1]


# TODO unify and move engine/session creation to code
# TODO use the same fixtures in ingest api and cli

@pytest.fixture(scope="function")
def db():
    """Return in-memory sqlite DB session for testing"""
    engine, sessionmaker = utils.init_sqla()
    return sessionmaker()


@pytest.fixture(scope="function")
def defaults():
    """Return default kwargs for creating DB models with"""
    return AttrDict(
        Ingest = dict(
            src_fs  = "/tmp",
            api_key = "flywheel.test:admin-apikey",
            fw_host = "flywheel.test",
            fw_user = "admin@flywheel.test",
            config  = {},
        ),
        Task = dict(),
        Container = dict(),
        Item = dict(),
        Review = dict(),
        Subject = dict(),
        DeidLog = dict(),
    )


@pytest.fixture(scope="function")
def data(db, defaults):
    """Return Data instance for simple DB record creation"""
    return Data(db, defaults)


class Data:
    """DB record creation helper"""
    def __init__(self, db, defaults):
        self.db = db
        self.defaults = defaults

    def create(self, cls_name, **kwargs):
        cls = getattr(models, cls_name)
        cls_defaults = self.defaults.get(cls_name, {})
        for key, value in cls_defaults.items():
            kwargs.setdefault(key, value)
        if cls_name == "Container" and isinstance(kwargs.get("level"), str):
            kwargs["level"] = getattr(schemas.ContainerLevel, kwargs["level"])
        record = cls(**kwargs)
        self.db.add(record)
        self.db.commit()
        if cls_name == "Ingest":
            ref_cls_names = [name for name in self.defaults if name != "Ingest"]
            for ref_cls_name in ref_cls_names:
                self.defaults[ref_cls_name]["ingest_id"] = record.id
        elif cls_name == "Container":
            self.defaults["Container"]["parent_id"] = record.id
            self.defaults["Item"]["container_id"] = record.id
        return record.id


class AttrDict(dict):
    """Utility class for creating mock objects with simple attr access"""
    def __getattr__(self, attr):
        try:
            value = self[attr]
        except KeyError:
            raise AttributeError(attr)
        if isinstance(value, dict):
            value = AttrDict(value)
        return value

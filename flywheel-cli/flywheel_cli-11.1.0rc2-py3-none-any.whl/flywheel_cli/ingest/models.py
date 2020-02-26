# pylint: disable=E0213,W0613,R0201
"""SQLAlchemy DB models"""
import datetime
import random
import string
import uuid

import sqlalchemy as sqla
from sqlalchemy_utils import UUIDType

from . import schemas


Base = sqla.ext.declarative.declarative_base()  # pylint: disable=invalid-name


def create_tables(engine: sqla.engine.Engine) -> None:
    """Create all DB tables as defined by the models"""
    Base.metadata.create_all(engine)


class IDMixin:
    """Mixin defining uuid primary key and schema serialization"""
    @sqla.ext.declarative.declared_attr
    def id(cls):  # pylint: disable=no-self-argument, invalid-name
        """ID primary key column (default: python-generated random uuid)"""
        return sqla.Column(UUIDType, primary_key=True, default=uuid.uuid4)

    def schema(self):
        """Return sqla model as pydantic schema"""
        schema_cls = getattr(schemas, f"{type(self).__name__}Out")
        return schema_cls.from_orm(self)


class IngestRefMixin:
    """Mixin defining many-to-one relationship to an ingest"""
    @sqla.ext.declarative.declared_attr
    def ingest_id(cls):
        """Ingest ID foreign key column"""
        return sqla.Column(UUIDType, sqla.ForeignKey("ingest.id"))

    @sqla.ext.declarative.declared_attr
    def ingest(cls):
        """Ingest relationship with (pluralized) backref"""
        return sqla.orm.relationship("Ingest", backref=f"{cls.__tablename__}s")


class StatusMixin:
    """Mixin adding status, status change validation and history"""
    @property
    def status_enum(self):
        """Abstract property to be defined w/ the status enum class"""
        raise NotImplementedError

    @property
    def status_transitions(self):
        """Abstract property to be defined w/ allowed status transitions"""
        raise NotImplementedError

    @classmethod
    def is_terminal(cls, status):
        """Return True if status is among the terminal statuses"""
        # pylint: disable=E1101
        status_value = cls.status_enum.get_item(status).value
        return cls.status_transitions.get(status_value) == set()

    @sqla.orm.validates("status")
    def validate_status(self, key, value):
        """Validate status change and add history record"""
        old = self.status_enum.get_item(self.status).value if self.status else None
        new = self.status_enum.get_item(value).value
        if old and new not in self.status_transitions[old]:
            raise ValueError(f"Invalid status transition {old} -> {new}")
        if self.history is None:
            self.history = []
        self.history.append(create_history_record(new))
        sqla.orm.attributes.flag_modified(self, "history")
        return new


def generate_ingest_label():
    """Generate random ingest operation label"""
    rand = random.SystemRandom()
    chars = string.ascii_uppercase + string.digits
    return "".join(rand.choice(chars) for _ in range(8))


def create_history_record(status):
    """Create status history record (status, timestamp)"""
    return status, datetime.datetime.now(tz=datetime.timezone.utc).timestamp()


class Ingest(IDMixin, StatusMixin, Base):
    """Ingest operation model"""
    __tablename__ = "ingest"
    created = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow)
    modified = sqla.Column(sqla.DateTime, onupdate=datetime.datetime.utcnow)
    label = sqla.Column(sqla.String, unique=True, default=generate_ingest_label)
    src_fs = sqla.Column(sqla.String)
    api_key = sqla.Column(sqla.String)
    fw_host = sqla.Column(sqla.String)
    fw_user = sqla.Column(sqla.String)
    config = sqla.Column(sqla.JSON)
    status = sqla.Column(sqla.String, default=schemas.IngestStatus.created)
    history = sqla.Column(sqla.JSON, default=lambda: [])

    # pylint: disable=C0326
    status_enum = schemas.IngestStatus
    status_transitions = {
        None:         {"created"},
        "created":    {"scanning",            "aborted"},
        "scanning":   {"resolving", "failed", "aborted"},
        "resolving":  {"in_review", "failed", "aborted"},
        "in_review":  {"preparing",           "aborted"},
        "preparing":  {"uploading", "failed", "aborted"},
        "uploading":  {"finalizing",          "aborted"},
        "finalizing": {"finished",  "failed", "aborted"},
        "finished":   set(),
        "failed":     set(),
        "aborted":    set(),
    }


class Task(IDMixin, IngestRefMixin, StatusMixin, Base):
    """Task model"""
    __tablename__ = "task"
    __table_args__ = (sqla.Index("ix_proc_stats", "ingest_id", "status"),)
    created = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow)
    modified = sqla.Column(sqla.DateTime, onupdate=datetime.datetime.utcnow)
    item_id = sqla.Column(UUIDType, sqla.ForeignKey("item.id"))
    item = sqla.orm.relationship("Item", backref=sqla.orm.backref("task", uselist=False))
    type = sqla.Column(sqla.String)
    context = sqla.Column(sqla.JSON)
    worker = sqla.Column(sqla.String)
    error = sqla.Column(sqla.String)
    retries = sqla.Column(sqla.Integer, default=0)
    status = sqla.Column(sqla.String, default=schemas.TaskStatus.pending)
    history = sqla.Column(sqla.JSON, default=lambda: [])

    # pylint: disable=C0326
    status_enum = schemas.TaskStatus
    status_transitions = {
        None:         {"pending"},
        "pending":    {"running", "canceled"},  # cancel via ingest fail/abort
        "running":    {"completed", "pending", "failed"},  # retry to pending
        "completed":  set(),
        "failed":     set(),  # NOTE this will get trickier with user retries
        "canceled":   set(),  # NOTE ^ same as above
    }

    @sqla.orm.validates("type")
    def validate_type(self, key, value):
        """Validate task type"""
        return schemas.TaskType.get_item(value)


class Container(IDMixin, IngestRefMixin, Base):
    """Container model which represents nodes in the destination hierarchy"""
    __tablename__ = "container"
    __table_args__ = (sqla.Index("ix_scan_stats", "ingest_id", "level"),)
    parent_id = sqla.Column(UUIDType, sqla.ForeignKey("container.id"))
    parent = sqla.orm.relationship("Container", remote_side="Container.id", backref="children")
    level = sqla.Column(sqla.Integer)
    path = sqla.Column(sqla.String)
    src_context = sqla.Column(sqla.JSON)
    dst_context = sqla.Column(sqla.JSON)
    dst_path = sqla.Column(sqla.String)

    @sqla.orm.validates("level")
    def validate_level(self, key, value):
        """Validate container level"""
        return schemas.ContainerLevel.get_item(value)


class Item(IDMixin, IngestRefMixin, Base):
    """Ingest item model"""
    __tablename__ = "item"
    container_id = sqla.Column(UUIDType, sqla.ForeignKey("container.id"))
    container = sqla.orm.relationship("Container", backref="items")
    dir = sqla.Column(sqla.String)
    type = sqla.Column(sqla.String)
    files = sqla.Column(sqla.JSON)
    filename = sqla.Column(sqla.String)
    files_cnt = sqla.Column(sqla.Integer)
    bytes_sum = sqla.Column(sqla.Integer)
    context = sqla.Column(sqla.JSON)
    existing = sqla.Column(sqla.Boolean)
    skipped = sqla.Column(sqla.Boolean)

    @sqla.orm.validates("type")
    def validate_type(self, key, value):
        """Validate item type"""
        return schemas.ItemType.get_item(value)


class Review(IDMixin, IngestRefMixin, Base):
    """Review model"""
    __tablename__ = "review"
    path = sqla.Column(sqla.String)
    skip = sqla.Column(sqla.Boolean)
    context = sqla.Column(sqla.JSON)


class Subject(IDMixin, IngestRefMixin, Base):
    """Subject model"""
    __tablename__ = "subject"
    code = sqla.Column(sqla.String)
    map_values = sqla.Column(sqla.JSON)


class DeidLog(IDMixin, IngestRefMixin, Base):
    """Deid log model"""
    __tablename__ = "deid_log"
    created = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow)
    src_path = sqla.Column(sqla.String)
    tags_before = sqla.Column(sqla.JSON)
    tags_after = sqla.Column(sqla.JSON)


sqla.orm.configure_mappers()  # NOTE create backrefs

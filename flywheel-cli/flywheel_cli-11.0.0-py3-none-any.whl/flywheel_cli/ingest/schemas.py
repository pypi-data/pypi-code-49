# pylint: disable=too-few-public-methods
"""Pydantic ingest input and output schemas"""
import datetime
from enum import Enum
from typing import Dict, List, Tuple, Optional
from uuid import UUID

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Schema(BaseModel):
    """Common base configured to play nice with sqlalchemy"""
    class Config:
        """Enable .from_orm() to load fields from attrs"""
        orm_mode = True


class IngestEnum(Enum):
    """Extended Enum with easy item lookup allowing name and value"""
    @classmethod
    def get_item(cls, info):
        """Return enum item for given item, name or value"""
        for item in cls:
            if info in (item, item.name, item.value):
                return item
        raise ValueError(f"Invalid {cls.__name__} {info}")

    @classmethod
    def has_item(cls, info):
        """Return True if info is a valid enum item, name or value"""
        try:
            cls.get_item(info)
        except ValueError:
            return False
        return True


# Ingests

class IngestStatus(str, IngestEnum):
    """Ingest status"""
    created = "created"
    scanning = "scanning"
    resolving = "resolving"
    in_review = "in_review"
    preparing = "preparing"
    uploading = "uploading"
    finalizing = "finalizing"
    finished = "finished"
    failed = "failed"
    aborted = "aborted"


class IngestInAPI(Schema):
    """Ingest input schema"""
    src_fs: str
    config: dict
    label: Optional[str]


class IngestIn(IngestInAPI):
    """Ingest input schema w/ api-key"""
    api_key: str
    fw_host: str
    fw_user: str


class IngestOutAPI(Schema):
    """Ingest output schema"""
    id: UUID
    label: str
    src_fs: str
    fw_host: str
    fw_user: str
    config: dict
    status: IngestStatus
    history: List[Tuple[IngestStatus, int]]
    created: datetime.datetime
    started: Optional[datetime.datetime]
    finished: Optional[datetime.datetime]


class IngestOut(IngestOutAPI):
    """Ingest output schema w/ api-key"""
    api_key: str


# Tasks

class TaskType(str, IngestEnum):
    """Task type enum"""
    scan = "scan"
    resolve = "resolve"
    prepare = "prepare"
    upload = "upload"
    finalize = "finalize"


class TaskStatus(str, IngestEnum):
    """Task status enum"""
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"
    canceled = "canceled"


class TaskIn(Schema):
    """Task input schema"""
    type: TaskType
    item_id: Optional[UUID]
    context: Optional[dict]


class TaskOut(TaskIn):
    """Task output schema"""
    id: UUID
    ingest_id: UUID
    status: TaskStatus
    history: List[Tuple[TaskStatus, int]]
    worker: Optional[str]
    error: Optional[str]
    created: datetime.datetime
    started: Optional[datetime.datetime]
    finished: Optional[datetime.datetime]
    retries: int


# Containers

class ContainerLevel(int, IngestEnum):
    """Container level enum (int for simple ordering)"""
    group = 0
    project = 1
    subject = 2
    session = 3
    acquisition = 4


class ContainerIn(Schema):
    """Container input schema"""
    parent_id: Optional[UUID]
    path: Optional[str]
    level: ContainerLevel
    src_context: dict
    dst_context: Optional[dict]
    dst_path: Optional[str]


class ContainerOut(ContainerIn):
    """Container output schema"""
    id: UUID
    ingest_id: UUID
    files_cnt: Optional[int]
    bytes_sum: Optional[int]


# Items

class ItemType(str, IngestEnum):
    """Ingest item type enum"""
    file = "file"
    packfile = "packfile"


class ItemIn(Schema):
    """Ingest item input schema"""
    container_id: Optional[UUID]
    dir: str
    type: ItemType
    files: List[str]
    filename: Optional[str]
    files_cnt: int
    bytes_sum: int
    context: Optional[dict]


class ItemOut(ItemIn):
    """Ingest item output schema"""
    id: UUID
    ingest_id: UUID
    container_id: Optional[UUID]
    existing: Optional[bool]
    skipped: Optional[bool]


# Ingest stats

class StatusCount(Schema):
    """Counts by status"""
    scanned: int = 0
    pending: int = 0
    running: int = 0
    failed: int = 0
    canceled: int = 0
    completed: int = 0
    skipped: int = 0
    finished: int = 0
    total: int = 0


class Progress(Schema):
    """Ingest progress with scan task and import- item/file/byte counts by status"""
    scans: StatusCount = StatusCount()
    items: StatusCount = StatusCount()
    files: StatusCount = StatusCount()
    bytes: StatusCount = StatusCount()


class Summary(Schema):
    """Ingest scan summary with hierarchy node and file counts"""
    groups: int = 0
    projects: int = 0
    subjects: int = 0
    sessions: int = 0
    acquisitions: int = 0
    files: int = 0
    packfiles: int = 0


class Error(Schema):
    """Ingest task error"""
    task: UUID
    type: TaskType
    message: str


class Report(Schema):
    """Final ingest report with status, elapsed times and list of errors"""
    status: IngestStatus
    elapsed: Dict[IngestStatus, int]
    errors: List[Error]


# Review

class ReviewChange(Schema):
    """Review change"""
    path: str
    skip: Optional[bool]
    context: Optional[dict]


ReviewIn = List[ReviewChange]


# Logs

class AuditLogOut(Schema):
    """Audit log output schema"""
    src_path: str
    dst_path: str
    failed: bool
    message: str


class DeidLogIn(Schema):
    """Deid log input schema"""
    src_path: str
    tags_before: dict
    tags_after: dict


class DeidLogOut(DeidLogIn):
    """De-id log output schema"""
    id: UUID
    created: datetime.datetime

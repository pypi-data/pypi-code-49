"""Ingest CRUD methods"""
import datetime
import re
from typing import Iterable, List, Optional, BinaryIO
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.sql import func

from . import deid, models, schemas


# Ingests

def create_ingest(db: Session, ingest: schemas.IngestIn) -> schemas.IngestOut:
    """Create a new ingest operation"""
    ingest = models.Ingest(**ingest.dict())
    db.add(ingest)
    db.commit()
    return ingest.schema()


def get_ingests(db: Session) -> List[schemas.IngestOut]:
    """Get all ingest operations"""
    ingests = (
        db.query(models.Ingest)
        .order_by(models.Ingest.created, models.Ingest.id)
        .all()
    )
    return [ingest.schema() for ingest in ingests]


def get_ingest(db: Session, ingest_id: UUID) -> schemas.IngestOut:
    """Get an ingest operation by id"""
    ingest = _get_ingest(db, ingest_id)
    return ingest.schema()


def set_ingest_status(db: Session, ingest_id: UUID, status: schemas.IngestStatus) -> schemas.IngestOut:
    """Set ingest status"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    if not models.Ingest.is_terminal(ingest.status):
        ingest.status = status
        db.commit()
    return ingest.schema()


def start_ingest(db: Session, ingest_id: UUID) -> schemas.IngestOut:
    """Start the ingest and create an initial scan task"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    ingest.status = schemas.IngestStatus.scanning
    db.add(models.Task(
        ingest_id=ingest_id,
        type=schemas.TaskType.scan,
        context={"scanner": {
            "type": "template",
            "dir": "/",
        }}
    ))
    db.commit()
    return ingest.schema()


def resolve_ingest_after_scan(db: Session, ingest_id: UUID) -> schemas.IngestOut:
    """Set ingest status to resolving and add resolve task if all scans finished"""
    # get the ingest w/o locking first
    ingest = _get_ingest(db, ingest_id)
    if models.Ingest.is_terminal(ingest.status):
        # ingest aborted or failed
        return ingest.schema()
    if has_unfinished_tasks(db, ingest_id):
        # still processing scan tasks - noop
        return ingest.schema()
    # all scan tasks finished - lock the ingest
    ingest = _get_ingest(db, ingest_id, for_update=True)
    # set status and add scan task (once - noop for 2nd worker)
    if ingest.status != schemas.IngestStatus.resolving:
        ingest.status = schemas.IngestStatus.resolving
        db.add(models.Task(
            ingest_id=ingest_id,
            type=schemas.TaskType.resolve,
        ))
        db.commit()
    return ingest.schema()


def review_ingest(
        db: Session,
        ingest_id: UUID,
        changes: Optional[schemas.ReviewIn] = None,
    ) -> schemas.IngestOut:
    """Add review changes, set status to preparing and add prepare task"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    ingest.status = schemas.IngestStatus.preparing
    if changes is not None:
        for change in changes:
            db.add(models.Review(ingest_id=ingest_id, **change))
    db.add(models.Task(
        ingest_id=ingest_id,
        type=schemas.TaskType.prepare,
    ))
    db.commit()
    return ingest.schema()


def finalize_ingest_after_upload(db: Session, ingest_id: UUID) -> schemas.IngestOut:
    """Set ingest status to finalizing and add finalize task if all uploads finished"""
    # get the ingest w/o locking first
    ingest = _get_ingest(db, ingest_id)
    if models.Ingest.is_terminal(ingest.status):
        # TODO finalize (save audit logs) if aborted or failed separately
        return ingest.schema()
    if has_unfinished_tasks(db, ingest_id):
        # still processing upload tasks - noop
        return get_ingest(db, ingest_id)
    # all upload tasks finished - lock the ingest
    ingest = _get_ingest(db, ingest_id, for_update=True)
    # set status and add finalize task (once - noop for 2nd worker)
    if ingest.status != schemas.IngestStatus.finalizing:
        ingest.status = schemas.IngestStatus.finalizing
        db.add(models.Task(
            ingest_id=ingest_id,
            type=schemas.TaskType.finalize,
        ))
        db.commit()
    return ingest.schema()


def finish_ingest(db: Session, ingest_id: UUID) -> schemas.IngestOut:
    """Finish ingest"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    ingest.status = schemas.IngestStatus.finished
    db.commit()
    return ingest.schema()


def fail_ingest(db: Session, ingest_id: UUID) -> schemas.IngestOut:
    """Set ingest status to failed and cancel pending tasks"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    ingest.status = schemas.IngestStatus.failed
    cancel_pending_tasks(db, ingest_id)
    db.commit()
    return ingest.schema()


def abort_ingest(db: Session, ingest_id: UUID) -> schemas.IngestOut:
    """Set ingest status to aborted and cancel pending tasks"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    # TODO: raise if ingest status is terminal but not aborted
    if not models.Ingest.is_terminal(ingest.status):
        ingest.status = schemas.IngestStatus.aborted
        cancel_pending_tasks(db, ingest_id)
        db.commit()
    return ingest.schema()


def has_unfinished_tasks(db: Session, ingest_id: UUID) -> bool:
    """Return True if there are pending or running tasks in the ingest"""
    pending_or_running = (
        db.query(models.Task.id)
        .filter(
            models.Task.ingest_id == ingest_id,
            models.Task.status.in_([
                schemas.TaskStatus.pending,
                schemas.TaskStatus.running,
            ])
        )
    )
    return bool(pending_or_running.count())


# Tasks

def create_task(db: Session, ingest_id: UUID, task: schemas.TaskIn) -> schemas.TaskOut:
    """Create task"""
    task = models.Task(ingest_id=ingest_id, **task.dict())
    db.add(task)
    db.commit()
    return task.schema()


def next_task(db: Session, worker: str) -> Optional[schemas.TaskOut]:
    """Get a task with pending status, also put it into running status"""
    query = _for_update(
        db.query(models.Task)
        .filter(models.Task.status == schemas.TaskStatus.pending),
        skip_locked=True
    )
    task = query.first()
    if task:
        task.worker = worker
        task.status = schemas.TaskStatus.running
        task.started = datetime.datetime.utcnow()
        db.commit()
        return task.schema()
    return None


def finish_task(db: Session, task_id: UUID) -> schemas.TaskOut:
    """Sets task status to complete and update finished field"""
    task = db.query(models.Task).filter(models.Task.id == task_id).one()
    task.status = schemas.TaskStatus.completed
    task.finished = datetime.datetime.utcnow()
    db.commit()
    return task.schema()


def fail_task(db: Session, task_id: UUID, error: str) -> schemas.TaskOut:
    """Fail task"""
    task = db.query(models.Task).filter(models.Task.id == task_id).one()
    task.status = schemas.TaskStatus.failed
    task.error = error
    db.commit()
    return task.schema()


def cancel_task(db: Session, task_id: UUID) -> schemas.TaskOut:
    """Cancel task"""
    task = db.query(models.Task).filter(models.Task.id == task_id).one()
    task.status = schemas.TaskStatus.canceled
    db.commit()
    return task.schema()


def retry_task(db: Session, task_id: UUID) ->  schemas.TaskOut:
    """Retry task"""
    task = db.query(models.Task).filter(models.Task.id == task_id).one()
    task.status = schemas.TaskStatus.pending
    task.retries = (task.retries or 0) + 1
    db.commit()
    return task.schema()


def cancel_pending_tasks(db: Session, ingest_id: UUID) -> None:
    """Cancel all pending tasks of an ingest"""
    pending_tasks = db.query(models.Task).filter(
        models.Task.ingest_id == ingest_id,
        models.Task.status == schemas.TaskStatus.pending,
    )
    pending_tasks.update({models.Task.status: schemas.TaskStatus.canceled})


# Containers

def create_container(db: Session, ingest_id: UUID, container_in: schemas.ContainerIn) -> schemas.ContainerOut:
    """Create container"""
    container = models.Container(**container_in.dict())
    container.ingest_id = ingest_id
    db.add(container)
    db.commit()
    return container.schema()


def get_containers(db: Session, ingest_id: UUID, level: Optional[schemas.ContainerLevel] = None) -> Iterable[schemas.ContainerOut]:
    """Get all containers for an ingest"""
    query = db.query(models.Container).filter(models.Container.ingest_id == ingest_id)
    if level:
        query = query.filter(models.Container.level == level)
    query = query.order_by(models.Container.level, models.Container.id)
    for container in _iter_query(query):
        yield container.schema()


def get_container(db: Session, container_id: UUID) -> schemas.ContainerOut:
    """Get container"""
    container = db.query(models.Container).filter(models.Container.id == container_id).one()
    return container.schema()


def get_container_by_path(db: Session, ingest_id: UUID, path: str) -> schemas.ContainerOut:
    """Get container by path"""
    container = (
        db.query(models.Container)
        .filter(
            models.Container.ingest_id == ingest_id,
            models.Container.path == path,
        )
        .scalar()
    )
    if container:
        return container.schema()
    return None


def update_container(db: Session, container_id: UUID, **kwargs):
    """Update container"""
    db.query(models.Container).filter(models.Container.id == container_id).update(kwargs)
    db.commit()


# Items

def create_item(db: Session, ingest_id: UUID, item_in: schemas.ItemIn) -> schemas.ItemOut:
    """Create an ingest item"""
    item = models.Item(ingest_id=ingest_id, **item_in.dict())
    db.add(item)
    db.commit()
    return item.schema()


def get_items(db: Session, ingest_id: UUID) -> Iterable[schemas.ItemOut]:
    """Get all items for an ingest operation"""
    query = (
        db.query(models.Item)
        .filter(models.Item.ingest_id == ingest_id)
        .order_by(models.Item.id)
    )
    for item in _iter_query(query):
        yield item.schema()


def get_item(db: Session, item_id: UUID) -> schemas.ItemOut:
    """Get the specified ingest item"""
    item = db.query(models.Item).filter(models.Item.id == item_id).one()
    return item.schema()


def update_item(db: Session, item_id: UUID, **kwargs):
    """Update item"""
    db.query(models.Item).filter(models.Item.id == item_id).update(kwargs)
    db.commit()


# Ingest stats

def get_ingest_progress(db: Session, ingest_id: UUID) -> schemas.Progress:
    """Get ingest scan task and item/file/byte counts by status"""
    _get_ingest(db, ingest_id)
    progress = schemas.Progress().dict()
    scan_tasks_by_status = (
        db.query(
            models.Task.status,
            func.count(models.Task.id).label("count"),
        )
        .filter(
            models.Task.ingest_id == ingest_id,
            models.Task.type == schemas.TaskType.scan,
        )
        .group_by(models.Task.status)
    )
    for row in scan_tasks_by_status:
        progress["scans"][row.status] = row.count
        progress["scans"]["total"] += row.count
        if models.Task.is_terminal(row.status):
            progress["scans"]["finished"] += row.count

    items_by_status = (
        db.query(
            models.Task.status,
            models.Item.skipped,
            func.count(models.Item.id).label("items"),
            func.sum(models.Item.files_cnt).label("files"),
            func.sum(models.Item.bytes_sum).label("bytes"),
        )
        .outerjoin(models.Item.task)
        .filter(models.Item.ingest_id == ingest_id)
        .group_by(models.Task.status, models.Item.skipped)
    )
    for row in items_by_status.all():
        if row.skipped:
            # items skipped via review tracked separately
            status = "skipped"
        elif row.status is None:
            # items that don't have any (upload task) status yet
            status = "scanned"
        else:
            # items with an upload task tracked as the task status
            status = row.status

        for attr in ("items", "files", "bytes"):
            progress[attr][status] = getattr(row, attr)
            progress[attr]["total"] += getattr(row, attr)
            if schemas.TaskStatus.has_item(status) and models.Task.is_terminal(status):
                progress[attr]["finished"] += getattr(row, attr)
    return schemas.Progress(**progress)


def get_ingest_summary(db: Session, ingest_id: UUID) -> schemas.Progress:
    """Get ingest hierarchy node and file count by level and type"""
    _get_ingest(db, ingest_id)
    summary = {}
    containers_by_level = (
        db.query(
            models.Container.level,
            func.count(models.Container.id).label("count"))
        .filter(models.Container.ingest_id == ingest_id)
        .group_by(models.Container.level)
    )
    for row in containers_by_level.all():
        level_name = schemas.ContainerLevel.get_item(row.level).name
        summary[f"{level_name}s"] = row.count
    items_by_type = (
        db.query(
            models.Item.type,
            func.count(models.Item.id).label("count"))
        .filter(models.Item.ingest_id == ingest_id)
        .group_by(models.Item.type)
    )
    for row in items_by_type.all():
        summary[f"{row.type}s"] = row.count
    return schemas.Summary(**summary)


def get_ingest_report(db: Session, ingest_id: UUID) -> schemas.Progress:
    """Get ingest status, elapsed time per status and list of failed tasks"""
    ingest = _get_ingest(db, ingest_id)
    elapsed = {}
    for old, new in zip(ingest.history, ingest.history[1:]):
        old_status, old_timestamp = old
        new_status, new_timestamp = new  # pylint: disable=W0612
        elapsed[old_status] = new_timestamp - old_timestamp
    failed_tasks = (
        db.query(
            models.Task.id.label("task"),  # pylint: disable=E1101
            models.Task.type,
            models.Task.error.label("message"),
        )
        .filter(
            models.Task.ingest_id == ingest_id,
            models.Task.status == schemas.TaskStatus.failed,
        )
        .order_by(models.Task.created, models.Task.id)
    )
    return schemas.Report(
        status=ingest.status,
        elapsed=elapsed,
        errors=failed_tasks.all(),
    )


def get_ingest_tree(db: Session, ingest_id: UUID) -> Iterable[schemas.ContainerOut]:
    """Get tree"""
    # TODO docs and individual items
    start_level = (
        db.query(func.max(models.Container.level))
        .join(models.Container.items)
        .filter(models.Container.ingest_id == ingest_id)
        .scalar()
    )
    query = (
        db.query(
            models.Container.id,
            models.Container.level,
            models.Container.parent_id,
            models.Container.src_context,
            models.Container.dst_context,
            models.Container.ingest_id,
            func.count(models.Item.id).label("files_cnt"),
            func.sum(models.Item.bytes_sum).label("bytes_sum"),
        )
        .outerjoin(models.Container.items)
        .filter(models.Container.ingest_id == ingest_id)
        .group_by(models.Container.id)
        .order_by(models.Container.id)
    )
    results = query.filter(models.Container.level == start_level).limit(20).all()
    level = start_level - 1
    parents = list(map(lambda c: c.parent_id, results))
    while level > -1:
        containers = (
            query
            .filter(
                models.Container.id.in_(parents),  # pylint: disable=no-member
                models.Container.level == level,
            )
            .all()
        )
        results.extend(containers)
        parents = list(map(lambda c: c.parent_id, containers))
        level -= 1
    for container in reversed(results):
        yield schemas.ContainerOut.from_orm(container)


# Subjects

def load_subject_csv(db: Session, ingest_id: UUID, subject_csv: BinaryIO) -> None:
    """Load subjects from an open CSV file"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    subject_config = ingest.config.setdefault("subject_config", {})
    subject_config.setdefault("code_serial", 0)
    header = subject_csv.readline().decode("utf8").strip()
    code_format, *map_keys = header.split(",")
    if subject_config:
        assert map_keys == subject_config["map_keys"]
    else:
        subject_config["code_format"] = code_format
        subject_config["map_keys"] = map_keys

    code_re = re.compile(r"^[^\d]*(\d+)[^\d]*$")
    for line in subject_csv:
        subject = line.decode("utf8").strip()
        code, *map_values = subject.split(",")
        code_int = int(code_re.match(code).group(1))
        if code_int > subject_config["code_serial"]:
            subject_config["code_serial"] = code_int
        # NOTE all subjects in memory
        db.add(models.Subject(
            ingest_id=ingest_id,
            code=code,
            map_values=map_values,
        ))
    flag_modified(ingest, "config")
    db.commit()


def resolve_subject(db: Session, ingest_id: UUID, map_values: List[str]) -> str:
    """Get existing or create new subject code based on the map values"""
    ingest = _get_ingest(db, ingest_id, for_update=True)
    subject = (
        db.query(models.Subject)
        .filter(
            models.Subject.ingest_id == ingest_id,
            models.Subject.map_values == map_values,
        )
        .first()
    )
    if subject is None:
        subject_config = ingest.config["subject_config"]
        subject_config["code_serial"] += 1
        flag_modified(ingest, "config")
        subject = models.Subject(
            ingest_id=ingest_id,
            code=subject_config["code_format"].format(
                SubjectCode=subject_config["code_serial"]
            ),
            map_values=map_values,
        )
        ingest.update_config()
        db.add(subject)
        db.commit()
    return subject.code


def get_subject_csv(db: Session, ingest_id: UUID) -> Iterable[str]:
    """Yield subject CSV lines for an ingest"""
    ingest = _get_ingest(db, ingest_id)
    query = (
        db.query(models.Subject)
        .filter(models.Subject.ingest_id == ingest_id)
        .order_by(models.Subject.code)
    )
    first = True
    for subject in _iter_query(query):
        if first:
            first = False
            config = ingest.config["subject_config"]
            fields = [config["code_format"]] + config["map_keys"]
            header = ",".join(fields)
            yield f"{header}\n"
        values = [subject.code] + subject.map_values
        row = ",".join(_csv_field_str(value) for value in values)
        yield f"{row}\n"


# Logs

def get_audit_logs(db: Session, ingest_id: UUID) -> Iterable[str]:
    """Yield audit log CSV lines for an ingest"""
    ingest = _get_ingest(db, ingest_id)
    # TODO assert status
    query = (
        db.query(
            models.Item.dir,
            models.Item.files,
            models.Item.filename,
            models.Item.context,
            models.Item.type,
            models.Item.existing,
            models.Item.skipped,
            models.Container.dst_path,
            models.Container.level,
            models.Task.status,
            models.Task.error,
        )
        .outerjoin(models.Item.container, models.Item.task)
        .filter(models.Item.ingest_id == ingest_id)
        .order_by(models.Item.dir, models.Item.id)
    )

    fields = ["src_path", "dst_path", "status", "existing", "error"]
    first = True
    for item in _iter_query(query):
        if first:
            first = False
            header = ",".join(fields)
            yield f"{header}\n"

        # TODO normalize src path, make sure win32/local works
        values = dict(
            src_path=f"{ingest.src_fs}{item.dir}/{item.filename}",
            dst_path=f"{item.dst_path}/{item.filename}",
            status="skipped" if item.skipped else item.status,
            existing=item.existing,
            error=item.error,
        )
        row = ",".join(_csv_field_str(values[field]) for field in fields)
        yield f"{row}\n"


def create_deid_log_entry(db: Session, ingest_id: UUID, deid_log: schemas.DeidLogIn) -> schemas.DeidLogOut:
    """Create deid log entry"""
    deid_log = models.DeidLog(ingest_id=ingest_id, **deid_log.dict())
    db.add(deid_log)
    db.commit()
    return deid_log.schema()


def get_deid_logs(db: Session, ingest_id: UUID) -> Iterable[str]:
    """Yield de-id log CSV lines for an ingest"""
    ingest = _get_ingest(db, ingest_id)
    assert ingest.config.get("de_identify")

    # add fields from all deid file profiles
    fields = ["src_path", "type"]
    profile_name = ingest.config.get("deid_profile")
    profiles = ingest.config.get("deid_profiles")
    deid_profile = deid.load_deid_profile(profile_name, profiles)
    for file_profile in deid_profile.file_profiles:
        fields.extend(file_profile.get_log_fields())

    query = (
        db.query(models.DeidLog)
        .filter(models.DeidLog.ingest_id == ingest_id)
        .order_by(models.DeidLog.created, models.DeidLog.id)
    )
    first = True
    for deid_log in _iter_query(query):
        if first:
            first = False
            header = ",".join(fields)
            yield f"{header}\n"

        before = {"src_path": deid_log.src_path, "type": "before", **deid_log.tags_before}
        before_row = ",".join(_csv_field_str(before.get(field)) for field in fields)
        yield f"{before_row}\n"

        after = {"src_path": deid_log.src_path, "type": "after", **deid_log.tags_after}
        after_row = ",".join(_csv_field_str(after.get(field)) for field in fields)
        yield f"{after_row}\n"


# Utils

def _get_ingest(db: Session, ingest_id: UUID, for_update=False) -> models.Ingest:
    """Return an ingest model by ID from the DB"""
    query = db.query(models.Ingest).filter(models.Ingest.id == ingest_id)
    if for_update:
        query = _for_update(query)
    return query.one()


def _for_update(query, skip_locked=False):
    """Lock as granularly as possible for given query and backend"""
    if query.session.bind.name == "sqlite":
        # lock the whole DB when using sqlite (in lack of anything better)
        query.session.execute("BEGIN IMMEDIATE")
    # with_for_update() locks selected rows in postgres (ignored w/ sqlite)
    # skip_locked silently skips over records that are currently locked
    # populate_existing to get objects with the latest modifications
    # see: https://github.com/sqlalchemy/sqlalchemy/issues/4774
    return query.with_for_update(skip_locked=skip_locked).populate_existing()


def _iter_query(query, size=1000):
    """Yield query results from results retrieved in batches"""
    # NOTE query must be ordered as retrieval order is indeterministic in postgres
    # TODO use the faster seek method instead
    # https://www.eversql.com/faster-pagination-in-mysql-why-order-by-with-limit-and-offset-is-slow/
    offset = 0
    while True:
        count = 0
        for result in query.limit(size).offset(offset):
            count += 1
            yield result
        if count < size:
            break
        offset += size


def _csv_field_str(field):
    """Stringify csv fields"""
    return "" if field is None else str(field)

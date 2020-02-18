"""Provides IngestDB class"""

import datetime
import inspect
import json
import logging
import threading
from contextlib import contextmanager

from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import sessionmaker

from ..sdk_impl import create_flywheel_client
from .. import util
from . import crud, models, schemas

log = logging.getLogger(__name__)

THREAD_LOCAL = threading.local()


class IngestDB:
    """Ingest with direct db access"""

    def __init__(self, ingest_id, config):
        self.ingest_id = ingest_id
        self.config = config
        self.engine = self.create_engine(config.db_url)
        self.create_session = self.get_sessionmaker(self.engine)

    def __getattr__(self, name):
        if hasattr(crud, name):
            def method(*args, **kwargs):
                _method = getattr(crud, name)
                # always append session as first arg
                with session_scope(self.create_session) as session:
                    _args = [session]
                    if "ingest_id" in inspect.signature(_method).parameters:
                        # suppose that if there is ingest_id, then it is the second arg
                        _args.append(self.ingest_id)
                    return _method(*_args, *args, **kwargs)
            return method
        raise AttributeError(f"Unknown attribute: {name}")

    @classmethod
    def create(cls, config):
        """Creates ingest operation"""
        ingest_name = "Ingest_" + str(datetime.datetime.now()).replace(" ", "_")
        fw = create_flywheel_client()
        auth_status = fw.get_auth_status()
        if not auth_status.user_is_admin:
            raise Exception("Only admin users can use this command")
        api_key = config.get_api_key()
        fw_host = api_key.split(":")[0]
        ingest = schemas.IngestIn(
            label=ingest_name,
            src_fs=config.src_fs_url,
            api_key=api_key,
            fw_user=auth_status.origin.id,
            fw_host=fw_host,
            config=config.dict(exclude_none=True),
        )
        engine = cls.create_engine(config.db_url)
        with session_scope(cls.get_sessionmaker(engine)) as db:
            ingest = crud.create_ingest(db, ingest)
        return cls(ingest.id, config)

    @classmethod
    def get_task(cls, config, worker=None):
        """Get task"""
        engine = cls.create_engine(config.db_url)
        with session_scope(cls.get_sessionmaker(engine)) as db:
            return crud.next_task(db, worker)

    @classmethod
    def create_tables(cls, db_url):
        """Create tables"""
        engine = cls.create_engine(db_url)
        with engine.connect() as conn:
            # solves the locking issue on OSX
            # where unlock notify is not available
            # so two BEGIN IMMEDIATE transaction waits for each other
            # one try to commit, but the other other holds a SHARED
            # lock on the sqlite_master table. So the last one will fail
            # after reach the timeout since couldn't get RESERVED lock,
            # first one will complete the commit.
            # WAL mode solves the issue since the readers don't block writers.
            # other solution would be using BEGIN EXCLUSIVE but it has
            # negative affect on concurrency
            # https://www.sqlite.org/wal.html
            conn.execute("PRAGMA journal_mode=WAL")
        models.create_tables(cls.create_engine(db_url))

    @classmethod
    def get_sessionmaker(cls, engine):
        """Get session maker"""
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine,
        )

    @staticmethod
    def create_engine(db_url):
        """Create sqlalchemy db engine"""
        if not hasattr(THREAD_LOCAL, "engine"):
            if db_url.startswith("sqlite"):
                engine = create_engine(
                    db_url,
                    json_serializer=_json_serializer,
                    # https://beets.io/blog/sqlite-nightmare.html
                    connect_args={"check_same_thread": False, "timeout": 60}
                )

                @event.listens_for(engine, "connect")
                def _do_connect(dbapi_connection, _):
                    # disable pysqlite's emitting of the BEGIN statement entirely.
                    # also stops it from emitting COMMIT before any DDL.
                    dbapi_connection.isolation_level = None
            else:
                engine = create_engine(db_url, json_serializer=_json_serializer)
            THREAD_LOCAL.engine = engine
        return THREAD_LOCAL.engine

    @staticmethod
    def check_connection(db_url):
        """Check whether or not the connection works"""
        engine = IngestDB.create_engine(db_url)
        try:
            # Test query
            engine.execute(text('SELECT 1'))
            return True
        except Exception:  # pylint: disable=broad-except
            return False

@contextmanager
def session_scope(create_session):
    """Close session automatically"""
    session = create_session()
    try:
        yield session
    finally:
        session.close()


def _json_serializer(*args, **kwargs):
    kwargs["default"] = util.custom_json_serializer
    return json.dumps(*args, **kwargs)

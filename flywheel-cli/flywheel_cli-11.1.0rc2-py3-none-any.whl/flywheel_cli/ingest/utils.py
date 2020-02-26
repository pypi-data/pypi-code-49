"""Ingest utility module"""
import datetime
import functools
import json
import logging
import os
from typing import Any, Tuple

import flywheel
import fs.filesize
import pytz
import sqlalchemy as sqla

from . import models
from ..util import get_cli_version

log = logging.getLogger(__name__)


def encode_json(obj: Any) -> Any:
    """JSON encode additional data types"""
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    if isinstance(obj, datetime.datetime):
        return pytz.timezone("UTC").localize(obj).isoformat()
    # default serialization/raising otherwise
    raise TypeError(repr(obj) + " is not JSON serializable")


# pylint: disable=C0103
json_serializer = functools.partial(
    json.dumps,
    default=encode_json,
    separators=(",", ":"),
)


def get_path_el(c_type, context, reverse=False):
    """Get the path element for container"""
    if c_type == "group":
        return context.get("_id")
    priority_order = ["_id", "label"]
    if reverse:
        # prefer label
        priority_order = reversed(priority_order)
    for field in priority_order:
        value = context.get(field)
        if not value:
            continue
        if field == "_id":
            return f"<id:{value}>"
        if field == "label":
            return f"{value}"
    log.error(f"Could not determine {c_type}")
    raise Exception("Not enough information to determine container")


def init_sqla(
        db_url: str = "sqlite:///:memory:"
    ) -> Tuple[sqla.engine.Engine, sqla.orm.sessionmaker]:
    """Return configured sqla engine and session factory for DB url"""
    if db_url.startswith("sqlite://"):
        engine = sqla.create_engine(
            db_url,
            json_serializer=json_serializer,
            connect_args={"check_same_thread": False},
            poolclass=sqla.pool.StaticPool,
        )

        # pylint: disable=W0612,W0613
        @sqla.event.listens_for(engine, "connect")
        def disable_isolation(dbapi_connection, connection_record):
            """
            Disable pysqlite BEGIN statement upon session creation
            to enable locking via explicit BEGIN IMMEDIATE later on.
            """
            dbapi_connection.isolation_level = None

        # autocreate all database tables on sqlite
        models.create_tables(engine)

    else:
        engine = sqla.create_engine(
            db_url,
            json_serializer=json_serializer,
            pool_pre_ping=True,
            connect_args={'connect_timeout': 10},
        )

    sessionmaker = sqla.orm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    return engine, sessionmaker


@functools.lru_cache(maxsize=16)
def get_sdk_client(api_key: str) -> flywheel.Flywheel:
    """Cache and return SDK client for given API key"""
    log.debug(f"Creating SDK client for {api_key}")
    return SDKClient(api_key)


class SDKClient:
    """SDK client w/o version check and w/ request timeouts and signed url support"""
    CONNECT_TIMEOUT = 5
    REQUEST_TIMEOUT = 60
    MAX_IN_MEMORY_XFER = 32 * (2 ** 20)  # files under 32MB sent in one chunk

    def __init__(self, api_key: str):
        fw = flywheel.Flywheel(api_key, minimum_supported_major_version=11)
        fw.api_client.user_agent = f'Flywheel CLI/{get_cli_version()} ' + fw.api_client.user_agent

        # disable version check
        fw.api_client.set_version_check_fn(None)

        # set request timeouts
        request = fw.api_client.rest_client.session.request
        timeout = self.CONNECT_TIMEOUT, self.REQUEST_TIMEOUT
        request_with_timeout = functools.partial(request, timeout=timeout)
        fw.api_client.rest_client.session.request = request_with_timeout

        # check signed url support
        config = fw.get_config()
        features = config.get("features")

        self.fw = fw
        self.session = fw.api_client.rest_client.session
        self.signed_url = features.get("signed_url") or config.get("signed_url")

    def __getattr__(self, name):
        """Pass-through attribute access to the original client"""
        return getattr(self.fw, name)

    def upload(self, cont_name, cont_id, filename, fileobj, metadata=None):
        """Upload file to container"""
        sdk_upload = getattr(self.fw, f"upload_file_to_{cont_name}")
        log.debug(f"Uploading {filename} to {cont_name}/{cont_id}")
        size = os.fstat(fileobj.fileno()).st_size
        if size < self.MAX_IN_MEMORY_XFER:
            data = fileobj.read()
        else:
            data = fileobj
        if self.signed_url:
            self.signed_url_upload(cont_name, cont_id, filename, data, metadata=metadata)
        else:
            filespec = flywheel.FileSpec(filename, data)
            sdk_upload(cont_id, filespec, metadata=json.dumps(metadata))
        log.debug(f"Uploaded {filename} ({fs.filesize.traditional(size)})")

    def signed_url_upload(self, cont_name, cont_id, filename, fileobj, metadata=None):
        """Upload file to container using signed urls"""
        url = f"/{cont_name}s/{cont_id}/files"
        ticket, signed_url = self.create_upload_ticket(url, filename, metadata=metadata)
        log.debug(f"Using signed url {signed_url}")
        self.session.put(signed_url, data=fileobj)  # use api session
        self.call_api(url, "POST", query_params=[("ticket", ticket)])

    def create_upload_ticket(self, url, filename, metadata=None):
        """Create signed url upload ticket"""
        response = self.call_api(
            url,
            "POST",
            body={"metadata": metadata or {}, "filenames": [filename]},
            query_params=[("ticket", "")],
            response_type=object,
        )
        return response["ticket"], response["urls"][filename]

    def call_api(self, resource_path, method, **kwargs):
        """Call api with defaults set to enable accessing the json response"""
        kwargs.setdefault("auth_settings", ["ApiKey"])
        kwargs.setdefault("_return_http_data_only", True)
        kwargs.setdefault("_preload_content", True)
        return self.fw.api_client.call_api(resource_path, method, **kwargs)

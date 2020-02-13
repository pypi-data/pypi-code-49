import logging
import platform
import re
from contextlib import asynccontextmanager
from pathlib import Path
from typing import List, Any, AsyncGenerator, Union, Optional
from urllib.parse import urlparse, urlunparse

import aiosql
import aiosqlite
import asyncpg
import click
import jinja2
from aiosqlite import Connection as sqliteConnection
from asyncpg import Connection as postgresConnection
from asyncpg.pool import Pool
from click import Context

import aiosqlembic
from aiosqlembic.models.cli import (
    Revision,
    RevisionPath,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

templateLoader = jinja2.FileSystemLoader(
    searchpath=str(Path(__file__).parent / "templates")
)
templateEnv = jinja2.Environment(loader=templateLoader)
aiosqlembic_queries = aiosql.from_path(
    Path(__file__).parent / "sql", "asyncpg", record_classes={"Revision": Revision}
)

REVISION_PATTERN = r"(?P<version_id>\d{14})_(?P<message>.*)\.sql"


def filter_revision(version_id: int, current_vid: int, target_vid: int) -> bool:
    if target_vid > current_vid:
        return version_id > current_vid & version_id <= target_vid
    if target_vid < current_vid:
        return version_id <= current_vid & version_id > target_vid
    else:
        return False


def get_revision_tree(
    base_directory: Path, current_vid: int, target_vid: int
) -> List[RevisionPath]:
    """
    Builds a list of RevisionPath from the revision directory
    """
    revision_files = list(base_directory.glob("*.sql"))
    revision_tree = []
    if revision_files:
        for revision_file in sorted(revision_files):
            m = re.match(REVISION_PATTERN, revision_file.name)
            if m is not None:
                # (?P<version_id>\d{14})_(?P<message>.*)\.sql
                revision = RevisionPath(
                    version_id=int(m.group("version_id")),
                    message=m.group("message"),
                    file=revision_file,
                    next=-1,
                    previous=-1,
                )
                if filter_revision(revision.version_id, current_vid, target_vid):
                    revision_tree.append(revision)
            else:
                raise ValueError("Wrong filename")
    else:
        revision_tree = [
            RevisionPath(version_id=0, message=None, file=None, next=-1, previous=-1)
        ]

    sorted_revisions = sorted(revision_tree, key=lambda x: x.version_id)
    for idx, sorted_revision in enumerate(sorted_revisions):
        logger.debug(idx)
        prev = -1
        if idx > 0:
            prev = sorted_revisions[idx - 1].version_id
            sorted_revisions[idx - 1].next = sorted_revision.version_id
        sorted_revisions[idx].previous = prev

    return sorted_revisions


def print_version(ctx: Context, param: Any, value: str) -> None:
    """
    Prints the aiosqlembic version as well as python version and the plateform used
    """
    if not value or ctx.resilient_parsing:
        return
    click.echo(
        "Running aiosqlembic %s with %s %s on %s"
        % (
            aiosqlembic.__version__,
            platform.python_implementation(),
            platform.python_version(),
            platform.system(),
        )
    )
    ctx.exit()


@asynccontextmanager
async def create_test_database(dsn: str, dbname: str) -> AsyncGenerator[str, None]:
    """Async context manager to create databases

    .. highlight:: python
    .. code-block:: python

        async with create_test_database(TEST_DSN, "d0") as d0, create_test_database(
            TEST_DSN, "d1"
        ) as d1:
            try:
                p0: Pool = await asyncpg.create_pool(dsn=d0)
                p1: Pool = await asyncpg.create_pool(dsn=d1)
                await p0.execute("select 1")
                await p1.execute("select 1")
            finally:
                await p1.close()
                await p0.close()

    """

    logger.debug(f"create_test_database: {dbname}")
    logger.debug(f"using dsn: {dsn}")
    try:
        conn: postgresConnection = await asyncpg.connect(dsn=dsn)
        response = await conn.execute(f"create database {dbname};")
        assert response == "CREATE DATABASE"
        logger.debug(f"yield create_test_database: {dbname}")
        parsed = urlparse(dsn)
        replaced = parsed._replace(path=dbname)
        dsn_unparse = urlunparse(replaced)
        await conn.close()
        yield dsn_unparse
        logger.debug(f"end yield create_test_database: {dbname}")
    finally:
        # drop database here
        conn = await asyncpg.connect(dsn=dsn)
        logger.debug(f"finally create_test_database: {dbname}")
        response = await conn.execute(f"drop database {dbname};")
        await conn.close()
        assert response == "DROP DATABASE"
        logger.debug(f"end create_test_database: {dbname}")


@asynccontextmanager
async def get_connection(driver: str, dsn: str) -> Union[Pool, sqliteConnection]:
    if driver == "asyncpg":
        connection = await asyncpg.connect(dsn)
    elif driver == "aiosqlite":
        connection = await aiosqlite.connect(dsn, isolation_level=None)
    else:
        raise ValueError(f"unregistered driver_adapter: {driver}")
    yield connection
    await connection.close()


def camel2snake(camel: str) -> str:
    """
    Converts a camelCase string to snake_case.
    """
    snake = re.sub(r"([a-zA-Z])([0-9])", lambda m: f"{m.group(1)}_{m.group(2)}", camel)
    snake = re.sub(r"([a-z0-9])([A-Z])", lambda m: f"{m.group(1)}_{m.group(2)}", snake)
    return snake.lower()


def get_next_revision(
    revisions: List[RevisionPath], current: int
) -> Optional[RevisionPath]:
    for idx, revision in enumerate(revisions):
        if revision.version_id > current:
            return revisions[idx]
    return None


def get_previous_revision(
    revisions: List[RevisionPath], current: int
) -> Optional[RevisionPath]:
    revisions = sorted(revisions, key=lambda x: x.version_id, reverse=True)
    for idx, revision in enumerate(revisions):
        if revision.version_id < current:
            return revisions[idx]
    return None


def get_current_revision(
    revisions: List[RevisionPath], current: int
) -> Optional[RevisionPath]:
    for idx, revision in enumerate(revisions):
        if revision.version_id == current:
            return revisions[idx]
    return None

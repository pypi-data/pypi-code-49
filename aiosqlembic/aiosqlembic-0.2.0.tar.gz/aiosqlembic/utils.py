import logging
import platform
import re
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Tuple, List, Any, AsyncGenerator, Union
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
REVISION_PATTERN = r"(?P<rev_number>.*)_(?P<rev_message>.*)\.sql"


async def check_connection(dsn: str) -> bool:
    """
    Checks if the database connection is alive
    """
    try:
        conn = await asyncpg.connect(dsn, timeout=5)
        await conn.execute("select 1")
        await conn.close()
        return True
    except Exception as e:
        logger.error(e)
    return False


def get_list_revision(base_directory: Path) -> Tuple[int, List[Path]]:
    """
    Get the number and a list of sql revisions from the revisions directory
    """
    revisions = list(base_directory.glob("*.sql"))
    if revisions:
        return len(revisions), revisions
    else:
        return 0, revisions


def get_revision_tree(base_directory: Path) -> List[RevisionPath]:
    """
    Builds a list of RevisionPath from the revision directory
    """
    revision_files = list(base_directory.glob("*.sql"))
    revision_tree = []
    if revision_files:
        for revision_file in sorted(revision_files):
            m = re.match(REVISION_PATTERN, revision_file.name)
            if m is not None:
                revision = RevisionPath(
                    rev_number=int(m.group("rev_number")),
                    rev_message=m.group("rev_message"),
                    file=revision_file,
                )
                revision_tree.append(revision)
            else:
                raise ValueError("Wrong filename")
    else:
        revision_tree = [RevisionPath(rev_number=0, rev_message=None, file=None)]
    return revision_tree


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


async def get_connection(driver: str, dsn: str) -> Union[Pool, sqliteConnection]:
    if driver == "asyncpg":
        connection = await asyncpg.create_pool(dsn)
    elif driver == "aiosqlite":
        connection = await aiosqlite.connect(dsn)
    else:
        raise ValueError(f"unregistered driver_adapter: {driver}")
    return connection


def camel2snake(camel: str) -> str:
    """
    Converts a camelCase string to snake_case.
    """
    snake = re.sub(r"([a-zA-Z])([0-9])", lambda m: f"{m.group(1)}_{m.group(2)}", camel)
    snake = re.sub(r"([a-z0-9])([A-Z])", lambda m: f"{m.group(1)}_{m.group(2)}", snake)
    return snake.lower()

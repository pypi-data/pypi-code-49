import json
import logging
import os
from contextlib import contextmanager
import typing
from typing import Union, Text, Any, Optional, Dict

from sanic import Sanic
from sanic.request import Request
from sqlalchemy import create_engine, Sequence
from sqlalchemy import event
from sqlalchemy.engine.base import Engine, Connection
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from time import sleep

import ragex.community.config as rasa_x_config
from ragex.community.constants import REQUEST_DB_SESSION_KEY

from sqlite3 import Connection as SQLite3Connection


logger = logging.getLogger(__name__)


def setup_db(app: Sanic, _, is_local=rasa_x_config.LOCAL_MODE) -> None:
    """Creates and initializes database."""

    url = get_db_url(is_local)
    logger.debug(f"url: {url}")
    app.session_maker = create_session_maker(url)
    configure_session_attachment(app)


def configure_session_attachment(app: Sanic) -> None:
    """Connects the database management to the sanic lifecyle."""
    app.register_middleware(set_session, "request")
    app.register_middleware(remove_session, "response")


def _sql_query_parameters_from_environment() -> Optional[Dict]:
    # fetch db query dict from environment, needs to be stored as a json dump
    # https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.engine.url.URL

    # skip if variable is not set
    db_query = os.environ.get("DB_QUERY")
    if not db_query:
        return None

    try:
        return json.loads(db_query)
    except (TypeError, ValueError):
        logger.exception(
            f"Failed to load SQL query dictionary from environment. Expecting a json dump of a dictionary, but found '{db_query}'."
        )
        return None


def get_db_url(is_local: bool = rasa_x_config.LOCAL_MODE) -> Union[Text, URL]:
    """Return the database connection url from the environment variables."""
    logger.info(f"is_local:{is_local}, os env DB_DRIVER:{os.environ.get('DB_DRIVER')}")
    # Users can also pass fully specified database urls instead of individual components
    if os.environ.get("DB_URL"):
        return os.environ["DB_URL"]

    # if is_local and os.environ.get("DB_DRIVER") is None:
    #     return "sqlite:///rasa.db"

    from ragex.community.services.user_service import ADMIN

    return URL(
        drivername=os.environ.get("DB_DRIVER", "postgresql"),
        username=os.environ.get("DB_USER", "rasa"),
        password=os.environ.get("DB_PASSWORD", "rasa"),
        host=os.environ.get("DB_HOST", "10.62.130.54"),
        port=os.environ.get("DB_PORT", 5432),
        database=os.environ.get("DB_DATABASE", "rasa_db_fresh"),
        query=_sql_query_parameters_from_environment(),
    )


@event.listens_for(Engine, "connect")
def _on_database_connected(dbapi_connection: Any, _) -> None:
    """Configures the database after the connection was established."""

    if isinstance(dbapi_connection, SQLite3Connection):
        set_sqlite_pragmas(dbapi_connection, True)


def set_sqlite_pragmas(
    connection: Union[SQLite3Connection, Connection], enforce_foreign_keys: bool = True
) -> None:
    """Configures the connected SQLite database.

    - Enforce foreign key constraints.
    - Enable `WAL` journal mode.
    """

    if not isinstance(connection, SQLite3Connection):
        logger.debug("Connection is not an sqlite3 connection. Cannot set pragmas.")
        return

    cursor = connection.cursor()
    # Turn on the enforcement of foreign key constraints for SQLite.
    enforce_setting = "ON" if enforce_foreign_keys else "OFF"
    cursor.execute(f"PRAGMA foreign_keys={enforce_setting};")
    logger.debug(
        "Turned SQLite foreign key enforcement {}.".format(enforce_setting.lower())
    )
    # Activate SQLite WAL mode
    cursor.execute("PRAGMA journal_mode=WAL")
    logger.debug("Turned on SQLite WAL mode.")

    cursor.close()


def create_session_maker(url: Union[Text, URL]) -> sessionmaker:
    """Create a new sessionmaker factory.

    A sessionmaker factory generates new Sessions when called.
    """
    import sqlalchemy.exc

    # Database might take a while to come up
    while True:
        try:
            # pool_size and max_overflow can be set to control the number of
            # connections that are kept in the connection pool. these parameters
            # are not available for SQLite (local mode)
            if (
                not rasa_x_config.LOCAL_MODE
                or os.environ.get("DB_DRIVER") == "postgresql"
            ):
                engine = create_engine(
                    url,
                    pool_size=int(os.environ.get("SQL_POOL_SIZE", "50")),
                    max_overflow=int(os.environ.get("SQL_MAX_OVERFLOW", "100")),
                )
            else:
                engine = create_engine(url)
            return sessionmaker(bind=engine)
        except sqlalchemy.exc.OperationalError as e:
            logger.warning(e)
            sleep(5)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""

    url = get_db_url(rasa_x_config.LOCAL_MODE)
    session = create_session_maker(url)()

    try:
        yield session
        session.commit()
    except Exception as _:
        session.rollback()
        raise
    finally:
        session.close()


def get_database_session(is_local: bool = False) -> Session:
    db_url = get_db_url(is_local)
    session_maker = create_session_maker(db_url)
    return session_maker()


async def set_session(request: Request) -> None:
    """Create a new session for the request."""
    request[REQUEST_DB_SESSION_KEY] = request.app.session_maker()


async def remove_session(request: Request, _) -> None:
    """Closes the database session after the request."""
    db_session = request.get(REQUEST_DB_SESSION_KEY)
    if db_session:
        db_session.commit()
        db_session.close()


def create_sequence(table_name: Text) -> Sequence:
    from ragex.community.database.base import Base

    sequence_name = f"{table_name}_seq"
    return Sequence(sequence_name, metadata=Base.metadata, optional=True)


def is_db_revision_latest(session: Session) -> bool:
    """Returns whether the database has been updated with the latest migration
    using Alembic.

    Args:
        session: Database session.

    Returns:
        `True` if the current revision matches the one specified by the newest
            migration file.
    """

    from alembic.runtime.migration import MigrationContext

    context = MigrationContext.configure(session.connection())
    heads = context.get_current_heads()
    if len(heads) != 1:
        logger.warning(
            f"Can't check if DB is migrated to latest Alembic revision, "
            f"multiple or no heads: {heads}."
        )
        return False

    current = context.get_current_revision()
    if not current:
        logger.error("Can't get current database revision.")
        return False

    latest = current == heads[0]
    if not latest:
        logger.debug(
            f"Current database revision: {current}. Target revision: {heads[0]}."
        )

    return latest

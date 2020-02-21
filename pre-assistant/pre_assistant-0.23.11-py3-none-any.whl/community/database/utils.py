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
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from time import sleep

import rasax.community.config as rasa_x_config
from rasax.community.constants import REQUEST_DB_SESSION_KEY
from rasax.community.database.base import Base

if typing.TYPE_CHECKING:
    from sqlite3 import Connection as SQLite3Connection


logger = logging.getLogger(__name__)


def setup_db(app: Sanic, _, is_local=rasa_x_config.LOCAL_MODE) -> None:
    """Creates and initializes database."""

    url = get_db_url(is_local)
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
    from rasax.community.services.user_service import ADMIN

    # Users can also pass fully specified database urls instead of individual components
    if os.environ.get("DB_URL"):
        return os.environ.get("DB_URL")

    if is_local and os.environ.get("DB_DRIVER") is None:
        return "sqlite:///rasa.db"

    from rasax.community.services.user_service import ADMIN

    return URL(
        drivername=os.environ.get("DB_DRIVER", "postgresql"),
        username=os.environ.get("DB_USER", ADMIN),
        password=os.environ.get("DB_PASSWORD", "password"),
        host=os.environ.get("DB_HOST", "db"),
        port=os.environ.get("DB_PORT", 5432),
        database=os.environ.get("DB_DATABASE", "rasa"),
        query=_sql_query_parameters_from_environment(),
    )


@event.listens_for(Engine, "connect")
def _on_database_connected(dbapi_connection: Any, _) -> None:
    """Configures the database after the connection was established."""

    from sqlite3 import Connection as SQLite3Connection

    if isinstance(dbapi_connection, SQLite3Connection):
        set_sqlite_pragmas(dbapi_connection, True)


def set_sqlite_pragmas(
    connection: "SQLite3Connection", enforce_foreign_keys: bool = True
) -> None:
    """Configures the connected SQLite database.

    - Enforce foreign key constraints.
    - Enable `WAL` journal mode.
    """

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
    sequence_name = f"{table_name}_seq"
    return Sequence(sequence_name, metadata=Base.metadata, optional=True)

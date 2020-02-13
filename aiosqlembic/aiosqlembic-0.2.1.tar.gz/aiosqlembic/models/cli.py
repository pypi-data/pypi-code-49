from datetime import datetime
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, BaseModel


class DSN(BaseModel):
    """
    Pydantic model for the database dsn
    """

    scheme: str
    user: str
    password: str
    host: str
    port: str
    db: str


class Migrations(BaseModel):
    """
    Pydantic model for the migration part of the settings
    """

    base_directory: Path


class AiosqlembicSettings(BaseSettings):
    """
    Pydantic model for the settings of the application
    """

    migrations: Migrations
    dsn: DSN


class Revision(BaseModel):
    """
    Pydantic model a base revision
    """

    version_id: int
    message: Optional[str]


class RevisionPath(Revision):
    """
    Pydantic model a base revision with a path
    """

    file: Optional[Path]
    next: int
    previous: int


class ConDB(BaseModel):
    exists: bool


class ConDBTable(BaseModel):
    exists: bool


class Version(BaseModel):
    version_id: int
    is_applied: bool


class MigrateRevision(BaseModel):
    tstamp: datetime
    is_applied: bool

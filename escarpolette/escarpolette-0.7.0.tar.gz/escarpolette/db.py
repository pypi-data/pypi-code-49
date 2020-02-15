from contextlib import contextmanager
from importlib import resources

from sqlalchemy import Column, create_engine, String
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker, Session

from escarpolette.settings import Config

Base: DeclarativeMeta = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False)


class Version(Base):
    __tablename__ = "version"

    version = Column(String, primary_key=True)


def init_app(config: Config):
    engine = create_engine(
        config.DATABASE_URI, connect_args={"check_same_thread": False}
    )
    SessionLocal.configure(bind=engine)

    apply_migrations(engine)


def apply_migrations(engine):
    Base.metadata.create_all(bind=engine, tables=[Version.__table__], checkfirst=True)

    db: Session = SessionLocal()
    current_version = db.query(Version).first()
    if current_version is None:
        current_version = Version(version="v000")

    migrations = resources.contents("escarpolette.migrations")
    for migration in sorted(migrations):
        if not migration.endswith(".sql"):
            continue

        migration_version, _ = migration.split(".")
        if migration_version <= current_version.version:
            continue

        sql = resources.read_text("escarpolette.migrations", migration)
        queries = sql.split(";")
        for query in queries:
            db.execute(query)

        current_version.version, _ = migration.split(".")
        db.add(current_version)
        db.commit()


@contextmanager
def get_db():
    db: Session = SessionLocal()
    db.execute("PRAGMA foreign_keys = ON")
    try:
        yield db
    finally:
        db.close()

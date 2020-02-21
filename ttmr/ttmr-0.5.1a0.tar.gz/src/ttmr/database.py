from datetime import datetime
from pathlib import Path
import pendulum
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


def init(dbfile):
    engine = create_engine(f"sqlite:///{dbfile}")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)


def create_default_config(Session, state):
    session = Session()
    Base.meta.create_all(session)
    session.commit()


class BaseTable:  # pylint: disable=R0903
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean(), default=True)
    created = Column(DateTime(timezone=False), default=pendulum.now)
    modified = Column(DateTime(timezone=False), default=pendulum.now, onupdate=pendulum.now)


FMTS = {
    "INC" : "{}{:0>8}",
    "WO"  : "{}{:0>9}",
    "FY16": "{}-{:0>6}",
    "FY17": "{}-{:0>6}",
    "FY18": "{}-{:0>6}",
    "FY19": "{}-{:0>6}",
    "FY20": "{}-{:0>6}",
    "FY21": "{}-{:0>6}",
    "FY22": "{}-{:0>6}",
    "": "{}-{:0>8}",
}


class Project(Base, BaseTable):
    __tablename__ = 'project'

    type = Column(String(25), nullable=False)
    number = Column(Integer, nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    persistant = Column(Boolean(), default=False)

    @property
    def identifier(self):
        return FMTS.get(self.type, FMTS[""]).format(self.type, self.number)


class Category(Base, BaseTable):
    __tablename__ = 'category'
    name = Column(String(100), nullable=False, unique=True)


class Entry(Base, BaseTable):
    __tablename__ = 'entry'
    category_id = Column(Integer, ForeignKey(Category.id))
    category = relationship(Category, lazy="immediate")
    project_id = Column(Integer, ForeignKey(Project.id))
    project = relationship(Project)
    note = Column(Text, default="")
    timestamp = Column(DateTime(timezone=False), default=datetime.now, unique=True)
    duration = Column(Integer)

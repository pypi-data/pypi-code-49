import os
import pymysql
import traceback

from typing import List

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.result import ResultProxy


class DatabaseException(Exception):
    """raise when fail in transform query in result"""


class Database:
    __engine: Engine
    __session: Session

    @staticmethod
    def create_engine(dsn: str):
        return create_engine(dsn)

    def __init__(self, dsn: str = None, engine: Engine = None):
        self.__engine = engine or create_engine(dsn)

    def __enter__(self):
        self.__session = sessionmaker(bind=self.__engine)()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.commit()
            self.__session.close()
        except:
            pass

    def get(self, object_, *multiparams, **params) -> dict:
        try:
            proxy = self.__session.execute(object_, *multiparams, **params)
            return dict(proxy.fetchone()) if proxy.rowcount > 0 else None
        except:
            traceback.print_exc()
            raise DatabaseException(f"fail when get tuple with query:\n {object_}")

    def list(self, object_, *multiparams, **params) -> List[dict]:
        try:
            proxy = self.__session.execute(object_, *multiparams, **params)
            return [dict(row) for row in proxy] if proxy.rowcount > 0 else []
        except:
            traceback.print_exc()
            raise DatabaseException(f"fail when list data with query:\n {object_}")

    def execute(self, object_, *multiparams, **params) -> ResultProxy:
        try:
            return self.__session.execute(object_, *multiparams, **params)
        except:
            raise DatabaseException(f"fail when execute query:\n {object_}")

    def commit(self):
        try:
            self.__session.commit()
        except:
            pass

    def begin(self):
        self.__session.begin()


class MysqlDriver:
    def __init__(self, hostname: str = None, database: str = None, username: str = None, password: str = None, port: int = None):
        self.hostname = hostname or os.getenv('DB_HOST')
        self.database = database or os.getenv('DB_NAME')
        self.username = username or os.getenv('DB_USER')
        self.password = password or os.getenv('DB_PASS')
        self.port = int(port) if port else int(os.getenv('DB_PORT'))

    def __connect(self):
        conn = pymysql.connect(host=self.hostname, port=self.port, user=self.username, passwd=self.password, db=self.database)
        conn.autocommit(True)
        return conn

    def insert_update_or_delete(self, query: str):
        with self.__connect() as cursor:
            try:
                cursor.execute(query)
            finally:
                cursor.close()

    def select(self, query: str):
        with self.__connect() as cursor:
            try:
                cursor.execute(query)
                rows = cursor.fetchall()
            finally:
                cursor.close()

            return rows

from .DatabaseDataManager import DatabaseDataManager
from .DatabaseEntity import DBEntity


def connect(db_host, db_username, db_password, db_name):
    return DatabaseDataManager(db_host,
                               db_username,
                               db_password,
                               db_name)


def entity(new_entity):
    return DBEntity(new_entity)

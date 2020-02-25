from .DatabaseDataManager import DatabaseDataManager
from .DatabaseEntity import DBEntity


def connect(logger_name, db_host, db_username, db_password, db_name):
    return DatabaseDataManager(logger_name,
                               db_host,
                               db_username,
                               db_password,
                               db_name)


def entity(new_entity):
    return DBEntity(new_entity)

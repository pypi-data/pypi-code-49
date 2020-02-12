from typing import Any

from django.db import connection

from . import rg_logger
from .rg_exceptions import SQLQueryException, RGException


class DatabaseUtil:
    __table_created_cache = {}

    @classmethod
    def execute_sql_query(cls, sql: str, logger_message: str) -> Any and RGException:
        try:
            cursor = connection.cursor()

            try:
                cursor.execute(sql)
                # # rg_logger.info("StatusMessage: " + cursor.status message)
                return cursor, None
            except Exception as e:
                rg_logger.exception(e, "Exception: " + logger_message)
                return None, SQLQueryException(sql, rg_logger.get_exception_msg(e))
        except Exception as e:
            rg_logger.exception(e, "Exception: " + logger_message)
            return None, SQLQueryException(sql, rg_logger.get_exception_msg(e))

    @classmethod
    def execute_sql_query_to_update_table_data(cls, sql: str, logger_message: str) -> Exception:
        try:
            cursor = connection.cursor()

            try:
                cursor.execute(sql)
                # # rg_logger.info("StatusMessage: " + cursor.statusmessage)
                if cursor:
                    cursor.close()
            except Exception as e:
                # rg_logger.info("Exception: " + logger_message)
                return SQLQueryException(sql, rg_logger.get_exception_msg(e))

        except Exception as e:
            rg_logger.info("Exception: " + logger_message + ", message: " + rg_logger.get_exception_msg(e))
            return SQLQueryException(sql, rg_logger.get_exception_msg(e))

    @classmethod
    def fetch_one_from_cursor_to_dict(cls, cursor):
        try:
            if cursor.rowcount > 0:
                columns = [col[0] for col in cursor.description]
                return dict(zip(columns, cursor.fetchone()))
        except Exception as e:
            rg_logger.exception(e)

        return None

    @classmethod
    def fetch_all_from_cursor_to_dict(cls, cursor):
        try:
            if cursor.rowcount > 0:
                desc = cursor.description
                return [
                    dict(zip([col[0] for col in desc], row))
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            rg_logger.exception(e)

        return None

    @classmethod
    def create_db_table(cls, sql_string: str, table_name: str) -> bool:
        is_table_created = False

        if not cls.is_table_name_exist_in_local_cache(table_name):
            if cls.is_table_exist_in_db(table_name):
                is_table_created = True
            else:
                try:
                    cursor = connection.cursor()
                    try:
                        cursor.execute(sql_string)
                        rg_logger.info("PlayerData.create_table_if_not_exist->>Table created:" + table_name)

                        is_table_created = True
                    except Exception as e:
                        if "already exists" in getattr(e, 'message', repr(e)):
                            is_table_created = True

                        rg_logger.exception(e, log_message="PlayerData.create_table_if_not_exist->>")

                    cursor.close()
                except Exception as e:
                    rg_logger.exception(e, "PlayerData.create_table_if_not_exist->>")

            if is_table_created:
                cls.__add_table_name_in_cache(table_name)
        else:
            pass

        return is_table_created

    @classmethod
    def is_table_exist_in_db(cls, table_name: str) -> bool:

        try:
            return table_name in connection.introspection.table_names()
        except Exception as e:
            rg_logger.logger("PlayerData.create_table_if_not_exist->>Exception: " + getattr(e, 'message', repr(e)))
        return False

    @classmethod
    def is_table_name_exist_in_local_cache(cls, table_name: str):
        return cls.__table_created_cache and table_name in cls.__table_created_cache

    @classmethod
    def __add_table_name_in_cache(cls, table_name):
        if not cls.__table_created_cache:
            cls.__table_created_cache = {}

        cls.__table_created_cache[table_name] = True

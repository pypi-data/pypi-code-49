import mysql.connector
import logging
from .DatabaseEntity import DBEntity


class DatabaseConnector:

    def __init__(self, logger_name, db_host, db_username, db_password, db_name):
        self.database = mysql.connector.connect(
            host=db_host,
            user=db_username,
            passwd=db_password,
            database=db_name,
            auth_plugin="mysql_native_password"
        )
        self.logger = logging.getLogger(logger_name)
        self.cursor = self.database.cursor(dictionary=True)
        self.select_statement = ""
        self.insert_statement = ""
        self.update_statement = ""
        self.delete_statement = ""

    def create_select(self, entity):
        self.select_statement = "SELECT "
        self.select_statement += entity.select_col_clause
        self.select_statement += " FROM "
        self.select_statement += entity.table.table_name()
        if entity.where_clause is not None:
            self.select_statement += entity.where_clause
        if entity.order_by_clause is not None:
            self.select_statement += entity.order_by_clause
        self.select_statement += ";"
        self.logger.info("Created statement: '" + self.select_statement + "'")

    def execute_select(self, table, single=False):
        self.cursor.execute(self.select_statement)
        if single:
            select_dict = self.cursor.fetchone()
        else:
            select_dict = self.cursor.fetchall()
        if select_dict is None:
            self.logger.info("Executed statement: '" + self.select_statement + "' NO ROWS SELECTED")
            return None
        else:
            self.logger.info("Executed statement: '" + self.select_statement + "' Rows: " + str(len(select_dict)))
            if single:
                db_obj = DBEntity(table, select_dict)
                return db_obj
            else:
                db_objs = []
                for record in select_dict:
                    db_objs.append(DBEntity(table, record))
                return db_objs

    def create_insert(self, entity):
        self.insert_statement = "INSERT INTO "
        self.insert_statement += entity.table.table_name() + " "
        self.insert_statement += entity.insert_col_val_clause
        self.insert_statement += ";"
        self.logger.info("Created statement: '" + self.insert_statement + "'")

    def execute_insert(self):
        row_count = self.cursor.execute(self.insert_statement)
        self.logger.info("Executed statement: '" + self.insert_statement + "' Row Count: " + str(row_count))
        return self.cursor.lastrowid

    def create_update(self, entity):
        self.update_statement = "UPDATE "
        self.update_statement += entity.table.table_name() + " "
        self.update_statement += entity.update_clause + " "
        self.update_statement += entity.where_clause + ";"
        self.logger.info("Created statement: '" + self.update_statement + "'")

    def execute_update(self):
        row_count = self.cursor.execute(self.update_statement)
        self.logger.info("Executed statement: '" + self.update_statement + "' Row Count: " + str(row_count))
        return self.cursor.lastrowid

    def create_delete(self, entity):
        self.delete_statement = "DELETE FROM "
        self.delete_statement += entity.table.table_name() + " "
        self.delete_statement += entity.where_clause
        self.delete_statement += ";"
        self.logger.info("Create statement: '" + self.delete_statement + "'")

    def execute_delete(self):
        row_count = self.cursor.execute(self.delete_statement)
        self.logger.info("Executed statement: '" + self.delete_statement + "' Row Count: " + str(row_count))
        return self.cursor.lastrowid

    def commit_execute(self):
        self.database.commit()
        self.logger.info("Committed execution.")
        return self.cursor.lastrowid

    def get_table_information(self):
        self.select_statement = "SHOW TABLES;"
        self.cursor.execute(self.select_statement)
        tables_dict = self.cursor.fetchall()
        tables = {}
        for table_dict in tables_dict:
            for schema, table_name in table_dict.items():
                self.select_statement = "DESCRIBE " + table_name
                self.cursor.execute(self.select_statement)
                table_description_dict = self.cursor.fetchall()
                tables[table_name] = table_description_dict
        return tables

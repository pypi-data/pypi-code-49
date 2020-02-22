from .DatabaseConnector import DatabaseConnector
from .FileDataManager import FileDataManager
import logging


class DatabaseDataManager:

    def __init__(self, logger_name, db_host, db_username, db_password, db_name):
        self.connector = DatabaseConnector(logger_name, db_host, db_username, db_password, db_name)
        self.insert_statement = ""
        self.update_statement = ""
        self.file_manager = FileDataManager(logger_name)
        self.logger = logging.getLogger(logger_name)

    def insert(self, entities, commit=True):
        last_row_id = None
        if isinstance(entities, list):
            for entity in entities:
                self.connector.create_insert(entity)
                last_row_id = self.connector.execute_insert()
        else:
            self.connector.create_insert(entities)
            last_row_id = self.connector.execute_insert()
        if commit:
            last_row_id = self.connector.commit_execute()

        return last_row_id

    def __select(self, entity, single=False):
        self.connector.create_select(entity)
        return self.connector.execute_select(entity.table, single)

    def select_all(self, entity):
        return self.__select(entity)

    def select_single(self, entity):
        return self.__select(entity, True)

    def update(self, entities, commit=True):
        last_row_id = None
        if isinstance(entities, list):
            for entity in entities:
                self.connector.create_update(entity)
                last_row_id = self.connector.execute_update()
        else:
            self.connector.create_update(entities)
            last_row_id = self.connector.execute_update()
        if commit:
            last_row_id = self.connector.commit_execute()

        return last_row_id

    def delete(self, entities, commit=True):
        last_row_id = None
        if isinstance(entities, list):
            for entity in entities:
                self.connector.create_delete(entity)
                last_row_id = self.connector.execute_delete()
        else:
            self.connector.create_delete(entities)
            last_row_id = self.connector.execute_delete()
        if commit:
            last_row_id = self.connector.commit_execute()

        return last_row_id

    def commit(self):
        return self.connector.commit_execute()

    def update_classes_file(self, file_path):
        table_info = self.connector.get_table_information()
        self.file_manager.open(file_path)
        self.file_manager.write("from enum import Enum")
        for table_name, columns in table_info.items():
            self.file_manager.write_line(lines=3)
            name_words = table_name.split('_')
            name = ''
            for name_word in name_words:
                name += name_word.capitalize()
            self.file_manager.write_line("class " + name + "(Enum):", lines=2)

            self.file_manager.write_line("@classmethod", tabs=1)
            self.file_manager.write_line("def table_name(cls):", tabs=1)
            self.file_manager.write_line("return '" + table_name + "'", tabs=2, lines=2)

            auto_increment_list = []
            not_null_list = []
            for column in columns:
                if 'auto_increment' in column['Extra']:
                    auto_increment_list.append(column['Field'])
                elif 'NO' in column['Null']:
                    not_null_list.append(column['Field'])

            self.file_manager.write_line("@classmethod", tabs=1)
            self.file_manager.write_line("def auto_increments(cls):", tabs=1)
            self.file_manager.write("return [", tabs=2)

            if len(auto_increment_list) > 0:
                for column in auto_increment_list[:-1]:
                    self.file_manager.write("'" + column + "', ")
                else:
                    self.file_manager.write("'" + auto_increment_list[-1] + "'")
            self.file_manager.write_line("]", lines=2)

            self.file_manager.write_line("@classmethod", tabs=1)
            self.file_manager.write_line("def not_nulls(cls):", tabs=1)
            self.file_manager.write("return [", tabs=2)

            if len(not_null_list) > 0:
                for column in not_null_list[:-1]:
                    self.file_manager.write("'" + column + "', ")
                else:
                    self.file_manager.write("'" + not_null_list[-1] + "'")
            self.file_manager.write_line("]")

            for column in columns:
                self.file_manager.write_line()
                self.file_manager.write(column['Field'].lower() + " = '" + column['Field'] + "'", tabs=1)
        self.file_manager.write_line(lines=3)

        self.file_manager.write("DB_TABLES = {")
        count = 0
        for table_name in table_info:
            name_words = table_name.split('_')
            name = ''
            for name_word in name_words:
                name += name_word.capitalize()
            self.file_manager.write("'" + table_name + "': " + name)
            count += 1
            if count < len(table_info):
                self.file_manager.write_line(",")
                self.file_manager.write(spaces=13)
        self.file_manager.write_line("}")
        self.file_manager.close()

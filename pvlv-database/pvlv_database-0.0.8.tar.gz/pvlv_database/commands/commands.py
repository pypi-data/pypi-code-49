from pvlv_database.configurations.configuration import DATABASE_NAME, COMMANDS_TABLE_NAME
from pvlv_database.connectors.connector import Connector


class Commands(object):

    def __init__(self, command_name):

        self.__command_name = command_name

        self.data = {}

        self.get_data()

    def set_data(self):
        self.data['unique_id'] = self.__command_name
        Connector().push_data(DATABASE_NAME, COMMANDS_TABLE_NAME, self.__command_name, self.data)

    def get_data(self):
        try:
            self.data = Connector().pull_data(DATABASE_NAME, COMMANDS_TABLE_NAME, self.__command_name)
            del self.data['unique_id']
            return self.data
        except KeyError:
            return {}

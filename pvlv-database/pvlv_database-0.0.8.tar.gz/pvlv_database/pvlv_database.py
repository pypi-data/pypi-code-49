from pvlv_database.cache.database_cache import DatabaseCache
from pvlv_database.commands.commands import Commands

db_cache = DatabaseCache()  # the global module that will handle the cache


class Database(object):

    def __init__(self, guild_id=0, user_id=0):

        self.user = db_cache.user(guild_id, user_id)
        self.guild = db_cache.guild(guild_id)

    def force_set_data(self):
        self.user.set_data()
        self.guild.set_data()


class DataCommands(object):

    @staticmethod
    def get_command_data(command_name):
        """
        :param command_name: name of the command
        :return: a dict with the data inside
        """
        return Commands(command_name).data

    @staticmethod
    def set_command_data(command_name, command_data):
        """
        :param command_name: name of the command
        :param command_data: the dict data to save
        :return: a dict with the data inside
        """
        c = Commands(command_name)
        c.data = command_data
        c.set_data()

from pvlv_database.configurations.configuration import DATABASE_NAME, USERS_TABLE_NAME
from pvlv_database.connectors.connector import Connector
from .guild_user.guild_user import GuildUser


class User(object):

    def __init__(self, guild_id, user_id):

        self.__scope = DATABASE_NAME
        self.__guild_id = guild_id
        self.__user_id = user_id

        # user data logging
        self.username = None
        self.emails = []
        self.time_zone = 0
        self.gender = ''
        self.age = 20
        self.country = ''
        self.vip_status_code = 101  # code of the vip status for the bot
        self.last_seen = None

        self.deep_logging = True
        self.global_permissions_code = 10  # to use commands with privilege
        self.suspended = False
        self.verification_code = 120028  # auto regenerated, is the code to send as verification.

        self.__guilds = []  # the list of the guild where the user is in
        self.guild = GuildUser()  # the guild where the user is currently typing

        self.get_data()

    def set_data(self):

        guilds = []
        for guild in self.__guilds:
            guilds.append(guild.build_data())

        data = {
            'unique_id': self.__user_id,
            'username': self.username,
            'emails': self.emails,
            'time_zone': self.time_zone,
            'gender': self.gender,
            'age': self.age,
            'country': self.country,
            'vip_status_code': self.vip_status_code,
            'last_seen': self.last_seen,

            'deep_logging': self.deep_logging,
            'global_permissions_code': self.global_permissions_code,
            'suspended': self.suspended,
            'verification_code': self.verification_code,

            'guilds': guilds,
        }

        Connector().push_data(self.__scope, USERS_TABLE_NAME, self.__user_id, data)

    def get_data(self):

        data = Connector().pull_data(self.__scope, USERS_TABLE_NAME, self.__user_id)

        self.username = data.get('username', self.username)
        self.emails = data.get('emails', self.emails)
        self.time_zone = data.get('time_zone', self.time_zone)
        self.gender = data.get('gender', self.gender)
        self.age = data.get('age', self.age)
        self.country = data.get('country', self.country)
        self.vip_status_code = data.get('vip_status_code', self.vip_status_code)
        self.last_seen = data.get('last_seen', self.last_seen)

        self.deep_logging = data.get('deep_logging', self.deep_logging)
        self.global_permissions_code = data.get('global_permissions_code', self.deep_logging)
        self.suspended = data.get('suspended', self.deep_logging)
        self.verification_code = data.get('verification_code', self.verification_code)

        guilds = data.get('guilds')
        if guilds:
            for guild in guilds:
                self.__guilds.append(GuildUser().extract_data(guild))

        self.__find_guild_by_id(self.__guild_id)

    def __find_guild_by_id(self, guild_id):
        """
        Find or create the guild by id.
        If is not found it will create a new object with the guild_id given

        :param guild_id: the numeric id of the guild
        :return: the guild object
        """
        if self.__guilds:
            for guild in self.__guilds:
                if guild.guild_id == guild_id:
                    self.guild: GuildUser = guild
                    return

        self.guild.guild_id = guild_id
        self.__guilds.append(self.guild)

    @property
    def user_id(self):
        return self.__user_id

from pvlv_database.cache.database_cache import DatabaseCache

db_cache = DatabaseCache()  # the global module that will handle the cache


class Database(object):

    def __init__(self, guild_id, user_id):

        self.user = db_cache.user(guild_id, user_id)
        self.guild = db_cache.guild(guild_id)

    def force_set_data(self):
        self.user.set_data()
        self.guild.set_data()

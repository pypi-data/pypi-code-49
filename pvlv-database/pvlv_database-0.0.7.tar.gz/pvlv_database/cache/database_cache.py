from time import time
from pvlv_database.user.user import User
from pvlv_database.guild.guild import Guild
from pvlv_database.cache.item_storage import ItemStorage
from pvlv_database.cache.saving_demon import SavingDemon
from pvlv_database.configurations.configuration import (
    logger,
    CACHE_INTERVAL_SECONDS,
    CACHE_MAX_ITEMS,
)


class DatabaseCache(object):

    def __init__(self):
        self.users = []
        self.guilds = []

        self.saving_demon = SavingDemon()
        self.saving_demon.start_loop(self.__save, CACHE_INTERVAL_SECONDS)

    @staticmethod
    def __find_el(storage_list, identifier):
        """
        :param storage_list: the list of item where perform the search
        :param identifier: the object that will identify that item
        :return: the item stored
        """
        for el in storage_list:
            el: ItemStorage
            if el.identifier == identifier:
                el.is_modified = True
                return el.item
        return None

    def __add_el(self, storage_list_name, identifier, item):
        """
        :param storage_list_name: the name of the array that store that item
        :param identifier: the object that will identify that item
        :param item: the item to store
        """
        storage_list = getattr(self, storage_list_name)  # get the obj by the name
        item_to_store = ItemStorage(identifier, item, time())  # create a new itemStorage
        if len(storage_list) > CACHE_MAX_ITEMS:  # Check if the storage has reached the maxim capability
            storage_list.pop(0)
        storage_list.append(item_to_store)

    def user(self, guild_id, user_id):
        identifier = (guild_id, user_id)
        u = self.__find_el(self.users, identifier)

        if not u:  # if the user is in the cache system return it, else get it from remote db
            u = User(guild_id, user_id)
            self.__add_el('users', identifier, u)

        return u

    def guild(self, guild_id):
        g = self.__find_el(self.guilds, guild_id)

        if not g:  # if the guild is in the cache system return it, else get it from remote db
            g = Guild(guild_id)
            self.__add_el('guilds', guild_id, g)

        return g

    @staticmethod
    def __save_storage_list(storage_list):
        """
        Function that will handle the save on the Database
        - check if the item has been modified.
        - check if the time has passed.
        if boot the preconditions are true then update the item on the remote db
        """
        for el in storage_list:
            el: ItemStorage
            if el.is_modified:
                logger.info('Database Save item in: {}'.format(el.identifier))
                el.is_modified = False
                el.last_save = time()
                el.item.set_data()

    def __save(self):

        self.__save_storage_list(self.users)
        self.__save_storage_list(self.guilds)

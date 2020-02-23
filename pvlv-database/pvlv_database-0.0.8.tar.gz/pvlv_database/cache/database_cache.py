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

        # set and start the demon for auto-save
        self.saving_demon = SavingDemon()
        self.saving_demon.start_loop(self.__save, CACHE_INTERVAL_SECONDS)

    @staticmethod
    def __find_el(storage_list, identifier):
        """
        :param storage_list: the list of item where perform the search
        :param identifier: the object that will identify that item
        :return: the item stored
        """
        for i, item in enumerate(storage_list):
            item: ItemStorage
            if item.identifier == identifier:
                storage_list[i].is_modified = True
                return storage_list[i].item

        return None

    def __add_el(self, storage_list_name, identifier, item):
        """
        :param storage_list_name: the name of the array that store that item
        :param identifier: the object that will identify that item
        :param item: the item to store
        """
        item_storage = ItemStorage(identifier, item)  # create a new itemStorage

        storage_list = getattr(self, storage_list_name)  # get the obj by the name
        if len(storage_list) > CACHE_MAX_ITEMS:  # Check if the storage has reached the maxim capability
            storage_list.pop(0)

        storage_list.append(item_storage)

    def user(self, guild_id, user_id):
        """
        Search the user in the cache,
        if is not present get it from the remote DB

        :param guild_id: the id
        :param user_id: the id
        :return: the user obj
        """
        identifier = (guild_id, user_id)
        u = self.__find_el(self.users, identifier)

        if not u:  # if the user is in the cache system return it, else get it from remote db
            u = User(guild_id, user_id)
            self.__add_el('users', identifier, u)

        return u

    def guild(self, guild_id):
        """
        Search the guild in the cache,
        if is not present get it from the remote DB

        :param guild_id: the id
        :return: the guild obj
        """
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
        for i, item in enumerate(storage_list):
            item: ItemStorage  # define the type of the item for object visibility
            if item.is_modified:
                logger.info('Db sync, item: {}'.format(item.identifier))
                storage_list[i].is_modified = False  # Reset the modified flag
                storage_list[i].last_save = time()  # update the time
                storage_list[i].item.set_data()  # call che method to sync with

    def __save(self):
        """
        The object called by the thread to save all the tables to the remote Database
        """
        logger.info('Database changes check')
        self.__save_storage_list(self.users)
        self.__save_storage_list(self.guilds)

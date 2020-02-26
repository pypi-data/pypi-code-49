from typing import Callable, T, Union
from collections.abc import Iterable

from networktables import NetworkTables
from networktables.networktable import NetworkTable

from gbrpi.constants.types import ConnEntryValue


class TableConn:
    """
    a simplified wrapper for a network table connection
    NOTE! the table initializes asynchronously, if you need a value immediately after initializing,
        use time.sleep before getting it

    :param ip: the network table server's ip (usually the RoboRIO's ip)
    :param table_name: the network table's name
    :param initialize: whether or not to initialize the network tables (default is true)
    """

    @staticmethod
    def __fix_func(func: Callable[[ConnEntryValue], None]):
        return lambda source, key, value, is_new: func(value)

    def __init__(self, ip: str, table_name: str, initialize=True):
        if initialize:
            NetworkTables.initialize(ip)
        self.table: NetworkTable = NetworkTables.getTable(table_name)

    def set_table(self, table: NetworkTable):
        """
        sets the inner network table

        :param table: the inner network table
        """
        self.table = table

    def get(self, key: str, default: T = None) -> Union[ConnEntryValue, T]:
        """
        retrieve a value from the network table

        :param key: the key of the value
        :param default: the default value to return if the key does not exist
        :return: the value from the network table
        """
        return self.table.getValue(key, default)

    def set(self, key: str, value: ConnEntryValue):
        """
        sets a value in the network table
        :param key:
        :param value:
        """
        if isinstance(value, Iterable) and type(value) not in [bytes, str]:
            value = tuple(value)
        self.table.putValue(key, value)

    def add_entry_change_listener(self, func: Callable[[ConnEntryValue], None], key: str, notify_now=True, notify_local=True):
        """
        add a function to be called every time a specific entry is changed on the vision table

        :param func: the callback function, receives the new value of the entry as the only argument
        :param key: the key to track
        :param notify_now: whether or not to call the function with the current value (if exists), default is true
        :param notify_local: whether or not to notify if the change was made locally, default is true
        """
        self.table.addEntryListener(self.__fix_func(func), key=key, localNotify=notify_local,
                                    immediateNotify=notify_now)

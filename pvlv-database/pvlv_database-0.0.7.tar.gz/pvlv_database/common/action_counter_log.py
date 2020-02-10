from pvlv_database.configurations.configuration import (
    MAX_RETENTION_HOUR,
    MAX_RETENTION_DAY,
    MAX_RETENTION_MONTH,
)
from datetime import timedelta


class ActionCounterLog(object):
    """
    Store the logs with timestamp. At a predetermined granularity
    The data retention for efficiency has a maximum data retention
    It will build a tuple with (timestamp, count, time_spent)
    The time_spent is an optional field to store the time spent to do that action
    """
    def __init__(self):
        self.__log_by_hour = []
        self.__log_by_day = []
        self.__log_by_month = []

        self.total_count = 1  # global use count with no data retention

    def extract_data(self, raw_data):
        self.__log_by_hour = raw_data.get('log_by_hour', self.log_by_hour)
        self.__log_by_day = raw_data.get('log_by_day', self.log_by_day)
        self.__log_by_month = raw_data.get('log_by_month', self.log_by_month)

        self.total_count = raw_data.get('total_count', self.total_count)

        return self

    def build_data(self):
        data_out = {
            'log_by_hour': self.__log_by_hour,
            'log_by_day': self.__log_by_day,
            'log_by_month': self.__log_by_month,

            'total_count': self.total_count,
        }
        return data_out

    @property
    def log_by_hour(self):
        return self.__log_by_hour

    def update_log_by_hour(self, value: tuple):
        """
        Update the current log array with new data
        :param value: a tuple timestamp, counter, time_spent (datetime, int, int)
        """
        timestamp, counter, time_spent = value  # de-tuple the value

        # Check if the len has reached the max, then pop the last element
        array_len = len(self.__log_by_hour)
        if array_len > MAX_RETENTION_HOUR:
            self.__log_by_hour.pop()

        # If the array is void, append the first item
        timestamp = timestamp.replace(minute=0, second=0, microsecond=0)
        if array_len is 0:
            self.__log_by_hour.append([timestamp, counter, time_spent])
            return

        # If there are items in the array check the last one
        # if time delta has passed, insert a new item, else sum to the first one
        sub = timestamp - self.__log_by_hour[0][0]  # get time from first el
        if sub >= timedelta(hours=1):
            self.__log_by_hour.insert(0, [timestamp, counter, time_spent])
        else:
            self.__log_by_hour[0][1] += counter
            self.__log_by_hour[0][2] += time_spent

    @property
    def log_by_day(self):
        return self.__log_by_day

    def update_log_by_day(self, value):
        timestamp, counter, time_spent = value  # de-tuple the value

        # Check if the len has reached the max, then pop the last element
        array_len = len(self.__log_by_day)
        if array_len > MAX_RETENTION_DAY:
            self.__log_by_day.pop()

        # If the array is void, append the first item
        timestamp = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
        if array_len is 0:
            self.__log_by_day.append([timestamp, counter, time_spent])
            return

        # If there are items in the array check the last one
        # if time delta has passed, insert a new item, else sum to the first one
        sub = timestamp - self.__log_by_day[0][0]  # get time from first el
        if sub >= timedelta(days=1):
            self.__log_by_day.insert(0, [timestamp, counter, time_spent])
        else:
            self.__log_by_day[0][1] += counter
            self.__log_by_day[0][2] += time_spent

    @property
    def log_by_month(self):
        return self.__log_by_month

    def update_log_by_month(self, value):
        timestamp, counter, time_spent = value  # de-tuple the value

        # Check if the len has reached the max, then pop the last element
        array_len = len(self.__log_by_month)
        if array_len > MAX_RETENTION_MONTH:
            self.__log_by_month.pop()

        # If the array is void, append the first item
        if array_len is 0:
            self.__log_by_month.append([timestamp, counter, time_spent])
            return

        # If there are items in the array check the last one
        # if time delta has passed, insert a new item, else sum to the first one
        db_timestamp = self.__log_by_month[0][0]  # get time from first el

        if timestamp.month > db_timestamp.month or (timestamp.month == 1 and db_timestamp.month == 12):
            self.__log_by_month.insert(0, [timestamp, counter, time_spent])
        else:
            self.__log_by_month[0][1] += counter
            self.__log_by_month[0][2] += time_spent

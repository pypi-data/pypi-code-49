import dateutil
import arrow
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse


class DateUtils:
    @staticmethod
    def now():
        """
        返回当前的时间
        :return: 
        """
        return datetime.now()
        pass

    @staticmethod
    def date2str(date, format='YYYY-MM-DD HH:mm:ss.SSS'):
        """
        
        :param date: 
        :param format: 
        :return: 
        """
        date_str = datetime.strftime(date, '%Y-%m-%d %H:%M:%S.%f')[:-3]
        return arrow.get(date_str).format(format)
        pass

    @staticmethod
    def str2date(date_str):
        """
        
        :param date_str: 
        :return: 
        """
        return parse(date_str)
        pass

    @staticmethod
    def of(year=None, month=None, day=None, hour=None, minute=None, second=None, millisecond=None, microsecond=None):
        """
        生成特定的时间
        :param year: 
        :param month: 
        :param day: 
        :param hour: 
        :param minute: 
        :param second: 
        :param millisecond: 
        :return: 
        """
        now = datetime.now()
        return datetime.now().replace(
            year or now.year,
            month or now.month,
            day or now.day,
            hour or now.hour,
            minute or now.minute,
            second or now.second,
            (millisecond or now.microsecond / 1000) * 1000 + (microsecond or now.microsecond % 1000)
        )

    @staticmethod
    def set(date, year=None, month=None, day=None, hour=None, minute=None, second=None, millisecond=None,
            microsecond=None):
        """
        
        :param date: 
        :param year: 
        :param month: 
        :param day: 
        :param hour: 
        :param minute: 
        :param second: 
        :param millisecond: 
        :param microsecond: 
        :return: 
        """
        sub_second = None
        if millisecond != None or microsecond != None:
            sub_second = 0
        if millisecond != None:
            sub_second = sub_second + 1000 * millisecond
        if microsecond != None:
            sub_second = sub_second + microsecond
        return date.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=second,
                            microsecond=sub_second)
        pass

    @staticmethod
    def add_time(base, year=0, month=0, day=0, hour=0, minute=0, second=0, millisecond=0,
                 microsecond=0):
        """
        
        :param base: 
        :param year: 
        :param month: 
        :param day: 
        :param hour: 
        :param minute: 
        :param second: 
        :param millisecond: 
        :param microsecond: 
        :return: 
        """
        delta = timedelta(days=year * 365 + month * 31 + day, hours=hour, minutes=minute,
                          seconds=second, milliseconds=millisecond, microseconds=microsecond)
        return base + delta
        pass

    @staticmethod
    def time_diff(start, end):
        """
        
        :param start: 
        :param end: 
        :return: 
        """
        return end - start
        pass

    @staticmethod
    def time_delta_with_diff_unit(start, end):
        """
        :param start: 
        :param end: 
        :param unit: 
        :return: 
        """
        diff = end - start
        print(diff)
        ret = {}
        # a = datetime.now()
        # b = datetime.now()
        # diff=(b-a)
        ret['year'] = int(diff.days / 365)
        ret['month'] = int(diff.days / 31)
        ret['day'] = diff.days
        ret['hour'] = ret['day'] * 24 + diff.seconds % 3600
        ret['minute'] = ret['day'] * 24 * 60 + diff.seconds % 60
        ret['second'] = ret['day'] * 24 * 60 * 60 + diff.seconds

        ret['millisecond'] = ret['second'] * 1000 + int(diff.microseconds / 1000)
        ret['microsecond'] = ret['second'] * 1000000 + diff.microseconds

        return ret

        pass

    @staticmethod
    def time_diff_by_second(start, end):
        pass

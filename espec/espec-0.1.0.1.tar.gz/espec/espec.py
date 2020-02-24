from datetime import datetime, timedelta
from guang.Utils.date import LunarDate as Lunar
from guang.Utils.time import beijing
from guang.Utils.toolsFunc import dict_dotable
import dill
import os


class Mycrony:
    def __init__(self, name=''):
        self.__crony = {}

        # self.name = ''
        self.load()
        self.__crony=  dict_dotable(self.__crony)

    def set_name(self, name):
        self.name = name

    def set_birthday(self, date, lunarORsolar="lunar"):
        """
        --data: a  [year, month, day] list
        --lunarORsolar: "lunar" or "solar"
        """
        self.__crony.setdefault(self.name, {})
        self.__crony[self.name].setdefault("birthday", {})

        if lunarORsolar=="lunar":
            lunar_date = Lunar(*date)
            print(lunar_date)
            self.__crony[self.name]["birthday"]["lunar"] = lunar_date
            solar_date = lunar_date.to_datetime()
            self.__crony[self.name]["birthday"]["_solar"] = solar_date

        elif lunarORsolar=="solar":
            solar_date = datetime(*date)
            self.__crony[self.name]["birthday"]["solar"] = solar_date
            self.__crony[self.name]["birthday"]["_lunar"] = Lunar.from_datetime(solar_date)
        else:
            raise ValueError("lunarORsolar: lunar or solar")


    def get_current_birthday(self, name, lunarORsolar="lunar", tz="beijing"):
        # Birth = {"lunar":self.__crony[name]["birthday"]["lunar"],
        #          "solar":self.__crony[name]["birthday"]["solar"]}
        # return Birth.get(lunarORsolar, None)
        solar_now = beijing.now if tz=="beijing" else datetime.now()
        lunar_now = Lunar.from_datetime(solar_now)
        if lunarORsolar=="lunar":
            lunar_birthday = self.__crony[name]["birthday"]["lunar"]
            year = lunar_now.lunar_year
            return Lunar(year, lunar_birthday.lunar_month, lunar_birthday.lunar_day)
        elif lunarORsolar=="solar":
            solar_birthday = self.__crony[name]["birthday"]["solar"]
            year = solar_now.year
            return datetime(year, solar_birthday.month, solar_birthday.day)
        else:
            raise ValueError("lunarORsolar: lunar/solar")

    def get_all_msg(self):
        return self.__crony

    def get_all_names(self):
        names = []
        for i in self.__crony.keys():
            names.append(i)
        return names

    def get_all_lunar_birthday(self):
        """
        return [name list, birthday list]
        """
        birthdays = []
        names = self.get_all_names()
        NAME = []
        for i in names:
            try:
                birthdays.append(self.__crony[i]["birthday"]["lunar"])
                NAME.append(i)
            except:
                continue
        return [NAME, birthdays]

    def get_all_solar_birthday(self):
        """
        return [name list, birthday list]
        """
        birthdays = []
        NAME = []
        names = self.get_all_names()
        for i in names:
            try:
                birthdays.append(self.__crony[i]["birthday"]["solar"])
                NAME.append(i)
            except:
                continue
        return [NAME, birthdays]

    def get_all_valid_birthday(self):
        """
        return [name list, birthday list]
        """
        birthdays = []
        Names =[]
        names = self.get_all_names()
        for i in names:
            try:
                birthdays.append(self.__crony[i]["birthday"]["lunar"])
                Names.append(i)
                try:
                    birthdays.append(self.__crony[i]["birthday"]["solar"])
                    Names.append(i)
                except:
                    pass
            except:
                birthdays.append(self.__crony[i]["birthday"]["solar"])
                Names.append(i)
        return [Names, birthdays]

    def find_name_from_birthday(self, date):
        """
        --date can be Lunar type or Solar type

        """

        target_names = []
        if type(date).__name__ == "LunarDate":
            for i in self.get_all_names():
                try:
                    if self.__crony[i]["birthday"]["lunar"] == date:
                        target_names.append(i)
                except:
                    continue
            return target_names

        elif type(date).__name__ == "datetime":
            for i in self.get_all_names():
                try:
                    if self.__crony[i]["birthday"]["solar"] == date:
                        target_names.append(i)
                except:
                    continue
            return target_names

        else:
            raise ValueError("The type of '--date' should be LunarDate or datetime")

    def del_brithday(self, name, date):
        """
        :arg date can be lunar or solar
        """
        if type(date).__name__ == "LunarDate":
            del self.__crony[name]["birthday"]["lunar"]
        elif type(date).__name__ == "datetime":
            del self.__crony[name]["birthday"]["solar"]
        else:
            print("'name' or 'date' invalid, nothing changes ")

    def load(self):
        try:
            with open("data", 'rb') as fi:
                self.__crony = dill.load(fi)
        except:
            print('Do not import data file')
            self.name = ''
    def save(self):
        with open("data", "wb") as fo:
            dill.dump(self.__crony, fo)

    @staticmethod
    def delta_days(date1, date2):
        """
        return days of (date2 - date1)
        """
        if type(date1).__name__ == "LunarDate":
            date1 = date1.to_datetime()
        if type(date2).__name__ == "LunarDate":
            date2 = date2.to_datetime()
        return date2 - date1

    @staticmethod
    def parseDeltaDays(delta_days):
        """
        return list[days, hours, minutes, seconds] of a daltatime type data.
        """
        days = delta_days.days
        total_seconds = delta_days.seconds
        hours, res_hour = divmod(total_seconds, 3600)
        minutes, seconds = divmod(res_hour*3600, 60)
        return {"days":days, "hours":hours, "minutes":minutes, "seconds":seconds}



class Remind(Mycrony):
    def __init__(self):
        super().__init__(self)
        print(self.get_all_names(), '...')

    def who_will_be_remind(self, period = 7):
        res = self.get_all_valid_birthday()
        NAME = []
        Days = []

        for name, birthday in zip(*res):
            # Uniform lunar calendar
            if type(birthday).__name__ == "datetime":
                print(birthday)
                birthday = Lunar.from_datetime(birthday)
            days = birthday - Lunar.from_datetime(beijing.now)

            if bool(days <= period and days >=0):
                print(birthday, Lunar.from_datetime(beijing.now))
                NAME.append(name)
                Days.append(days)
        return NAME, Days


def parseDate(date):
    """
    Parse the date into year, month, and day
    :param date: Lunar date or Solar date
    :return: year, month, day
    """
    if type(date).__name__ == "LunarDate":
        year = date.lunar_year
        month = date.lunar_month
        day = date.lunar_day
    elif type(date).__name__ == "datetime":
        year=  date.year
        month = date.month
        day = date.day
    else:
        raise ValueError("'date' invalid!" )
    return year, month, day


def awayFromToday(specDate):
    """ return how much times is left before that special day
        :param specDate: `Lunar` or `datetime` type date.
    """
    _, specialMonth, specialDay = parseDate(specDate)

    solarNow = datetime.now()
    now_year, now_month, now_day = parseDate(solarNow)
    lunarNow = Lunar.from_datetime(solarNow)

    if type(specDate).__name__ == "LunarDate":
        """LunarDate type do not support minute and second"""
        specialDate_this_year = Lunar(now_year, specialMonth, specialDay)
        delta_days = specialDate_this_year - lunarNow
        if delta_days < 0:
            specialDate_this_year = Lunar(now_year+1, specialMonth, specialDay)
            delta_days = specialDate_this_year - lunarNow

        delta_times = timedelta(days = delta_days)
        rest = timedelta(days=1) - timedelta(hours=solarNow.hour, minutes=solarNow.minute)
        delta_times = delta_times - timedelta(days=1) + rest
        return delta_times

    elif type(specDate).__name__ == "datetime":
        specialDate_this_year = datetime(now_year, specialMonth, specialDay)
        delta_times = specialDate_this_year - solarNow
        if delta_times.days < 0:
            one_solor_year = (datetime(now_year + 1, specialMonth, specialDay) - specialDate_this_year)
            specialDate_next_year = specialDate_this_year + one_solor_year
            delta_times = specialDate_next_year - solarNow
        return delta_times
    else:
        raise ValueError("The type of 'spacialDate' should be `datetime` or `LunarDate`!")


print(awayFromToday(datetime(1993, 2, 4)))
if __name__ == "__main__":
    pass
    # from pprint import pprint;
    # person = Mycrony()
    # person.set_name('yao')
    # person.set_birthday([2020, 12, 18], "lunar")
    # person.set_birthday([2020, 1, 15], "solar")
    # person.save()
    #
    # # pprint(person.get_all_valid_birthday())
    # pprint(person.get_all_msg())
    # pprint(person.get_all_valid_birthday())

    # pprint(person.find_name_from_birthday(Lunar(2020,12,18)))
    # pprint(person.find_name_from_birthday(datetime(2020,1,10)))
    # remind_me = Remind()
    #
    # print(remind_me.who_will_be_remind())

    # person.save()




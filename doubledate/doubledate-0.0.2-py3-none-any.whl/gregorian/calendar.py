"""
Calendar object
"""
import sortedcontainers
import collections
import datetime

import gregorian.utils as utils
import gregorian.internals as internals

RAISE = object()

class Calendar(sortedcontainers.SortedSet):
    def __init__(self, dates=None, key=None):
        """
        Creates a calendar using the optional dates iterable

        Throws
        ------------
        TypeError
            if dates is not an iterable of date-like objects
        """
        if dates is None: 
            dates = []
        else: 
            dates = list(dates)
        if not all([internals.isdatelike(item) for item in dates]):
            raise TypeError("Calendar expected an iterable of date objects")
        super(Calendar, self).__init__(dates)
    
    @property
    def last(self):
        """
        Returns the last date in the calendar

        Throws
        ------------
        KeyError
            if the calendar is empty
        """
        return self[-1]

    @property
    def first(self):
        """
        Returns the first date in the calendar

        Throws
        ------------
        KeyError
            if the calendar is empty
        """
        return self[0]

    @property
    def dates(self):
        """
        Returns the dates as a list
        """
        return list(self)

    @property
    def length(self):
        """
        Returns the length of the calendar
        """
        return len(self)

    def __getitem__(self, value):
        """
        Retrieves a value at a given index
        Retrieves a calendar by a slice
        """
        if isinstance(value, int):
            return super(Calendar, self).__getitem__(value)
        elif isinstance(value, slice):
            if internals.isdatelike(value.start):
                value = slice(self.bisect_left(value.start), value.stop)
            if internals.isdatelike(value.stop):
                value = slice(value.start, self.bisect_right(value.stop))
            return Calendar(super(Calendar, self).__getitem__(value))
        raise KeyError("Invalid index or slice object")

    def __add__(self, other): 
        """
        Alias for union
        """
        if internals.isdatelike(other): 
            return Calendar(self).union(Calendar([other]))
        return Calendar(self).union(Calendar(other))

    def filter(self, func=None, *, year=None, semester=None, quarter=None, month=None, week=None, weekday=None):
        """
        Returns a new filtered calendar
        Either pass a filtering function, one or several filtering criterai

        Arguments
        ------------
        func : function, optional
            the filtering function
        year : int, optional
            pass a value to filter dates of the given year only
        semester : int, optional (1 or 2)
            pass a value to filter dates of the given semester only
        quarter : int, optional (1, 2, 3, or 4)
            pass a value to filter dates of the given quarter only
        month : int, optional (1 through 12)
            pass a value to filter dates of the given month only
        week : int, optional (1 through 53)
            pass a value to filter dates of the given week number only
        weekday : int, optional (0 through 6)
            pass a value to filter dates of the given weekday only
            Monday = 0, Tuesday = 1... Sunday = 6

        Return
        ------------
        filtered : Calendar
        """
        if func is not None:
            if not callable(func):
                raise ValueError("Filter accepts either a function, one or several named arguments")
            return Calendar([date for date in self if func(date)])
        if all([arg is None for arg in [year, semester, quarter, month, week, weekday]]):
            raise ValueError("You need to provide one of year, semester, quarter, month, week, weekday")
        dates = list(self)
        if year is not None: 
            dates = list(filter(lambda date: date.year == year, dates))
        if semester is not None: 
            dates = list(filter(lambda date: utils.semester(date) == semester, dates))
        if quarter is not None: 
            dates = list(filter(lambda date: utils.quarter(date) == quarter, dates))
        if month is not None: 
            dates = list(filter(lambda date: date.month == month, dates))
        if week is not None: 
            dates = list(filter(lambda date: date.isocalendar()[1] == week, dates))
        if weekday is not None: 
            dates = list(filter(lambda date: date.weekday() == weekday, dates))
        return Calendar(dates)

    def weekdays(self):
        """
        Filters out all the weekends
        Assumed to mean Saturdays and Sundays

        Return
        ------------
        filtered : Calendar
        """
        return self.filter(lambda date: date.weekday() not in [5, 6])

    def weekends(self):
        """
        Filters out all the weekdays

        Return
        ------------
        filtered : Calendar
        """
        return self.filter(lambda date: date.weekday() in [5, 6])

    def inverse(self, starting=None, ending=None):
        """
        Returns the negative of the calendar, using this calendar as the holiday mask

        Return
        ------------
        inversed : Calendar
        """
        if starting is None: 
            starting = self[0]
        if ending is None: 
            ending = self[-1]
        calendar = Calendar()
        for i in range(1, (ending-starting).days):
            if starting + datetime.timedelta(i) not in self:
                calendar.add(starting + datetime.timedelta(i))
        return calendar

    def dayof(self, date, frequency=None, *, base=1):
        """
        Returns the position of the date in the calendar at a given 
        frequency. By default, base is 1. 

        Return
        ------------
        position : int 
            the index + 1 of the given date in the filtered frequency
        """
        if date not in self: 
            raise ValueError(f"the given date ({date}) is not in the calendar")
        if frequency == None: 
            return self.index(date) + base
        if frequency.lower() in ["y", "year", "a"]:
            return self.filter(year=date.year).index(date) + base
        if frequency.lower() == "semester":
            return self.filter(year=date.year, semester=utils.semester(date)).index(date) + base
        if frequency.lower() == "quarter":
            return self.filter(year=date.year, quarter=utils.quarter(date)).index(date) + base
        if frequency.lower() in ["m", "month"]:
            return self.filter(year=date.year, month=date.month).index(date) + base
        if frequency.lower() in ["week", "w"]:
            return self.filter(year=date.year, week=date.isocalendar()[1]).index(date) + base
        raise ValueError("Invalid frequency")

    def daysfrom(self, start=None, *, asof=None):
        """
        Returns the number of days since the start of the given frequency
        This is exclusive of the given date (i.e. base 0)

        Return
        ------------
        days : int 
            the number of days prior to the date but in the same frequency
        """
        if asof is None: 
            raise ValueError("expected an asof date, None given")
        if asof not in self: 
            raise ValueError(f"the given as-of date ({asof}) is not in the calendar")
        if internals.isdatelike(start): 
            if start not in self: 
                raise ValueError(f"the given starting date ({start}) is not in the calendar")
            return self[start:asof].length - 1
        if start in ["ys", "year-start", "year start"]: 
            return self.dayof(asof, "year", base=0)
        if start in ["ss", "semester-start", "semester start"]: 
            return self.dayof(asof, "semester", base=0)
        if start in ["qs", "quarter-start", "quarter start"]:
            return self.dayof(asof, "quarter", base=0)
        if start in ["ms", "month-start", "month start"]: 
            return self.dayof(asof, "month", base=0)
        if start in ["ws", "week-start", "week start"]: 
            return self.dayof(asof, "week", base=0)
        raise ValueError(f"start should be a date or one of 'year-start', 'semester-start', 'quarter-start', 'month-start', or 'week-start' or any of their abbreviations (ys,ss,qs,ms,ws); {start} given")

    def daysto(self, to=None, *, asof=None):
        """
        returns the number of days left until the end of the given frequency

        Returns 
        ------------
        days : int 
            number of days in the calendar until the end of the frequency;
            exlusive of the given date
        """
        if asof is None: 
            raise ValueError("expected an asof date, None given")
        if asof not in self: 
            raise ValueError(f"the given as-of date ({asof}) is not in the calendar")
        if internals.isdatelike(to): 
            if to not in self: 
                raise ValueError(f"the given target date ({to}) is not in the calendar")
            return len(self[asof:to]) - 1
        if to.lower() in ["ye", "year-end", "year end"]:
            return len(self.filter(lambda d: d.year == asof.year and d >= asof)) - 1
        if to.lower() in ["se", "semester-end", "semester end"]: 
            return len(self.filter(lambda d: d.year == asof.year and utils.semester(d) == utils.semester(asof) and d >= asof)) - 1
        if to.lower() in ["qe", "quarter-end", "quarter end"]: 
            return len(self.filter(lambda d: d.year == asof.year and utils.quarter(d) == utils.quarter(asof) and d >= asof)) - 1
        if to.lower() in ["me", "month-end", "month end"]: 
            return len(self.filter(lambda d: d.year == asof.year and d.month == asof.month and d >= asof)) - 1
        if to.lower() in ["we", "week-end", "week end"]: 
            return len(self.filter(lambda d: d.year == asof.year and d.isocalendar()[1] == asof.isocalendar()[1] and d >= asof)) - 1
        raise ValueError(f"to should be a date or one of 'year-end', 'semester-end', 'quarter-end', 'month-end' or 'week-end' or any of their abbreviations (ye,se,qe,me,we), {to} given")
    
    def between(self, this, that, bounds="both"): 
        """
        slices (inclusive by default of the bounds) between two dates

        Arguments
        ------------
        this : date-like
            the left-bound of the calendar
        that : date-like
            the right-bound of the calenar
        bounds : str, optional
            whether to include this or that in the calendar
            one of 'both' (default), 'left' or 'right'

        Returns 
        ------------
        sliced : Calendar
            the calendar starting no earlier than this, and ending no later than that
        """
        if bounds == "both":
            return self.filter(lambda date: min(this, that) <= date <= max(this, that))
        if bounds == "left":
            return self.filter(lambda date: min(this, that) <= date < max(this, that))
        if bounds == "right":
            return self.filter(lambda date: min(this, that) < date <= max(this, that))
        raise ValueError(f"bounds should be one of 'both', 'left' or 'right', {bounds} given")

    def offset(self, date, days):
        """
        returns the date in the calendar offset by n days

        Arguments
        ------------
        date : date-like
            the reference date
        days : int
            the offset

        Returns
        ------------
        offsetted : date-like
            the date in the calendar days-away from the given date
        """
        if not date in self: 
            raise ValueError(f"{date} is not in the calendar")
        return self[self.index(date) + days]

    def groupby(self, grouper):
        """
        Returns a calendar-grouper object containing the sub-calendars
        Dates are grouped by the grouper argument
        Grouper argument can be a function or a string frequency
        If the grouper is a string, groups are created by year
        IF the grouper is a callable, the callable will receive the date and must return a hashable value

        Arguments
        ------------
        grouper : str | callable
            the criterion to group dates by
            string groupers include
                - w, week :    groupby by week number
                - m, month:    groupby by month
                - q, quarter:  groupby by quarter
                - s, semester: groupby semester
                - y, year:     groupby year
        """
        if isinstance(grouper, str):
            if grouper.lower() in ["w", "week"]:
                return self.groupby(lambda date: (date.year, date.isocalendar()[1]))
            elif grouper.lower() in ["m", "month"]:
                return self.groupby(lambda date: (date.year, date.month))
            elif grouper.lower() in ["q", "quarter"]:
                return self.groupby(lambda date: (date.year, utils.quarter(date)))
            elif grouper.lower() in ["s", "semester"]:
                return self.groupby(lambda date: (date.year, date.month > 6))
            elif grouper.lower() in ["y", "year"]:
                return self.groupby(lambda date: date.year)
            raise ValueError(f"grouper should be a callable or one of 'week', 'month', 'quarter', 'semester' or 'year'; {grouper} given")
        if callable(grouper):
            calendars = collections.defaultdict(lambda: Calendar())
            for date in self: 
                calendars[grouper(date)].add(date)
            return Grouper(calendars.values())
        raise ValueError("Expected string or function")

    def resample(self, grouper): 
        """
        alias for groupby
        """
        return self.groupby(grouper)

    def fa(self, date, default=RAISE):
        """
        Returns the first date after ("first-after", or "fa")

        Arguments
        ------------
        date : date-like
            the date from which to compute the first date strictly after in the calendar
        default : optional
            the default value if the given date is on or after the last date in the calendar
            if no default value is given, it will raise an KeyError

        Return
        ------------
        date : datetime.date
            the first date following the given date argument
        """
        if date > self[-1]:
            if default == RAISE:
                raise KeyError(f"Out-of-range error: {date} is after last date in the calendar")
            return default
        return self[self.bisect_right(date)]

    def lb(self, date, default=RAISE):
        """
        Returns the last date immediately before ("last-before", or "lb")

        Arguments
        ------------
        date : date-like
            the lookup date

        default: *, optional
            default value if the given date is strictly before the first date in the calendar

        Return
        ------------
        date : datetime.date
            the last date immediately before the given date argument
        """
        if date < self[0]: 
            if default == RAISE:
                raise KeyError(f"Out-of-range error: {date} is before the first date in the calendar")
            return default
        return self[self.bisect_left(date) - 1]

    def asof(self, date, default=RAISE):
        """
        Returns the date if the date is in the calendar, or the last date before that

        Arguments
        ------------
        date : date-like
            the lookup date

        default: *, optional
            default value if the given date is strictly before the first date in the calendar

        Return
        ------------
        date : datetime.date
            the date or its immediate precedent in the calendar 
        """
        if date in self: 
            return date
        return self.lb(date, default=default)

    def snap(self, other, fallback="drop"):
        """
        Snaps this calendar to another
        Date in both calendars are kept
        Dates in this calendar but not in other are either dropped or
        replaced with either the first previous or following date in other

        Arguments
        ------------
        other : iterable
            other calendar
        
        fallback : str, optional
            one of drop, previous (a.k.a. ffill), next (a.k.a. bfill)

        Return
        ------------
        snapped : Calendar
            the snapped calendar
        """
        if fallback not in ["drop", "previous", "ffill", "next", "bfill"]: 
            raise ValueError("fallback should be one of 'drop', 'previous' or 'next'")
        filtered, other = Calendar(), Calendar(other)
        for date in self: 
            if date in other: 
                filtered.add(date)
            else: 
                if fallback == "drop":
                    pass
                elif fallback in ["last", "previous", "ffill"]:
                    filtered.add(other.lb(date))
                elif fallback in ["next", "bfill", "following"]:
                    filtered.add(other.fa(date))
        return filtered

    def map(self, func):
        """
        Passes all the dates in the calendar to the function
        If all mapped values are date-like objects, function returns a new calendar
        Else it returns a new list

        Returns
        ------------
        mapped : Calendar | List
            the mapped values
        """ 
        if not callable(func): 
            raise ValueError("Expected func to be a callable function")
        mapped = [func(date) for date in self]
        if all([internals.isdatelike(m) for m in mapped]): 
            return Calendar(mapped)
        return mapped

    def iter(self, *fields):
        """
        Returns a generator yielding the fields for each date
        If no fields are passed, it yields (i, date)
        Available fields are: 
            - index (i) 
            - date (d)
            - previous (p) the previous date (or None)
            - next (n) the next date (or None)
            - DOW, DOM, DOQ, DOS, DOY day of frequency (weekend, month... year)
            - DWE, DME, DQE, DSE, DYE days to end of frequency
            - DWS, DMS, DQS, DSS, DYS days from frequency start
        """
        if len(fields) == 0: 
            fields = ["index", "date"]
        for i, date in enumerate(self):
            values = []
            for field in fields: 
                if field in ["i", "index"]: 
                    values.append(i)
                elif field in [0, "d", "date", "today"]: 
                    values.append(date)
                elif field in [-1, "-1", "previous", "p"]: 
                    values.append(self[i-1] if i != 0 else None)
                elif field in [+1, "+1", "next", "n"]: 
                    values.append(self[i+1] if i != (len(self)-1) else None)
                elif field.upper() in ["DOW", "DOM", "DOQ", "DOS", "DOY"]: 
                    values.append(self.dayof(date, field[-1]))
                elif field.upper() in ["DWE", "DME", "DQE", "DSE", "DYE"]: 
                    values.append(self.daysto(date, field[-2]))
                elif field.upper() in ["DWS", "DMS", "DQS", "DSS", "DYS"]:
                    values.append(self.daysfrom(date, fields[-2]))
                else: 
                    raise ValueError(f"unexpected field {field}")
            yield tuple(values)

class Grouper: 
    def __init__(self, calendars=None):
        if calendars is None: 
            self.calendars = []
        else:
            if not all([isinstance(calendar, Calendar) for calendar in calendars]): 
                raise TypeError("Expected a list of calendar objects")
            self.calendars = list(calendars)

    def first(self):
        return Calendar([calendar[0] for calendar in self.calendars])

    def last(self):
        return Calendar([calendar[-1] for calendar in self.calendars])

    def __getitem__(self, value):
        if isinstance(value, int):
            return self.calendars[value]
        if isinstance(value, slice):
            return Calendar().union(*self.calendars[value])

    def apply(self, func):
        """
        Apply a function to each sub-calendars
        and merge them back into a single calendar
        """
        if not callable(func): 
            raise ValueError("Expected func to be a callable function")
        calendar = Calendar()
        for cdr in self.calendars: 
            mapped = func(cdr)
            if isinstance(mapped, Calendar):
                calendar = calendar.union(mapped)
            else:
                if not isinstance(mapped, collections.abc.Iterable):
                    mapped = [mapped]
                calendar = calendar.union(Calendar(mapped))
        return calendar

    def __len__(self):
        return len(self.calendars)
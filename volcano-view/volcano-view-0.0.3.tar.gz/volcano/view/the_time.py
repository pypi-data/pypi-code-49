import enum
from datetime import datetime, timedelta
import calendar

# this list is always sorted from less to greater. You can use .indexOf() function to compare ivl types
IVL_LIST = 'mhDWMY'


def json_serialize_datetime(dtm: datetime) -> str:
    assert isinstance(dtm, datetime), dtm
    
    return dtm.strftime ('%Y%m%dT%H%M00.000Z')


class IvlDef:
    def __init__(self, nb, t):
        assert t in IVL_LIST, t

        self.nb = int(nb)
        self.type = t

    # !ValueError
    def parse(s) -> 'IvlDef':
        assert isinstance(s, str), s

        if len(s) < 2:
            raise ValueError('Value "{}" is not a valid interval definition'.format(s))

        n = int(s[:-1]) # int() raises ValueError

        t = s[-1]
        if not t in IVL_LIST:
            raise ValueError('Interval definition "{}" refers to unknown interval type "{}"'.format(s, t))

        return IvlDef(n, t)

    def __str__(self):
        return '{}{}'.format(self.nb, self.type)

    def normalized (self):
        return IvlDef(1, self.type)

    def get_default_sub_ivl_n(self):
        if self.nb > 1:
            return self.normalized ()
        
        if self.type == 'm':	return None
        if self.type == 'h':	return IvlDef (1, 'm')
        if self.type == 'D':	return IvlDef (1, 'h')
        if self.type == 'W':	return IvlDef (1, 'D')
        if self.type == 'M':	return IvlDef (1, 'D')
        if self.type == 'Y':	return IvlDef (1, 'M')

        assert False, self.type

    # None for months and years
    def to_timedelta_n(self):
        if self.type == 'm':	return timedelta (minutes = self.nb)
        if self.type == 'h':	return timedelta (hours = self.nb)
        if self.type == 'D':	return timedelta (days = self.nb)
        if self.type == 'W':	return timedelta (weeks = self.nb)
        if self.type == 'M':	return None
        if self.type == 'Y':	return None

        assert False, self.type


    def add_to(self, dtm, nb_times = 1):
        assert isinstance(dtm, datetime)

        if self.type in 'mhDW':
            scaled = IvlDef (self.nb * nb_times, self.type)
            assert scaled
            tm_delta = scaled.to_timedelta_n()
            
            assert tm_delta
            return dtm + tm_delta

        if self.type in 'MY':
            n = self.nb * nb_times
            if self.type == 'Y':
                n *= 12

            M = dtm.month - 1 + n
            Y = dtm.year + M // 12
            M = M % 12 + 1
            day = min( dtm.day, calendar.monthrange(Y, M)[1])
            return datetime(Y, M, day, dtm.hour, dtm.minute)

        assert False, self.type

    def subtract_from (self, dtm, nb_times = 1):
        return self.add_to (dtm, -nb_times)

    # align_dir:	
    #		forward
    #		backward
    #		test		- returns [d] itself (aligned) if align is possible, otherwise null
    def try_align (self, d, align_dir):
        assert align_dir in ('back', 'forward', 'test'), align_dir

        Y = d.year
        M = d.month
        D = d.day
        h = d.hour
        m = d.minute

        nb = self.nb

        rs = None
        if self.type == 'm':
            if nb >= 60 or (60 % nb) != 0:
                return None
            
            if align_dir == 'test':
                return d
            
            x = m - (m % nb)

            rs = datetime(Y, M, D, h, x)

        elif self.type == 'h':
            if nb >= 24 or (24 % nb) != 0:
                return None
            
            if align_dir == 'test':
                return d
            
            x = h - (h % nb)

            rs = datetime(Y, M, D, x)
        
        elif self.type == 'D':
            if nb != 1:         # двудневный интервал уже непонятно к чему приводить.. В разные месяцы он будет попадать то на четные, то на нечетные числа
                return None
            
            if align_dir == 'test':
                return d
            
            rs = datetime(Y, M, D)

        elif self.type == 'W':
            if nb != 1:
                return None
            
            if align_dir == 'test':
                return d

            rs = datetime(Y, M, D)

            dow = rs.isoweekday()   # mon = 1, sun = 7
            if dow != 1:
                nb_days_to_subtract = dow - 1
                rs = rs.replace (day = D - nb_days_to_subtract)

        elif self.type == 'M':
            if nb >= 12 or (12 % nb) != 0:
                return None
            
            if align_dir == 'test':
                return d
            
            x = M - (M % nb)

            rs = datetime(Y, x, 1)
        
        elif self.type == 'Y':
            if nb != 1:
                return None
            
            if align_dir == 'test':
                return d
            
            rs = datetime(Y, 1, 1)
        
        else:
            assert False, self.type

        if align_dir == 'forward' and rs < d:
            return self.add_to (rs)
        else:
            return rs

    # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    def get_ivl_title(self, s, e):
        ts_type = None
        ts_fmt = None

        if self.type == 'm':
            ts_type = 'end'
            ts_fmt = '%H:%M'
        elif self.type == 'h':
            ts_type = 'end'
            ts_fmt = '%H:%M'
        elif self.type == 'D':
            ts_type = 'mid'
            ts_fmt = '%d %b'
        elif self.type == 'W':
            ts_type = 'end'
            ts_fmt = '%d %b'
        elif self.type == 'M':
            ts_type = 'mid'
            ts_fmt = "%b '%y"
        elif self.type == 'Y':        
            ts_type = 'mid'
            ts_fmt = "%Y"
        else:
            assert False, self.type

        if ts_fmt=='begin': d = s
        elif ts_fmt=='end': d = e
        else:               d = e - timedelta(seconds = 1)

        return d.strftime ( ts_fmt )


IVL_1m = IvlDef (1, 'm')
IVL_1h = IvlDef (1, 'h')
IVL_1D = IvlDef (1, 'D')
IVL_1W = IvlDef (1, 'W')
IVL_1M = IvlDef (1, 'M')
IVL_1Y = IvlDef (1, 'Y')

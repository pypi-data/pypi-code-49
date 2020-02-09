#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
import formulas
import math

_wind_gust_delta = 10


def calculate_rainRate(record):
    return record['rain'] / (float(record['interval']) / 3600) if record['interval'] != 0 else None


def calculate_dewpoint(record):
    if 'outTemp' in record and 'outHumidity' in record:
        if record['units'] == 'ENGLISH':
            return formulas.dewpointF(record['outTemp'], record['outHumidity'])
        else:
            return formulas.dewpointC(record['outTemp'], record['outHumidity'])


class ScalarStats(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.min = None
        self.max = None
        self.sum = 0.0
        self.count = 0

    def add(self, val):
        if val is not None:
            self.sum += val
            self.count += 1
            self.last = val

            if self.first is None:
                self.first = val
            if self.min is None or val < self.min:
                self.min = val
            if self.max is None or val > self.max:
                self.max = val

    @property
    def delta(self):
        return self.last - self.first if (self.last is not None and self.first is not None) else None

    @property
    def avg(self):
        return self.sum / self.count if self.count > 0 else None


class VectorStats(object):

    def __init__(self):
        self.xsum = 0.0
        self.ysum = 0.0
        self.count = 0

    def add(self, magnitude, direction):
        if magnitude is not None and direction is not None:
            self.xsum += magnitude * math.cos(math.radians(90.0 - direction))
            self.ysum += magnitude * math.sin(math.radians(90.0 - direction))
            self.count += 1

    @property
    def avg(self):
        if self.count > 0 and (self.xsum != 0 or self.ysum != 0):
            direction_avg = 90.0 - math.degrees(math.atan2(self.ysum, self.xsum))
            if direction_avg < 0.0:
                direction_avg += 360.0
            return direction_avg
        else:
            return None


class Accum(dict):

    def __init__(self, interval):
        self.unit_system = None
        self.interval = interval

    def addPacket(self, packet):
        for obs_type in packet:
            func = add_record_dict.get(obs_type, Accum.add_value)
            if obs_type == 'windDir':
                func(self, obs_type, (packet['windSpeed'], packet[obs_type]))
            else:
                func(self, obs_type, packet[obs_type])

        if self['dateTime'].delta >= self.interval:
            record = self.getAccumulatedRecord()
            self.clear()
            return record

    def getAccumulatedRecord(self):
        record = {'units': self.unit_system,
                  'interval': self['dateTime'].delta}

        for obs_type in self:
            func = extract_dict.get(obs_type, Accum.avg_extract)
            record[obs_type] = func(self, obs_type)

        for obs_type in calculate_dict:
            if obs_type not in record or record[obs_type] is None:
                record[obs_type] = calculate_dict[obs_type](record)

        return record

    def sum_extract(self, obs_type):
        return self[obs_type].sum

    def max_extract(self, obs_type):
        return self[obs_type].max

    def last_extract(self, obs_type):
        return self[obs_type].last

    def avg_extract(self, obs_type):
        return self[obs_type].avg

    def init_type(self, obs_type):
        if obs_type in self:
            return
        self[obs_type] = type_dict.get(obs_type, ScalarStats)()

    def add_value(self, obs_type, val):
        self.init_type(obs_type)

        if obs_type == 'windDir':
            magnitude, direction = val
            if magnitude is None or magnitude == 0:
                magnitude = 0.1
            self[obs_type].add(magnitude, direction)
        else:
            self[obs_type].add(val)

        if obs_type == 'windSpeed' and self['windSpeed'] is not None and self['windSpeed'].max is not None and self['windSpeed'].min is not None:
            if (self['windSpeed'].max - self['windSpeed'].min) > _wind_gust_delta:
                self.init_type('windGust')
                self['windGust'].add(self['windSpeed'].max)

            if (self['windSpeed'].max > 1):
                self.init_type('windGust2')
                self['windGust2'].add(self['windSpeed'].max)

    def check_units(self, obs_type, val):
        if self.unit_system is None:
            self.unit_system = val
        else:
            if self.unit_system != val:
                raise ValueError("Unit system mismatch %d v. %d" % (self.unit_system, val))


type_dict = {'windDir': VectorStats}

add_record_dict = {'units': Accum.check_units}

calculate_dict = {'dewpoint': calculate_dewpoint,
                  'rainRate': calculate_rainRate}

extract_dict = {'rain': Accum.sum_extract,
                'ET': Accum.sum_extract,
                'dayET': Accum.last_extract,
                'monthET': Accum.last_extract,
                'yearET': Accum.last_extract,
                'hourRain': Accum.last_extract,
                'dayRain': Accum.last_extract,
                'rain24': Accum.last_extract,
                'monthRain': Accum.last_extract,
                'yearRain': Accum.last_extract,
                'windGust': Accum.max_extract,
                'windGust2': Accum.max_extract,
                'totalRain': Accum.last_extract,
                'dateTime': Accum.last_extract}

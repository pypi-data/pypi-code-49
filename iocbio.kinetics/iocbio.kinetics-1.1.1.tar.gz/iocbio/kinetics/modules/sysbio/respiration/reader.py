# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
#!/usr/bin/env python3
# Original Author: Pearu Peterson
# Adopted by Martin Laasmaa and Marko Vendelin
# Created: June 2010

import numpy, hashlib, re
from scipy.stats import linregress
from datetime import datetime
from collections import defaultdict, OrderedDict

from iocbio.kinetics.io.data import Data, Carrier
from .experiment_strathkelvin import ExperimentStrathkelvin

### Required definition for exported module ###
IocbioKineticsModule = ['args', 'reader']

### Implementaiton

"""Time units.

Provides time classes with arithmetic support to manipulate time
quantity with various units (Seconds, Minutes, and Hours).

Examples
--------

::

  >>> from iocbio.timeunit import *
  >>> Seconds(10)
  Seconds(10.0)
  >>> print Seconds(10)+Minutes(1)
  70.0sec
  >>> print Hours(1) - Minutes(20)
  0.666667h
  >>> print Hours(1) - Minutes(30)
  0.5h
  >>> print Seconds(Hours(1) - Minutes(30))
  1800.0sec

The base class, ``Time``, of ``Seconds``, ``Minutes``, and ``Hours`` classes can be used
to construct time instances from strings and to convert between different
units. For example::

  >>> Time(20, unit='min')
  Minutes(20.0)
  >>> Time('60 seconds', unit='min')
  Minutes(1.0)
  >>> Time(Hours(1), unit='min')
  Minutes(60.0)

"""


import re

__all__ = ['Time', 'Seconds', 'Minutes', 'Hours']

re_time = re.compile(r'(?P<data>[+-]?(\d+(\s*[.]\s*\d+)?|[.]\s*\d+))\s*(?P<unit>(s|sec|seconds|second|m|min|minutes|minute|h|hour|hours|))')

class Time(object):
    """ Base class to time quantity with units.

    See also
    --------
    iocbio.timeunit
    """
    def __new__(cls, data, unit=None):
        """ Construct a Time instance.

        Parameters
        ----------
        data : {float, int, long, Seconds, Minutes, Hours}
        unit : {None, 's', 'm', 'h',...}
        """
        if isinstance(data, str):
            m = re_time.match(data.lower())
            if m is None:
                raise ValueError(cls, data)
            data = float(m.group('data'))
            u = m.group('unit')
            if u:
                data = Time(data, unit = u)

        if cls is Time:
            if isinstance(data, Time) and unit is None:
                return data
            objcls = dict(s=Seconds, sec=Seconds, secs = Seconds, seconds = Seconds, second=Seconds,
                          m=Minutes, min=Minutes, minutes=Minutes, minute=Minutes,
                          h=Hours, hour = Hours, hours = Hours).get(str(unit).lower(), None)
            if objcls is None:
                raise NotImplementedError(cls, unit, data)
            if isinstance(data, Time):
                data = objcls(data).data
            if isinstance (data, (float, int)):
                obj = object.__new__ (objcls)
                obj.data = objcls.round(data)
                return obj
            raise NotImplementedError (cls, objcls, data)

        assert unit is None, unit
        if isinstance(data, Time):
            if data.__class__ is cls:
                return data # assume that Time is immutable
            else:
                to_other_name = 'to_%s' % (cls.__name__)
                to_other = getattr (data, to_other_name, None)
                if to_other_name is None:
                    raise NotImplementedError ('%s class needs %s member' % (data.__class__.__name__, to_other_name))
                data = to_other * data.data
        if isinstance (data, (float, int)):
            obj = object.__new__(cls)
            obj.data = cls.round(data)
            return obj
        raise NotImplementedError(cls, data)

    def __str__ (self):
        return '%s%s' % (self.data, self.unit_label)

    def __repr__ (self):
        return '%s(%r)' % (self.__class__.__name__, self.data)

    def __abs__ (self):
        return self.__class__(abs(self.data))

    def __pos__ (self): return self
    def __neg__ (self): return self.__class__(-self.data)

    def __add__ (self, other):
        if isinstance (other, Time):
            return self.__class__ (self.data + self.__class__(other).data)
        return NotImplemented
    __radd__ = __add__

    def __sub__ (self, other):
        return self + (-other)

    def __rsub__ (self, other):
        return other + (-self)

    def __mul__ (self, other):
        if isinstance (other, (float, int, long)):
            return self.__class__ (self.data * other)
        return NotImplemented

    __rmul__ = __mul__

    def __floordiv__(self, other):
        if isinstance (other, (float, int, long)):
            return self.__class__(self.data // other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance (other, (float, int, long)):
            return self.__class__(self.data / other)
        return NotImplemented

    __div__ = __truediv__

    def __float__(self):
        return float(self.data)

    def __int__ (self):
        return int(self.data)

    def __hash__ (self):
        return hash((self.__class__.__name__, self.data))

    def __eq__ (self, other):
        if isinstance (other, Time):
            return self.data == self.__class__(other).data
        return NotImplemented
    def __ne__ (self, other):
        if isinstance (other, Time):
            return self.data != self.__class__(other).data
        return NotImplemented
    def __lt__ (self, other):
        if isinstance (other, Time):
            return self.data < self.__class__(other).data
        return NotImplemented
    def __le__ (self, other):
        if isinstance (other, Time):
            return self.data <= self.__class__(other).data
        return NotImplemented
    def __gt__ (self, other):
        if isinstance (other, Time):
            return self.data > self.__class__(other).data
        return NotImplemented
    def __ge__ (self, other):
        if isinstance (other, Time):
            return self.data >= self.__class__(other).data
        return NotImplemented


class Seconds(Time):
    """ Time in seconds.

    See also
    --------
    iocbio.timeunit
    """

    unit_label = 'sec'
    to_Minutes = 1/60
    to_Hours = to_Minutes/60

    @classmethod
    def round(cls, data):
        return round (data, 2)


class Minutes(Time):
    """ Time in minutes.

    See also
    --------
    iocbio.timeunit
    """

    unit_label = 'min'
    to_Seconds = 60
    to_Hours = 1/60

    @classmethod
    def round(cls, data):
        return round (data, 4)


class Hours(Time):
    """ Time in hours.

    See also
    --------
    iocbio.timeunit
    """

    unit_label = 'h'
    to_Minutes = 60
    to_Seconds = to_Minutes * 60

    @classmethod
    def round(cls, data):
        return round (data, 6)


def splitline(line):
    r = line.split(None, 3)
    if len(r)==3:
        r.append ('')
    return r

def get_protocol(lines):
    protocol = None
    for line in lines:
        if line.startswith('#  protocol :'):
                protocol = line.split(':',1)[-1].strip()
    if protocol is None or protocol == "None":
        for line in lines:
            m = re.match(r"# [\w\s]*[.]float volume_ml :", line)
            # print(line, m)
            if m is not None:
                protocol = m.group()[2:-18]
                return protocol
            # if line.find("volume") > 0:
            #     aaa
    return protocol


def reader(lines):
    """ Reader of strathkelvin929 output files.

    Parameters
    ----------
    filename : str
      Path to experiment file.

    Returns
    -------
    data : dict
      Dictionary of time, oxygen, respiration_rate, and event arrays.
    info : dict
      Dictionary of experimental parameters.
    """
    start_time_format = '%y-%m-%d %H:%M'
    protocol = get_protocol(lines)
    print("Detected protocol:", protocol)
    timeunit = None
    info = {}
    keys = []
    data = defaultdict (list)
    events = {}
    datastr = ''
    for i, line in enumerate(lines):
        datastr += line + '\n'
        if line.startswith('#'):
            print(line)
            if line.startswith('# Configuration.rate_regression_points :'):
                n = int(line.split(':',1)[-1].strip())
            elif line.startswith('#  protocol :'):
                #protocol = line.split(':',1)[-1].strip()
                pass # separate protocol detector was written
            elif line.startswith('#  start time :'):
                start_time = datetime.strptime(line.split(':',1)[-1].strip(), start_time_format)
            elif line.startswith('# Configuration.oxygen_units :'):
                oxygenunit = line.split(':', 1)[-1].strip()
            elif line.startswith('# Configuration.time_units :'):
                timeunit = line.split(':', 1)[-1].strip()
            elif 'volume_ml :' in line:
                if line.startswith('# %s.' % (protocol)):
                    volume_ml = float(line.split (':',1)[-1].strip ())
                else:
                    # sometimes we have volume defined for several protocols
                    # in this case, check if volume for correct protocol has been
                    # supplied
                    check_volume = line
            if ':' in line:
                key, value = line[1:].split (':', 1)
                info[key.strip()] = value.strip()
            elif not keys:
                for i,w in enumerate(line[1:].strip().split()):
                    if i%2:
                        keys[-1] += ' ' + w.strip()
                    else:
                        keys.append (w.strip())
            else:
                index = None
                for i,w in enumerate(splitline(line[1:].strip())):
                    if i==0:
                        time = float(Seconds(Time (w, timeunit)))
                        for index, t in enumerate(data[keys[0]]):
                            if isinstance(value, float):
                                if t > value:
                                    break
                    elif i<3:
                        value = float(w)
                    else:
                        events[time] = w
                #print 'Unprocessed line: %r' % (line)
        else:
            for i,w in enumerate(splitline(line.strip())):
                if i==0:
                    value = float(Seconds(Time (w, timeunit)))
                elif i<3:
                    value = float(w)
                else:
                    value = w
                data[keys[i]].append (value)
    for k in keys[:-1]:
        data[k] = numpy.array(data[k])
    info['events'] = events
    info['protocol'] = protocol
    if 'protocol override' in info:
        override = info['protocol override']
        info['protocol'] = override
        keys = list(info.keys())
        for key in keys:
            if key.startswith(protocol + "."):
                info[override + key[len(protocol):]] = info[key]

    # check that settings are there
    data_test = Data('bogus_id', config=info)
    if ExperimentStrathkelvin.getvalue(data_test, "volume_ml") is None or ExperimentStrathkelvin.getvalue(data_test, "temperature") is None:
        print('Cannot find volume or temperature in specified settings. Maybe protocol is specified wrongly?')
        print('Current settings:\n')
        for k in info:
            print(k,info[k])
        print()
        force_crash

    return data, info, hashlib.sha256(datastr.encode('utf-8')).hexdigest()

def calc_rate(time, o2, interval=0.5):
    t = []
    vo2 = []
    o2_interp = []
    # time in minutes
    N = 3 + int(interval / max(1e-5, time[1] - time[0]))
    N2 = int(N/2)+1
    for i in range(N2, o2.size-N2):
        slope, intercept, r_value, p_value, std_err = linregress(time[i-N2:i+N2], o2[i-N2:i+N2])
        t.append(time[i])
        vo2.append(-slope)
        o2_interp.append(numpy.mean(o2[i-N2:i+N2]))
    return numpy.array(t), numpy.array(o2_interp), numpy.array(vo2)



#########################################
########## Modules API ##################
def args(parser):
    return '''Respiration
-----------
ADP titration
ATP titration
ATP_AMP_ADP
ATP_AMP_PEP_PK
ATP_glucose_ADP
ATP_glucose_PEP_PK
creatine_ATP_ADP
creatine_ATP_PEP_PK
GMPS
merviPK
Respiratory complexes
SGMP
'''

def create_data(database, experiment_id=None, args=None):
    from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric

    filename=getattr(args, "file_name", None)
    fulltxt=None
    protocol=getattr(args, "protocol", None)
    if experiment_id is not None:
        fulltxt = ExperimentStrathkelvin.get_fulltxt(database, experiment_id)

    if filename is not None:
        fulltxt = open(filename, 'r').read()
        # identify if it is strathkelvin file
        if not fulltxt.startswith('#  channel index :') or fulltxt.find('# Configuration.path_to_strathkelvin_program :') < 0:
            return None

        # seems to be strathkelvin, load it
        if protocol is not None:
            fulltxt = '# protocol override: ' + protocol + '\n' + fulltxt

    # check if we can load anything
    if fulltxt is None: return None

    lines = fulltxt.splitlines()

    d, info, expid = reader(lines)
    print("Using protocol:", info['protocol'])

    e = {}
    # make events in minutes
    eold = info['events']
    for k, v in eold.items():
        e[k / 60.0] = eold[k]
    info["events"] = e

    t = d['time [min]'] * 1.0/60

    exp_time = '20' + info['start time'].replace('-','.')

    t_vo2, o2_vo2, vo2 = calc_rate( t, d['oxygen [umol/l]'] )

    dd = [('o2', { "x": t,
                   "y": Carrier("oxygen", "umol/l",
                                d['oxygen [umol/l]']) }),
          ('vo2', { "x": t_vo2,
                    "y": Carrier("respiration rate", "umol/l/min", vo2)})]

    if info['protocol'].find('Respiratory complexes') == 0:
        dd.append( ('o2_vo2', { "x": t_vo2,
                                "y": Carrier("oxygen smooth", "umol/l", o2_vo2) }) )

    data = Data(expid,
                config=info,
                type="Strathkelvin " + info['protocol'],
                type_generic = "VO2 " + info['protocol'],
                time = exp_time,
                name = info["this file"],
                xname = "Time", xunit = "min",
                xlim = (t[0], t[-1]),
                data = OrderedDict( dd ),
    )
    data.fulltext = fulltxt

    if not ExperimentGeneric.has_record(database, data.experiment_id):
        database.set_read_only(False)
        ExperimentStrathkelvin.store(database, data)

    return data


if __name__=='__main__':
    import sys
    filename = sys.argv[1]

    data = create_data(filename)
    print(data)

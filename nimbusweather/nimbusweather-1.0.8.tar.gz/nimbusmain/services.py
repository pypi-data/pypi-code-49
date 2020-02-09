#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

"""Services specific to weather."""

import gc
import accum
from rest import *
from util import timestamp_to_string


class Service(object):
    """Abstract base class for all services."""

    def __init__(self, engine):
        self.engine = engine

    def shutDown(self):
        pass


class Sentinel(Service):

    def __init__(self, engine, config_dict):
        super(Sentinel, self).__init__(engine)
        self.start_time = time.time()
        engine.bind(nimbusmain.NEW_LOOP_PACKET, self.new_loop_packet)

    def new_loop_packet(self, event):
        if (time.time() - self.start_time) > 60:
            self.start_time = time.time()
            raise nimbusmain.BreakLoop()


class GC(Service):

    def __init__(self, engine, config_dict):
        super(GC, self).__init__(engine)
        self.gc_interval = int(config_dict.get('gc_interval', 3 * 3600))
        engine.bind(nimbusmain.NEW_LOOP_PACKET, self.new_loop_packet)
        engine.bind(nimbusmain.STARTUP, self.startup)

    def startup(self, event):
        self.last_gc = int(time.time())

    def new_loop_packet(self, event):
        if int(time.time()) - self.last_gc > self.gc_interval:
            ngc = gc.collect()
            logging.debug("GC: garbage collected %d objects" % ngc)
            self.last_gc = int(time.time())


class QC(Service):
    """Performs quality check on incoming data."""

    min_max_dict = {'barometer': [26, 32.5],
                    'outTemp': [-40, 120],
                    'inTemp': [10, 120],
                    'outHumidity': [0, 100],
                    'inHumidity': [0, 100],
                    'windSpeed': [0, 120]}

    def __init__(self, engine, config_dict):
        super(QC, self).__init__(engine)
        engine.bind(nimbusmain.NEW_LOOP_PACKET, self.new_loop_packet)

    def new_loop_packet(self, event):
        """Apply quality check to the data in a LOOP packet"""

        data_dict = to_ENGLISH(event.packet)
        for obs_type in self.min_max_dict:
            if obs_type in data_dict and data_dict[obs_type] is not None:
                if not self.min_max_dict[obs_type][0] <= data_dict[obs_type] <= self.min_max_dict[obs_type][1]:
                    logging.info("QC: %s LOOP value '%s' %s outside limits (%s, %s)" %
                                 (timestamp_to_string(data_dict['dateTime']),
                                  obs_type, data_dict[obs_type],
                                  self.min_max_dict[obs_type][0], self.min_max_dict[obs_type][1]))
                    event.packet[obs_type] = None


class TimeSync(Service):
    """Regularly asks the station to synch up its clock."""

    def __init__(self, engine, config_dict):
        super(TimeSync, self).__init__(engine)

        # Zero out the time of last synch, and get the time between synchs.
        self.last_synch_ts = 0
        self.clock_check = int(config_dict.get('clock_check', 14400))
        self.max_drift = int(config_dict.get('max_drift', 5))

        engine.bind(nimbusmain.STARTUP, self.startup)
        engine.bind(nimbusmain.PRE_LOOP, self.pre_loop)

    def startup(self, event):
        """Called when the engine is starting up."""
        self._do_sync()

    def pre_loop(self, event):
        """Called before the main event loop is started."""
        self._do_sync()

    def _do_sync(self):
        """Ask the station to synch up if enough time has passed."""

        now_ts = time.time()
        if now_ts - self.last_synch_ts >= self.clock_check:
            self.last_synch_ts = now_ts
            try:
                console_time = self.engine.console.getTime()
                if console_time is None:
                    return
                diff = console_time - time.time()
                logging.debug("engine: Clock error is %.2f seconds (positive is fast)" % diff)
                if abs(diff) > self.max_drift:
                    try:
                        self.engine.console.setTime()
                    except NotImplementedError:
                        logging.debug("engine: Station does not support setting the time")
            except NotImplementedError:
                logging.debug("engine: Station does not support reading the time")


class Print(Service):
    """Service that prints diagnostic information when a LOOP
    or archive packet is received."""

    def __init__(self, engine, config_dict):
        super(Print, self).__init__(engine)

        engine.bind(nimbusmain.NEW_LOOP_PACKET, self.new_loop_packet)

    def new_loop_packet(self, event):
        """Print out the new LOOP packet"""
        logging.debug("Received a loop packt: %s" % event.packet)

    @staticmethod
    def sort(rec):
        return ", ".join(["%s: %s" % (k, rec.get(k)) for k in sorted(rec, key=str.lower)])


class RESTful(Service):
    """Abstract base class for RESTful nimbusmain services.
    Offers a few common bits of functionality."""

    def __init__(self, engine, interval):
        super(RESTful, self).__init__(engine)
        self.accumulator = accum.Accum(interval)
        engine.bind(nimbusmain.NEW_LOOP_PACKET, self.new_loop_packet)

    def new_loop_packet(self, event):
        accumulated_record = self.accumulator.addPacket(event.packet)
        if accumulated_record is not None and hasattr(self, 'archive_thread'):
            self.archive_thread.queue.put(accumulated_record)

    def shutDown(self):
        if hasattr(self, 'archive_thread'):
            RESTful.shutDown_thread(self.archive_thread)

    @staticmethod
    def shutDown_thread(t):
        """Function to shut down a thread."""
        if t.isAlive():
            # Put a None in the queue to signal the thread to shutdown
            t.queue.put(None)
            # Wait up to 20 seconds for the thread to exit:
            t.join(20.0)
            if t.isAlive():
                logging.error("restx: Unable to shut down %s thread" % t.name)
            else:
                logging.error("restx: Shut down %s thread." % t.name)


class Nimbus(RESTful):
    """Post to nimbus server
    """

    def __init__(self, engine, config_dict):

        super(Nimbus, self).__init__(engine, int(config_dict.get('Nimbus', {}).get('interval', 5)))

        _dict = dict()

        try:
            _dict['location_id'] = config_dict['Nimbus']['location_id']
            _dict['structures'] = config_dict['Nimbus']['structures']
            _dict['device_id'] = config_dict['Nimbus']['device_id']
            _dict['token'] = config_dict['Nimbus']['token']
        except KeyError:
            return

        self.archive_thread = NimbusThread(protocol_name="Nimbus-PWS", **_dict)
        self.archive_thread.start()
        logging.info("restx: Nimbus-PWS: Data for location %s will be posted" % _dict['location_id'])


class NimbusWind(RESTful):
    """Post to nimbus server
    """

    def __init__(self, engine, config_dict):

        super(NimbusWind, self).__init__(engine, int(config_dict.get('Nimbus', {}).get('interval', 330)))

        _dict = dict()

        try:
            _dict['location'] = config_dict['Nimbus']['location']
            _dict['structures'] = config_dict['Nimbus']['structures']
            _dict['device'] = config_dict['Nimbus']['device']
            _dict['token'] = config_dict['Nimbus']['token']
        except KeyError:
            return

        self.archive_thread = NimbusWindThread(protocol_name="NimbusWind-PWS", **_dict)
        self.archive_thread.start()
        logging.info("restx: NimbusWind-PWS: Data for location %s will be posted" % _dict['location'])


class Wunderground(RESTful):
    """Specialized version of the Ambient protocol for the Weather Underground.
    """

    archive_url = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php"

    def __init__(self, engine, config_dict):

        super(Wunderground, self).__init__(engine, int(config_dict.get('Wunderground', {}).get('interval', 330)))

        _dict = dict()

        try:
            _dict['station'] = config_dict['Wunderground']['station']
            _dict['password'] = config_dict['Wunderground']['password']
            _dict['server_url'] = Wunderground.archive_url
        except KeyError:
            return

        self.archive_thread = AmbientThread(protocol_name="Wunderground-PWS", **_dict)
        self.archive_thread.start()
        logging.info("restx: Wunderground-PWS: Data for station %s will be posted" % _dict['station'])


class PWSWeather(RESTful):
    """Specialized version of the Ambient protocol for PWSWeather"""

    archive_url = "http://www.pwsweather.com/pwsupdate/pwsupdate.php"

    def __init__(self, engine, config_dict):

        super(PWSWeather, self).__init__(engine, int(config_dict.get('PWSweather', {}).get('interval', 60)))

        _dict = dict()

        try:
            _dict['station'] = config_dict['PWSweather']['station']
            _dict['password'] = config_dict['PWSweather']['password']
            _dict['server_url'] = PWSWeather.archive_url
        except KeyError:
            return

        self.archive_thread = AmbientThread(protocol_name="PWSWeather", **_dict)
        self.archive_thread.start()
        logging.info("restx: PWSWeather: Data for station %s will be posted" % _dict['station'])


class CWOP(RESTful):
    """Weewx service for posting using the CWOP protocol.

    Manages a separate thread CWOPThread"""

    valid_prefix_re = re.compile('[C-Z]W+[0-9]+')

    def __init__(self, engine, config_dict):

        super(CWOP, self).__init__(engine, int(config_dict.get('CWOP', {}).get('interval', 60)))

        _dict = dict()

        try:
            _dict['station'] = config_dict['CWOP']['station'].upper()
            if re.match(CWOP.valid_prefix_re, _dict['station']):
                _dict['passcode'] = -1
            else:
                _dict['passcode'] = config_dict['CWOP']['passcode']
        except KeyError:
            return

        _dict.setdefault('latitude', config_dict['Station']['latitude'])
        _dict.setdefault('longitude', config_dict['Station']['longitude'])
        _dict.setdefault('station_type', config_dict['Station'].get('station_type', 'Unknown'))
        self.archive_thread = CWOPThread(**_dict)
        self.archive_thread.start()
        logging.info("restx: CWOP: Data for station %s will be posted" % _dict['station'])

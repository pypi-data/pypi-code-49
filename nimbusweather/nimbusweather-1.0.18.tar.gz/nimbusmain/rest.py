# -*- coding: utf-8 -*-
#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
from __future__ import with_statement

import Queue
import datetime
import hashlib
import logging
import re
import socket
import threading
import time
import urllib
import urllib2
import nimbusmain
from units import to_ENGLISH, to_METRIC, convert
from util import timestamp_to_string, latlon_string
import requests


class FailedPost(IOError):
    pass


class BadLogin(Exception):
    pass


class ConnectError(IOError):
    pass


class SendError(IOError):
    pass


class RESTThread(threading.Thread):
    max_tries = 10
    retry_wait = 5
    max_backlog = 1000
    timeout = 10

    def __init__(self, protocol_name, post_interval=None):
        threading.Thread.__init__(self, name=protocol_name)
        self.setDaemon(True)
        self.queue = Queue.Queue(self.max_backlog)
        self.protocol_name = protocol_name
        self.post_interval = post_interval
        self.last_post = 0

    def run(self):
        while True:
            record = self.queue.get()

            if record is None:
                return

            if self.skip_this_post(record['dateTime']):
                continue

            try:
                self.process_record(record)
            except BadLogin:
                logging.error("restx: %s: bad login; waiting 60 minutes then retrying" % self.protocol_name)
                time.sleep(3600)
            except FailedPost as e:
                time_str = timestamp_to_string(record['dateTime'])
                logging.error("restx: %s: Failed to publish record %s: %s" % (self.protocol_name, time_str, e))
            except Exception as e:
                logging.critical("restx: %s: Unexpected exception of type %s: %s" % (self.protocol_name, type(e), e))

    def skip_this_post(self, time_ts):
        if self.post_interval is not None:
            how_long = time_ts - self.last_post
            if how_long < self.post_interval:
                logging.debug("restx: %s: wait interval (%d < %d) has not passed for record %s" %
                              (self.protocol_name,
                               how_long, self.post_interval,
                               timestamp_to_string(time_ts)))
                return True

        self.last_post = time_ts
        return False


class NimbusThread(RESTThread):

    def __init__(self, device_id, location_id, structures, token, protocol_name="Nimbus", post_interval=None):
        super(NimbusThread, self).__init__(protocol_name=protocol_name, post_interval=post_interval)
        self.token = token
        self.device_id = device_id
        self.location_id = location_id
        self.structures = structures
        self.url_template = "https://api-edge.nimbusweather.org/v2/data/location/%s/structure/%s/measurements?device_id=%s"

    _indoorKeyMap = {
        'dateTime': 'time',
        'inTemp': 'temperature',
        'inHumidity': 'humidity'
    }

    _outdoorKeyMap = {
        'dateTime': 'time',
        'barometer': 'pressure',
        'outTemp': 'temperature',
        'outHumidity': 'humidity',
        'windSpeed': 'wind_speed',
        'windGust2': 'wind_gust_speed',
        'dewpoint': 'dewpoint',
        'rainRate': 'rain_rate',
        'sunrise': 'sunrise',
        'sunset': 'sunset',
        'radiation': 'radiation',
        'consBatteryVoltage': 'voltage',
        'dayRain': 'day_rain'
    }

    _greenhouseKeyMap = {
        'dateTime': 'time',
        'extraTemp1': 'temperature'
    }

    def process_record(self, record):

        headers = {'x-api-key': '%s' % self.token}

        for key in self.structures:
            logging.info("Structure key: %s" % key)
            for count in range(self.max_tries):
                try:
                    params = self.get_params(record, self.structures[key]['params'])
                    logging.info("Structure: %s" % self.structures[key])
                    url = self.url_template % (self.location_id, self.structures[key]['id'], self.device_id)
                    logging.info(url)
                    response = requests.post(url, headers=headers, json=params, timeout=self.timeout)
                    if response.status_code == 200:
                        break
                    else:
                        logging.error("restx: %s: Failed %s upload attempt %d: Code %s: %s" % (self.protocol_name, key, count + 1, response.status_code, response.text))

                except Exception as e:
                    logging.error("restx: %s: Failed upload attempt %d: Exception %s" % (self.protocol_name, count + 1, e))

                time.sleep(self.retry_wait)
            else:
                raise FailedPost("Failed upload after %d tries" % (self.max_tries,))

    def get_params(self, record, keyMap):

        params = {}

        for key in record:
            value = record.get(key)
            if value is not None and keyMap.get(key) is not None:
                if key == 'dateTime':
                    value = value * 1000
                params[keyMap[key]] = value

        return params


class NimbusWindThread(RESTThread):

    def __init__(self, device, location, structure, token, protocol_name="Nimbus", post_interval=None):
        super(NimbusWindThread, self).__init__(protocol_name=protocol_name, post_interval=post_interval)
        self.token = token
        self.server_url = "https://api-edge.nimbusweather.org/v2/data/location/%s/structure/%s/measurements?device_id=%s" % (location, structure, device)

    _keyMap = {
        'dateTime': 'time',
        'windDir': 'wind_dir'
    }

    def process_record(self, record):

        params = self.get_params(to_ENGLISH(record))
        headers = {'x-api-key': '%s' % self.token}
        logging.info(params)
        logging.info(self.server_url)

        for count in range(self.max_tries):
            try:
                response = requests.post(self.server_url, headers=headers, json=params, timeout=self.timeout)
                if 200 <= response.status_code <= 299:
                    self.check_response(response)
                    return
                else:
                    logging.error("restx: %s: Failed upload attempt %d: Code %s: %s" % (self.protocol_name, count + 1, response.status_code, response.text))
            except Exception as e:
                logging.error("restx: %s: Failed upload attempt %d: Exception %s" % (self.protocol_name, count + 1, e))

            time.sleep(self.retry_wait)
        else:
            raise FailedPost("Failed upload after %d tries" % (self.max_tries,))

    def get_params(self, record):

        params = {}

        for key in record:
            value = record.get(key)
            if value is not None and self._keyMap.get(key) is not None:
                if key == 'windGust':
                    logging.error("TRYING TO POST WIND GUST")
                if key == 'dateTime':
                    value = value * 1000
                params[self._keyMap[key]] = value

        return params

    def check_response(self, response):
        for line in response:
            if not line.startswith('Success'):
                logging.debug("received an invalid response: %s" % line)


class AmbientThread(RESTThread):

    def __init__(self, station, password, server_url, protocol_name="Unknown-Ambient", post_interval=None):
        super(AmbientThread, self).__init__(protocol_name=protocol_name, post_interval=post_interval)
        self.station = station
        self.password = password
        self.server_url = server_url

    _keyMap = {'dateTime': 'dateutc',
               'barometer': 'baromin',
               'outTemp': 'tempf',
               'outHumidity': 'humidity',
               'windSpeed': 'windspeedmph',
               'windDir': 'winddir',
               'windGust': 'windgustmph',
               'dewpoint': 'dewptf',
               'rainRate': 'rainin',
               'dayRain': 'dailyrainin',
               'radiation': 'solarradiation',
               'UV': 'UV',
               'soilTemp1': "soiltempf",
               'soilTemp2': "soiltemp2f",
               'soilTemp3': "soiltemp3f",
               'soilTemp4': "soiltemp4f",
               'soilMoist1': "soilmoisture",
               'soilMoist2': "soilmoisture2",
               'soilMoist3': "soilmoisture3",
               'soilMoist4': "soilmoisture4",
               'leafWet1': "leafwetness",
               'leafWet2': "leafwetness2",
               'realtime': 'realtime',
               'rtfreq': 'rtfreq'}

    def process_record(self, record):

        params = self.get_params(to_ENGLISH(record))

        for count in range(self.max_tries):
            try:
                response = requests.get(self.server_url, params=params, timeout=self.timeout)
                if 200 <= response.status_code <= 299:
                    self.check_response(response)
                    return
                else:
                    logging.error("restx: %s: Failed upload attempt %d: Code %s" % (self.protocol_name, count + 1, response.code))
            except Exception as e:
                logging.error("restx: %s: Failed upload attempt %d: Exception %s" % (self.protocol_name, count + 1, e))

            time.sleep(self.retry_wait)
        else:
            raise FailedPost("Failed upload after %d tries" % (self.max_tries,))

    def get_params(self, record):

        params = {
            "action": "updateraw",
            "ID": self.station,
            "PASSWORD": self.password,
            "softwaretype": "nimbus"
        }

        for key in record:
            value = record.get(key)
            if value is not None and self._keyMap.get(key) is not None:
                if key == 'dateTime':
                    value = str(datetime.datetime.utcfromtimestamp(value))
                params[self._keyMap[key]] = value

        return params

    def check_response(self, response):
        for line in response:
            if not line.startswith('success'):
                logging.debug("received an invalid response: %s" % line)
            if line.startswith('ERROR') or line.startswith('INVALID'):
                raise BadLogin(line)


class CWOPThread(RESTThread):

    default_servers = ['cwop.aprs.net:14580', 'cwop.aprs.net:23']

    def __init__(self,
                 station, passcode, latitude, longitude, station_type,
                 server_list=default_servers, post_interval=600):

        super(CWOPThread, self).__init__(protocol_name="CWOP",
                                         post_interval=post_interval)
        self.station = station
        self.passcode = passcode
        self.server_list = server_list
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.station_type = station_type

    def process_record(self, record):
        us_record = to_ENGLISH(record)
        login = self.get_login_string()
        tnc_packet = self.get_tnc_packet(us_record)
        self.send_packet(login, tnc_packet)

    def get_login_string(self):
        login = "user %s pass %s vers nimbus\r\n" % (self.station, self.passcode)
        return login

    def get_tnc_packet(self, record):
        """Form the TNC2 packet used by CWOP."""

        # Preamble to the TNC packet:
        _prefix = "%s>APRS,TCPIP*:" % (self.station,)

        # Time:
        _time_tt = time.gmtime(record['dateTime'])
        _time_str = time.strftime("@%d%H%Mz", _time_tt)

        # Position:
        _lat_str = latlon_string(self.latitude,
                                 ('N', 'S'), 'lat')
        _lon_str = latlon_string(self.longitude,
                                 ('E', 'W'), 'lon')
        _latlon_str = '%s%s%s/%s%s%s' % (_lat_str + _lon_str)

        # Wind and temperature
        _wt_list = []
        for _obs_type in ['windDir', 'windSpeed', 'windGust', 'outTemp']:
            _v = record.get(_obs_type)
            _wt_list.append("%03d" % _v if _v is not None else '...')
        _wt_str = "_%s/%sg%st%s" % tuple(_wt_list)

        # Rain
        _rain_list = []
        for _obs_type in ['hourRain', 'rain24', 'dayRain']:
            _v = record.get(_obs_type)
            _rain_list.append("%03d" % (_v * 100.0) if _v is not None else '...')
        _rain_str = "r%sp%sP%s" % tuple(_rain_list)

        # Barometer:
        _baro = record.get('altimeter')
        if _baro is None:
            _baro_str = "b....."
        else:
            # While everything else in the CWOP protocol is in US Customary,
            # they want the barometer in millibars.
            _new_baro = convert(_baro, 'inHg', 'mbar')
            _baro_str = "b%05d" % (_new_baro * 10.0)

        # Humidity:
        _humidity = record.get('outHumidity')
        if _humidity is None:
            _humid_str = "h.."
        else:
            _humid_str = ("h%02d" % _humidity) if _humidity < 100.0 else "h00"

        # Radiation:
        _radiation = record.get('radiation')
        if _radiation is None:
            _radiation_str = ""
        elif _radiation < 1000.0:
            _radiation_str = "L%03d" % _radiation
        elif _radiation < 2000.0:
            _radiation_str = "l%03d" % (_radiation - 1000)
        else:
            _radiation_str = ""

        # Station equipment
        _equipment_str = ".nimbus-%s" % self.station_type

        _tnc_packet = ''.join([_prefix, _time_str, _latlon_str, _wt_str,
                               _rain_str, _baro_str, _humid_str,
                               _radiation_str, _equipment_str, "\r\n"])

        return _tnc_packet

    def send_packet(self, login, tnc_packet):

        # Go through the list of known server:ports, looking for
        # a connection that works:
        for _serv_addr_str in self.server_list:

            try:
                _server, _port_str = _serv_addr_str.split(":")
                _port = int(_port_str)
            except ValueError:
                logging.critical("restx: Bad CWOP server address: '%s'; ignoring..." % _serv_addr_str)
                continue

            # Try each combination up to max_tries times:
            for _count in range(self.max_tries):
                try:
                    # Get a socket connection:
                    _sock = self._get_connect(_server, _port)
                    logging.debug("restx: %s: Connected to server %s:%d" %
                                  (self.protocol_name, _server, _port))

                    try:
                        # Send the login ...
                        self._send(_sock, login, 'login')
                        # ... and then the packet
                        self._send(_sock, tnc_packet, 'packet')
                        logging.debug("restx: %s: APRS Packet: %s" % (self.protocol_name, tnc_packet))
                        return

                    finally:
                        _sock.close()
                except ConnectError as e:
                    logging.debug("restx: %s: Attempt #%d to %s:%d. Connection error: %s" %
                                  (self.protocol_name, _count + 1, _server, _port, e))
                except SendError as e:
                    logging.debug("restx: %s: Attempt #%d to %s:%d. Socket send error: %s" %
                                  (self.protocol_name, _count + 1, _server, _port, e))

        # If we get here, the loop terminated normally, meaning we failed all tries
        raise FailedPost("Tried %d servers %d times each" % (len(self.server_list), self.max_tries))

    def _get_connect(self, server, port):
        """Get a socket connection to a specific server and port."""

        try:
            _sock = socket.socket()
            _sock.connect((server, port))
        except IOError as e:
            # Unsuccessful. Close it in case it was open:
            try:
                _sock.close()
            except BaseException:
                pass
            raise ConnectError(e)

        return _sock

    def _send(self, sock, msg, dbg_msg):
        """Send a message to a specific socket."""

        try:
            sock.send(msg)
        except IOError as e:
            # Unsuccessful. Log it and go around again for another try
            raise SendError("Packet %s; Error %s" % (dbg_msg, e))
        else:
            # Success. Look for response from the server.
            try:
                _resp = sock.recv(1024)
                return _resp
            except IOError as e:
                logging.debug("restx: %s: Exception %s (%s) when looking for response to %s packet" %
                              (self.protocol_name, type(e), e, dbg_msg))
                return

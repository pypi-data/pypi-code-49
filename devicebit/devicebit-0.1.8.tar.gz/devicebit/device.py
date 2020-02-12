#!/usr/bin/env python3
# -*- coding: utf-8 -*
import json
from collections import namedtuple
import requests

import aiohttp
import voluptuous as vol
import logging
_LOGGER = logging.getLogger(__name__)

class DevicebitError(Exception):
    """Indicates error communicating with Devicebit"""


class DiscoveryError(Exception):
    """Raised when unable to discover Devicebit"""


DevicebitResponse = namedtuple('DevicebitResponse',
                              'data, serial_number, server, mac')
                              

class Devicebit:
    """Base wrapper around Devicebit HTTP API"""
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.serial_number = ""
        self.server = ""
        self.mac = ""

    async def get_data(self):
        try:
            data = await self.make_request(
                self.host, self.port
            )
            self.serial_number = data.serial_number
            self.mac = data.mac
            self.server = data.server
        except aiohttp.ClientError as ex:
            msg = "Could not connect to Devicebit endpoint"
            raise DevicebitError(msg) from ex
        except ValueError as ex:
            msg = "Received non-JSON data from Devicebit endpoint"
            raise DevicebitError(msg) from ex
        except vol.Invalid as ex:
            msg = "Received malformed JSON from Devicebit"
            raise DevicebitError(msg) from ex
        except:
        	msg = "error"
        	raise DevicebitError("error")
        return data

    @classmethod
    async def make_request(cls, host, port):
        """
        Return instance of 'DevicebitResponse'
        Raise exception if unable to get data
        """
        raise NotImplementedError()

    @classmethod
    def sensor_map(cls):
        """
        Return sensor map
        """
        raise NotImplementedError()

async def fetch(url):
    async with aiohttp.request("GET",url) as r:
        #_LOGGER.error(r.status)
        reponse = await r.text(encoding="utf-8")
        #yield reponse
        
async def discover(host, port) -> Devicebit:
    base = 'http://admin:admin@{}:{}/monitorjson'
    url = base.format(host, port)
    _LOGGER.error(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #_LOGGER.error(resp.status)
            txt_data = await resp.text()
            json_data = json.loads(txt_data)
            #_LOGGER.error(json_data)
            #json_response = json.loads(json_data)
            server = json_data.get('server')
            if server :
                if server == "HT":
                    return WTH3080(host,port)
                if server == "PM":
                    return YNM3000(host,port)
    raise DiscoveryError()
    

class WTH3080(Devicebit):
    __schema = vol.Schema({
    	vol.Required('SN'): str,
    	vol.Required('mac'): str,
    	vol.Required('server'): str,
    	vol.Required('Data'): list,
    }, extra=vol.REMOVE_EXTRA)
	#Voltage,Current,Power,ImportEnergy,ExportGrid,frequency,PF
    __sensor_map = {
        'Temperature':              (0, 0, '°C'),
        'Humidity':                 (0, 1, '%'),

    }
    
    @staticmethod
    def map_response(resp_data, sensor_map):
        return {
            f"{sensor_name}": resp_data[j]
            for sensor_name, (i, j, _)
            in sensor_map.items()
        }

    @classmethod
    async def make_request(cls, host, port=80):
        base = 'http://admin:admin@{}:{}/monitorjson'
        url = base.format(host, port)
        #_LOGGER.error(url)
        #resp = requests.get(url)
        #json_response = resp.json()
        #_LOGGER.error(json_response)
        #response = cls.__schema(json_response)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as req:
                garbage = await req.read()
        formatted = garbage.decode("utf-8")
        json_response = json.loads(formatted)
        response = cls.__schema(json_response)
        #_LOGGER.error(cls.map_response(response['Data'], cls.__sensor_map))
        cls.dev_type = "WTH3080"
        return DevicebitResponse(
            data=cls.map_response(response['Data'], cls.__sensor_map),
            serial_number=response['SN'],
            server=response['server'],
            mac=response['mac']
        )

    @classmethod
    def sensor_map(cls):
        """
        Return sensor map
        """
        return cls.__sensor_map



class YNM3000(Devicebit):
    __schema = vol.Schema({
    	vol.Required('SN'): str,
    	vol.Required('mac'): str,
    	vol.Required('server'): str,
    	vol.Required('Data'): list,
    }, extra=vol.REMOVE_EXTRA)
	#Voltage,Current,Power,ImportEnergy,ExportGrid,frequency,PF
    __sensor_map = {
        'Temperature':              (0, 0, '°C'),
        'Humidity':                 (0, 1, '%'),
        'PM25':                     (0, 2, 'ug/m3'),
        'AQI':                      (0, 3, ''),
        'HCHO':                     (0, 4, 'mg/m3'),
        'CO2':                      (0, 5, 'ppm'),
    }
    
    @staticmethod
    def map_response(resp_data, sensor_map):
        return {
            f"{sensor_name}": resp_data[j]
            for sensor_name, (i, j, _)
            in sensor_map.items()
        }

    @classmethod
    async def make_request(cls, host, port=80):
        base = 'http://admin:admin@{}:{}/monitorjson'
        url = base.format(host, port)
        #_LOGGER.error(url)
        #resp = requests.get(url)
        #json_response = resp.json()
        #response = cls.__schema(json_response)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as req:
                garbage = await req.read()
        formatted = garbage.decode("utf-8")
        json_response = json.loads(formatted)
        response = cls.__schema(json_response)
        #_LOGGER.error(response)
        #_LOGGER.error(cls.map_response(response['Datas'], cls.__sensor_map))
        cls.dev_type = "YNM3000"
        return DevicebitResponse(
            data=cls.map_response(response['Data'], cls.__sensor_map),
            serial_number=response['SN'],
            server = response['server'],
            mac=response['mac']
        )

    @classmethod
    def sensor_map(cls):
        """
        Return sensor map
        """
        return cls.__sensor_map


# registry of Devicebits
REGISTRY = [WTH3080,YNM3000]
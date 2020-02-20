#!/usr/bin/env python3


from datetime import datetime
from raodata.File import File
from raodata import exceptions
import logging
import zeep
from zeep import Client
import requests


class Data():
    '''This class is used to retrieve RAO archive meta data'''

    SERVICE_URL = "data.rao.istp.ac.ru/Access.wsdl"

    def get_instruments(self):
        """Retruns list of available instruments"""
        client = self._connect()
        try:
            while True:
                try:
                    instruments = client.service.instrumentsList()
                    break
                except zeep.exceptions.TransportError as error:
                    if error.status_code == 504:
                        pass
                    else:
                        raise Exception(error.message)
        except zeep.exceptions.Fault as error:
            raise Exception(error.message)

        return instruments

    def get_file_types(self, instrument):
        """Retruns list of file types for a particular instrument"""
        client = self._connect()
        try:
            while True:
                try:
                    types = client.service.instrumentFileTypes(instrument)
                    break
                except zeep.exceptions.TransportError as error:
                    if error.status_code == 504:
                        pass
                    else:
                        raise Exception(error.message)
        except zeep.exceptions.Fault as error:
            raise Exception(error.message)

        return types

    def get_types_by_instruments(self):
        """Retruns list of instruments with relevant file types"""
        client = self._connect()
        try:
            while True:
                try:
                    types = client.service.typesByInstrumentsList()
                    break
                except zeep.exceptions.TransportError as error:
                    if error.status_code == 504:
                        pass
                    else:
                        raise Exception(error.message)
        except zeep.exceptions.Fault as error:
            raise Exception(error.message)

        return types

    def get_files(self, instrument, filetype, timefrom, timeto):
        """Retruns list of files for a period"""
        if not isinstance(instrument, str):
            raise exceptions.InstrumentNotString(
                  "instrument should be of a type string")

        if not isinstance(filetype, str):
            raise exceptions.FiletypeNotString(
                  "filetype should be a string")

        if not isinstance(timefrom, datetime):
            raise exceptions.InvalidTime(
                  "timefrom should be datetime.datetime object")

        if not isinstance(timeto, datetime):
            raise exceptions.InvalidTime(
                  "timeto should be datetime.datetime object")

        timefrom = datetime.strftime(timefrom, "%Y-%m-%dT%H:%M:%S")
        timeto = datetime.strftime(timeto, "%Y-%m-%dT%H:%M:%S")

        client = self._connect()

        try:
            while True:
                try:
                    files = client.service.getFiles(instrument, filetype,
                                                    timefrom, timeto)
                    break
                except zeep.exceptions.TransportError as error:
                    if error.status_code == 504:
                        pass
                    else:
                        raise Exception(error.message)
        except zeep.exceptions.Fault as error:
            if error.code == "INVALIDINSTRUMENTORTYPE":
                raise exceptions.InvalidInstrumentOrType(
                      "Invalid instrument or file type")
            elif error.code == "INVALIDTIME":
                raise exceptions.InvalidTime(
                      "Time should be in ISO 8601 format: '%Y-%m-%dT%H:%M:%S'")
            else:
                raise Exception(error.message)

        if not files:
            raise exceptions.NoDataForThePeriod(
                  "No available data for the period")

        for _f in files:
            file = File(_f.filename, _f.URL, _f.hash, _f.date)
            yield file

    def _connect(self):
        """Connection to the RAO data access web service"""
        protocol = "http://"
        logging.getLogger("zeep").setLevel("ERROR")
        try:
            request = requests.get(protocol + self.SERVICE_URL,
                                   allow_redirects=False)
            if request.status_code == 301:
                protocol = "https://"
            while True:
                try:
                    client = Client(protocol + self.SERVICE_URL)
                    break
                except requests.exceptions.HTTPError as error:
                    if error.response.status_code == 504:
                        pass
                    else:
                        raise exceptions.CannotConnect(
                                        "Cannot connect to the web service")
        except requests.exceptions.RequestException:
            raise exceptions.CannotConnect("Cannot connect to the web service")

        return client

    def _request(self, client, request, *argv):
        """Get response from SOAP server"""
        result = client.service.request(*argv)
        print(result)

        return result

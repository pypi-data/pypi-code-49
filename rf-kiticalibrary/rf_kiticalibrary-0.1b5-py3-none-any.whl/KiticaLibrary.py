# -*- coding: utf-8 -*-

# Copyright (C) 2019 Spiralworks Technologies Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#  _     _       _             _  _ _
# | |   (_)  _  (_)           | |(_) |
# | |  _ _ _| |_ _  ____ _____| | _| |__   ____ _____  ____ _   _
# | |_/ ) (_   _) |/ ___|____ | || |  _ \ / ___|____ |/ ___) | | |
# |  _ (| | | |_| ( (___/ ___ | || | |_) ) |   / ___ | |   | |_| |
# |_| \_)_|  \__)_|\____)_____|\_)_|____/|_|   \_____|_|    \__  |
#                                                          (____/
# kitica DevicePool API
# Created by    : Joshua Kim Rivera
# Date          : February 4 2020 14:55 UTC-8
# Company       : Spiralworks Technologies Inc.
#
import re
import requests
import logging
import json
import socket
from os import environ

from KiticaLibrary.version import VERSION

from robotlibcore import (HybridCore,
                          keyword)

__version__ = VERSION

LOGGER = logging.getLogger(__name__)


class KiticaLibrary(HybridCore):
    """
    A test library providing device pool support for testing.

        ``KiticaLibrary`` is a Robot Framework third party library that \
            enables test to borrow available user from a device pool. These \
                allows test to run in CI server without user conflict and \
                    lessen setup and maintenance on a project.

        - borrowing an available user from the user pool and returning it.
        - retrieving a user from the user pool by user id
        - updating user password

        == Table of contents ==

        - `Usage`
        - `Borrowed Device Object`
        - `Author`
        - `Importing`
        - `Shortcuts`
        - `Keywords`

    = Usage =

    == Adding this Library to your Test Suite ==

    | =Settings= | =Value=         | =Parameter=                        |
    | Library    | KiticaLibrary   | base_url                           |

    You can import this library in your robot test suite by using the       \
        syntax below.
    For the parameters on import. Read `Importing`.

    *Example:*
    | =Settings= | =Value=         | =Parameter=                        |
    | Library    | UserpoolLibrary | http://kitica.dev                  |


    = Borrowed Device Object =

    Both `Borrow Android Device` and `Borrow iOS Device` returns a json \
        object containing the following information:
    | =Attribute=           | =Type=    | =Description=                 |
    | deviceId              | int       | Unique Device ID              |
    | deviceName            | string    | The device's name             |
    | platformName          | string    | Device's platform             |
    | server                | string    | Device's accessible Address   |
    | udid                  | string    | Unique Device Identification  |
    | platformVersion       | string    | Device's platform version     |
    | status                | string    | Device's current status       |
    | version               | int       | Device Modified counter       |
    | borrowerIp            | string    | Device Borrower's IP          |
    | borrowerHostname      | string    | Device Borrower's Hostname    |
    | lastBorrower          | string    | Device's Lending timestamp    |
    | deviceType            | string    | Indicated what type of device \
                                          is returned                   |

    *JSON Representation:*
    | {
    |     "deviceId": 1,
    |     "deviceName": "Samsung Galaxy S20 Ultra",
    |     "platformName": "Android",
    |     "server": "192.168.xxx.xxx:4723/wd/hub",
    |     "udid": "xxxxxxx",
    |     "platformVersion": "10",
    |     "status": "FREE",
    |     "version": 1,
    |     "borrowerIp": "192.168.xxx.xxx",
    |     "borrowerHostname": "joshuarivera[User-Borrowed]",
    |     "lastBorrowed": "2020-02-04 18:33:31",
    |     "deviceType": "Real Device"
    | }

    = Author =

    Created: February 4 2020 14:55 UTC-8

    Author: Joshua Kim Rivera | email:joshua.rivera@mnltechnology.com
    Company: Spiralworks Technologies Inc.

    Contributor:  Shiela Buitizon | email: shiela.buitizon@mnltechnology.com
    Company: Spiralworks Technologies Inc.

    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, base_url=None):
        """
        Initialize with  base url.
        """
        libraries = []
        HybridCore.__init__(self, libraries)
        self.base_url = base_url
        if base_url is not None:
            self.device_url = base_url + '/devices'
            self.device_lending = base_url + '/device/lending'
            self.device_utils = base_url + '/device/utils'
        self.machineHostName = self._append_test_trigger_category()
        self.machineIp = self._get_machine_ip()

    @keyword
    def borrow_android_device(self,
                              platformVersion=None,
                              teamName='',
                              ):
        """ Borrows an Android Device with a status of FREE.
        Accepts platformVersion as parameter.
        """
        device = self._borrow_device('Android',
                                     platformVersion,
                                     teamName)
        return device

    @keyword
    def borrow_ios_device(self,
                          platformVersion=None,
                          teamName='',
                          ):
        """ Borrows an iOS Device with a status of FREE.
        Accepts platformVersion as parameter.
        """
        device = self._borrow_device('iOS',
                                     platformVersion,
                                     teamName)
        return device

    @keyword
    def return_device(self, device):
        if device:
            return self._free_device(device['deviceId'])
        raise TypeError('Cannot Return Nonetype Device')

    def _borrow_device(self,
                       platformName,
                       teamName,
                       platformVersion=None,
                       deviceId=None,
                       ):
        params = {'platformName': platformName,
                  'borrowerIp': self.machineIp,
                  'borrowerHostname': self.machineHostName,
                  'teamName': teamName
                  }
        if deviceId is not None:
            params.update({'deviceId': deviceId})
        else:
            if platformVersion is not None:
                params.update({'platformVersion': platformVersion})
        response = self._get_request(self.device_lending, params)
        device = response.json()

        if bool(response):
            return device

        return None

    def _free_device(self, deviceId):
        try:
            response = self._post_request(self.device_lending,
                                          params={'deviceId': int(deviceId)}
                                          )
            return response
        except Exception as err:
            raise err

    def _get_request(self, url, params):
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response

    def _post_request(self, url, params):
        response = requests.post(url, params=params)
        response.raise_for_status()
        return response

    def _get_machine_hostname(self):
        """Uses python 3 socket library to get the machine IP and hostname.
        """
        try:
            hostName = socket.gethostname()
            return hostName
        except Exception as err:
            raise err

    def _append_test_trigger_category(self):
        """Appends test trigger category to machine hostname.
        """
        hostName = self._get_machine_hostname()
        if environ.get('CI_RUNNER_DESCRIPTION') is not None:
            hostName = hostName + "[" \
                        + environ.get('CI_RUNNER_DESCRIPTION') \
                        + "]"
        else:
            hostName = hostName + "[User-Borrowed]"
        return hostName

    def _get_machine_ip(self, hostName=None):
        """Uses python 3 socket library to obtain machine IP Address.
        Takes machine hostName as parameter
        """
        try:
            hostIp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            hostIp.connect(("8.8.8.8", 80))
            return hostIp.getsockname()[0]
        except Exception as err:
            raise err

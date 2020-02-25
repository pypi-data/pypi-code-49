#!/usr/bin/env python
# Copyright (c) 2019 Radware LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# @author: Leon Meguira, Radware


from abc import ABCMeta, abstractmethod
from radware.sdk.api import BaseAPI
from radware.sdk.exceptions import DeviceError
import time

MSG_NOT_ACCESSIBLE = 'Device not accessible'
MSG_REBOOT = 'Device Reset'
MSG_REBOOT_STATEFUL = 'Device Restarted and Returned'
MSG_IMG_UPLOAD = 'Image Uploaded Successfully'
MSG_CONFIG_DOWNLOAD = 'Configuration Downloaded Successfully'
MSG_CONFIG_UPLOAD = 'Configuration Uploaded Successfully'


class DeviceMng(BaseAPI):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def connection(self):
        pass


class DeviceInfo(object):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def device_name(self):
        pass

    @abstractmethod
    def is_accessible(self, timeout_second=5, retries=1):
        pass


class DeviceOper(object):
    pass


class DeviceConfig(object):
    pass


class DeviceTools(object):
    __metaclass__ = ABCMeta

    @staticmethod
    def device_wait(mng_info: DeviceInfo, interval, timeout):
        e = None
        while timeout > 0:
            try:
                return mng_info.is_accessible()
            except DeviceError as err:
                e = err
                pass
            time.sleep(interval)
            timeout -= 10
        raise DeviceError(e.device_type, MSG_NOT_ACCESSIBLE + '\n' + e.message)


class DeviceManagement(BaseAPI):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def _device_mng_info(self) -> DeviceInfo:
        pass

    @property
    @abstractmethod
    def _device_mng_oper(self) -> DeviceOper:
        pass

    @property
    @abstractmethod
    def _device_mng_config(self) -> DeviceConfig:
        pass

    @property
    def device_name(self):
        return self._device_mng_info.device_name

    def verify_device_accessible(self, timeout_second=5, retries=1):
        try:
            self._device_mng_info.is_accessible(timeout_second, retries)
        except DeviceError as e:
            raise DeviceError(e.device_type, MSG_NOT_ACCESSIBLE + '\n' + e.message)
        return True

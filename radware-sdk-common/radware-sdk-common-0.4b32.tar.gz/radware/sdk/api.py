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


class BaseAPI(object):
    __metaclass__ = ABCMeta

    @classmethod
    def api_function_names(cls, exclude_input=None):
        func_names = list()
        exclude_func_list = list()
        exclude_func_list.append('connection')
        exclude_func_list.extend(dir(BaseAPI))
        if exclude_input:
            exclude_func_list.extend(exclude_input)
        for item in dir(cls):
            if not item.startswith('_') and item not in exclude_func_list:
                if callable(getattr(cls, item)):
                    func_names.append(item)
                elif type(getattr(cls, item)) == property:
                    func_names.append(item)
        return func_names

    @staticmethod
    def _dict_keys_translation(src_dict, attrs_dict):
        new_dict = dict()
        for k, v in src_dict.items():
            if k in attrs_dict:
                new_dict.update({attrs_dict[k]: v})
            else:
                new_dict.update({k: v})
        return new_dict


class BaseDeviceConnection(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def connection_details_update(self, **kwargs):
        pass


class DeviceAPI(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self, bean, retries=3):
        pass

    @abstractmethod
    def read_all(self, bean, retries=3):
        pass

    @abstractmethod
    def update(self, bean, retries=3, dry_run=None):
        pass

    @abstractmethod
    def delete(self, bean, retries=3, dry_run=None):
        pass

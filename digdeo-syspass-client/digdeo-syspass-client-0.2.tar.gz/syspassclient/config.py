#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of SysPass Client
#
# Copyright (C) 2020  DigDeo SAS
#
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


import os
import sys
from syspassclient.object import Object
from syspassclient.constants import dd
from syspassclient.check_type import is_str_or_raise
# from syspassclient.utils import get_terminal_columns
# TODO: Should be enable on python 3
# if sys.version_info[0] > 3:
#     import shutil
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


# Inspired by: http://zetcode.com/python/yaml/
# Inspired by: https://gitlab.com/Tuuux/galaxie-little-alice/raw/master/GLXLittleAlice/Config.py

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Config(Object):
    def __init__(self):
        Object.__init__(self)

        # Load config file
        self.__data = None
        self.__api_directory = None
        self.__api_filename = None
        self.__api_filename_ext = None
        self.__api_file = None
        self.__api_version = None
        self.__config_file = None

        self.api_directory = None
        self.api_filename_ext = None

        self.read()

    @property
    def config_directory(self):
        if 'DD_SYSPASS_CLIENT_CONFIG_DIR' in os.environ:
            return os.path.realpath(os.environ['DD_SYSPASS_CLIENT_CONFIG_DIR'])
        else:
            return os.path.abspath(
                os.path.join(
                    os.path.join(
                        os.environ['HOME'],
                        '.config'),
                    'digdeo-syspass-client'
                )
            )

    @property
    def config_file(self):
        return self.__config_file

    @config_file.setter
    def config_file(self, value=None):
        if self.config_file != value:
            self.__config_file = value

    @property
    def data(self):
        """
        Return the config file as Python dictionary structure

        :return: Config as a big dictionary
        :rtype: dict
        """
        return self.__data

    @data.setter
    def data(self, parameters):
        """
        set en data and raise in case of error

        :param parameters: something it like a dictionary key
        :type parameters: dict
        :raise TypeError: 'parameters' is not a dict type
        """
        if self.__data != parameters:
            self.__data = parameters

    @property
    def api_3_0(self):
        return {
            "account/search": {
                # Search for accounts
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                # categoryId 	int 	no 	        Category’s Id for filtering
                # clientId 	    int 	no 	        Client’s Id for filtering
                # tagsId 	    array 	no 	        Tags’ Id for filtering
                # op 	        string 	no 	        Operator used for filtering. It can be either ‘or’ or ‘and’
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                    "categoryId": {"type": "int", "required": False},
                    "clientId": {"type": "int", "required": False},
                    "tagsId": {"type": "array", "required": False},
                    "op": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/search",
                    "params": {
                        "authToken": None,
                        "text": None,
                        "count": None,
                        "categoryId": None,
                        "clientId": None,
                        "tagsid": None,
                        "op": None,
                    },
                    "id": None,
                },
            },
            "account/view": {
                # Get account’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    Account’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/view",
                    "params": {"authToken": None, "account_id": None, "tokenPass": None},
                    "id": None,
                },
            },
            "account/viewPass": {
                # Get account’s password
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    Account’s Id
                # details 	    int 	no 	        Whether to return account’s details within response account/editPass
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                    "details": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/viewPass",
                    "params": {"authToken": None, "account_id": None, "tokenPass": None, "details": None},
                    "id": None,
                },
            },
            "account/editPass": {
                # Edit account’s password
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # tokenPass 	string 	yes 	API token’s pass
                # id 	int 	yes 	Account’s Id
                # pass 	string 	yes 	Account’s password
                # expireDate 	int 	no 	Expire date in UNIX timestamp format
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                    "password": {"type": "str", "required": True},
                    "expireDate": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/editPass",
                    "params": {"authToken": None, "tokenPass": None, "account_id": None, "password": None,
                               "expireDate": None},
                    "id": None,
                },
            },
            "account/create": {
                # Create account
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # tokenPass 	string 	yes 	API token’s pass
                # name 	        string 	yes 	Account’s name
                # categoryId 	int 	yes 	Account’s category Id
                # clientId 	    int 	yes 	Account’s client Id
                # pass 	        string 	yes 	Account’s password
                # tagsId 	    array 	no 	    Account’s tags Id
                # userGroupId 	int 	no 	    Account’s user group Id
                # parentId 	    int 	no 	    Account’s parent Id
                # login 	    string 	no 	    Account’s login
                # url 	        string 	no 	    Account’s access URL or IP
                # notes 	    string 	no 	    Account’s notes
                # private 	    int 	no 	    Set account as private. It can be either 0 or 1
                # privateGroup 	int 	no 	    Set account as private for group. It can be either 0 or 1
                # expireDate 	int 	no 	    Expire date in UNIX timestamp format
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "categoryId": {"type": "int", "required": True},
                    "clientId": {"type": "int", "required": True},
                    "password": {"type": "str", "required": True},
                    "tagsId": {"type": "array", "required": False},
                    "userGroupId": {"type": "int", "required": False},
                    "parentId": {"type": "int", "required": False},
                    "login": {"type": "str", "required": False},
                    "url": {"type": "str", "required": False},
                    "notes": {"type": "str", "required": False},
                    "private": {"type": "int", "required": False},
                    "privateGroup": {"type": "int", "required": False},
                    "expireDate": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/create",
                    "params": {
                        "authToken": None,
                        "tokenPass": None,
                        "name": None,
                        "categoryId": None,
                        "clientId": None,
                        "password": None,
                        "tagsId": None,
                        "userGroupId": None,
                        "parentId": None,
                        "login": None,
                        "url": None,
                        "notes": None,
                        "private": None,
                        "privateGroup": None,
                        "expireDate": None,
                    },
                    "id": None,
                },
            },
            "account/edit": {
                # Create account
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # tokenPass 	string 	yes 	API token’s pass
                # id 	        int 	yes 	Account’s Id
                # name 	        string 	no 	    Account’s name
                # categoryId 	int 	no 	    Account’s category Id
                # clientId 	    int 	no 	    Account’s client Id
                # tagsId 	    array 	no 	    Account’s tags Id
                # userGroupId 	int 	no 	    Account’s user group Id
                # parentId 	    int 	no 	    Account’s parent Id
                # login 	    string 	no 	    Account’s login
                # url 	        string 	no 	    Account’s access URL or IP
                # notes 	    string 	no 	    Account’s notes
                # private 	    int 	no 	    Set account as private. It can be either 0 or 1
                # privateGroup 	int 	no 	    Set account as private for group. It can be either 0 or 1
                # expireDate 	int 	no 	    Expire date in UNIX timestamp format
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                    "name": {"type": "str", "required": False},
                    "categoryId": {"type": "int", "required": False},
                    "clientId": {"type": "int", "required": False},
                    "tagsId": {"type": "array", "required": False},
                    "userGroupId": {"type": "int", "required": False},
                    "parentId": {"type": "int", "required": False},
                    "login": {"type": "str", "required": False},
                    "url": {"type": "str", "required": False},
                    "notes": {"type": "str", "required": False},
                    "private": {"type": "int", "required": False},
                    "privateGroup": {"type": "int", "required": False},
                    "expireDate": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/edit",
                    "params": {
                        "authToken": None,
                        "tokenPass": None,
                        "account_id": None,
                        "name": None,
                        "categoryId": None,
                        "clientId": None,
                        "tagsId": None,
                        "userGroupId": None,
                        "parentId": None,
                        "login": None,
                        "url": None,
                        "notes": None,
                        "private": None,
                        "privateGroup": None,
                        "expireDate": None,
                    },
                    "id": None,
                },
            },
            "account/delete": {
                # Delete an account
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # id 	        int 	yes 	Account’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/delete",
                    "params": {"authToken": None, "account_id": None},
                    "id": None,
                },
            },
            "category/search": {
                # Search for categories
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "category/view": {
                # Get category’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": True},
                    "count": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/view",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "category/create": {
                # Create category
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # name 	        string 	yes 	    Category’s name
                # description 	string 	no 	        Category’s description
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/create",
                    "params": {"authToken": None, "name": None, "description": None},
                    "id": None,
                },
            },
            "category/edit": {
                # Edit category
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Category’s Id
                # name 	        string 	yes 	    Category’s name
                # description 	string 	no 	        Category’s description
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/edit",
                    "params": {"authToken": None, "cid": None, "name": None, "description": None},
                    "id": None,
                },
            },
            "category/delete": {
                # Delete category
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Category’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/delete",
                    "params": {"authToken": None, "cid": None},
                    "cid": None,
                },
            },
            "client/search": {
                # Search for clients
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "client/view": {
                # Get client’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    Client’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/view",
                    "params": {"authToken": None, "tokenPass": None, "cid": None},
                    "id": None,
                },
            },
            "client/create": {
                # Get client’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # name 	        string 	yes 	Client’s name
                # description 	string 	no 	    Client’s description
                # Global 	    int 	no 	    Set client as Global. It can be either 0 or 1
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "str", "required": False},
                    "Global": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/create",
                    "params": {"authToken": None, "name": None, "description": None, "Global": None},
                    "id": None,
                },
            },
            "client/edit": {
                # Edit client
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Client’s Id
                # name 	        string 	yes 	    Client’s name
                # description 	string 	no 	        Client’s description
                # Global 	    int 	no 	        Set client as Global. It can be either 0 or 1
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "int", "required": False},
                    "Global": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/edit",
                    "params": {"authToken": None, "cid": None, "name": None, "description": None, "Global": None},
                    "id": None,
                },
            },
            "client/delete": {
                # Delete client
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Client’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/delete",
                    "params": {"authToken": None, "cid": None},
                    "id": None,
                },
            },
            "tag/search": {
                # Search for tags
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "tag/view": {
                # Get tag’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    Tag’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "tagid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/view",
                    "params": {"authToken": None, "tokenPass": None, "tagid": None},
                    "id": None,
                },
            },
            "tag/create": {
                # Create tag
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # name 	        string 	yes 	    API token’s pass
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/create",
                    "params": {"authToken": None, "name": None},
                    "id": None,
                },
            },
            "tag/edit": {
                # Create tag
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Tag’s Id
                # name 	        string 	yes 	    Tag’s name
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "id": {"type": "int", "required": True},
                    "name": {"type": "str", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/edit",
                    "params": {"authToken": None, "id": None, "name": None},
                    "id": None,
                },
            },
            "tag/delete": {
                # Delete tag
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Tag’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tagid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/delete",
                    "params": {"authToken": None, "tagid": None},
                    "id": None,
                },
            },
            "usergroup/search": {
                # Search for user groups
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "usergroup/view": {
                # Get user group’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    User group’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "ugid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/view",
                    "params": {"authToken": None, "tokenPass": None, "ugid": None},
                    "id": None,
                },
            },
            "usergroup/create": {
                # Create user group
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # name 	        string 	yes 	    User group’s name
                # description 	string 	no 	        User group’s description
                # usersId 	    array 	no 	        User group’s users Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "str", "required": False},
                    "usersId": {"type": "array", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/create",
                    "params": {"authToken": None, "name": None, "description": None, "usersId": None},
                    "id": None,
                },
            },
            "usergroup/edit": {
                # Edit user group
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    User group’s Id
                # name 	        string 	yes 	    User group’s name
                # description 	string 	no 	        User group’s description
                # usersId 	    array 	no 	        User group’s users Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "ugid": {"type": "int", "required": True},
                    "name": {"type": "string", "required": True},
                    "description": {"type": "string", "required": False},
                    "usersId": {"type": "array", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/edit",
                    "params": {"authToken": None, "ugid": None, "name": None, "description": None, "usersId": None},
                    "id": None,
                },
            },
            "usergroup/delete": {
                # Delete user group
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    User group’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "ugid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/delete",
                    "params": {"authToken": None, "ugid": None},
                    "ugid": None,
                },
            },
            "config/backup": {
                # Perform an application and database backup
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # path 	        string 	no 	        Server path to store the application and database backup
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "path": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "config/backup",
                    "params": {"authToken": None, "path": None},
                    "id": None,
                },
            },
            "config/export": {
                # Export application data in XML format
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # path 	        string 	no 	        Server path to store the XML file
                # password 	    string 	no 	        Password used to encrypt the exported data
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "path": {"type": "str", "required": False},
                    "password": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "config/export",
                    "params": {"authToken": None, "path": None, "password": None},
                    "id": None,
                },
            },
        }

    @property
    def api_3_1(self):
        return {
            "account/search": {
                # Search for accounts
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                # categoryId 	int 	no 	        Category’s Id for filtering
                # clientId 	    int 	no 	        Client’s Id for filtering
                # tagsId 	    array 	no 	        Tags’ Id for filtering
                # op 	        string 	no 	        Operator used for filtering. It can be either ‘or’ or ‘and’
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                    "categoryId": {"type": "int", "required": False},
                    "clientId": {"type": "int", "required": False},
                    "tagsId": {"type": "array", "required": False},
                    "op": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/search",
                    "params": {
                        "authToken": None,
                        "text": None,
                        "count": None,
                        "categoryId": None,
                        "clientId": None,
                        "tagsid": None,
                        "op": None,
                    },
                    "id": None,
                },
            },
            "account/view": {
                # Get account’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    Account’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/view",
                    "params": {"authToken": None, "account_id": None, "tokenPass": None},
                    "id": None,
                },
            },
            "account/viewPass": {
                # Get account’s password
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    Account’s Id
                # details 	    int 	no 	        Whether to return account’s details within response account/editPass
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                    "details": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/viewPass",
                    "params": {"authToken": None, "account_id": None, "tokenPass": None, "details": None},
                    "id": None,
                },
            },
            "account/editPass": {
                # Edit account’s password
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # tokenPass 	string 	yes 	API token’s pass
                # id 	int 	yes 	Account’s Id
                # pass 	string 	yes 	Account’s password
                # expireDate 	int 	no 	Expire date in UNIX timestamp format
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                    "password": {"type": "str", "required": True},
                    "expireDate": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/editPass",
                    "params": {"authToken": None,
                               "tokenPass": None,
                               "account_id": None,
                               "password": None,
                               "expireDate": None
                               },
                    "id": None,
                },
            },
            "account/create": {
                # Create account
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # tokenPass 	string 	yes 	API token’s pass
                # name 	        string 	yes 	Account’s name
                # categoryId 	int 	yes 	Account’s category Id
                # clientId 	    int 	yes 	Account’s client Id
                # pass 	        string 	yes 	Account’s password
                # tagsId 	    array 	no 	    Account’s tags Id
                # userGroupId 	int 	no 	    Account’s user group Id
                # parentId 	    int 	no 	    Account’s parent Id
                # login 	    string 	no 	    Account’s login
                # url 	        string 	no 	    Account’s access URL or IP
                # notes 	    string 	no 	    Account’s notes
                # private 	    int 	no 	    Set account as private. It can be either 0 or 1
                # privateGroup 	int 	no 	    Set account as private for group. It can be either 0 or 1
                # expireDate 	int 	no 	    Expire date in UNIX timestamp format
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "categoryId": {"type": "int", "required": True},
                    "clientId": {"type": "int", "required": True},
                    "password": {"type": "str", "required": True},
                    "tagsId": {"type": "array", "required": False},
                    "userGroupId": {"type": "int", "required": False},
                    "parentId": {"type": "int", "required": False},
                    "login": {"type": "str", "required": False},
                    "url": {"type": "str", "required": False},
                    "notes": {"type": "str", "required": False},
                    "private": {"type": "int", "required": False},
                    "privateGroup": {"type": "int", "required": False},
                    "expireDate": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/create",
                    "params": {
                        "authToken": None,
                        "tokenPass": None,
                        "name": None,
                        "categoryId": None,
                        "clientId": None,
                        "password": None,
                        "tagsId": None,
                        "userGroupId": None,
                        "parentId": None,
                        "login": None,
                        "url": None,
                        "notes": None,
                        "private": None,
                        "privateGroup": None,
                        "expireDate": None,
                    },
                    "id": None,
                },
            },
            "account/edit": {
                # Create account
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # tokenPass 	string 	yes 	API token’s pass
                # id 	        int 	yes 	Account’s Id
                # name 	        string 	no 	    Account’s name
                # categoryId 	int 	no 	    Account’s category Id
                # clientId 	    int 	no 	    Account’s client Id
                # tagsId 	    array 	no 	    Account’s tags Id
                # userGroupId 	int 	no 	    Account’s user group Id
                # parentId 	    int 	no 	    Account’s parent Id
                # login 	    string 	no 	    Account’s login
                # url 	        string 	no 	    Account’s access URL or IP
                # notes 	    string 	no 	    Account’s notes
                # private 	    int 	no 	    Set account as private. It can be either 0 or 1
                # privateGroup 	int 	no 	    Set account as private for group. It can be either 0 or 1
                # expireDate 	int 	no 	    Expire date in UNIX timestamp format
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                    "name": {"type": "str", "required": False},
                    "categoryId": {"type": "int", "required": False},
                    "clientId": {"type": "int", "required": False},
                    "tagsId": {"type": "array", "required": False},
                    "userGroupId": {"type": "int", "required": False},
                    "parentId": {"type": "int", "required": False},
                    "login": {"type": "str", "required": False},
                    "url": {"type": "str", "required": False},
                    "notes": {"type": "str", "required": False},
                    "private": {"type": "int", "required": False},
                    "privateGroup": {"type": "int", "required": False},
                    "expireDate": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/edit",
                    "params": {
                        "authToken": None,
                        "tokenPass": None,
                        "account_id": None,
                        "name": None,
                        "categoryId": None,
                        "clientId": None,
                        "tagsId": None,
                        "userGroupId": None,
                        "parentId": None,
                        "login": None,
                        "url": None,
                        "notes": None,
                        "private": None,
                        "privateGroup": None,
                        "expireDate": None,
                    },
                    "id": None,
                },
            },
            "account/delete": {
                # Delete an account
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # id 	        int 	yes 	Account’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "account_id": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "account/delete",
                    "params": {"authToken": None, "account_id": None},
                    "id": None,
                },
            },
            "category/search": {
                # Search for categories
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "category/view": {
                # Get category’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": True},
                    "count": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/view",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "category/create": {
                # Create category
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # name 	        string 	yes 	    Category’s name
                # description 	string 	no 	        Category’s description
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/create",
                    "params": {"authToken": None, "name": None, "description": None},
                    "id": None,
                },
            },
            "category/edit": {
                # Edit category
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Category’s Id
                # name 	        string 	yes 	    Category’s name
                # description 	string 	no 	        Category’s description
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/edit",
                    "params": {"authToken": None, "cid": None, "name": None, "description": None},
                    "id": None,
                },
            },
            "category/delete": {
                # Delete category
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Category’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "category/delete",
                    "params": {"authToken": None, "id": None},
                    "cid": None,
                },
            },
            "client/search": {
                # Search for clients
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "client/view": {
                # Get client’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    Client’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/view",
                    "params": {"authToken": None, "tokenPass": None, "cid": None},
                    "id": None,
                },
            },
            "client/create": {
                # Get client’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	User’s API token
                # name 	        string 	yes 	Client’s name
                # description 	string 	no 	    Client’s description
                # Global 	    int 	no 	    Set client as Global. It can be either 0 or 1
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "str", "required": False},
                    "Global": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/create",
                    "params": {"authToken": None, "name": None, "description": None, "Global": None},
                    "id": None,
                },
            },
            "client/edit": {
                # Edit client
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    Client’s Id
                # name 	        string 	yes 	    Client’s name
                # description 	string 	no 	        Client’s description
                # Global 	    int 	no 	        Set client as Global. It can be either 0 or 1
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "int", "required": False},
                    "Global": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/edit",
                    "params": {"authToken": None, "cid": None, "name": None, "description": None, "Global": None},
                    "id": None,
                },
            },
            "client/delete": {
                # Delete client
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # cid 	        int 	yes 	    Client’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "cid": {"type": "int", "required": True}
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "client/delete",
                    "params": {"authToken": None, "cid": None},
                    "id": None,
                },
            },
            "tag/search": {
                # Search for tags
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "tag/view": {
                # Get tag’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # tagid 	    int 	yes 	    Tag’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "tagid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/view",
                    "params": {"authToken": None, "tokenPass": None, "tagid": None},
                    "id": None,
                },
            },
            "tag/create": {
                # Create tag
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # name 	        string 	yes 	    API token’s pass
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/create",
                    "params": {"authToken": None, "name": None},
                    "id": None,
                },
            },
            "tag/edit": {
                # Create tag
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tagid 	    int 	yes 	    Tag’s Id
                # name 	        string 	yes 	    Tag’s name
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tagid": {"type": "int", "required": True},
                    "name": {"type": "str", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/edit",
                    "params": {"authToken": None, "id": None, "name": None},
                    "id": None,
                },
            },
            "tag/delete": {
                # Delete tag
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tagid 	    int 	yes 	    Tag’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tagid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "tag/delete",
                    "params": {"authToken": None, "tagid": None},
                    "id": None,
                },
            },
            "userGroup/search": {
                # Search for user groups
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # text 	        string 	no 	        Text to search for
                # count 	    int 	no 	        Number of results to display
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "text": {"type": "str", "required": False},
                    "count": {"type": "int", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "userGroup/search",
                    "params": {"authToken": None, "text": None, "count": None},
                    "id": None,
                },
            },
            "userGroup/view": {
                # Get user group’s details
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # tokenPass 	string 	yes 	    API token’s pass
                # id 	        int 	yes 	    User group’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "tokenPass": {"type": "str", "required": True},
                    "ugid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/view",
                    "params": {"authToken": None, "tokenPass": None, "ugid": None},
                    "id": None,
                },
            },
            "userGroup/create": {
                # Create user group
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # name 	        string 	yes 	    User group’s name
                # description 	string 	no 	        User group’s description
                # usersId 	    array 	no 	        User group’s users Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "name": {"type": "str", "required": True},
                    "description": {"type": "str", "required": False},
                    "usersId": {"type": "array", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/create",
                    "params": {"authToken": None, "name": None, "description": None, "usersId": None},
                    "id": None,
                },
            },
            "userGroup/edit": {
                # Edit user group
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    User group’s Id
                # name 	        string 	yes 	    User group’s name
                # description 	string 	no 	        User group’s description
                # usersId 	    array 	no 	        User group’s users Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "ugid": {"type": "int", "required": True},
                    "name": {"type": "string", "required": True},
                    "description": {"type": "string", "required": False},
                    "usersId": {"type": "array", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/edit",
                    "params": {"authToken": None, "ugid": None, "name": None, "description": None, "usersId": None},
                    "id": None,
                },
            },
            "userGroup/delete": {
                # Delete user group
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # id 	        int 	yes 	    User group’s Id
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "ugid": {"type": "int", "required": True},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "usergroup/delete",
                    "params": {"authToken": None, "ugid": None},
                    "ugid": None,
                },
            },
            "config/backup": {
                # Perform an application and database backup
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # path 	        string 	no 	        Server path to store the application and database backup
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "path": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "config/backup",
                    "params": {"authToken": None, "path": None},
                    "id": None,
                },
            },
            "config/export": {
                # Export application data in XML format
                # Parameter 	Type 	Required 	Description
                # authToken 	string 	yes 	    User’s API token
                # path 	        string 	no 	        Server path to store the XML file
                # password 	    string 	no 	        Password used to encrypt the exported data
                "params_details": {
                    "authToken": {"type": "str", "required": True},
                    "path": {"type": "str", "required": False},
                    "password": {"type": "str", "required": False},
                },
                "json_body": {
                    "jsonrpc": "2.0",
                    "method": "config/export",
                    "params": {"authToken": None, "path": None, "password": None},
                    "id": None,
                },
            },
        }

    @property
    def api_version(self):
        if self.__api_version is None:
            return dd.syspass["api"]["version"]
        else:
            return self.__api_version

    @api_version.setter
    def api_version(self, version=None):
        if version is None:
            if self.__api_version is not None:
                self.__api_version = None
            return

        is_str_or_raise(obj=version)

        if self.__api_version != version:
            self.__api_version = version

    @property
    def api_filename_ext(self):
        """
        Return the api_filename_extension property

        :return: the filename extension like '.yaml'
        :rtype: str
        """
        return self.__api_filename_ext

    @api_filename_ext.setter
    def api_filename_ext(self, extension=None):
        """
        Set the api_filename_ext property

        :param extension: a extension like '.yaml' or None for restore default one ('.yaml')
        :type extension: str or None
        :raise TypeError: When 'extension' is not a str type
        """
        if extension is None:
            extension = ".yaml"

        if not isinstance(extension, str):
            raise TypeError("'extension' must be a str type")

        if self.__api_filename_ext != extension:
            self.__api_filename_ext = extension

    @property
    def api_directory(self):
        return self.__api_directory

    @api_directory.setter
    def api_directory(self, directory=None):
        """
        Return the directory path where is store API yaml file(s)

        :param directory: in case you want force a special directory
        :type directory: str
        :return: the absolute path of the api_directory
        :rtype: str
        """
        if directory is None:
            if self.__api_directory != os.path.join(os.path.dirname(os.path.abspath(__file__)), "api"):
                self.__api_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "api")

        else:
            is_str_or_raise(directory)
            if self.__api_directory != directory:
                self.__api_directory = directory

    @property
    def api_filename(self):
        """
        Return the api_filename)

        :return: the filename to load
        :rtype: str
        """
        return self.api_version + self.api_filename_ext

    @property
    def api_file(self):
        """
        Return the absolute path of the API yaml file to load

        :return: path of the API yaml file to load
        :rtype: str
        """
        return os.path.join(self.api_directory, self.api_filename)

    def write(self, api_file=None):
        """
        Write the config file

        :param api_file: the file where write data, or None for default one.
        :type api_file: str or None
        """
        if api_file is None:
            api_file = self.api_file

        with open(api_file, "w") as f:
            if self.verbose:
                sys.stdout.write("write:  " + str(self.api_file))
                sys.stdout.write("\n")
                sys.stdout.flush()
            dump(self.data, f)
            f.close()
            for line in dump(self.data).split("\n"):
                if self.verbose:
                    sys.stdout.write("config: >" + str(line))
                    sys.stdout.write("\n")
                    sys.stdout.flush()

    def read(self,
             api_file=None,
             config_file=None,
             debug=None,
             debug_level=None,
             verbose=None,
             verbose_level=None
             ):
        """
        Read the configuration file

        :param api_file: the file path to to load
        :type api_file: str or None for the default one
        :param config_file:the file it store the dd_ansible_syspass
        :type config_file: str or None for default
        """
        if config_file is None:
            config_file = self.get_config_file()

        if api_file is None:
            api_file = self.api_file

        with open(api_file) as f:
            self.data = load(f, Loader=Loader)
            f.close()

        with open(config_file) as f:
            config = load(f, Loader=Loader)
            f.close()

            self.data["api_url"] = config["syspassclient"]["api_url"]
            self.data["authToken"] = config["syspassclient"]["authToken"]
            self.data["tokenPass"] = config["syspassclient"]["tokenPass"]
            self.data["debug"] = config["syspassclient"]["debug"]
            self.data["debug_level"] = config["syspassclient"]["debug_level"]
            self.data["verbose"] = config["syspassclient"]["verbose"]
            self.data["verbose_level"] = config["syspassclient"]["verbose_level"]
            self.data["api_version"] = config["syspassclient"]["api_version"]

            self.api_version = self.data["api_version"]

            if debug is None:
                self.debug = self.data["debug"]
            else:
                self.debug = debug

            if debug_level is None:
                self.debug_level = self.data["debug_level"]
            else:
                self.debug_level = debug_level

            if verbose is None:
                self.verbose = self.data["verbose"]
            else:
                self.verbose = verbose

            if verbose_level is None:
                self.verbose_level = self.data["verbose_level"]
            else:
                self.verbose_level = verbose_level

        if self.debug and self.debug_level > 0:
            class_name = "{0}: ".format(self.__class__.__name__.upper())
            action_name = "{0} ".format("Load config file".lower())
            sys.stdout.write("\u001b[33m")
            sys.stdout.write("{0}".format(class_name))
            sys.stdout.write("\u001b[0m")
            sys.stdout.write("{0}".format(action_name))
            len_test = len(class_name) + len(action_name)
            # TODO: Should be enable on python 3
            # if sys.version_info[0] > 3:
            #     len_term = shutil.get_terminal_size().columns
            #     sys.stdout.write("*" * int(len_term - len_test - 1))
            sys.stdout.write("\n")
            sys.stdout.write("file: {0} ".format(str(self.config_file)))
            sys.stdout.write("\n")
            if self.debug_level > 2:
                sys.stdout.write("api_url: {0}\n".format(self.data["api_url"]))
                sys.stdout.write("authToken: {0}\n".format(self.data["authToken"]))
                sys.stdout.write("tokenPass: {0}\n".format(self.data["tokenPass"]))

            sys.stdout.write("debug: {0}\n".format(self.data["debug"]))
            sys.stdout.write("debug_level: {0}\n".format(self.data["debug_level"]))
            sys.stdout.write("verbose: {0}\n".format(self.data["verbose"]))
            sys.stdout.write("verbose_level: {0}\n".format(self.data["verbose_level"]))
            sys.stdout.write("\n")
            sys.stdout.flush()

        if self.debug and self.debug_level > 0:
            class_name = "{0}: ".format(self.__class__.__name__.upper())
            action_name = "{0} ".format("Load API File".lower())
            sys.stdout.write("\u001b[33m")
            sys.stdout.write("{0}".format(class_name))
            sys.stdout.write("\u001b[0m")
            sys.stdout.write("{0}".format(action_name))
            len_test = len(class_name) + len(action_name)
            # TODO: Should be enable on python 3
            # if sys.version_info[0] > 3:
            #     len_term = shutil.get_terminal_size().columns
            #     sys.stdout.write("*" * int(len_term - len_test - 1))
            sys.stdout.write("\n")
            sys.stdout.write("api_version: {0}\n".format(str(self.api_version)))
            sys.stdout.write("file: {0}\n".format(str(self.api_file)))
            sys.stdout.write("\n")
            sys.stdout.flush()
            if self.verbose and self.verbose_level > 1:
                for line in dump(self.data).split("\n"):
                    sys.stdout.write("config: {0}\n".format(str(line)))
                    sys.stdout.flush()

    def reset(self):
        if self.api_version == "3.0":
            self.data = self.api_3_0
        else:
            self.data = self.api_3_1

    def get_data(self):
        """
        return teh data dictionary

        :return: the data dictionary
        :rtype: dit
        """
        return self.data

    @staticmethod
    def get_empty_config_dict():
        return {
            'syspassclient': {
                'api_url': None,
                'api_version': '3.1',
                'authToken': None,
                'tokenPass': None,
                'debug': True,
                'debug_level': 3,
                'verbose': False,
                'verbose_level': 0
            }
        }

    def get_config_file(self):
        return os.path.join(
            self.config_directory,
            "config.yml",
        )

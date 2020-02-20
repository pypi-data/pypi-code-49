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

# python 3 headers, required if submitting to Ansible
import sys

if sys.version_info[0] > 3:
    import shutil

import requests
import urllib3
# from ansible.errors import AnsibleError
from yaml import dump
from syspassclient.check_type import is_ascii_or_raise
from syspassclient.check_type import is_int_or_raise
from syspassclient.check_type import is_str_or_raise
from syspassclient.check_type import is_url_or_raise
from syspassclient.object import Object
from syspassclient.utils import look_for_args, look_for_error
from syspassclient import Config

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

urllib3.disable_warnings()


class SyspassClient(Object):
    def __init__(self):
        Object.__init__(self)

        # Private property's
        self.__authToken = None
        self.__api_url = None
        self.__tokenPass = None
        self.__r_id = None

        # Initialize
        self.api_url = Config.get_data()['api_url']
        self.authToken = Config.get_data()['authToken']
        self.tokenPass = Config.get_data()['tokenPass']
        self.debug = Config.get_data()['debug']
        self.debug_level = Config.get_data()['debug_level']
        self.verbose = Config.get_data()['verbose']
        self.verbose_level = Config.get_data()['verbose_level']

        self.r_id = 1

    @property
    def api_url(self):
        """
        The url of the SysPass API

        :return: the url of the SysPass API or None if not set
        :rtype: str or None
        """
        return self.__api_url

    @api_url.setter
    def api_url(self, api_url=None):
        """
        Set ``api_url`` property

        :param api_url: A SysPass API Key
        :type api_url: str or None
        :raise TypeError: if ``api_url`` is not a str of None
        """

        if api_url is None:
            if self.__api_url is not None:
                self.__api_url = None
            return

        is_str_or_raise(api_url)
        is_url_or_raise(api_url)

        if self.__api_url != api_url:
            self.__api_url = api_url

    @property
    def authToken(self):
        """
        Whether the application will paint directly on the widget.

        :return: True or False
        :rtype: bool
        """
        return self.__authToken

    @authToken.setter
    def authToken(self, authToken=None):
        """
        Set ``api_key`` property

        :param authToken: A SysPass API Key
        :type authToken: str or None
        :raise TypeError: if ``api_key`` is not a str of None
        """
        if authToken is None or authToken == "":
            if self.__authToken != authToken:
                self.__authToken = None
            return

        is_str_or_raise(authToken)
        is_ascii_or_raise(authToken)

        if self.__authToken != authToken:
            self.__authToken = authToken

    @property
    def tokenPass(self):
        """
        Whether the application will paint directly on the widget.

        :return: True or False
        :rtype: bool
        """
        return self.__tokenPass

    @tokenPass.setter
    def tokenPass(self, tokenPass=None):
        """
        Set ``api_acc_tokpwd`` property

        :param tokenPass: A SysPass API Key
        :type tokenPass: str or None
        :raise TypeError: if ``api_acc_tokpwd`` is not a str of None
        """
        if tokenPass is None or tokenPass == "":
            if self.__tokenPass != tokenPass:
                self.__tokenPass = None
            return

        if tokenPass is not None:
            is_str_or_raise(tokenPass)
            is_ascii_or_raise(tokenPass)

        if self.__tokenPass != tokenPass:
            self.__tokenPass = tokenPass

    def make_post_request(self, data=None, verify=False):
        """
        make the request by 'request' function.

        :param data: the data it will be convert on json
        :type data: dict
        :param verify: ssl certificate verification
        :type verify: bool
        :return: the request.post return
        :rtype: dict
        """
        if self.debug and self.debug_level > 0:
            class_name = "{0} ".format(self.__class__.__name__.upper())
            action_name = "| {1} | {0} ".format("request >".lower(), data['method'])
            text = class_name + action_name
            sys.stdout.write("\u001b[33m")
            sys.stdout.write("{0}".format(class_name))
            sys.stdout.write("\u001b[0m")
            sys.stdout.write("{0}".format(action_name))
            if sys.version_info[0] > 3:
                sys.stdout.write("*" * int(shutil.get_terminal_size().columns - (len(text))))
            sys.stdout.write("\n")
            sys.stdout.write("{0}".format(dump(data)))
            sys.stdout.write("\u001b[0m")
            sys.stdout.write("\n")

            sys.stdout.flush()
        return requests.post(url=self.api_url, json=data, verify=verify).json()

    def increase_request_id(self, increment=1):
        """
        In case of multi request, request ID must be increase for permit to the API work with.

        :param increment: a increment value
        :type increment: int
        :raise TypeError: if ``increment`` is not a int
        :raise ValueError: if ``increment`` is not a positive value
        """
        is_int_or_raise(increment)

        if increment <= 0:
            raise ValueError("'increment' must be a positive value")

        self.r_id += increment

    def generate_json(self, **parameters):

        if "method" not in parameters:
            raise (KeyError('"parameters" must have a key name "method"'))
        method = parameters["method"]
        del parameters["method"]

        # workaround about 'pass' python world reserved
        if "password" in parameters:
            password = parameters["password"]
            del parameters["password"]
            parameters["pass"] = password

        # workaround for 'global' world reserved
        if "Global" in parameters:
            Global = parameters["Global"]
            del parameters["Global"]
            parameters["global"] = Global

        # workaround for 'id' world reserved
        if "ugid" in parameters:
            ugid = parameters["ugid"]
            del parameters["ugid"]
            parameters["id"] = ugid
        if "cid" in parameters:
            cid = parameters["cid"]
            del parameters["cid"]
            parameters["id"] = cid
        if "tagid" in parameters:
            tagid = parameters["tagid"]
            del parameters["tagid"]
            parameters["id"] = tagid
        if "account_id" in parameters:
            account_id = parameters["account_id"]
            del parameters["account_id"]
            parameters["id"] = account_id

        for key, value in dict(parameters).items():
            if value is None:
                del parameters[key]
            if value is []:
                del parameters[key]

        data = {"jsonrpc": "2.0", "method": method, "params": parameters, "id": self.r_id}
        return data

    def print_returned_value(self, req):
        if self.debug and self.debug_level > 0:

            class_name = "{0}: ".format(self.__class__.__name__.upper())
            action_name = "{0} ".format("Returned value".lower())
            text = class_name + action_name
            sys.stdout.write("\u001b[33m")
            sys.stdout.write("{0}".format(class_name))
            sys.stdout.write("\u001b[0m")
            sys.stdout.write("{0}".format(action_name))
            sys.stdout.write("\n")

            if 'error' in req:
                sys.stdout.write(u"\u001b[31m{0}\u001b[0m".format(dump(req, allow_unicode=True)))
            else:
                sys.stdout.write(u"{0}".format(dump(req, allow_unicode=True)))
            sys.stdout.write("\n")
            sys.stdout.flush()

    def account_search(
            self,
            method="account/search",
            authToken=None,
            text=None,
            count=None,
            categoryId=None,
            clientId=None,
            tagsId=None,
            op=None,
            matchall=None
    ):
        """
        Search for accounts:

        method: account/search

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	 User’s API token
        text 	    string 	no 	     Text to search for
        count 	    int 	no 	     Number of results to display
        categoryId 	int 	no 	     Category’s Id for filtering
        clientId 	int 	no 	     Client’s Id for filtering
        tagsId 	    array 	no 	     Tags’ Id for filtering
        op 	        string 	no 	     Operator used for filtering. It can be either ‘or’ or ‘and’

        parameter ``match_all`` is not on the original API

        :param method: the method name
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param text: Text to search for
        :type text: str or None
        :param count: Number of results to display
        :type count: int or None
        :param categoryId: Category’s Id for filtering
        :type categoryId: int or None
        :param clientId: Client’s Id for filtering
        :type clientId: int or None
        :param tagsId: Tags’ Id for filtering
        :type tagsId: array or None
        :param op: Operator used for filtering. It can be either ‘or’ or ‘and’
        :type: op: str or None
        :return: Return the searching result
        :rtype: str in case of success or None if nothing found
        """
        if authToken is None:
            authToken = self.authToken

        # Exit as soon of possible
        look_for_args(
            method=method,
            authToken=authToken,
            text=text,
            count=count,
            categoryId=categoryId,
            clientId=clientId,
            tagsId=tagsId,
            op=op,
        )

        data = self.generate_json(
            method=method,
            authToken=authToken,
            text=text,
            count=count,
            categoryId=categoryId,
            clientId=clientId,
            tagsId=tagsId,
            op=op,
        )

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        # look_for_error(data, req)

        if 'result' in req and 'count' in req['result'] and req['result']['count'] > 0:
            if matchall is None:
                for res in req['result']['result']:
                    if res['name'] == text:
                        return req['result']['result'][0]['id']
            else:
                return req['result']['result']
        # elif 'error' in req:
        #     raise AnsibleError('AccountSearch Error : %s' % req)
        else:
            return None

    def account_delete(self, method="account/delete", authToken=None, account_id=None):
        """
        Delete an account

        method: account/delete

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        id 	        int 	yes 	    Account’s Id

        :param method: must be 'account/delete'
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param account_id: Account’s Id
        :type account_id: int
        """
        if authToken is None:
            authToken = self.authToken

        # Exit as soon of possible
        look_for_args(method=method, authToken=authToken, account_id=account_id)

        data = self.generate_json(method=method, authToken=authToken, account_id=account_id)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        look_for_error(data, req)

        if req["result"]["resultCode"] == 0:
            return req["result"]
        # else:
        #     raise AnsibleError("AccountDelete Error : %s" % req)

    def account_view(self, method="account/view", authToken=None, tokenPass=None, account_id=None):
        """
        Search for accounts:

        method: account/search

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        tokenPass 	string 	yes 	    API token’s pass
        id 	        int 	yes 	    Account’s Id

        :param method: the method name
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param tokenPass: API token’s pass, is used to decrypt encrypted data.
        :type tokenPass: str
        :param account_id:  Account’s Id
        :type account_id: int
        """
        if authToken is None:
            authToken = self.authToken

        if tokenPass is None:
            tokenPass = self.tokenPass

        look_for_args(method=method, authToken=authToken, tokenPass=tokenPass, account_id=account_id)

        data = self.generate_json(method=method, authToken=authToken, tokenPass=tokenPass, account_id=account_id)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        look_for_error(data, req)

        if 'result' in req and 'result' in req['result'] and len(req['result']['result']) > 0:
            return req["result"]["result"]
        else:
            return None

    def account_viewpass(self, method="account/viewPass", authToken=None, tokenPass=None, account_id=None,
                         details=None):
        """
        Get account’s password

        Parameter 	Type 	Required 	Description
        authtoken 	string 	yes 	    User’s API token
        tokenpass 	string 	yes 	    API token’s pass
        account_id 	int 	yes 	    Account’s Id
        details 	int 	no 	        Whether to return account’s details within response

        method: account/viewPass

        :param method: the method name
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param tokenPass: API token’s pass, is used to decrypt encrypted data.
        :type tokenPass: str
        :param account_id: Account’s Id
        :type account_id: int
        :param details: Whether to return account’s details within response
        :type details: int or None
        """
        if authToken is None:
            authToken = self.authToken

        if tokenPass is None:
            tokenPass = self.tokenPass

        look_for_args(
            method=method,
            authToken=authToken,
            tokenPass=tokenPass,
            account_id=account_id,
            details=details
        )

        data = self.generate_json(
            method=method,
            authToken=authToken,
            tokenPass=tokenPass,
            account_id=account_id,
            details=details
        )

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        look_for_error(data, req)

        # We got a response
        if 'result' in req and 'count' in req['result'] and req['result']['count'] > 0:
            return req['result']['result']['password']
        # else:
        #     raise AnsibleError('AccountViewpass Error : %s' % req)

    def account_create(
            self,
            method="account/create",
            authToken=None,
            tokenPass=None,
            name=None,
            categoryId=None,
            clientId=None,
            password=None,
            tagsId=None,
            userGroupId=None,
            parentId=None,
            login=None,
            url=None,
            notes=None,
            private=None,
            privateGroup=None,
            expireDate=None,
    ):
        """
        Create account

        account/create

        Parameter 	    Type 	Required 	Description
        authToken 	    string 	yes 	    User’s API token
        tokenPass 	    string 	yes 	    API token’s pass
        name 	        string 	yes 	    Account’s name
        categoryId 	    int 	yes 	    Account’s category Id
        clientId 	    int 	yes 	    Account’s client Id
        pass 	        string 	yes 	    Account’s password
        tagsId 	        array 	no 	        Account’s tags Id
        userGroupId     int 	no 	        Account’s user group Id
        parentId 	    int 	no 	        Account’s parent Id
        login 	        string 	no 	        Account’s login
        url 	        string 	no 	        Account’s access URL or IP
        notes 	        string 	no 	        Account’s notes
        private 	    int 	no 	        Set account as private. It can be either 0 or 1
        privateGroup 	int 	no 	        Set account as private for group. It can be either 0 or 1
        expireDate 	    int 	no 	        Expire date in UNIX timestamp format

        Note: pass have been change by password, due that a python reserved world. That is the json request creator it
        change password for pass just at end of the process.
        
        :param method: must be account/create.
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param tokenPass: API token’s pass
        :type tokenPass: str
        :param name: Account’s name
        :type name: str
        :param categoryId: Account’s category Id
        :type categoryId: int
        :param clientId: Account’s client Id
        :type clientId: int
        :param password: Account’s password
        :type password: str
        :param tagsId: Account’s tags Id
        :type tagsId: list
        :param userGroupId: Account’s user group Id
        :type userGroupId: int
        :param parentId: Account’s parent Id
        :type parentId: int or None
        :param login: Account’s login
        :type login: str
        :param url: Account’s access URL or IP
        :type url: str
        :param notes: Account’s notes
        :type notes: str
        :param private: Set account as private. It can be either 0 or 1
        :type private: int
        :param privateGroup: Set account as private for group. It can be either 0 or 1
        :type privateGroup: int
        :param expireDate: Expire date in UNIX timestamp format
        :type expireDate: int
        """
        if authToken is None:
            authToken = self.authToken
        if authToken is None:
            raise TypeError("'authToken' must be set")

        if tokenPass is None:
            tokenPass = self.tokenPass

        if tokenPass is None:
            raise TypeError("'tokenPass' must be set")
        if expireDate == "":
            expireDate = None

        look_for_args(
            method=method,
            authToken=authToken,
            tokenPass=tokenPass,
            name=name,
            categoryId=categoryId,
            clientId=clientId,
            password=password,
            tagsId=tagsId,
            userGroupId=userGroupId,
            parentId=parentId,
            login=login,
            url=url,
            notes=notes,
            private=private,
            privateGroup=privateGroup,
            expireDate=expireDate,
        )

        data = self.generate_json(
            method=method,
            authToken=authToken,
            tokenPass=tokenPass,
            name=name,
            categoryId=categoryId,
            clientId=clientId,
            password=password,
            tagsId=tagsId,
            userGroupId=userGroupId,
            parentId=parentId,
            login=login,
            url=url,
            notes=notes,
            private=private,
            privateGroup=privateGroup,
            expireDate=expireDate,
        )
        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        look_for_error(data, req)

        if req["result"]["itemId"] > 0:
            return req["result"]["itemId"]
        else:
            return None

    def category_search(self, method="category/search", authToken=None, text=None, count=None):
        """
        Searches syspass category.
        text is the keyword.
        count is the number of results.
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, text=text, count=count)

        data = self.generate_json(method=method, authToken=authToken, text=text, count=count)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        # look_for_error(data, req)

        # We got a response

        if 'result' in req and 'count' in req['result'] and req['result']['count'] > 0:
            for res in req['result']['result']:
                if res['name'] == text:
                    return req['result']['result'][0]['id']
        # elif 'error' in req:
        #     raise AnsibleError('CategorySearch Error : %s' % (req['error']))
        else:
            return None

    def category_create(self, method="category/create", authToken=None, name=None, description=None):
        """
        Create category

        Parameter 	Type 	Required 	Description
        method      string  yes         category/create
        authToken 	string 	yes 	    User’s API token
        name 	    string 	yes 	    Category’s name
        description string 	no 	        Category’s description

        :param method: must be category/create
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param name: Category’s name
        :type name: str
        :param description: Category’s description
        :type description: str
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, name=name, description=description)

        data = self.generate_json(method=method, authToken=authToken, name=name, description=description)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        # look_for_error(data, req)
        if 'result' in req and 'itemId' in req['result'] and req['result']['itemId'] > 0:
            if req["result"]['itemId'] is None:
                return self.category_search(text=name)
            else:
                return req["result"]['itemId']
        else:
            return self.category_search(text=name)

    def category_delete(self, method="category/delete", authToken=None, cid=None):
        """
        category/delete

        Delete category

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        cid 	    int 	yes 	    Category’s Id
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, cid=cid)

        data = self.generate_json(method=method, authToken=authToken, cid=cid)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        look_for_error(data, req)

        print(req)
        if req["result"]["resultCode"] == 0:
            return req["result"]
        # else:
        #     raise AnsibleError("CategoryDelete Error : %s" % req)

    def client_search(self, method="client/search", authToken=None, text=None, count=None):
        """
        client/search

        Search for clients
        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        text 	    string 	no 	        Text to search for
        count 	    int 	no 	        Number of results to display
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, text=text, count=count)

        data = self.generate_json(method=method, authToken=authToken, text=text, count=count)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        # look_for_error(data, req)

        # We got a response
        if 'result' in req and 'count' in req['result'] and req['result']['count'] > 0:
            for res in req['result']['result']:
                if res['name'].upper() == text.upper():
                    return req['result']['result'][0]['id']
        # elif 'error' in req:
        #     raise AnsibleError('ClientSearch Error : %s' % (req['error']))
        else:
            return None

    def client_create(self, method="client/create", authToken=None, name=None, description=None, Global=False):
        """
        Creates a syspass client.

        :param method: must be 'client/create'
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param name: Client’s name
        :type name: str
        :param description: Client’s description
        :type description: str
        :param Global: Set client as global. It can be either 0 or 1
        :type Global: int
        """
        if authToken is None:
            authToken = self.authToken

        if Global is not None:
            Global = int(bool(Global))

        look_for_args(method=method, authToken=authToken, name=name, description=description, Global=Global)

        data = self.generate_json(method=method, authToken=authToken, name=name, description=description, Global=Global)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        # look_for_error(data, req)

        if 'result' in req and 'itemId' in req['result'] and req['result']['itemId'] > 0:
            return req['result']['itemId']

        return self.client_search(text=name)

    def client_delete(self, method='client/delete', authToken=None, cid=None):
        """
        client/delete

        Delete client

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        cid 	        int 	yes 	    Client’s Id

        :param method: must be 'client/create'
        :type method: str
        :param authToken: User’s API token
        :type: authToken: str
        :param cid: Client’s Id
        :type cid: int
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, cid=cid)

        data = self.generate_json(method=method, authToken=authToken, cid=cid)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        look_for_error(data, req)

        if 'result' in req and 'resultCode' in req['result'] and req['result']['resultCode'] == 0:
            return req['result']['resultCode']
        else:
            return None

    def tag_create(self, method='tag/create', authToken=None, name=None):
        """
        tag/create

        Create tag

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        name 	    string 	yes 	    Tag’s name

        :param method: must be "tag/search"
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param name: Tag’s name
        :type name: str
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, name=name)

        data = self.generate_json(method=method, authToken=authToken, name=name)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        # look_for_error(data, req)

        if 'result' in req and 'itemId' in req['result'] and req['result']['itemId'] > 0:
            return req['result']['itemId']

        return self.tag_search(text=name)

    def tag_search(self, method="tag/search", authToken=None, text=None, count=None):
        """
        Tags

        tag/search

        Search for tags

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        text 	    string 	no      	Text to search for
        count 	    int 	no 	        Number of results to display

        :param method: must be "tag/search"
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param text: Text to search for
        :type text: str
        :param count: Number of results to display
        :type count: int
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, text=text, count=count)

        data = self.generate_json(method=method, authToken=authToken, text=text, count=count)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        # look_for_error(data, req)

        if 'result' in req and 'count' in req['result'] and req['result']['count'] > 0:
            for res in req['result']['result']:
                if res['name'].upper() == text.upper():
                    return req['result']['result'][0]['id']
        # elif 'error' in req:
        #     raise AnsibleError('TagSearch Error : %s' % (req['error']))
        else:
            return None

    def tag_delete(self, method='tag/delete', authToken=None, tagid=None):
        """
        tag/delete

        Delete tag

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        id 	        int 	yes 	    Tag’s Id

        :param method: must be 'tag/delete'
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param tagid: Tag’s Id
        :type tagid: int
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, tagid=tagid)

        data = self.generate_json(method=method, authToken=authToken, tagid=tagid)

        self.increase_request_id()

        req = self.make_post_request(data)

        self.print_returned_value(req)

        look_for_error(data, req)

        if 'result' in req and 'resultCode' in req['result']:
            return req['result']['resultCode']
        else:
            return None
        # if req['result']['resultCode'] == 0:
        #     return req['result']
        # else:
        #     raise AnsibleError('TagDelete Error : %s' % (req))

    def user_group_create(self, method="userGroup/create", authToken=None, name=None, description=None, usersId=None):
        """
        userGroup/create

        Create user group

        Parameter 	    Type 	Required 	Description
        authToken 	    string 	yes 	    User’s API token
        name 	        string 	yes 	    User group’s name
        description 	string 	no 	        User group’s description
        usersId 	    array 	no 	        User group’s users Id

        :param method: must be 'userGroup/create'
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param name: User group’s name
        :type name: str
        :param description: User group’s description
        :type description: str
        :param usersId: User group’s users Id
        :type usersId: list
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, name=name, description=description, usersId=usersId)
        data = self.generate_json(
            method=method, authToken=authToken, name=name, description=description, usersId=usersId
        )
        self.increase_request_id()
        req = self.make_post_request(data)
        self.print_returned_value(req)

        # look_for_error(data, req)
        if 'result' in req and 'itemId' in req['result'] and req['result']['itemId'] > 0:
            return req["result"]["itemId"]

        return self.user_group_search(text=name)

    def user_group_search(self, method="userGroup/search", authToken=None, text=None, count=None):
        """
        Search for user groups

        userGroup/search

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        text    	string 	no 	        Text to search for
        count 	    int 	no 	        Number of results to display
        """

        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, text=text, count=count)
        data = self.generate_json(method=method, authToken=authToken, text=text, count=count)
        self.increase_request_id()
        req = self.make_post_request(data)
        self.print_returned_value(req)

        if 'result' in req and 'count' in req['result'] and req['result']['count'] > 0:
            for res in req['result']['result']:
                if res['name'].upper() == text.upper():
                    return req['result']['result'][0]['id']

        else:
            look_for_error(data, req)
            return None

    def user_group_delete(self,
                          method='userGroup/delete', authToken=None, ugid=None):
        """
        userGroup/delete

        Delete user group

        Parameter 	Type 	Required 	Description
        authToken 	string 	yes 	    User’s API token
        ugid 	    int 	yes 	    User group’s Id

        :param method: must be 'userGroup/delete'
        :type method: str
        :param authToken: User’s API token
        :type authToken: str
        :param ugid: User group’s Id
        :type ugid: int
        """
        if authToken is None:
            authToken = self.authToken

        look_for_args(method=method, authToken=authToken, ugid=ugid)
        data = self.generate_json(method=method, authToken=authToken, ugid=ugid)
        self.increase_request_id()
        req = self.make_post_request(data)
        self.print_returned_value(req)

        if 'result' in req and 'resultCode' in req['result'] and req['result']['resultCode'] == 0:
            return req['result']
        else:
            return None
            # look_for_error(data, req)

#
#     def Backup(self):
#         """
#         https://github.com/nuxsmin/sysPass/issues/1004#issuecomment-411487284
#         """
#         data = {"jsonrpc": "2.0",
#                 "method": "backup",
#                 "params": {
#                     "authToken": self.api_key,
#                 },
#                 "id": self.r_id
#                 }
#
#         self.r_id += 1
#         req = requests.post(self.api_url, json=data, verify=False)
#         if 'result' in req.json():
#             return req.json()['result']
#         else:
#             raise AnsibleError('Backup Error : %s' % (req.json()))
#
#

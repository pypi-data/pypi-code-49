#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from syspassclient import SyspassClient
from syspassclient import Config
from syspassclient import random_string

# try:
#     from yaml import CLoader as Loader, CDumper as Dumper
# except ImportError:
#     from yaml import Loader, Dumper


class TestSyspassClient(unittest.TestCase):
    def test_account_delete(self):
        # sp_client = SyspassClient()
        self.assertTrue(True)

    def test_AccountSearch(self):
        """Test"""
        sp_client = SyspassClient()
        conf = Config()

        self.assertRaises(TypeError, sp_client.account_view)
        self.assertRaises(TypeError, sp_client.account_view, authToken="Hello")
        self.assertRaises(TypeError, sp_client.account_view, authToken="Hello", tokenPass="Hello")
        self.assertRaises(TypeError, sp_client.account_view, authToken="Hello", tokenPass="Hello", hello=42)

        # prepare a category
        category_random_name = 'FOR_TEST'
        req = sp_client.category_create(
            authToken=conf.get_data()['authToken'],
            name=category_random_name,
            description='a Category for tests'
        )

        actual_category_id = req

        req = sp_client.category_search(
            authToken=conf.get_data()['authToken'],
            text=category_random_name
        )

        found_category_id = req

        self.assertEqual(actual_category_id, found_category_id)

        # create a client
        client_random_name = 'FOR_TEST'
        req = sp_client.client_create(
            authToken=conf.get_data()['authToken'],

            name=client_random_name,
            description='a Client for tests'
        )
        actual_client_id = req

        req = sp_client.client_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )

        found_client_id = req

        self.assertEqual(actual_client_id, found_client_id)

        # group
        random_group_name = 'FOR_TEST'
        req = sp_client.user_group_create(
            authToken=conf.get_data()['authToken'],
            name=random_group_name,
            description='a UserGroup for test'
        )
        ugid = req

        req = sp_client.user_group_search(
            authToken=conf.get_data()['authToken'],
            text=random_group_name
        )

        found_ugid = req

        self.assertEqual(ugid, found_ugid)

        # create the account
        random_name = random_string(length=20, prefix='account_test_')
        random_password = random_string(length=20)

        req = sp_client.account_create(
            authToken=conf.get_data()['authToken'],
            tokenPass=conf.get_data()['tokenPass'],
            name=random_name,
            categoryId=int(actual_category_id),
            clientId=int(actual_client_id),
            password=random_password,
            userGroupId=int(ugid)
        )
        actual_account_id = req

        # Case where nothing is found
        rep = sp_client.account_search(text=random_name)
        self.assertIsNotNone(rep)
        self.assertEqual(type(req), int)

        # clean up
        sp_client.account_delete(
            authToken=conf.get_data()['authToken'],
            account_id=actual_account_id
        )

        req = sp_client.account_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )
        self.assertIsNone(req)

        # authToken - must be set and be a str
        self.assertRaises(TypeError, sp_client.account_search, authToken=42)

        # text - can be None, if not must be a str
        self.assertRaises(TypeError, sp_client.account_search, authToken=conf.get_data()['authToken'], text=42)
        # count - can be None, if not must be a int
        self.assertRaises(TypeError, sp_client.account_search, authtoken=conf.get_data()['authToken'], count="Hello")
        # category_id - can be None, if not must be a int
        self.assertRaises(TypeError, sp_client.account_search, authToken=conf.get_data()['authToken'],
                          categoryId="Hello")
        # client_id - can be None, if not must be a int
        self.assertRaises(TypeError, sp_client.account_search, authToken=conf.get_data()['authToken'],
                          categoryId="Hello")
        # tags_id - can be None, if not must be a int
        self.assertRaises(TypeError, sp_client.account_search, authToken=conf.get_data()['authToken'],
                          categoryId="Hello")
        # op - can be None or only have 'and' or 'or' value
        self.assertRaises(TypeError, sp_client.account_search, authToken=conf.get_data()['authToken'], op=42)
        # self.assertRaises(AssertionError, sp_client.account_search,
        #                   authtoken=self.authtoken,
        #                   op='Hello'
        #                   )
        self.assertRaises(TypeError, sp_client.account_search, authToken=conf.get_data()['authToken'], match_all=42)

        # Test without require args
        # self.assertRaises(TypeError, sp_client.account_search)

    def test_AccountView(self):
        sp_client = SyspassClient()
        conf = Config()

        self.assertRaises(TypeError, sp_client.account_view)
        self.assertRaises(TypeError, sp_client.account_view, authToken="Hello")
        self.assertRaises(TypeError, sp_client.account_view, authToken="Hello", tokenPass="Hello")
        self.assertRaises(TypeError, sp_client.account_view, authToken="Hello", tokenPass="Hello", hello=42)

        # Normal case

        # prepare a category
        category_random_name = 'FOR_TEST'
        req = sp_client.category_create(
            authToken=conf.get_data()['authToken'],
            name=category_random_name,
            description='a Category for tests'
        )

        actual_category_id = req

        req = sp_client.category_search(
            authToken=conf.get_data()['authToken'],
            text=category_random_name
        )

        found_category_id = req

        self.assertEqual(actual_category_id, found_category_id)

        # create a client
        client_random_name = 'FOR_TEST'
        req = sp_client.client_create(
            authToken=conf.get_data()['authToken'],

            name=client_random_name,
            description='a Client for tests'
        )
        actual_client_id = req

        req = sp_client.client_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )

        found_client_id = req

        self.assertEqual(actual_client_id, found_client_id)

        # group
        random_group_name = 'FOR_TEST'
        req = sp_client.user_group_create(
            authToken=conf.get_data()['authToken'],
            name=random_group_name,
            description='a UserGroup for test'
        )
        ugid = req

        req = sp_client.user_group_search(
            authToken=conf.get_data()['authToken'],
            text=random_group_name
        )

        found_ugid = req

        self.assertEqual(ugid, found_ugid)

        # create the account
        random_name = random_string(length=20, prefix='account_test_')
        random_password = random_string(length=20)

        req = sp_client.account_create(
            authToken=conf.get_data()['authToken'],
            tokenPass=conf.get_data()['tokenPass'],
            name=random_name,
            categoryId=int(actual_category_id),
            clientId=int(actual_client_id),
            password=random_password,
            userGroupId=int(ugid)
        )
        actual_account_id = req

        req = sp_client.account_view(
            authToken=conf.get_data()['authToken'],
            tokenPass=conf.get_data()['tokenPass'],
            account_id=actual_account_id
        )

        self.assertIsNotNone(req)
        self.assertTrue('dateAdd' in req)

        # clean up
        sp_client.account_delete(
            authToken=conf.get_data()['authToken'],
            account_id=actual_account_id
        )

        req = sp_client.account_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )
        self.assertIsNone(req)

    def test_AccountViewpass(self):
        """Test"""

        sp_client = SyspassClient()
        conf = Config()

        # prepare a category
        category_random_name = 'FOR_TEST'
        req = sp_client.category_create(
            authToken=conf.get_data()['authToken'],
            name=category_random_name,
            description='a Category for tests'
        )

        actual_category_id = req

        req = sp_client.category_search(
            authToken=conf.get_data()['authToken'],
            text=category_random_name
        )

        found_category_id = req

        self.assertEqual(actual_category_id, found_category_id)

        # create a client
        client_random_name = 'FOR_TEST'
        req = sp_client.client_create(
            authToken=conf.get_data()['authToken'],

            name=client_random_name,
            description='a Client for tests'
        )
        actual_client_id = req

        req = sp_client.client_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )

        found_client_id = req

        self.assertEqual(actual_client_id, found_client_id)

        # group
        random_group_name = 'FOR_TEST'
        req = sp_client.user_group_create(
            authToken=conf.get_data()['authToken'],
            name=random_group_name,
            description='a UserGroup for test'
        )
        ugid = req

        req = sp_client.user_group_search(
            authToken=conf.get_data()['authToken'],
            text=random_group_name
        )

        found_ugid = req

        self.assertEqual(ugid, found_ugid)

        # create the account
        random_name = random_string(length=20, prefix='account_test_')
        random_password = random_string(length=20)

        req = sp_client.account_create(
            authToken=conf.get_data()['authToken'],
            tokenPass=conf.get_data()['tokenPass'],
            name=random_name,
            categoryId=int(actual_category_id),
            clientId=int(actual_client_id),
            password=random_password,
            userGroupId=int(ugid)
        )
        actual_account_id = req

        rep = sp_client.account_viewpass(
            account_id=actual_account_id
        )

        self.assertIsNotNone(rep)
        self.assertEqual(type(rep), str)

        # clean up
        sp_client.account_delete(
            authToken=conf.get_data()['authToken'],
            account_id=actual_account_id
        )

        req = sp_client.account_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )
        self.assertIsNone(req)

    def test_AccountEditPass(self):
        # user_name_to_test = "test"
        # sp_client = SyspassClient()
        self.assertTrue(True)

        # req = sp_client.AccountSearch(text="Charles Palmolive", authToken=self.authToken)

        # categoryId = sp_client.category_search(text=user_name_to_test, count=1)
        # if isinstance(categoryId, dict):
        #     categoryId = categoryId["id"]
        # else:
        #     categoryId = sp_client.category_create(name=user_name_to_test)["itemId"]
        #
        # userGroupId = sp_client.user_group_search(text=user_name_to_test, count=1)
        # if isinstance(userGroupId, dict):
        #     userGroupId = userGroupId['id']
        # else:
        #     userGroupId = sp_client.user_group_create(
        #         name=user_name_to_test,
        #         description=user_name_to_test)['itemId']
        #
        # user_exist = sp_client.AccountSearch(text=user_name_to_test, authToken=self.authToken)

        # if user_exist is None:
        #     sp_client.AccountCreate(
        #             authToken=self.authToken,
        #             tokenPass=self.tokenPass,
        #             name=user_name_to_test,
        #             categoryId=categoryId,
        #             userGroupId=userGroupId,
        #             password=random_string()
        #         )

    def test_AccountCreate(self):
        """Test"""
        sp_client = SyspassClient()
        conf = Config()

        # prepare a category
        category_random_name = 'FOR_TEST'
        req = sp_client.category_create(
            authToken=conf.get_data()['authToken'],
            name=category_random_name,
            description='a Category for tests'
        )

        actual_category_id = req

        req = sp_client.category_search(
            authToken=conf.get_data()['authToken'],
            text=category_random_name
        )

        found_category_id = req

        self.assertEqual(actual_category_id, found_category_id)

        # create a client
        client_random_name = 'FOR_TEST'
        req = sp_client.client_create(
            authToken=conf.get_data()['authToken'],

            name=client_random_name,
            description='a Client for tests'
        )
        actual_client_id = req

        req = sp_client.client_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )

        found_client_id = req

        self.assertEqual(actual_client_id, found_client_id)

        # group
        random_group_name = 'FOR_TEST'
        req = sp_client.user_group_create(
            authToken=conf.get_data()['authToken'],
            name=random_group_name,
            description='a UserGroup for test'
        )
        ugid = req

        req = sp_client.user_group_search(
            authToken=conf.get_data()['authToken'],
            text=random_group_name
        )

        found_ugid = req

        self.assertEqual(ugid, found_ugid)

        # create the account
        random_name = random_string(length=20, prefix='account_test_')
        random_password = random_string(length=20)

        req = sp_client.account_create(
            authToken=conf.get_data()['authToken'],
            tokenPass=conf.get_data()['tokenPass'],
            name=random_name,
            categoryId=int(actual_category_id),
            clientId=int(actual_client_id),
            password=random_password,
            userGroupId=int(ugid)
        )
        actual_account_id = req

        # sp_client.category_delete(
        #     authToken=conf.get_data()['authToken'],
        #     cid=actual_category_id
        # )
        # req = sp_client.category_search(
        #     authToken=self.authToken,
        #     text=category_random_name
        # )
        # self.assertIsNone(req)

        # clean everything
        # sp_client.client_delete(
        #     authToken=conf.get_data()['authToken'],
        #     cid=actual_client_id
        # )
        # req = sp_client.client_search(
        #     authToken=conf.get_data()['authToken'],
        #     text=client_random_name
        # )
        # self.assertIsNone(req)

        # clean up
        sp_client.account_delete(
            authToken=conf.get_data()['authToken'],
            account_id=actual_account_id
        )

        req = sp_client.account_search(
            authToken=conf.get_data()['authToken'],
            text=client_random_name
        )
        self.assertIsNone(req)

    def test_Categories(self):
        sp_client = SyspassClient()
        conf = Config()

        random_name = random_string()
        req = sp_client.category_create(
            name=random_name,
            description='a Client for tests'
        )
        cid = req

        req = sp_client.category_search(
            text=random_name
        )

        found_cid = req

        self.assertEqual(cid, found_cid)

        sp_client.category_delete(
            cid=cid
        )
        # Try to re-create a deleted category
        # import time
        # time.sleep(15)
        req = sp_client.category_create(
            authToken=conf.get_data()['authToken'],
            name=random_name,
            description='a Client for tests'
        )
        cid1 = req

        req = sp_client.category_create(
            authToken=conf.get_data()['authToken'],
            name=random_name,
            description='a Client for tests'
        )
        cid2 = req

        self.assertEqual(cid1, cid2)
        sp_client.category_delete(
            authToken=conf.get_data()['authToken'],
            cid=cid1
        )

    def test_Clients(self):
        sp_client = SyspassClient()
        conf = Config()

        random_name = random_string()
        req = sp_client.client_create(
            authToken=conf.get_data()['authToken'],
            name=random_name,
            description='a Client for tests'
        )
        cid = req

        req = sp_client.client_search(
            text=random_name
        )

        found_cid = req

        self.assertEqual(cid, found_cid)

        sp_client.client_delete(
            cid=cid
        )
        self.assertIsNone(sp_client.client_delete(
            cid=cid
        ))

    def test_Tags(self):
        sp_client = SyspassClient()
        conf = Config()

        random_name = random_string()
        req = sp_client.tag_create(
            authToken=conf.get_data()['authToken'],
            name=random_name
        )
        tagid = req

        req = sp_client.tag_search(
            authToken=conf.get_data()['authToken'],
            text=random_name
        )

        found_tagid = req

        self.assertEqual(tagid, found_tagid)

        req = sp_client.tag_delete(
            authToken=conf.get_data()['authToken'],
            tagid=tagid
        )
        self.assertEqual(0, req)

        self.assertIsNone(sp_client.tag_delete(
            tagid=tagid
        ))

    def test_UserGroup(self):
        sp_client = SyspassClient()
        conf = Config()

        random_name = random_string()

        self.assertIsNone(sp_client.user_group_search(text=random_name))

        req = sp_client.user_group_create(
            authToken=conf.get_data()['authToken'],
            name=random_name,
            description='a UserGroup for test'
        )
        ugid = req

        self.assertEqual(ugid, sp_client.user_group_create(
            name=random_name,
            description='a UserGroup for test'
        ))
        # self.assertIsNone(sp_client.user_group_create(
        #     name=random_name,
        #     description='a UserGroup for test'
        # )
        # )

        req = sp_client.user_group_search(
            authToken=conf.get_data()['authToken'],
            text=random_name
        )

        found_ugid = req

        self.assertEqual(ugid, found_ugid)

        sp_client.user_group_delete(
            authToken=conf.get_data()['authToken'],
            ugid=ugid
        )

        # test if it return None in case of error
        self.assertIsNone(sp_client.user_group_delete(
            ugid=ugid
        ))

    def test_SyspassClient_api_url_property(self):
        """Test SyspassClient.api_url property  """
        sp_client = SyspassClient()
        sp_client.api_url = "http://perdu.com"
        sp_client.authToken = "Hello"
        sp_client.tokenPass = "Hello"
        # check if the init have work
        self.assertEqual(sp_client.api_url, "http://perdu.com")

        # Check with a malformed URL
        # Test Raise
        self.assertEqual(sp_client.api_url, "http://perdu.com")

        # Check if ve can back to default value, that suppose to be None
        sp_client.api_url = None
        self.assertEqual(sp_client.api_url, None)

        # Check Raise
        self.assertRaises(ValueError, setattr, sp_client, "api_url", "Hello")
        self.assertRaises(TypeError, setattr, sp_client, "api_url", 42)

    def test_SyspassClient_api_key(self):
        """Test SyspassClient.api_url property  """
        # check if the init have work
        sp_client = SyspassClient()
        sp_client.api_url = "http://perdu.com"
        sp_client.authToken = "Hello"
        sp_client.tokenPass = ""
        self.assertEqual(sp_client.authToken, "Hello")

        # Check if we can back to default value
        sp_client.authToken = "Hello"
        self.assertEqual(sp_client.authToken, "Hello")
        sp_client.authToken = None
        self.assertEqual(sp_client.authToken, None)
        sp_client.authToken = "Hello"
        self.assertEqual(sp_client.authToken, "Hello")
        sp_client.authToken = ""
        self.assertEqual(sp_client.authToken, None)
        # Test Raise
        self.assertRaises(TypeError, setattr, sp_client, "authToken", 42)

    def test_SyspassClient_tokenPass(self):
        """Test SyspassClient.api_acc_tokpwd property  """
        # check if the init have work
        sp_client = SyspassClient()
        sp_client.api_url = "http://perdu.com"
        sp_client.authToken = "Hello"
        sp_client.tokenPass = "Hello"
        self.assertEqual(sp_client.tokenPass, "Hello")

        # Check if we can back to default value
        sp_client.tokenPass = "Hello2"
        self.assertEqual(sp_client.tokenPass, "Hello2")
        sp_client.tokenPass = None
        self.assertEqual(sp_client.tokenPass, None)
        sp_client.tokenPass = "Hello"
        self.assertEqual(sp_client.tokenPass, "Hello")
        sp_client.tokenPass = ""
        self.assertEqual(sp_client.tokenPass, None)

        # Test Raise
        self.assertRaises(TypeError, setattr, sp_client, "authToken", 42)

    def test_generate_json(self):
        sp_client = SyspassClient()
        data = sp_client.generate_json(method="account/viewPass")
        self.assertEqual({"id": 1, "jsonrpc": "2.0", "method": "account/viewPass", "params": {}}, data)
        self.assertRaises(KeyError, sp_client.generate_json)

    def test_increase_request_id(self):
        sp_client = SyspassClient()
        self.assertEqual(sp_client.r_id, 1)
        sp_client.increase_request_id(increment=1)
        self.assertEqual(sp_client.r_id, 2)
        sp_client.increase_request_id(increment=42)
        self.assertEqual(sp_client.r_id - 2, 42)
        self.assertRaises(TypeError, sp_client.increase_request_id, increment="Hello")
        self.assertRaises(ValueError, sp_client.increase_request_id, increment=0)
        self.assertRaises(ValueError, sp_client.increase_request_id, increment=-42)


if __name__ == "__main__":
    unittest.main()

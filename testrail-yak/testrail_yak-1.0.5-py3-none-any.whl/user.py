#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class User:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_users(self):
        """Get a list of TestRail users.

        :return: response from TestRail API containing the user collection
        """
        try:
            result = self.client.send_get("get_users")
        except APIError as error:
            raise error
        else:
            return result

    def get_user(self, user_id):
        """Get a TestRail user by user_id.

        :param user_id: user ID of the user we want to grab
        :return: response from TestRail API containing the user
        """
        if not user_id or user_id is None:
            raise APIValidationError("[!] Invalid user_id")

        try:
            result = self.client.send_get("get_user/{}".format(user_id))
        except APIError as error:
            raise error
        else:
            return result

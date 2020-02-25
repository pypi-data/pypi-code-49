#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class TestSuite:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api
        self._fields = [
            "description"
        ]

    def get_test_suites(self, project_id):
        """Get a list of test suites associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test suites
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        try:
            result = self.client.send_get("get_suites/{}".format(project_id))
        except APIError as error:
            raise error
        else:
            return result

    def get_test_suite(self, suite_id):
        """Get a test suite by suite_id.

        :param suite_id: ID of the test suite
        :return: response from TestRail API containing the test suites
        """
        if not suite_id or suite_id is None:
            raise APIValidationError("[*] Invalid suite_id")

        if type(suite_id) not in [int, float]:
            raise APIValidationError("[*] suite_id must be an int or float")

        if suite_id <= 0:
            raise APIValidationError("[*] suite_id must be > 0")

        try:
            result = self.client.send_get("get_suite/{}".format(suite_id))
        except APIError as error:
            raise error
        else:
            return result

    def add_test_suite(self, project_id, name, data):
        """Add a new test suite to a TestRail project.

        :param project_id: ID of the TestRail project
        :param name: name of the new TestRail test suite
        :param data: request data dictionary
        :return: response from TestRail API containing the newly created test suite
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        if not name or name is None:
            raise APIValidationError("[*] Invalid suite name. Unable to add test suite.")

        data = self._validate_data(data)

        try:
            result = self.client.send_post("add_suite/{}".format(project_id), data)
        except APIError as error:
            raise error
        else:
            return result

    def _validate_data(self, data_dict):
        """Field validation static method that I may pull out and use everywhere if it works well.

        :param data_dict:
        :return:
        """
        def _valid_key(field):
            return field in self._fields

        def _valid_value(value):
            return value is not None and value is not ""

        _valid = dict()
        for k, v in data_dict.items():

            print("[debug] Valid key:\t", _valid_key(k),
                  "\tValid value:\t", _valid_value(v))

            if _valid_key(k) and _valid_value(v):
                _valid[k] = v

        return _valid

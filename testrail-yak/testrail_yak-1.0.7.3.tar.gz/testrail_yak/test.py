#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class Test:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_run_tests(self, run_id):
        """Get a collection of individual tests by run_id.

        :param run_id: ID of the test run
        :return: response from TestRail API containing the test cases
        """
        if not run_id or run_id is None:
            raise APIValidationError("[*] Invalid run_id")

        if type(run_id) not in [int, float]:
            raise APIValidationError("[*] run_id must be an int or float")

        if run_id <= 0:
            raise APIValidationError("[*] run_id must be > 0")

        try:
            result = self.client.send_get("get_tests/{}".format(run_id))
        except APIError as error:
            raise error
        else:
            return result

    def get_test_run_test(self, test_id):
        """Get an individual test.

        :param test_id: ID of the individual test
        :return: response from TestRail API containing the test
        """
        if not test_id or test_id is None:
            raise APIValidationError("[*] Invalid test_id")

        if type(test_id) not in [int, float]:
            raise APIValidationError("[*] test_id must be an int or float")

        if test_id <= 0:
            raise APIValidationError("[*] test_id must be > 0")

        try:
            result = self.client.send_get("get_test/{}".format(test_id))
        except APIError as error:
            raise error
        else:
            return result

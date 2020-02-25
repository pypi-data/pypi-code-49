#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class TestCase:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api
        self._fields = [
            "title",
            "template_id",
            "type_id",
            "priority_id",
            "estimate",
            "milestone_id",
            "refs",
        ]

    def get_test_cases(self, project_id):
        """Get a list of test cases associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test cases
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        try:
            result = self.client.send_get("get_cases/{}".format(project_id))
        except APIError as error:
            raise error
        else:
            return result

    def get_test_case(self, case_id):
        """Get a test case by case_id.

        :param case_id: ID of the test case
        :return: response from TestRail API containing the test cases
        """
        if not case_id or case_id is None:
            raise APIValidationError("[*] Invalid case_id")

        if type(case_id) not in [int, float]:
            raise APIValidationError("[*] case_id must be an int or float")

        if case_id <= 0:
            raise APIValidationError("[*] case_id must be > 0")

        try:
            result = self.client.send_get("get_case/{}".format(case_id))
        except APIError as error:
            raise error
        else:
            return result

    def add_test_case(self, section_id, title, data):
        """Add a test case to a project by section_id.

        :param section_id: ID of the TestRail section
        :param title: title of the test case
        :param data:
        :return: response from TestRail API containing the newly created test case
        """
        if not section_id or section_id is None:
            raise APIValidationError("[*] Invalid section_id.")

        if type(section_id) not in [int, float]:
            raise APIValidationError("[*] section_id must be an int or float.")

        if section_id <= 0:
            raise APIValidationError("[*] section_id must be > 0.")

        if not title or title is None:
            raise APIValidationError("[*] Test case title required.")

        data["title"] = title
        data = self._validate_data(data)

        try:
            result = self.client.send_post("add_case/{}".format(section_id), data)
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

            # print("[debug] Key:\t{} \tValid:\t{} ".format(k, _valid_key(k)),
            #       " Value:\t{} \tValid:\t{} ".format(v, _valid_value(v)))

            if _valid_key(k) and _valid_value(v):
                _valid[k] = v

        return _valid

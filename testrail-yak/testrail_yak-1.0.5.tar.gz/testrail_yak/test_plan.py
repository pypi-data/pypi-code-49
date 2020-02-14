#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class TestPlan:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api
        self._plan_fields = [
            "description",
            "milestone_id"
        ]
        self._entry_fields = [
            "name",
            "description",
            "assignedto_id",
            "include_all",
            "case_ids",
        ]

    def get_test_plans(self, project_id):
        """Get a list of test plans associated with a given project_id.

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
            result = self.client.send_get("get_plans/{}".format(project_id))
        except APIError as error:
            raise error
        else:
            return result

    def get_test_plan(self, plan_id):
        """Get a test plan by plan_id.

        :param plan_id: ID of the test plan
        :return: response from TestRail API containing the test cases
        """
        if not plan_id or plan_id is None:
            raise APIValidationError("[*] Invalid plan_id")

        if type(plan_id) not in [int, float]:
            raise APIValidationError("[*] plan_id must be an int or float")

        if plan_id <= 0:
            raise APIValidationError("[*] plan_id must be > 0")

        try:
            result = self.client.send_get("get_plan/{}".format(plan_id))
        except APIError as error:
            raise error
        else:
            return result

    def add_test_plan(self, project_id, name, data, entries=None):
        """Add a test plan to a project.

        :param project_id: ID of the TestRail project
        :param name: title of the test plan
        :param data: request data dictionary
        :param entries: test plan entries
        :return: response from TestRail API containing the newly created test plan
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id.")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float.")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0.")

        if not name or name is None:
            raise APIValidationError("[*] Test plan name value required.")

        data = self._validate_data(data)

        if entries is not None and len(entries) > 0:
            data["entries"] = entries

        try:
            result = self.client.send_post("add_plan/{}".format(project_id), data)
        except APIError as error:
            raise error
        else:
            return result

    def add_plan_entry(self, plan_id, suite_id, name, data):

        if not plan_id or plan_id is None:
            raise APIValidationError("[*] Invalid plan_id.")

        if type(plan_id) not in [int, float]:
            raise APIValidationError("[*] plan_id must be an int or float.")

        if plan_id <= 0:
            raise APIValidationError("[*] plan_id must be > 0.")

        if not suite_id or suite_id is None:
            raise APIValidationError("[*] Invalid suite_id.")

        if type(suite_id) not in [int, float]:
            raise APIValidationError("[*] suite_id must be an int or float.")

        if suite_id <= 0:
            raise APIValidationError("[*] suite_id must be > 0.")

        if not name or name is None:
            raise APIValidationError("[*] Test plan name value required.")

        data = self._validate_data(data, entry=True)

        raise NotImplementedError

    def update_plan(self, plan_id, data, name=None):

        if not plan_id or plan_id is None:
            raise APIValidationError("[*] Invalid plan_id.")

        if type(plan_id) not in [int, float]:
            raise APIValidationError("[*] plan_id must be an int or float.")

        if plan_id <= 0:
            raise APIValidationError("[*] plan_id must be > 0.")

        data = self._validate_data(data)

        if name is not None:
            data["name"] = name

        raise NotImplementedError

    def update_plan_entry(self, plan_id, entry_id, data):

        if not plan_id or plan_id is None:
            raise APIValidationError("[*] Invalid plan_id.")

        if type(plan_id) not in [int, float]:
            raise APIValidationError("[*] plan_id must be an int or float.")

        if plan_id <= 0:
            raise APIValidationError("[*] plan_id must be > 0.")

        if not entry_id or entry_id is None:
            raise APIValidationError("[*] Invalid entry_id.")

        if type(entry_id) not in [int, float]:
            raise APIValidationError("[*] entry_id must be an int or float.")

        if entry_id <= 0:
            raise APIValidationError("[*] entry_id must be > 0.")

        data = self._validate_data(data, entry=True)

        raise NotImplementedError

    def close_plan(self, plan_id):

        if not plan_id or plan_id is None:
            raise APIValidationError("[*] Invalid plan_id.")

        if type(plan_id) not in [int, float]:
            raise APIValidationError("[*] plan_id must be an int or float.")

        if plan_id <= 0:
            raise APIValidationError("[*] plan_id must be > 0.")

        raise NotImplementedError

    def delete_plan(self, plan_id):

        if not plan_id or plan_id is None:
            raise APIValidationError("[*] Invalid plan_id.")

        if type(plan_id) not in [int, float]:
            raise APIValidationError("[*] plan_id must be an int or float.")

        if plan_id <= 0:
            raise APIValidationError("[*] plan_id must be > 0.")

        raise NotImplementedError

    def delete_plan_entry(self, plan_id, entry_id):

        if not plan_id or plan_id is None:
            raise APIValidationError("[*] Invalid plan_id.")

        if type(plan_id) not in [int, float]:
            raise APIValidationError("[*] plan_id must be an int or float.")

        if plan_id <= 0:
            raise APIValidationError("[*] plan_id must be > 0.")

        if not entry_id or entry_id is None:
            raise APIValidationError("[*] Invalid entry_id.")

        if type(entry_id) not in [int, float]:
            raise APIValidationError("[*] entry_id must be an int or float.")

        if entry_id <= 0:
            raise APIValidationError("[*] entry_id must be > 0.")

        raise NotImplementedError

    def _validate_data(self, data_dict, entry=False):
        """Field validation static method that I may pull out and use everywhere if it works well.

        :param data_dict:
        :param entry:
        :return:
        """
        if entry is None or type(entry) != bool:
            raise APIValidationError("[!] caller required for validation.")

        def _valid_key(field):
            if entry:
                return field in self._entry_fields
            else:
                return field in self._plan_fields

        def _valid_value(value):
            return value is not None and value is not ""

        _valid = dict()
        for k, v in data_dict.items():

            print("[debug] Valid key:\t", _valid_key(k),
                  "\tValid value:\t", _valid_value(v))

            if _valid_key(k) and _valid_value(v):
                _valid[k] = v

        return _valid

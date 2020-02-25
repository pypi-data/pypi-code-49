#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class TestRun:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api
        self._fields = [
            "description",
            "milestone_id",
            "include_all",
            "case_ids",
            "refs"
        ]

    def get_test_runs(self, project_id):
        """Get a list of test runs associated with a given project_id.

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
            result = self.client.send_get("get_runs/{}".format(project_id))
        except APIError as error:
            raise error
        else:
            return result

    def get_test_run(self, run_id):
        """Get a test run by run_id.

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
            result = self.client.send_get("get_run/{}".format(run_id))
        except APIError as error:
            raise error
        else:
            return result

    def add_test_run(self, project_id, name, data):
        """Add a test run to a project.

        Supported fields:

            suite_id (int)
                The ID of the test suite for the test run (optional if the project is operating in single suite mode, required otherwise)

            name (string)
                The name of the test run

            description (string)
                The description of the test run

            milestone_id (int)
                The ID of the milestone to link to the test run

            assignedto_id
                int
                The ID of the user the test run should be assigned to

            include_all	(bool)
                True for including all test cases of the test suite and false for a custom case selection (default: true)

            case_ids (array)
                An array of case IDs for the custom case selection

            refs (string)
                A comma-separated list of references/requirements

        :param project_id: ID of the TestRail project
        :param name:
        :param data: request data dictionary
        :return: response from TestRail API containing the newly created test run
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id.")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float.")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0.")

        if not name or name is None:
            raise APIValidationError("[*] Test run name value required.")

        if not data or data is None:
            raise APIValidationError("[*] data cannot be empty")

        data = self._validate_data(data)

        try:
            result = self.client.send_post("add_run/{}".format(project_id), data)
        except APIError as error:
            raise error
        else:
            return result

    def update_test_run(self, run_id, data, name=None):
        """Update a test run in a project.

        Supported fields:

            name (string)
                The name of the test run

            description (string)
                The description of the test run

            milestone_id (int)
                The ID of the milestone to link to the test run

            include_all	(bool)
                True for including all test cases of the test suite and false for a custom case selection (default: true)

            case_ids (array)
                An array of case IDs for the custom case selection

            refs (string)
                A comma-separated list of references/requirements

        :param run_id:
        :param data: request data dictionary
        :param name:
        :return:
        """
        if not run_id or run_id is None:
            raise APIValidationError("[*] Invalid run_id.")

        if type(run_id) not in [int, float]:
            raise APIValidationError("[*] run_id must be an int or float.")

        if run_id <= 0:
            raise APIValidationError("[*] run_id must be > 0.")

        if not data or data is None:
            raise APIValidationError("[*] data cannot be empty")

        data = self._validate_data(data)

        if name is not None:
            data["name"] = name

        try:
            result = self.client.send_post("update_run/{}".format(run_id), data)
        except APIError as error:
            raise error
        else:
            return result

    def close_test_run(self, run_id):
        """Close out a test run.

        :param run_id:
        :return:
        """
        if not run_id or run_id is None:
            raise APIValidationError("[*] Invalid run_id.")

        if type(run_id) not in [int, float]:
            raise APIValidationError("[*] run_id must be an int or float.")

        if run_id <= 0:
            raise APIValidationError("[*] run_id must be > 0.")

        try:
            result = self.client.send_post("close_run/{}".format(run_id))
        except APIError as error:
            raise error
        else:
            return result

    def delete_test_run(self, run_id):
        """Delete out a test run.

        :param run_id:
        :return:
        """
        if not run_id or run_id is None:
            raise APIValidationError("[*] Invalid run_id.")

        if type(run_id) not in [int, float]:
            raise APIValidationError("[*] run_id must be an int or float.")

        if run_id <= 0:
            raise APIValidationError("[*] run_id must be > 0.")

        try:
            result = self.client.send_post("delete_run/{}".format(run_id))
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

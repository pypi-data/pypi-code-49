#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class Project:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api
        self._fields = [
            "announcement",
            "show_announcement",
            "suite_mode"
        ]

    def _suite_mode(self, project_id):
        """Figure out the suite_mode value of a given project.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the project
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")
        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")
        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        try:
            p = self.get_project(project_id)
        except APIError as error:
            raise error
        else:
            sadf = p["suite_mode"]
            return sadf

    def get_projects(self):
        """Get all projects from the TestRail API."""
        try:
            result = self.client.send_get("get_projects")
        except APIError as error:
            raise error
        else:
            return result

    def get_project(self, project_id):
        """Get a single project from the TestRail API by passing in its project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the project
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        try:
            result = self.client.send_get("get_project/{}".format(project_id))
        except APIError as error:
            raise error
        else:
            return result

    def add_project(self, name, data):
        """Add a new project to TestRail.

        :param name: name of the new TestRail project
        :param data: request data dictionary
        :return: response from TestRail API containing the newly created project
        """
        if not name or name is None:
            raise APIValidationError("[*] Invalid project name. Unable to create new project.")

        proj_data = self._validate_data(data)
        proj_data["name"] = name

        try:
            result = self.client.send_post("add_project", proj_data)
        except APIError as error:
            raise error
        else:
            return result

    def update_project(self, project_id, data, name=None, is_completed=False):

        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        proj_data = self._validate_data(data)

        raise NotImplementedError

    def delete_project(self, project_id):

        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        raise NotImplementedError

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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class Section:
    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api
        self._fields = [
            "name",
        ]

    def get_sections(self, project_id, suite_id=None):
        """Get a list of test sections associated with a project_id and an optional suite_id

        :param project_id:
        :param suite_id:
        :return: response from TestRail API containing the collection of sections
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        if suite_id is not None:
            if type(suite_id) not in [int, float]:
                raise APIValidationError("[*] suite_id must be an int or float")

            if suite_id <= 0:
                raise APIValidationError("[*] suite_id must be > 0")

            try:
                result = self.client.send_get("get_sections/{}&suite_id={}".format(project_id, suite_id))
            except APIError as error:
                raise error

        else:
            try:
                result = self.client.send_get("get_sections/{}".format(project_id))
            except APIError as error:
                raise error

        return result

    def get_section(self, section_id):
        """Get test section from a test suite by section_id.

        :param section_id: section ID to grab section from
        :return: response from TestRail API containing the test section
        """
        if not section_id or section_id is None:
            raise APIValidationError("[*] Invalid section_id")

        if type(section_id) not in [int, float]:
            raise APIValidationError("[*] section_id must be an int or float")

        if section_id <= 0:
            raise APIValidationError("[*] section_id must be > 0")

        try:
            result = self.client.send_get("get_section/{}".format(section_id))
        except APIError as error:
            raise error
        else:
            return result

    def add_sprint_section(self, project_id, data):
        """Add a new section representing a "sprint" to a TestRail project.

        For readability, this separate method is just for adding parent sections (Jira sprints) vs child sections (Jira stories).

        To populate a new child section with a Jira story, use add_story_section() and give it the id value returned here.

        :param project_id: project ID of the TestRail project
        :param data: request data dictionary
        :return: response from TestRail API containing the newly created test section
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        sect_data = self._validate_data(data)

        try:
            result = self.client.send_post("add_section/{}".format(project_id), sect_data)
        except APIError as error:
            raise error
        else:
            return result

    def add_story_section(self, project_id, parent_id, data):
        """Add a new section representing a "story" to a TestRail project.

        This section will be assigned to a parent/child relationship with a parent section, thus parent_id is required.

        Use the id value returned by add_sprint_section as the parent_id.

        Because of this parent id requirement, no suite_id will be needed. If it is ever used in the future, add_sprint_section is the more appropriate place for it.

        :param project_id: project ID of the TestRail project
        :param parent_id: section ID of the parent section (to build section hierarchies)
        :param data: request data dictionary
        :return: response from TestRail API containing the newly created test section
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        sect_data = self._validate_data(data)

        if parent_id is not None:
            if type(parent_id) not in [int, float]:
                raise APIValidationError("[*] parent_id must be an int or float")

            if parent_id <= 0:
                raise APIValidationError("[*] parent_id must be > 0")

            sect_data["parent_id"] = parent_id

        try:
            result = self.client.send_post("add_section/{}".format(project_id), sect_data)
        except APIError as error:
            raise error
        else:
            return result

    def update_section(self, section_id, data):

        if not section_id or section_id is None:
            raise APIValidationError("[*] Invalid section_id")

        if type(section_id) not in [int, float]:
            raise APIValidationError("[*] section_id must be an int or float")

        if section_id <= 0:
            raise APIValidationError("[*] section_id must be > 0")

        sect_data = self._validate_data(data)

        raise NotImplementedError

    def delete_section(self, section_id):

        if not section_id or section_id is None:
            raise APIValidationError("[*] Invalid section_id")

        if type(section_id) not in [int, float]:
            raise APIValidationError("[*] section_id must be an int or float")

        if section_id <= 0:
            raise APIValidationError("[*] section_id must be > 0")

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

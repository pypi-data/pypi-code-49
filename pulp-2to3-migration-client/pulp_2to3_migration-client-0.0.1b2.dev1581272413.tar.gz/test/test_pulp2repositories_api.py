# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_2to3_migration
from pulpcore.client.pulp_2to3_migration.api.pulp2repositories_api import Pulp2repositoriesApi  # noqa: E501
from pulpcore.client.pulp_2to3_migration.rest import ApiException


class TestPulp2repositoriesApi(unittest.TestCase):
    """Pulp2repositoriesApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_2to3_migration.api.pulp2repositories_api.Pulp2repositoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list(self):
        """Test case for list

        List pulp2 repositorys  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a pulp2 repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_container
from pulpcore.client.pulp_container.api.content_manifests_api import ContentManifestsApi  # noqa: E501
from pulpcore.client.pulp_container.rest import ApiException


class TestContentManifestsApi(unittest.TestCase):
    """ContentManifestsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_container.api.content_manifests_api.ContentManifestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list(self):
        """Test case for list

        List manifests  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a manifest  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

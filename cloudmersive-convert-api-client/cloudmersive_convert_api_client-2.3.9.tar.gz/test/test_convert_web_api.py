# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.api.convert_web_api import ConvertWebApi  # noqa: E501
from cloudmersive_convert_api_client.rest import ApiException


class TestConvertWebApi(unittest.TestCase):
    """ConvertWebApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_convert_api_client.api.convert_web_api.ConvertWebApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_convert_web_html_to_pdf(self):
        """Test case for convert_web_html_to_pdf

        Convert HTML string to PDF  # noqa: E501
        """
        pass

    def test_convert_web_url_to_pdf(self):
        """Test case for convert_web_url_to_pdf

        Convert a URL to PDF  # noqa: E501
        """
        pass

    def test_convert_web_url_to_screenshot(self):
        """Test case for convert_web_url_to_screenshot

        Take screenshot of URL  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

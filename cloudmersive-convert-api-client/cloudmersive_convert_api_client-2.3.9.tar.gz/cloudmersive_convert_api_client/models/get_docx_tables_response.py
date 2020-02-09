# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cloudmersive_convert_api_client.models.docx_table import DocxTable  # noqa: F401,E501


class GetDocxTablesResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'successful': 'bool',
        'tables': 'list[DocxTable]'
    }

    attribute_map = {
        'successful': 'Successful',
        'tables': 'Tables'
    }

    def __init__(self, successful=None, tables=None):  # noqa: E501
        """GetDocxTablesResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._tables = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if tables is not None:
            self.tables = tables

    @property
    def successful(self):
        """Gets the successful of this GetDocxTablesResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this GetDocxTablesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this GetDocxTablesResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this GetDocxTablesResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def tables(self):
        """Gets the tables of this GetDocxTablesResponse.  # noqa: E501

        Tables in the DOCX file  # noqa: E501

        :return: The tables of this GetDocxTablesResponse.  # noqa: E501
        :rtype: list[DocxTable]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this GetDocxTablesResponse.

        Tables in the DOCX file  # noqa: E501

        :param tables: The tables of this GetDocxTablesResponse.  # noqa: E501
        :type: list[DocxTable]
        """

        self._tables = tables

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetDocxTablesResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetDocxTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

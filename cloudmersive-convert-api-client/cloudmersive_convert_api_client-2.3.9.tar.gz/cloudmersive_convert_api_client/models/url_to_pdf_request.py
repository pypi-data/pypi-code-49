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


class UrlToPdfRequest(object):
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
        'url': 'str',
        'extra_loading_wait': 'int',
        'include_background_graphics': 'bool'
    }

    attribute_map = {
        'url': 'Url',
        'extra_loading_wait': 'ExtraLoadingWait',
        'include_background_graphics': 'IncludeBackgroundGraphics'
    }

    def __init__(self, url=None, extra_loading_wait=None, include_background_graphics=None):  # noqa: E501
        """UrlToPdfRequest - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._extra_loading_wait = None
        self._include_background_graphics = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if extra_loading_wait is not None:
            self.extra_loading_wait = extra_loading_wait
        if include_background_graphics is not None:
            self.include_background_graphics = include_background_graphics

    @property
    def url(self):
        """Gets the url of this UrlToPdfRequest.  # noqa: E501

        URL address of the website to screenshot.  HTTP and HTTPS are both supported, as are custom ports.  # noqa: E501

        :return: The url of this UrlToPdfRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UrlToPdfRequest.

        URL address of the website to screenshot.  HTTP and HTTPS are both supported, as are custom ports.  # noqa: E501

        :param url: The url of this UrlToPdfRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def extra_loading_wait(self):
        """Gets the extra_loading_wait of this UrlToPdfRequest.  # noqa: E501

        Optional: Additional number of milliseconds to wait once the web page has finished loading before taking the screenshot.  Can be helpful for highly asynchronous websites.  Provide a value of 0 for the default of 5000 milliseconds (5 seconds)  # noqa: E501

        :return: The extra_loading_wait of this UrlToPdfRequest.  # noqa: E501
        :rtype: int
        """
        return self._extra_loading_wait

    @extra_loading_wait.setter
    def extra_loading_wait(self, extra_loading_wait):
        """Sets the extra_loading_wait of this UrlToPdfRequest.

        Optional: Additional number of milliseconds to wait once the web page has finished loading before taking the screenshot.  Can be helpful for highly asynchronous websites.  Provide a value of 0 for the default of 5000 milliseconds (5 seconds)  # noqa: E501

        :param extra_loading_wait: The extra_loading_wait of this UrlToPdfRequest.  # noqa: E501
        :type: int
        """

        self._extra_loading_wait = extra_loading_wait

    @property
    def include_background_graphics(self):
        """Gets the include_background_graphics of this UrlToPdfRequest.  # noqa: E501

        Optional: Set to true to include background graphics in the PDF, or false to not include.  Default is true.  # noqa: E501

        :return: The include_background_graphics of this UrlToPdfRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_background_graphics

    @include_background_graphics.setter
    def include_background_graphics(self, include_background_graphics):
        """Sets the include_background_graphics of this UrlToPdfRequest.

        Optional: Set to true to include background graphics in the PDF, or false to not include.  Default is true.  # noqa: E501

        :param include_background_graphics: The include_background_graphics of this UrlToPdfRequest.  # noqa: E501
        :type: bool
        """

        self._include_background_graphics = include_background_graphics

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
        if issubclass(UrlToPdfRequest, dict):
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
        if not isinstance(other, UrlToPdfRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

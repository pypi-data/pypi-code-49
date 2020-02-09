# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GeolocateResponse(object):
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
        'country_code': 'str',
        'country_name': 'str',
        'city': 'str',
        'region_code': 'str',
        'region_name': 'str',
        'zip_code': 'str',
        'timezone_standard_name': 'str',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'country_code': 'CountryCode',
        'country_name': 'CountryName',
        'city': 'City',
        'region_code': 'RegionCode',
        'region_name': 'RegionName',
        'zip_code': 'ZipCode',
        'timezone_standard_name': 'TimezoneStandardName',
        'latitude': 'Latitude',
        'longitude': 'Longitude'
    }

    def __init__(self, country_code=None, country_name=None, city=None, region_code=None, region_name=None, zip_code=None, timezone_standard_name=None, latitude=None, longitude=None):  # noqa: E501
        """GeolocateResponse - a model defined in Swagger"""  # noqa: E501

        self._country_code = None
        self._country_name = None
        self._city = None
        self._region_code = None
        self._region_name = None
        self._zip_code = None
        self._timezone_standard_name = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        if country_code is not None:
            self.country_code = country_code
        if country_name is not None:
            self.country_name = country_name
        if city is not None:
            self.city = city
        if region_code is not None:
            self.region_code = region_code
        if region_name is not None:
            self.region_name = region_name
        if zip_code is not None:
            self.zip_code = zip_code
        if timezone_standard_name is not None:
            self.timezone_standard_name = timezone_standard_name
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def country_code(self):
        """Gets the country_code of this GeolocateResponse.  # noqa: E501

        Two-letter country code of IP address  # noqa: E501

        :return: The country_code of this GeolocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this GeolocateResponse.

        Two-letter country code of IP address  # noqa: E501

        :param country_code: The country_code of this GeolocateResponse.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def country_name(self):
        """Gets the country_name of this GeolocateResponse.  # noqa: E501

        Country name of IP address  # noqa: E501

        :return: The country_name of this GeolocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this GeolocateResponse.

        Country name of IP address  # noqa: E501

        :param country_name: The country_name of this GeolocateResponse.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def city(self):
        """Gets the city of this GeolocateResponse.  # noqa: E501

        City of IP address  # noqa: E501

        :return: The city of this GeolocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this GeolocateResponse.

        City of IP address  # noqa: E501

        :param city: The city of this GeolocateResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def region_code(self):
        """Gets the region_code of this GeolocateResponse.  # noqa: E501

        State/region code of IP address  # noqa: E501

        :return: The region_code of this GeolocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GeolocateResponse.

        State/region code of IP address  # noqa: E501

        :param region_code: The region_code of this GeolocateResponse.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def region_name(self):
        """Gets the region_name of this GeolocateResponse.  # noqa: E501

        State/region of IP address  # noqa: E501

        :return: The region_name of this GeolocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this GeolocateResponse.

        State/region of IP address  # noqa: E501

        :param region_name: The region_name of this GeolocateResponse.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def zip_code(self):
        """Gets the zip_code of this GeolocateResponse.  # noqa: E501

        Zip or postal code of IP address  # noqa: E501

        :return: The zip_code of this GeolocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this GeolocateResponse.

        Zip or postal code of IP address  # noqa: E501

        :param zip_code: The zip_code of this GeolocateResponse.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def timezone_standard_name(self):
        """Gets the timezone_standard_name of this GeolocateResponse.  # noqa: E501

        Timezone of IP address  # noqa: E501

        :return: The timezone_standard_name of this GeolocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._timezone_standard_name

    @timezone_standard_name.setter
    def timezone_standard_name(self, timezone_standard_name):
        """Sets the timezone_standard_name of this GeolocateResponse.

        Timezone of IP address  # noqa: E501

        :param timezone_standard_name: The timezone_standard_name of this GeolocateResponse.  # noqa: E501
        :type: str
        """

        self._timezone_standard_name = timezone_standard_name

    @property
    def latitude(self):
        """Gets the latitude of this GeolocateResponse.  # noqa: E501

        Latitude of IP address  # noqa: E501

        :return: The latitude of this GeolocateResponse.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this GeolocateResponse.

        Latitude of IP address  # noqa: E501

        :param latitude: The latitude of this GeolocateResponse.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this GeolocateResponse.  # noqa: E501

        Longitude of IP address  # noqa: E501

        :return: The longitude of this GeolocateResponse.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this GeolocateResponse.

        Longitude of IP address  # noqa: E501

        :param longitude: The longitude of this GeolocateResponse.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if issubclass(GeolocateResponse, dict):
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
        if not isinstance(other, GeolocateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

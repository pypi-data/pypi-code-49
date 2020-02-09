# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_container.configuration import Configuration


class ContainerContainerDistribution(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'content_guard': 'str',
        'pulp_created': 'datetime',
        'repository_version': 'str',
        'pulp_href': 'str',
        'name': 'str',
        'repository': 'str',
        'base_path': 'str',
        'registry_path': 'str'
    }

    attribute_map = {
        'content_guard': 'content_guard',
        'pulp_created': 'pulp_created',
        'repository_version': 'repository_version',
        'pulp_href': 'pulp_href',
        'name': 'name',
        'repository': 'repository',
        'base_path': 'base_path',
        'registry_path': 'registry_path'
    }

    def __init__(self, content_guard=None, pulp_created=None, repository_version=None, pulp_href=None, name=None, repository=None, base_path=None, registry_path=None, local_vars_configuration=None):  # noqa: E501
        """ContainerContainerDistribution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content_guard = None
        self._pulp_created = None
        self._repository_version = None
        self._pulp_href = None
        self._name = None
        self._repository = None
        self._base_path = None
        self._registry_path = None
        self.discriminator = None

        self.content_guard = content_guard
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.repository_version = repository_version
        if pulp_href is not None:
            self.pulp_href = pulp_href
        self.name = name
        self.repository = repository
        self.base_path = base_path
        if registry_path is not None:
            self.registry_path = registry_path

    @property
    def content_guard(self):
        """Gets the content_guard of this ContainerContainerDistribution.  # noqa: E501

        An optional content-guard.  # noqa: E501

        :return: The content_guard of this ContainerContainerDistribution.  # noqa: E501
        :rtype: str
        """
        return self._content_guard

    @content_guard.setter
    def content_guard(self, content_guard):
        """Sets the content_guard of this ContainerContainerDistribution.

        An optional content-guard.  # noqa: E501

        :param content_guard: The content_guard of this ContainerContainerDistribution.  # noqa: E501
        :type: str
        """

        self._content_guard = content_guard

    @property
    def pulp_created(self):
        """Gets the pulp_created of this ContainerContainerDistribution.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this ContainerContainerDistribution.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this ContainerContainerDistribution.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this ContainerContainerDistribution.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def repository_version(self):
        """Gets the repository_version of this ContainerContainerDistribution.  # noqa: E501

        RepositoryVersion to be served  # noqa: E501

        :return: The repository_version of this ContainerContainerDistribution.  # noqa: E501
        :rtype: str
        """
        return self._repository_version

    @repository_version.setter
    def repository_version(self, repository_version):
        """Sets the repository_version of this ContainerContainerDistribution.

        RepositoryVersion to be served  # noqa: E501

        :param repository_version: The repository_version of this ContainerContainerDistribution.  # noqa: E501
        :type: str
        """

        self._repository_version = repository_version

    @property
    def pulp_href(self):
        """Gets the pulp_href of this ContainerContainerDistribution.  # noqa: E501


        :return: The pulp_href of this ContainerContainerDistribution.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this ContainerContainerDistribution.


        :param pulp_href: The pulp_href of this ContainerContainerDistribution.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def name(self):
        """Gets the name of this ContainerContainerDistribution.  # noqa: E501

        A unique name. Ex, `rawhide` and `stable`.  # noqa: E501

        :return: The name of this ContainerContainerDistribution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContainerContainerDistribution.

        A unique name. Ex, `rawhide` and `stable`.  # noqa: E501

        :param name: The name of this ContainerContainerDistribution.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def repository(self):
        """Gets the repository of this ContainerContainerDistribution.  # noqa: E501

        The latest RepositoryVersion for this Repository will be served.  # noqa: E501

        :return: The repository of this ContainerContainerDistribution.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ContainerContainerDistribution.

        The latest RepositoryVersion for this Repository will be served.  # noqa: E501

        :param repository: The repository of this ContainerContainerDistribution.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def base_path(self):
        """Gets the base_path of this ContainerContainerDistribution.  # noqa: E501

        The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \"foo\" and \"foo/bar\")  # noqa: E501

        :return: The base_path of this ContainerContainerDistribution.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this ContainerContainerDistribution.

        The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \"foo\" and \"foo/bar\")  # noqa: E501

        :param base_path: The base_path of this ContainerContainerDistribution.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base_path is None:  # noqa: E501
            raise ValueError("Invalid value for `base_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                base_path is not None and len(base_path) < 1):
            raise ValueError("Invalid value for `base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._base_path = base_path

    @property
    def registry_path(self):
        """Gets the registry_path of this ContainerContainerDistribution.  # noqa: E501

        The Registry hostame/name/ to use with docker pull command defined by this distribution.  # noqa: E501

        :return: The registry_path of this ContainerContainerDistribution.  # noqa: E501
        :rtype: str
        """
        return self._registry_path

    @registry_path.setter
    def registry_path(self, registry_path):
        """Sets the registry_path of this ContainerContainerDistribution.

        The Registry hostame/name/ to use with docker pull command defined by this distribution.  # noqa: E501

        :param registry_path: The registry_path of this ContainerContainerDistribution.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                registry_path is not None and len(registry_path) < 1):
            raise ValueError("Invalid value for `registry_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._registry_path = registry_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContainerContainerDistribution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerContainerDistribution):
            return True

        return self.to_dict() != other.to_dict()

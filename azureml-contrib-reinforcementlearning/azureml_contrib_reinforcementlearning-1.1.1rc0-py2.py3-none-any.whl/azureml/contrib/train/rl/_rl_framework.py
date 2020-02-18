# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

""" Reinforcement Learning framework base, and supported framework classes"""

from abc import ABC, abstractmethod
from azureml.exceptions import UserErrorException


class RLFramework(ABC):
    _version = None
    _name = None
    _args = None

    def __init__(self, version=None, framework_arguments=None, *args, **kwargs):
        super().__init__()
        self.version = version if version else self.default_framework_version
        self.framework_arguments = framework_arguments

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        if self.isSupportedVersion(version):
            self._version = version
        else:
            raise UserErrorException("Version {0} of Framework {1} is not currently "
                                     "supported, supported versions are: {2}".format(version,
                                                                                     self.name,
                                                                                     self.supported_versions))

    @property
    def framework_arguments(self):
        return self._args

    @framework_arguments.setter
    def framework_arguments(self, arguments):
        self._args = arguments

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    @abstractmethod
    def default_framework_version(self):
        pass

    @property
    @abstractmethod
    def supported_versions(self):
        pass

    def isSupportedVersion(self, version):
        if version in self.supported_versions:
            return True
        else:
            return False

    def __repr__(self):
        return '{}-{}'.format(self.name, self.version).lower()


class Ray(RLFramework):
    """Defines the version and arguments for the Ray framework.

    :param version: The version of the Ray framework to use. If not specified, Ray.default_framework_version is used.
    :type version: str
    :param framework_arguments: Additional arguments passed to the ray start command when starting the Ray cluster.
        For example, you can set the redis memory size by specifying ['--redis-max-memory=100000000'].
        Note: these arguments are only applied when starting the head node and are not specified for worker nodes.
    :type framework_arguments: list
    """

    def __init__(self, version=None, framework_arguments=None, *args, **kwargs):
        """Initializes the version and arguments for the Ray framework.

        :param version: The version of the Ray framework to use. If not specified, Ray.default_framework_version
            is used.
        :type version: str
        :param framework_arguments: Additional arguments passed to the ray start command when starting the Ray cluster.
            For example, you can set the redis memory size by specifying ['--redis-max-memory=100000000'].
            Note: these arguments are only applied when starting the head node and are not specified for worker nodes.
        :type framework_arguments: list
        """
        super().__init__(version, framework_arguments, *args, **kwargs)
        self.name = "Ray"

    @property
    def default_framework_version(self):
        """The version of the Ray framework to use if one is explicitly specified.

        :return: The version.
        :rtype: str
        """
        return "0.7.2"

    @property
    def supported_versions(self):
        """The list of supported Ray versions.

        :return: The list of versions.
        :rtype: list
        """
        return [
            self.default_framework_version
        ]

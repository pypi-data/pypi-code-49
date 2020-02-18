# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains class for managing resources configuration for AML entities."""

import logging
from azureml.exceptions import WebserviceException

module_logger = logging.getLogger(__name__)


class ResourceConfiguration(object):
    """Class containing details for the resource configuration for AML resources.

    Initialize the resource configuration.

    :param cpu: The number of CPU cores to allocate for this resource. Can be a decimal
    :type cpu: float
    :param memory_in_gb: The amount of memory (in GB) to allocate for this resource. Can be a decimal
    :type memory_in_gb: float
    :param gpu: The number of GPUs to allocate for this resource.
    :type gpu: int
    """

    _expected_payload_keys = ['cpu', 'memoryInGB', 'gpu']

    def __init__(self, cpu=None, memory_in_gb=None, gpu=None):
        """Initialize the  ResourceConfiguration.

        :param cpu: The number of CPU cores to allocate for this resource. Can be a decimal
        :type cpu: float
        :param memory_in_gb: The amount of memory (in GB) to allocate for this resource. Can be a decimal
        :type memory_in_gb: float
        :param gpu: The number of GPUs to allocate for this resource.
        :type gpu: int
        """
        self.cpu = cpu
        self.memory_in_gb = memory_in_gb
        self.gpu = gpu

    def serialize(self):
        """Convert this ResourceConfiguration into a json serialized dictionary.

        :return: The json representation of this ResourceConfiguration
        :rtype: dict
        """
        return {'cpu': self.cpu, 'memoryInGB': self.memory_in_gb, 'gpu': self.gpu}

    @staticmethod
    def deserialize(payload_obj):
        """Convert a json object into a ResourceConfiguration object.

        :param payload_obj: A json object to convert to a ResourceConfiguration object
        :type payload_obj: dict
        :return: The ResourceConfiguration representation of the provided json object
        :rtype: azureml.core.resource_configuration.ResourceConfiguration
        """
        if payload_obj is None:
            return None
        for payload_key in ResourceConfiguration._expected_payload_keys:
            if payload_key not in payload_obj:
                raise WebserviceException('Invalid webservice payload, missing {} for ResourceConfiguration:\n'
                                          '{}'.format(payload_key, payload_obj), logger=module_logger)

        return ResourceConfiguration(payload_obj['cpu'], payload_obj['memoryInGB'], payload_obj['gpu'])

    def _validate_configuration(self):
        """Check that the specified configuration values are valid.

        Will raise a :class:`azureml.exceptions.WebserviceException` if validation fails.

        :raises: azureml.exceptions.WebserviceException
        """
        error = ""
        if self.cpu and self.cpu <= 0:
            error += 'Invalid configuration, cpu must be greater than zero.\n'
        if self.memory_in_gb and self.memory_in_gb <= 0:
            error += 'Invalid configuration, memory_in_gb must be greater than zero.\n'
        if self.gpu and not isinstance(self.gpu, int) and self.gpu <= 0:
            error += 'Invalid configuration, gpu must be integer and greater than zero.\n'

        if error:
            raise WebserviceException(error, logger=module_logger)

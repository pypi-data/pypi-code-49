# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Contains functionality for managing an Azure Container Registry."""

import collections

from azureml._base_sdk_common.abstract_run_config_element import _AbstractRunConfigElement
from azureml._base_sdk_common.field_info import _FieldInfo


class ContainerRegistry(_AbstractRunConfigElement):
    """Defines a connection to an Azure Container Registry.

    :var address: The DNS name or IP address of the Azure Container Registry (ACR).
    :vartype address: str

    :var username: The username for ACR.
    :vartype username: str

    :var password: The password for ACR.
    :vartype password: str
    """

    # This is used to deserialize.
    # This is also the order for serialization into a file.
    _field_to_info_dict = collections.OrderedDict([
        ("address", _FieldInfo(str, "DNS name or IP address of azure container registry(ACR)")),
        ("username", _FieldInfo(str, "The username for ACR")),
        ("password", _FieldInfo(str, "The password for ACR"))
    ])

    def __init__(self):
        """Class ContainerRegistry constructor."""
        super(ContainerRegistry, self).__init__()
        self.address = None
        self.username = None
        self.password = None
        self._initialized = True

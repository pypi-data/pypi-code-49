# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""This package is used for packaging Azure Machine Learning models for use on Azure Functions.
"""

from ._package import SERVICE_BUS_QUEUE_TRIGGER, BLOB_TRIGGER, HTTP_TRIGGER, package, package_http, package_blob, \
    package_service_bus_queue
from azureml.core import VERSION

__version__ = VERSION

__all__ = [
    "SERVICE_BUS_QUEUE_TRIGGER",
    "BLOB_TRIGGER",
    "HTTP_TRIGGER",
    "package",
    "package_http",
    "package_blob",
    "package_service_bus_queue"
]

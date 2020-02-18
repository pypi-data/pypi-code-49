# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains the classes needed for Windows Compute"""

from ._amlWindowsCompute import AmlWindowsCompute
from azureml._base_sdk_common import __version__ as VERSION
import azureml._base_sdk_common.user_agent as user_agent

__version__ = VERSION

user_agent.append("azureml-contrib-reinforcementlearning", __version__)

__all__ = [
    "AmlWindowsCompute"
]

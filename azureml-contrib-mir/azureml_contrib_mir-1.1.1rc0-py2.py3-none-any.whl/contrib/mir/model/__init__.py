# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""This package contains classes used for Model Profiling in Azure Machine Learning."""

from azureml._base_sdk_common import __version__ as VERSION
from .model import Model
from .profile import ModelProfile
__version__ = VERSION

__all__ = ['Model', 'ModelProfile']

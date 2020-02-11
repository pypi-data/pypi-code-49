# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Package containing modules used in automated machine learning.

Included classes provide resources for configuring, managing pipelines, and examining run output
for automated machine learning experiments.

For more information on automated machine learning, please see
https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-automated-ml

To define a reusable machine learning workflow for automated machine learning, you may use
:class:`azureml.train.automl.runtime.AutoMLStep` to create a
:class:`azureml.pipeline.core.pipeline.Pipeline`.
"""
import azureml.automl.core

import warnings
with warnings.catch_warnings():
    # Suppress the warnings at the import phase.
    warnings.simplefilter("ignore")
    from .automl_step import AutoMLStep, AutoMLStepRun

__all__ = [
    'AutoMLStep',
    'AutoMLStepRun']

try:
    from ._version import ver as VERSION, selfver as SELFVERSION
    __version__ = VERSION
except ImportError:
    VERSION = '0.0.0+dev'
    SELFVERSION = VERSION
    __version__ = VERSION

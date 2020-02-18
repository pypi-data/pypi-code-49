# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""This package contains specialized step and config which can be executed in an AzureMl Pipeline."""
from .parallel_run_config import ParallelRunConfig
from .parallel_run_step import ParallelRunStep

__all__ = ["ParallelRunConfig",
           "ParallelRunStep",
           ]

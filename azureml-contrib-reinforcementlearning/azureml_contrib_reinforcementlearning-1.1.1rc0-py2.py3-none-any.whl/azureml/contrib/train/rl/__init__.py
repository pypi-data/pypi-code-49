# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains the classes needed for Reinforcement Learning training"""

from ._rl_estimator import ReinforcementLearningEstimator
from ._rl_run import ReinforcementLearningRun
from ._rl_runconfig import ReinforcementLearningConfiguration, WorkerConfiguration, SimulatorConfiguration
from ._rl_framework import Ray
from ._rl_simulator import Simulator
from azureml._base_sdk_common import __version__ as VERSION
import azureml._base_sdk_common.user_agent as user_agent

__version__ = VERSION

user_agent.append("azureml-contrib-reinforcementlearning", __version__)

__all__ = [
    "ReinforcementLearningEstimator",
    "ReinforcementLearningRun",
    "ReinforcementLearningConfiguration",
    "WorkerConfiguration",
    "Ray",
    "SimulatorConfiguration",
    "Simulator"
]

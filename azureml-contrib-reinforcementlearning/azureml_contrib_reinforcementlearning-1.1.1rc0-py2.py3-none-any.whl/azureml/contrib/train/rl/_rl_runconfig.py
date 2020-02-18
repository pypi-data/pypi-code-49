# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import collections
import json
import logging

from azureml._base_sdk_common.abstract_run_config_element import _AbstractRunConfigElement
from azureml._base_sdk_common.field_info import _FieldInfo
from azureml.core._serialization_utils import _serialize_to_dict
from azureml.core.compute_target import AbstractComputeTarget
from azureml.core.compute import ComputeTarget
from azureml.train._estimator_helper import _create_conda_dependencies

from azureml.exceptions import UserErrorException
from azureml.core.runconfig import EnvironmentDefinition, HistoryConfiguration, Data, DataReferenceConfiguration
from azureml.core._experiment_method import experiment_method

from azureml.contrib.train.rl._rl_environment_helper import _setup_environment
module_logger = logging.getLogger(__name__)


def submit(rl_config, workspace, experiment_name, run_id=None):
    """Launch a Reinforcement Learning run with the given configuration.

    :param rl_config: A `ReinforcementLearningConfiguration` that defines the configuration for this run.
    :type rl_config: azureml.contrib.train.rl.ReinforcementLearningConfiguration
    :param workspace: The workspace in which to run the experiment.
    :type workspace: azureml.core.workspace.Workspace
    :param experiment_name: The name of the experiment.
    :type experiment_name: str
    :param run_id: The run_id to use for the created run.
    :type run_id: str
    :return: A `ReinforcementLearningRun` object.
    :rtype: azureml.contrib.train.rl.ReinforcementLearningRun
    """
    from azureml.core import Experiment
    from azureml._project.project import Project
    from azureml.contrib._rlservice import _commands
    from azureml._base_sdk_common.tracking import global_tracking_info_registry

    experiment = Experiment(workspace, experiment_name)
    project = Project(directory=rl_config._source_directory, experiment=experiment)

    run_config_copy = ReinforcementLearningConfiguration._get_run_config_object(rl_config)

    run = _commands.start_run(project, run_config_copy,
                              telemetry_values=rl_config._telemetry_values,
                              run_id=run_id)

    run.add_properties(global_tracking_info_registry.gather_all(rl_config._source_directory))

    return run


class SimulatorConfiguration(_AbstractRunConfigElement):
    """Contains details of the simulators used during a reinforcement learning run.

    :param source_directory: A local directory containing experiment configuration files.
    :type source_directory: str
    :param environment: The environment definition for the experiment. It includes
        PythonSection, DockerSection, and environment variables.
    :type environment: azureml.core.Environment
    :param entry_script: The relative path to the file containing the simulator startup script.
    :type entry_script: str
    :param script_params: A dictionary of command-line arguments to pass to the entry script specified in
        ``entry_script``.
    :type script_params: dict
    :param compute_target: The compute target where the simulators will run. This can either be an object or the
        compute target name.
    :type compute_target: azureml.core.compute_target.AbstractComputeTarget or str
    :param inputs: A list of :class:`azureml.data.data_reference.DataReference` or
        :class:`azureml.data.dataset_consumption_config.DatasetConsumptionConfig` objects to use as input.
    :type inputs: list
    :param node_count: The number of compute nodes to run simulators on.
    :type node_count: int
    :param instances_per_node: The number of simulator instances that will be started on each node.
    :type instances_per_node: int
    :param retry_count: The number of times to restart the simulator if it fails. A negative value indicates infinite
        retries.
    :type retry_count: int
    :param history: The history configuration to use for the simulators.  This configuration allows turning off
        collection of outputs and/or monitoring of additional directories for logs.
    :type history: azureml.core.runconfig.HistoryConfiguration
    :param enable_port_check: DEPRECATED. Use ``enable_health_check``.
    :type enable_port_check: bool
    :param enable_health_check: Defaults to True, when True the health check is used to check the health
        of the simulator during a run. Default behavior will check that a TCP connection
        can be established using the port passed to the simulators' start script.
    :type enable_health_check: bool
    :param health_check_script: The relative path to the file containing the simulator health check script.
    :type health_check_script: str
    """

    _field_to_info_dict = collections.OrderedDict([
        ("entry_script", _FieldInfo(str, "The name of the script used to start the run.", serialized_name="script")),
        ("script_params", _FieldInfo(str, "The parameters to the entry script.", serialized_name="arguments")),
        ("_target", _FieldInfo(str, "The name of the compute target to use.", serialized_name="target")),
        ("node_count", _FieldInfo(int, "Number of compute nodes to run the job on.", serialized_name="nodecount")),
        ("instances_per_node",
         _FieldInfo(int, "Number of compute nodes to run the job on.", serialized_name="instancespernode")),
        ("retry_count", _FieldInfo(int, "Number of times to restart the simulator on failure.",
                                   serialized_name="retrycount")),
        ("_data_references", _FieldInfo(dict, "data reference configuration details",
                                        list_element_type=DataReferenceConfiguration,
                                        serialized_name="data_references")),
        ("_data", _FieldInfo(dict, "The configuration details for data.",
                             list_element_type=Data, serialized_name="data")),
        ("_snapshot_id", _FieldInfo(str, "The snapshot that contains the code that will be used for simulators run",
                                    serialized_name="snapshotid")),
        ("environment", _FieldInfo(EnvironmentDefinition, "The environment definition.")),
        ("history", _FieldInfo(HistoryConfiguration, "History details.")),
        ("enable_port_check", _FieldInfo(bool, "Flag to enable or disable port checking",
                                         serialized_name="enableportchecking")),
        ("enable_health_check", _FieldInfo(bool, "Flag to enable or disable health checking",
                                           serialized_name="enablehealthchecking")),
        ("health_check_script", _FieldInfo(str, "The name of the script used for simulator health checking",
                                           serialized_name="healthcheckscript"))
    ])

    def __init__(self,
                 source_directory,
                 *,
                 environment=None,
                 entry_script=None,
                 script_params=None,
                 compute_target=None,
                 inputs=None,
                 node_count=1,
                 instances_per_node=1,
                 retry_count=0,
                 history=None,
                 enable_port_check=None,
                 enable_health_check=True,
                 health_check_script=""):
        """Initializes the simulator configuration used during a reinforcement learning run.

        :param source_directory: A local directory containing experiment configuration files.
        :type source_directory: str
        :param environment: The environment definition for the experiment. It includes
            PythonSection, DockerSection, and environment variables.
        :type environment: azureml.core.Environment
        :param entry_script: The relative path to the file containing the simulator startup script.
        :type entry_script: str
        :param script_params: A dictionary of command-line arguments to pass to the entry script specified in
            ``entry_script``.
        :type script_params: dict
        :param compute_target: The compute target where the simulators will run. This can either be an object or the
            compute target name.
        :type compute_target: azureml.core.compute_target.AbstractComputeTarget or str
        :param inputs: A list of :class:`azureml.data.data_reference.DataReference` or
            :class:`azureml.data.dataset_consumption_config.DatasetConsumptionConfig` objects to use as input.
        :type inputs: list
        :param node_count: The number of compute nodes to run simulators on.
        :type node_count: int
        :param instances_per_node: The number of simulator instances that will be started on each node. Note: more
            than one instance is not currently supported.
        :type instances_per_node: int
        :param retry_count: The number of times to restart the simulator if it fails. A negative value indicates
            infinite retries.
        :type retry_count: int
        :param history: The history configuration to use for the simulators.  This configuration allows turning off
            collection of outputs and/or monitoring of additional directories for logs.
        :type history: azureml.core.runconfig.HistoryConfiguration
        :param enable_port_check: DEPRECATED. Use ``enable_health_check``.
        :type enable_port_check: bool
        :param enable_health_check: Defaults to True, when True the health check is used to check the health
            of the simulator during a run. Default behavior will check that a TCP connection
            can be established using the port passed to the simulators' start script.
        :type enable_health_check: bool
        :param health_check_script: The relative path to the file containing the simulator health check script.
        :type health_check_script: str
        """

        super(SimulatorConfiguration, self).__init__()
        self.source_directory = source_directory
        self.environment = environment
        self.entry_script = entry_script
        self.script_params = script_params
        self.target = compute_target
        self.inputs = inputs
        self.history = history if history else HistoryConfiguration()
        self.node_count = node_count
        self.instances_per_node = instances_per_node
        self.retry_count = retry_count
        self.enable_port_check = enable_port_check
        self.enable_health_check = enable_health_check
        self.health_check_script = health_check_script
        self._snapshot_id = ""
        self._data_references = None
        self._data = None
        self._initialized = True

        if enable_port_check is not None:
            module_logger.warning("enable_port_check is deprecated. Please use enable_health_check.")

    @property
    def arguments(self):
        """Get the arguments for the simulator entry script.

        :return: The script parameters.
        :rtype: dict
        """
        return self.script_params

    @property
    def data(self):
        """Get the data for the simulators.

        :return: The data.
        :rtype: dict
        """
        return self._data

    @property
    def target(self):
        """Get the compute target used by the simulators.

        Target refers to the compute where the job is scheduled for execution.
        Available cloud compute targets can be found using the function
        :attr:`azureml.core.Workspace.compute_targets`

        :return: The target name.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Set the compute target.

        :param target: The name of the compute target.
        :type target: str
        """
        if isinstance(target, (AbstractComputeTarget, ComputeTarget)):
            self._target = target.name
        elif isinstance(target, str):
            self._target = target

    @property
    def snapshot_id(self):
        """Get the snapshot id used by the simulators.

        :return: The snapshot id.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Set the snapshot id used by the simulators.

        :param snapshot_id: The snapshot id.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id


class WorkerConfiguration(_AbstractRunConfigElement):
    """ WorkerConfiguration is the class that holds all the necessary information for the workers to run.

    :param node_count: Number of worker nodes to be initialized, one worker will run per machine in the
        compute target.
    :type node_count: int
    :param compute_target: The compute target where the workers will run. This can either be an object or the
        the compute target's name.
    :type compute_target: azureml.core.compute_target.ComputeTarget or str
    :param environment: The environment definition for the workers. It includes
        PythonSection, DockerSection, and environment variables. Any environment option not directly
        exposed through other parameters to the WorkerConfiguration construction can be set using this
        parameter. If this parameter is specified, it will be used as a base upon which packages specified in
        ``pip_packages`` and ``conda_packages`` will be added.
    :type environment: azureml.core.Environment
    :param history: History configuration for the worker's run, this controls which logs folders will be monitored
    :type azureml.core.runconfig.HistoryConfiguration
    :param use_gpu: Prameter used to signal whether the default base image should have the packages for
        gpu added. This parameter is ignored if ``enviroment`` is set.
    :type is_gpu_enable: bool
    :param conda_packages: A list of strings representing conda packages to be added to the Python environment
        for the workers.
    :type conda_packages: list
    :param pip_packages: A list of strings representing pip packages to be added to the Python environment
        for the workers
    :type pip_packages: list
    :param pip_requirements_file: The relative path to the workers' pip requirements text file.
            This can be provided in combination with the ``pip_packages`` parameter.
    :type pip_requirements_file: str
    :param conda_dependencies_file: The relative path to the workers' conda dependencies
    yaml file.
    :type conda_dependencies_file: str
    """

    _field_to_info_dict = collections.OrderedDict([
        ("_target", _FieldInfo(str, "The name of the compute target to use.", serialized_name="target")),
        ("node_count", _FieldInfo(int, "Number of compute nodes to run the job on.", serialized_name="nodecount")),
        ("environment", _FieldInfo(EnvironmentDefinition, "The environment definition.")),
        ("history", _FieldInfo(HistoryConfiguration, "History details."))
    ])

    def __init__(self, node_count, compute_target=None, environment=None, history=None, use_gpu=False,
                 pip_packages=None, conda_packages=None, conda_dependencies_file=None,
                 pip_requirements_file=None):

        """Initialize the WorkerConfiguration

        :param node_count: Number of worker nodes to be initialized, one worker will run per machine in the
            compute target.
        :type node_count: int
        :param compute_target: The compute target where the workers will run. This can either be an object or the
            the compute target's name.
        :type compute_target: azureml.core.compute_target.ComputeTarget or str
        :param environment: The environment definition for the workers. It includes
            PythonSection, DockerSection, and environment variables. Any environment option not directly
            exposed through other parameters to the WorkerConfiguration construction can be set using this
            parameter. If this parameter is specified, it will be used as a base upon which packages specified in
            ``pip_packages`` and ``conda_packages`` will be added.
        :type environment: azureml.core.Environment
        :param history: History configuration for the worker's run, this controls which logs folders will be monitored
        :type azureml.core.runconfig.HistoryConfiguration
        :param use_gpu: Prameter used to signal whether the default base image should have the packages for
            gpu added. This parameter is ignored if ``enviroment`` is set.
        :type is_gpu_enable: bool
        :param conda_packages: A list of strings representing conda packages to be added to the Python environment
            for the workers.
        :type conda_packages: list
        :param pip_packages: A list of strings representing pip packages to be added to the Python environment
            for the workers
        :type pip_packages: list
        :param pip_requirements_file: The relative path to the workers' pip requirements text file.
            This can be provided in combination with the ``pip_packages`` parameter.
        :type pip_requirements_file: str
        :param conda_dependencies_file: The relative path to the workers' conda dependencies
        yaml file.
        :type conda_dependencies_file: str
        """

        super(WorkerConfiguration, self).__init__()
        self.target = compute_target
        self.environment = environment
        self.history = history if history else HistoryConfiguration()
        # TODO add validators
        self.node_count = node_count
        self._use_gpu = use_gpu
        self._pip_packages = pip_packages
        self._conda_packages = conda_packages
        self._pip_requirements_file = pip_requirements_file
        self._conda_dependencies_file = conda_dependencies_file
        self._initialized = True

    @property
    def target(self):
        """Get target.

        Target refers to compute where the job is scheduled for execution.
        Available cloud compute targets can be found using the function
        :attr:`azureml.core.Workspace.compute_targets`

        :return: The target name
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Set target.

        :param target:
        :type target: str
        """
        if isinstance(target, (AbstractComputeTarget, ComputeTarget)):
            self._target = target.name
        elif isinstance(target, str):
            self._target = target

    def _is_environment_initialized(self):
        if self.environment:
            return True
        return False

    def _are_extra_dependencies_specified(self):
        return self._pip_packages or self._pip_requirements_file \
            or self._conda_dependencies_file or self._conda_packages

    def _initialize_env_for_framework(self, framework, source_directory):
        conda_dependencies = None
        if self._are_extra_dependencies_specified():
            conda_dependencies = _create_conda_dependencies(source_directory=source_directory,
                                                            pip_packages=self._pip_packages,
                                                            pip_requirements_file=self._pip_requirements_file,
                                                            conda_packages=self._conda_packages,
                                                            conda_dependencies_file=self._conda_dependencies_file)
        self.environment = _setup_environment(framework=framework, use_gpu=self._use_gpu,
                                              conda_dependencies=conda_dependencies)

    def _initialize_custom_env(self, head_environment, source_directory):
        conda_dependencies = None
        if self._are_extra_dependencies_specified():
            conda_dependencies = _create_conda_dependencies(source_directory=source_directory,
                                                            pip_packages=self._pip_packages,
                                                            pip_requirements_file=self._pip_requirements_file,
                                                            conda_packages=self._conda_packages,
                                                            conda_dependencies_file=self._conda_dependencies_file)
        self.environment = _setup_environment(base_env=head_environment, framework=None,
                                              use_gpu=self._use_gpu,
                                              conda_dependencies=conda_dependencies)


class HeadConfiguration(_AbstractRunConfigElement):
    """ HeadConfiguration is the class that holds all the necessary information for the head to run."""

    _field_to_info_dict = collections.OrderedDict([
        ("script", _FieldInfo(str, "The relative path to the python script file. \
            The file path is relative to the source_directory.")),
        ("arguments", _FieldInfo(list, "The arguments to the script file.", list_element_type=str)),
        ("_target", _FieldInfo(str, "The name of the compute target to use.", serialized_name="target")),
        ("_snapshot_id", _FieldInfo(str, "The snapshot that contains the code that will be used for head run",
                                    serialized_name="snapshotid")),
        ("data_references", _FieldInfo(dict, "data reference configuration details",
                                       list_element_type=DataReferenceConfiguration)),
        ("data", _FieldInfo(dict, "The configuration details for data.", list_element_type=Data)),
        ("environment", _FieldInfo(EnvironmentDefinition, "The environment definition.")),
        ("history", _FieldInfo(HistoryConfiguration, "History details."))
    ])

    def __init__(self, script=None, arguments=None, compute_target=None,
                 environment=None, history=None, data_references=None, data=None):
        super(HeadConfiguration, self).__init__()
        # TODO do we want to keep this default.
        self.script = script if script else "train.py"
        self.arguments = arguments if arguments else []
        self.target = compute_target
        self._snapshot_id = ""
        self.environment = environment if environment else EnvironmentDefinition()
        self.history = history if history else HistoryConfiguration()
        self.data_references = data_references
        self.data = data
        self._initialized = True

    @property
    def target(self):
        """Get target.

        Target refers to compute where the job is scheduled for execution.
        Available cloud compute targets can be found using the function
        :attr:`azureml.core.Workspace.compute_targets`

        :return: The target name
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Set target.

        :param target:
        :type target: str
        """
        if isinstance(target, (AbstractComputeTarget, ComputeTarget)):
            self._target = target.name
        elif isinstance(target, str):
            self._target = target

    @property
    def snapshot_id(self):
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        self._snapshot_id = snapshot_id


class ReinforcementLearningConfiguration(_AbstractRunConfigElement):

    _field_to_info_dict = collections.OrderedDict([
        ("framework", _FieldInfo(str, "RL framework to use")),
        ("framework_arguments", _FieldInfo(list, "Additional arguments for the RL Framework", list_element_type=str)),
        ("head", _FieldInfo(HeadConfiguration, "Configuration for the head's run")),
        ("workers", _FieldInfo(WorkerConfiguration, "Configuration for the workers' run")),
        ("simulators", _FieldInfo(SimulatorConfiguration, "Configuration for the simulators' run")),
        ("max_run_duration_seconds", _FieldInfo(int, "Maximum allowed duration for the run",
                                                serialized_name="maxRunDurationSeconds")),
        ("queue_timeout_seconds", _FieldInfo(int,
                                             ('The maximum allowed time for the run to be queued'
                                              'before it\'s cancelled'),
                                             serialized_name="queueTimeoutSeconds")),
        ("cluster_coordination_timeout_seconds", _FieldInfo(int,
                                                            ('The maximum allowed time for nodes in a cluster'
                                                             'to be in running state before all clusters are'
                                                             'in running state.'),
                                                            serialized_name="clusterCoordinationTimeoutSeconds"))
    ])

    @experiment_method(submit_function=submit)
    def __init__(self, framework, head_configuration, worker_configuration, simulator_configuration,
                 max_run_duration_seconds, cluster_coordination_timeout_seconds, queue_timeout_seconds,
                 source_directory=None):
        super(ReinforcementLearningConfiguration, self).__init__()

        DEFAULT_RUN_DURATION = None   # TODO define defaults
        DEFAULT_COORDINATION_PERIOD = None
        DEFAULT_QUEUE_TIMEOUT = None

        self.framework = framework.name
        self.framework_arguments = framework.framework_arguments if framework.framework_arguments else []
        self._name = None
        self._path = None
        self._source_directory = source_directory
        self._telemetry_values = None
        self.head = head_configuration if head_configuration else HeadConfiguration()
        self.workers = worker_configuration
        self.simulators = simulator_configuration

        self.max_run_duration_seconds = max_run_duration_seconds if max_run_duration_seconds else DEFAULT_RUN_DURATION
        self.cluster_coordination_timeout_seconds = cluster_coordination_timeout_seconds \
            if cluster_coordination_timeout_seconds else DEFAULT_COORDINATION_PERIOD
        self.queue_timeout_seconds = queue_timeout_seconds if queue_timeout_seconds else DEFAULT_QUEUE_TIMEOUT
        self._iterable = None
        self._initialized = True

    def __repr__(self):
        """Return the string representation of the RunConfiguration object.

        :return: String representation of the RunConfiguration object
        :rtype: str
        """
        run_config_dict = _serialize_to_dict(self)
        return json.dumps(run_config_dict, indent=4)

    @staticmethod
    def _get_run_config_object(rl_config):
        """Return the reinforcement learning configuration object.

        :param rl_config: The reinforcement learning configuration.
        :type rl_config: azureml.contrib.train.rl.ReinforcementLearningConfiguration
        :return: Returns the `ReinforcementLearningConfiguration` object.
        :rtype: azureml.contrib.train.rl.ReinforcementLearningConfiguration
        """
        if isinstance(rl_config, str):
            # TODO: load ReinforcementLearningConfig from file
            pass
        elif isinstance(rl_config, ReinforcementLearningConfiguration):
            # TODO: Deep copy of project and auth object too.
            import copy
            return copy.deepcopy(rl_config)
        else:
            raise UserErrorException("Unsupported rl_config type {}."
                                     "rl_config can be of str or "
                                     "azureml.contrib.train.rl.ReinforcementLearningConfiguration"
                                     "type.".format(type(rl_config)))

    # TODO implement helper methods to load/save ReinforcementLearningConfigs from files.

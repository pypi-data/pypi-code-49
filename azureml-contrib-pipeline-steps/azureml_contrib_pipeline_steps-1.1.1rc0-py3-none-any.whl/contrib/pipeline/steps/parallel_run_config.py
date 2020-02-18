# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""ParallelRunConfig for ParallelRunStep."""
import os
import re
import logging
import ruamel.yaml

from azureml.core import Environment
from azureml.core.compute import AmlCompute

module_logger = logging.getLogger(__name__)


class ParallelRunConfig(object):
    """
    Configuration for parallel run step.

    :param environment: The environment definition. This field configures the Python environment.
        It can be configured to use an existing Python environment or to set up a temp environment
        for the experiment. The definition is also responsible for setting the required application
        dependencies.
    :type environment: azureml.core.Environment
    :param entry_script: User script which will be run in parallel on multiple nodes. This is
        specified as local file path. If source_directory is specified, then entry_script is
        a relative path inside. Otherwise, it can be any path accessible on machine.
    :type entry_script: str
    :param error_threshold: The number of record failures for TabularDataset and file failures
        for FileDataset that should be ignored during processing. If the error count goes
        above this value, then the job will be aborted. Error threshold is for the entire
        input and not for individual mini-batches sent to run() method.
        The range is [-1, int.max]. -1 indicates ignore all failures during processing.
    :type error_threshold: int
    :param output_action: How the output to be organized. Currently supported values
        are 'append_row' and 'summary_only'.
        1. 'append_row' – All values output by run() method invocations will be aggregated into
        one unique file named parallel_run_step.txt that is created in the output location.
        2. 'summary_only' – User script is expected to store the output by itself. An output row
        is still expected for each successful input item processed. The system uses this output
        only for error threshold calculation (ignoring the actual value of the row).
    :type output_action: str
    :param compute_target: Compute target to use for ParallelRunStep.
    :type compute_target: azureml.core.compute.AmlCompute
    :param node_count: Number of nodes in the compute target used for running the ParallelRunStep.
    :type node_count: int
    :param process_count_per_node: Number of processes executed on each node.
        (optional, default value is number of cores on node.)
    :type process_count_per_node: int
    :param mini_batch_size: For FileDataset input it is number of files user script can process
        in one run() call. For TabularDataset input it is approximate size of data user script
        can process in one run() call. E.g. 1024, 1024KB, 10MB, 1GB.
        (optional, default value is 10 files for FileDataset and 1MB for TabularDataset.)
    :type mini_batch_size: str
    :param source_directory: Paths to folders that contains the entry_script and supporting files used
        to execute on compute target.
    :type source_directory: : str
    :param description: A description to give batch service used for display purposes.
    :type description: str
    :param logging_level: A string of the logging level name, which is defined in 'logging'.
        (optional, default value is 'INFO'.)
    :type logging_level: str
    :param run_invocation_timeout: Timeout in seconds for each invocation of the run() method.
        (optional, default value is 60.)
    :type run_invocation_timeout: int
    :param input_format: Deprecated.
    :type input_format: str
    """

    def __init__(self, environment, entry_script, error_threshold, output_action, compute_target,
                 node_count, process_count_per_node=None, mini_batch_size=None,
                 source_directory=None, description=None, logging_level='INFO',
                 run_invocation_timeout=60, input_format=None):
        """Initialize the config object.

        :param environment: The environment definition. This field configures the Python environment.
            It can be configured to use an existing Python environment or to set up a temp environment
            for the experiment. The definition is also responsible for setting the required application
            dependencies.
        :type environment: azureml.core.Environment
        :param entry_script: User script which will be run in parallel on multiple nodes. This is
            specified as local file path. If source_directory is specified, then entry_script is
            a relative path inside. Otherwise, it can be any path accessible on machine.
        :type entry_script: str
        :param error_threshold: The number of record failures for TabularDataset and file failures
            for FileDataset that should be ignored during processing. If the error count goes
            above this value, then the job will be aborted. Error threshold is for the entire
            input and not for individual mini-batches sent to run() method.
            The range is [-1, int.max]. -1 indicates ignore all failures during processing.
        :type error_threshold: int
        :param output_action: How the output to be organized. Currently supported values
            are 'append_row' and 'summary_only'.
            1. append_row – All values output by run() method invocations will be aggregated into
               one unique file named parallel_run_step.txt that is created in the output location.
            2. summary_only – User script is expected to store the output by itself. An output row
               is still expected for each successful input item processed. The system uses this output
               only for error threshold calculation (ignoring the actual value of the row).
        :type output_action: str
        :param compute_target: Compute target to use for ParallelRunStep.
        :type compute_target: azureml.core.compute.AmlCompute
        :param node_count: Number of nodes in the compute target used for running the ParallelRunStep.
        :type node_count: int
        :param process_count_per_node: Number of processes executed on each node.
            (optional, default value is number of cores on node.)
        :type process_count_per_node: int
        :param mini_batch_size: For FileDataset input it is number of files user script can process
            in one run() call. For TabularDataset input it is approximate size of data user script
            can process in one run() call. E.g. 1024, 1024KB, 10MB, 1GB.
            (optional, default value 10 files for FileDataset and 1MB for TabularDataset.)
        :type mini_batch_size: str
        :param source_directory: Paths to folders that contains the entry_script and supporting files used
            to execute on compute target.
        :type source_directory: : str
        :param description: A description to give batch service used for display purposes.
        :type description: str
        :param logging_level: A string of the logging level name, which is defined in 'logging'.
            The default value is 'INFO'.
        :type logging_level: str
        :param run_invocation_timeout: Timeout in seconds for each invocation of the run() method.
            (optional, Defaults to 60.)
        :type run_invocation_timeout: int
        :param input_format: Deprecated.
        :type input_format: str
        """
        self.input_format = input_format
        self.mini_batch_size = mini_batch_size
        self.error_threshold = error_threshold
        self.output_action = output_action
        self.logging_level = logging_level
        self.compute_target = compute_target
        self.node_count = node_count
        self.process_count_per_node = process_count_per_node
        self.entry_script = entry_script if entry_script is None else entry_script.strip()
        self.source_directory = source_directory if source_directory is None else source_directory.strip()
        self.description = description
        self.environment = environment
        self.run_invocation_timeout = run_invocation_timeout

        if self.environment is None:
            raise ValueError('Parameter environment is required. It should be instance of azureml.core.Environment.')

        if not isinstance(self.environment, Environment):
            raise ValueError(
                "Parameter environment must be an instance of azureml.core.Environment."
                " The actual value is {0}.".format(self.environment)
            )

        if self.output_action.lower() not in ['summary_only', 'append_row']:
            raise ValueError('Parameter output_action must be summary_only or append_row')

        if not isinstance(self.error_threshold, int) or self.error_threshold < -1:
            raise ValueError('Parameter error_threshold must be an int value greater than or equal to -1')

        if self.mini_batch_size is not None:
            self._mini_batch_size_to_int()

        if self.process_count_per_node is not None and self.process_count_per_node < 1:
            raise ValueError("Parameter process_count_per_node must be a greater than 0")

        if self.compute_target.type.lower() != AmlCompute._compute_type.lower():
            raise ValueError(
                "Compute compute_target {0} is not supported in ParallelRunStep. "
                "AmlCompute is the only supported compute_target."
                .format(self.compute_target))

        if (self.node_count > self.compute_target.scale_settings.maximum_node_count or self.node_count <= 0):
            raise ValueError(
                "Parameter node_count must be between 1 and max_nodes {}"
                .format(self.compute_target.scale_settings.maximum_node_count))

        if self.run_invocation_timeout <= 0:
            raise ValueError('Parameter run_invocation_timeout must be a greater than 0')

    def _mini_batch_size_to_int(self):
        """Convert str to int."""
        pattern = re.compile(r"^\d+([kKmMgG][bB])*$")
        if not pattern.match(self.mini_batch_size):
            raise ValueError(r"Parameter mini_batch_size must follow regex rule ^\d+([kKmMgG][bB])*$")

        try:
            self.mini_batch_size = int(self.mini_batch_size)
        except ValueError:
            unit = self.mini_batch_size[-2:].lower()
            if unit == 'kb':
                self.mini_batch_size = int(self.mini_batch_size[0:-2]) * 1024
            elif unit == 'mb':
                self.mini_batch_size = int(self.mini_batch_size[0:-2]) * 1024 * 1024
            elif unit == 'gb':
                self.mini_batch_size = int(self.mini_batch_size[0:-2]) * 1024 * 1024 * 1024

    def save_to_yaml(self, path):
        """Export parallel run config as yaml file."""
        env_output_dir = os.path.join(os.path.dirname(os.path.abspath(path)), "parallel_run_env")
        self.environment.save_to_directory(env_output_dir)
        config = {"input_format": self.input_format,
                  "mini_batch_size": self.mini_batch_size,
                  "error_threshold": self.error_threshold,
                  "output_action": self.output_action,
                  "logging_level": self.logging_level,
                  "compute_target_name": self.compute_target.name,
                  "node_count": self.node_count,
                  "process_count_per_node": self.process_count_per_node,
                  "entry_script": self.entry_script,
                  "source_directory": self.source_directory,
                  "description": self.description,
                  "run_invocation_timeout": self.run_invocation_timeout,
                  "environment_name": self.environment.name,
                  "environment_dir_path": env_output_dir}
        with open(path, 'w') as f:
            ruamel.yaml.round_trip_dump({"parallel_run_config": config}, f)

    @staticmethod
    def load_yaml(workspace, path):
        """Load parallel run config from yaml file."""
        with open(path, 'r') as f:
            config = ruamel.yaml.round_trip_load(f)["parallel_run_config"]
            compute_target = AmlCompute(workspace, config["compute_target_name"])

            if "environment_dir_path" in config.keys() and config["environment_dir_path"] is not None:
                env = Environment.load_from_directory(config["environment_dir_path"])
            else:
                env = Environment.get(workspace, name=config["environment_name"])

            return ParallelRunConfig(env,
                                     config["entry_script"],
                                     config["error_threshold"],
                                     config["output_action"],
                                     compute_target,
                                     config["node_count"],
                                     config["process_count_per_node"],
                                     "{0}".format(config["mini_batch_size"]),
                                     config["source_directory"],
                                     config["description"],
                                     config["logging_level"],
                                     config["run_invocation_timeout"],
                                     config["input_format"])

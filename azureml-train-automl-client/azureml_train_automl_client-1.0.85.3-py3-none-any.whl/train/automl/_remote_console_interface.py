# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Console interface for AutoML experiments logs"""
import json
import logging
import time
from typing import Any, Dict, Optional, TYPE_CHECKING

import pytz
from azureml._restclient.constants import RunStatus

from automl.client.core.common import constants, logging_utilities
from automl.client.core.common.utilities import minimize_or_maximize
from azureml.automl.core._experiment_observer import ExperimentStatus
from azureml.automl.core.console_interface import ConsoleInterface
from azureml.automl.core.console_writer import ConsoleWriter
from . import _constants_azureml
from . import constants as automl_constants
from ._azureautomlsettings import AzureAutoMLSettings
from .exceptions import SystemException

if TYPE_CHECKING:
    from .run import AutoMLRun


class RemoteConsoleInterface:
    """
    Class responsible for printing iteration information to console for a remote run
    """

    def __init__(self,
                 logger: ConsoleWriter,
                 file_logger: Optional[logging.Logger] = None,
                 check_status_interval: float = 10) -> None:
        """
        RemoteConsoleInterface constructor

        :param logger: Console logger for printing this info
        :param file_logger: Optional file logger for more detailed logs
        :param check_status_interval: Number of seconds to sleep before checking again for status
        """
        self._ci = None
        self._console_logger = logger
        self.logger = file_logger
        self.metric_map = {}        # type: Dict[str, Dict[str, float]]
        self.run_map = {}           # type: Dict[str, Any]
        self.best_metric = None
        self._check_status_interval = check_status_interval

    def _init_console_interface(self, parent_run: 'AutoMLRun') -> bool:
        """
        Initialize the console interface once the setup iteration is complete.

        :param parent_run: AutoMLRun object for the parent run
        :return: True if the initialization succeeded, False otherwise
        """
        # If there are any setup errors, print them and exit
        parent_run_status = parent_run.get_status()
        setup_errors = RemoteConsoleInterface._setup_errors(parent_run_status, parent_run.properties)
        if setup_errors:
            if self._ci is None:
                self._ci = ConsoleInterface("score", self._console_logger)
            self._ci.print_line("")
            self._ci.print_error(setup_errors)
            return False

        setup_run = RemoteConsoleInterface._get_setup_run(parent_run)
        # Run some validations to make sure the setup run is in an expected terminal state, and has
        # the expected keys in it's properties.
        # Check the local status first and double check from RH only if the cached status is non-terminal
        if not RemoteConsoleInterface._is_run_terminal(setup_run.status) and \
                not RemoteConsoleInterface._is_run_terminal(setup_run.get_status()):
            raise SystemException('Expected setup run to have terminated before initializing the console '
                                  'interface. Current status: {}'.format(setup_run.status))

        # Check the local properties first and double check from RH only if it was not found in the cached object
        if _constants_azureml.Properties.PROBLEM_INFO not in setup_run.properties and \
                _constants_azureml.Properties.PROBLEM_INFO not in setup_run.get_properties():
            raise SystemException('Key "{}" missing from setup run properties'.
                                  format(_constants_azureml.Properties.PROBLEM_INFO))

        problem_info_str = setup_run.properties[_constants_azureml.Properties.PROBLEM_INFO]
        problem_info_dict = json.loads(problem_info_str)
        subsampling = problem_info_dict.get('subsampling', False)

        self._ci = ConsoleInterface("score", self._console_logger, mask_sampling=not subsampling)

        try:
            self._ci.print_descriptions()
            self._ci.print_columns()
        except Exception as e:
            logging_utilities.log_traceback(e, self.logger)
            raise SystemException(str(e))

        return True

    def print_scores(self, parent_run: 'AutoMLRun', primary_metric: str) -> None:
        """
        Print all history for a given parent run

        :param parent_run: AutoMLRun to print status for
        :param primary_metric: Metric being optimized for this run
        :return:
        """
        # initialize ConsoleInterface when setup iteration is complete
        if not self._init_console_interface(parent_run):
            return

        best_metric = None
        automl_settings = AzureAutoMLSettings(
            experiment=None, **json.loads(parent_run.properties['AMLSettingsJsonString']))
        tags = parent_run.get_tags()
        total_children_count = int(tags.get('iterations', "0"))
        if total_children_count == 0:
            total_children_count = automl_settings.iterations
        max_concurrency = automl_settings.max_concurrent_iterations

        i = 0
        child_runs_not_finished = []

        while i < total_children_count:
            child_runs_not_finished.append('{}_{}'.format(parent_run.run_id, i))
            i += 1

        objective = minimize_or_maximize(metric=primary_metric)

        while True:
            runs_to_query = child_runs_not_finished[:max_concurrency]
            if not runs_to_query and RemoteConsoleInterface._is_run_terminal(parent_run.get_status()):
                break   # Finished processing all the runs

            new_children_dtos = parent_run._client.run.get_runs_by_run_ids(run_ids=runs_to_query)
            # An indicator to check if we processed any children, if not, it means there were no runs to query for
            processed_children = False
            runs_finished = []

            for run in new_children_dtos:
                if not processed_children:
                    processed_children = True
                run_id = run.run_id
                status = run.status
                if run_id not in self.run_map and RemoteConsoleInterface._is_run_terminal(status):
                    runs_finished.append(run_id)
                    self.run_map[run_id] = run

            # Don't re-use `parent_run_status` from above, as the status can constantly be mutating
            if not processed_children and RemoteConsoleInterface._is_run_terminal(parent_run.get_status()):
                # We got no child runs and the parent is completed - we are done with all the children.
                break

            if runs_finished:
                run_metrics_map = parent_run._client.get_metrics(run_ids=runs_finished)

                for run_id in run_metrics_map:
                    self.metric_map[run_id] = run_metrics_map[run_id]

                for run_id in runs_finished:
                    if "setup" in run_id:
                        continue
                    run = self.run_map[run_id]
                    properties = run.properties
                    current_iter = properties.get('iteration', None)
                    # Bug-393631
                    if current_iter is None:
                        continue
                    run_metric = self.metric_map.get(run_id, {})
                    run_preprocessor = properties.get('run_preprocessor', "")
                    run_algorithm = properties.get('run_algorithm', "")
                    print_line = " ".join(filter(None, [run_preprocessor, run_algorithm]))

                    start_iter_time = run.created_utc.replace(tzinfo=pytz.UTC)

                    end_iter_time = run.end_time_utc.replace(tzinfo=pytz.UTC)

                    iter_duration = str(end_iter_time - start_iter_time).split(".")[0]

                    if primary_metric in run_metric:
                        score = run_metric[primary_metric]
                    else:
                        score = constants.Defaults.DEFAULT_PIPELINE_SCORE

                    if best_metric in [None, 'nan', 'NaN']:
                        best_metric = score
                    elif objective == constants.OptimizerObjectives.MINIMIZE:
                        if score < best_metric:
                            best_metric = score
                    elif objective == constants.OptimizerObjectives.MAXIMIZE:
                        if score > best_metric:
                            best_metric = score
                    else:
                        best_metric = 'Unknown'

                    self._ci.print_start(current_iter)
                    self._ci.print_pipeline(print_line)
                    self._ci.print_end(iter_duration, score, best_metric)

                    errors = properties.get('friendly_errors', None)
                    if errors is not None:
                        error_dict = json.loads(errors)
                        for error in error_dict:
                            self._ci.print_error(error_dict[error])
                    if run_id in child_runs_not_finished:
                        child_runs_not_finished.remove(run_id)

            time.sleep(self._check_status_interval)

    def print_pre_training_progress(self, parent_run: 'AutoMLRun') -> None:
        """
        Print pre-training progress during an experiment.

        :param parent_run: the parent run to print status for.
        :return: None
        """
        try:
            self._console_logger.println()
            last_experiment_status = None
            while True:
                tags = parent_run.get_tags()

                status = tags.get('_aml_system_automl_status', None)
                if status is None:
                    status = parent_run.get_status()
                if RemoteConsoleInterface._is_run_terminal(status):
                    break

                experiment_status = tags.get(automl_constants.ExperimentObserver.EXPERIMENT_STATUS_TAG_NAME, None)

                if experiment_status is not None and experiment_status != last_experiment_status:
                    status_description = tags.get(
                        automl_constants.ExperimentObserver.EXPERIMENT_STATUS_DESCRIPTION_TAG_NAME, "")
                    self._console_logger.println(
                        "Current status: {}. {}".format(experiment_status, status_description))
                    last_experiment_status = experiment_status

                if experiment_status == ExperimentStatus.ModelSelection:
                    break
                time.sleep(self._check_status_interval)
        except Exception:
            pass

    def print_auto_parameters(self, parent_run: 'AutoMLRun') -> None:
        """
        Print the heiristic parameters if they were set.

        :param parent_run: the parent run to print status for.
        :return: None
        """
        try:
            tags = parent_run.get_tags()
            message = tags.get('auto', None)
            if message is not None:
                self._console_logger.println(message)
        except Exception:
            pass

    @staticmethod
    def _is_run_terminal(status: str) -> bool:
        return status in [RunStatus.COMPLETED, RunStatus.FAILED, RunStatus.CANCELED]

    @staticmethod
    def _get_setup_run(parent_run: 'AutoMLRun') -> 'AutoMLRun':
        setup_run_list = list(parent_run._client.run.get_runs_by_run_ids(
            run_ids=['{}_{}'.format(parent_run.run_id, 'setup')]))
        # if this is a local run there will be no setup iteration
        if len(setup_run_list) == 0:
            setup_run = parent_run
        else:
            setup_run = setup_run_list[0]
        return setup_run

    @staticmethod
    def _setup_errors(parent_run_status: str, parent_run_properties: Dict[str, Any]) -> Optional[Any]:
        """Return any setup errors that may have occurred in the parent run."""
        parent_run_status = parent_run_status
        if RemoteConsoleInterface._is_run_terminal(parent_run_status):
            parent_errors = parent_run_properties.get('errors')
            if parent_errors is not None and parent_errors.startswith("Setup iteration failed"):
                return parent_errors
        return None

    @staticmethod
    def _show_output(current_run: 'AutoMLRun',
                     logger: ConsoleWriter,
                     file_logger: Optional[logging.Logger],
                     primary_metric: str) -> None:
        try:
            remote_printer = RemoteConsoleInterface(logger, file_logger)
            remote_printer.print_pre_training_progress(current_run)
            remote_printer.print_auto_parameters(current_run)
            remote_printer.print_scores(current_run, primary_metric)
        except KeyboardInterrupt:
            logger.write("Received interrupt. Returning now.")

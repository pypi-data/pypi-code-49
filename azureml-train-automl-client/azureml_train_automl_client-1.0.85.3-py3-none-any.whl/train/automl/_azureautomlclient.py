# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""AutoML object in charge of orchestrating various AutoML runs for predicting models."""
import json
import logging
import os
import os.path
import shutil
import sys
import warnings
from pathlib import Path
from types import ModuleType
from typing import Any, List, Optional, Dict, Union

from msrest.exceptions import HttpOperationError

from automl.client.core.common import logging_utilities
from automl.client.core.common import import_utilities
from automl.client.core.common import utilities as common_utilities
from automl.client.core.common.constants import TelemetryConstants
from automl.client.core.common.logging_utilities import BLACKLISTED_LOGGING_KEYS
from azureml._restclient.constants import RunStatus
from azureml._restclient.experiment_client import ExperimentClient
from azureml._restclient.jasmine_client import JasmineClient
from azureml._restclient.models import IterationTaskDto, LocalHistoryPayload, MiroProxyInputDto
from azureml._restclient.models.create_parent_run_dto import CreateParentRunDto
from azureml.automl.core import dataprep_utilities
from azureml.automl.core import dataset_utilities, package_utilities
from azureml.automl.core.console_writer import ConsoleWriter
from azureml.automl.core.systemusage_telemetry import SystemResourceUsageTelemetryFactory
from azureml.core import Experiment
from azureml.core import Run
from azureml.core._serialization_utils import _serialize_to_dict
from azureml.core.compute_target import AbstractComputeTarget
from azureml.core.runconfig import RunConfiguration
from azureml.exceptions import ServiceException as AzureMLServiceException
from azureml.telemetry import get_diagnostics_collection_info, is_diagnostics_collection_info_available
from azureml.telemetry.activity import log_activity
from . import constants, _logging
from ._automl_feature_config_manager import AutoMLFeatureConfigManager
from ._azureautomlsettings import AzureAutoMLSettings
from ._environment_utilities import modify_run_configuration
from ._logging import TELEMETRY_AUTOML_COMPONENT_KEY
from ._remote_console_interface import RemoteConsoleInterface
from .exceptions import (ClientException,
                         ConfigException,
                         ServiceException,
                         OptionalDependencyMissingException,
                         ValidationException)
from .run import AutoMLRun
from .utilities import friendly_http_exception, _raise_exception


class AzureAutoMLClient:
    """Client to run AutoML experiments on Azure Machine Learning platform."""

    # constants for run properties
    DISPLAY_TASK_TYPE_PROPERTY = 'display_task_type'
    SDK_DEPENDENCIES_PROPERTY = 'dependencies_versions'

    # Caches for querying and printing child runs
    run_map = {}
    metric_map = {}
    properties_map = {}

    def __init__(self, experiment: Experiment, settings: AzureAutoMLSettings):
        """
        Create an AzureAutoMLClient.

        :param settings: the AutoML settings to use
        """
        self.automl_settings = settings
        self.experiment = experiment

        self._status = constants.Status.NotStarted
        self._loop = None
        self._score_max = None
        self._score_min = None
        self._score_best = None
        self._model_max = None
        self._model_min = None
        self._model_best = None
        self._console_writer = ConsoleWriter()

        self.parent_run_id = None   # type: Optional[str]
        self.current_iter = None
        self.input_data = None      # type: Optional[Dict[str, Union[Any, Any]]]
        self._adb_thread = None
        self.onnx_cvt = None        # runtime_type: Optional[OnnxConverter]

        self._check_create_folders(self.automl_settings.path)

        telemetry_set_by_user = True
        # turn on default telemetry collection, if user is not set
        if not is_diagnostics_collection_info_available():
            telemetry_set_by_user = False

        self.logger = _logging.get_logger(automl_settings=self.automl_settings, parent_run_id=None,
                                          child_run_id=None)

        if not telemetry_set_by_user:
            self.logger.info("Telemetry collection is not set, turning it on by default.")

        send_telemetry, level = get_diagnostics_collection_info(component_name=TELEMETRY_AUTOML_COMPONENT_KEY)
        self.automl_settings.telemetry_verbosity = level
        self.automl_settings.send_telemetry = send_telemetry
        self._usage_telemetry = SystemResourceUsageTelemetryFactory.get_system_usage_telemetry(
            self.logger)
        self._usage_telemetry.start()

        self.experiment_start_time = None

        if not self.automl_settings.show_warnings:
            # sklearn forces warnings, so we disable them here
            warnings.simplefilter('ignore', DeprecationWarning)
            warnings.simplefilter('ignore', RuntimeWarning)
            warnings.simplefilter('ignore', UserWarning)
            warnings.simplefilter('ignore', FutureWarning)

        # Setup the user script.
        self._setup_data_script()

        # Set up clients to communicate with AML services
        self._jasmine_client = JasmineClient(self.experiment.workspace.service_context, self.experiment.name,
                                             host=self.automl_settings.service_url)
        self.feature_config_manager = AutoMLFeatureConfigManager(self._jasmine_client, self.logger)
        self.experiment_client = ExperimentClient(self.experiment.workspace.service_context, self.experiment.name,
                                                  host=self.automl_settings.service_url)

        self.current_run = None     # type: Optional[AutoMLRun]

    def __del__(self):
        """Clean up AutoML loggers and close files."""
        try:
            logging_utilities.cleanup_log_map(self.automl_settings.debug_log,
                                              self.automl_settings.verbosity)

            if self._usage_telemetry is not None:
                self._usage_telemetry.stop()
        except Exception:
            # last chance, nothing can be done, so ignore any exception
            pass

    def cancel(self):
        """
        Cancel the ongoing local run.

        :return: None
        """
        self._status = constants.Status.Terminated

    def _setup_data_script(self) -> None:
        module_path = self.automl_settings.data_script
        if self.automl_settings.data_script is not None:
            # Show warnings to user when use the data_script.
            warnings.warn('Please make sure in the data script the data script '
                          'uses the paths of data files on the remote machine.'
                          'The data script is not recommended anymore, '
                          'please take a look at the latest documentation to use the dprep interface.')

            if self.automl_settings.path is None:
                raise ConfigException('Please set the path (the project folder) in AutoMLConfig.')

            is_data_script_in_proj_dir = True
            if not os.path.exists(self.automl_settings.data_script):
                # Check if the data_script is a relative sub path from the project path (automl_settings.path)
                script_path = os.path.join(self.automl_settings.path,
                                           self.automl_settings.data_script)
                if os.path.exists(script_path):
                    module_path = script_path
                else:
                    raise ConfigException("Could not find data script with name '{0}' or '{1}'."
                                          .format(self.automl_settings.data_script, script_path))
            else:
                # Check if the data_script path is under the project path or it's sub folders.
                try:
                    path_script = Path(self.automl_settings.data_script)
                    path_project = Path(self.automl_settings.path)
                    if path_project not in path_script.parents:
                        is_data_script_in_proj_dir = False
                except Exception:
                    is_data_script_in_proj_dir = False
                module_path = self.automl_settings.data_script

            # Check if the data_script path is actually a file path.
            if not os.path.isfile(module_path):
                raise ConfigException("The provided user script path '{0}' is not a file."
                                      .format(self.automl_settings.data_script))

            # Make sure the script_path (the data script path) has the script file named as DATA_SCRIPT_FILE_NAME.
            module_file_name = os.path.basename(module_path)
            if module_file_name != constants.DATA_SCRIPT_FILE_NAME:
                raise ConfigException("The data script file name '{}' is incorrect, please use '{}'."
                                      .format(module_file_name, constants.DATA_SCRIPT_FILE_NAME))

            # If data_script is not in project folder, copy the data_script file into the project folder.
            # We'll take the snapshot of the project folder.
            if not is_data_script_in_proj_dir:
                # Need to copy the data script file.
                des_module_path = os.path.join(self.automl_settings.path,
                                               constants.DATA_SCRIPT_FILE_NAME)
                shutil.copy(os.path.abspath(module_path), des_module_path)
                module_path = des_module_path

            try:
                import azureml.train.automl.runtime
                from azureml.train.automl.runtime import utilities as utils
                from azureml.automl.runtime import training_utilities
                from automl.client.core.runtime import utilities as runtime_utilities
                self.user_script = runtime_utilities._load_user_script(
                    module_path, self.logger)  # type: Optional[ModuleType]
                self.input_data = training_utilities._extract_user_data(self.user_script)
                training_utilities.auto_blacklist(self.input_data, self.automl_settings)
                if self.automl_settings.exclude_nan_labels:
                    self.input_data = runtime_utilities._y_nan_check(self.input_data)
            except ConfigException:
                raise
            except Exception as e:
                self.logger.warning('Failed to load user script, skipping.')
                logging_utilities.log_traceback(e, self.logger)
                self.user_script = None
        else:
            self.user_script = None

    def fit(self,
            run_configuration: Optional[RunConfiguration] = None,
            compute_target: Optional[AbstractComputeTarget] = None,
            X: Optional[Any] = None,
            y: Optional[Any] = None,
            sample_weight: Optional[Any] = None,
            X_valid: Optional[Any] = None,
            y_valid: Optional[Any] = None,
            sample_weight_valid: Optional[Any] = None,
            cv_splits_indices: Optional[List[Any]] = None,
            show_output: bool = False,
            existing_run: bool = False,
            training_data: Optional[Any] = None,
            validation_data: Optional[Any] = None,
            _script_run: Optional[Run] = None,
            kwargs: Optional[Dict[str, Any]] = None) -> AutoMLRun:
        """
        Start a new AutoML execution on the specified compute target.

        :param run_configuration: The run confiuguration used by AutoML, should contain a compute target for remote
        :type run_configuration: Azureml.core RunConfiguration
        :param compute_target: The AzureML compute node to run this experiment on
        :type compute_target: azureml.core.compute.AbstractComputeTarget
        :param X: Training features
        :type X: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow or
                 azureml.core.Dataset, azureml.data.dataset_definition.DatasetDefinition
                 or azureml.data.TabularDataset
        :param y: Training labels
        :type y: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow or
                 azureml.core.Dataset, azureml.data.dataset_definition.DatasetDefinition
                 or azureml.data.TabularDataset
        :param sample_weight:
        :type sample_weight: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow
                or azureml.data.TabularDataset
        :param X_valid: validation features
        :type X_valid: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow or
                   azureml.core.Dataset, azureml.data.dataset_definition.DatasetDefinition
                   or azureml.data.TabularDataset
        :param y_valid: validation labels
        :type y_valid: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow or
                   azureml.core.Dataset, azureml.data.dataset_definition.DatasetDefinition
                   or azureml.data.TabularDataset
        :param sample_weight_valid: validation set sample weights
        :type sample_weight_valid: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow
                or azureml.data.TabularDataset
        :param cv_splits_indices: Indices where to split training data for cross validation
        :type cv_splits_indices: list(int), or list(Dataflow) in which each Dataflow represent a train-valid set
                                 where 1 indicates record for training and 0 indicates record for validation
        :param show_output: Flag whether to print output to console
        :type show_output: bool
        :param existing_run: Flag whether this is a continuation of a previously completed experiment
        :type existing_run: bool
        :param _script_run: Run to associate with parent run id
        :type _script_run: azureml.core.Run
        :return: AutoML parent run
        :rtype: azureml.train.automl.AutoMLRun
        """
        self._status = constants.Status.Started

        if show_output:
            self._console_writer = ConsoleWriter(sys.stdout)

        if run_configuration is None:
            run_configuration = RunConfiguration()
            if compute_target is not None:
                run_configuration.name = compute_target.name
                self._console_writer.println('No run_configuration provided, running on {0} with default configuration'
                                             .format(compute_target.name))
            else:
                self._console_writer.println(
                    'No run_configuration provided, running locally with default configuration')
            run_configuration.environment.docker.enabled = True

        if run_configuration.framework.lower() != 'python':
            raise ConfigException('AutoML requires the run configuration framework to be set to "Python".')

        self.automl_settings.compute_target = run_configuration.target

        # Save the Dataset to Workspace so that its saved id will be logged for telemetry and lineage
        dataset_utilities.ensure_saved(
            self.experiment.workspace, X=X, y=y, sample_weight=sample_weight, X_valid=X_valid, y_valid=y_valid,
            sample_weight_valid=sample_weight_valid, training_data=training_data, validation_data=validation_data
        )

        dataset_utilities.collect_usage_telemetry(
            compute=run_configuration.target, spark_context=self.automl_settings.spark_context,
            X=X, y=y, sample_weight=sample_weight, X_valid=X_valid, y_valid=y_valid,
            sample_weight_valid=sample_weight_valid, training_data=training_data, validation_data=validation_data
        )

        X, y, sample_weight, X_valid, y_valid, sample_weight_valid = dataset_utilities.convert_inputs(
            X, y, sample_weight, X_valid,
            y_valid, sample_weight_valid
        )

        training_data, validation_data = dataset_utilities.convert_inputs_dataset(
            training_data,
            validation_data
        )

        try:
            if self.automl_settings.spark_context:
                try:
                    from azureml.train.automl.runtime import _runtime_client
                    runtime_client = _runtime_client.RuntimeClient(self)
                    runtime_client._init_adb_driver_run(run_configuration=run_configuration,
                                                        X=X,
                                                        y=y,
                                                        sample_weight=sample_weight,
                                                        X_valid=X_valid,
                                                        y_valid=y_valid,
                                                        sample_weight_valid=sample_weight_valid,
                                                        cv_splits_indices=cv_splits_indices,
                                                        training_data=training_data,
                                                        validation_data=validation_data,
                                                        show_output=show_output)
                except Exception:
                    raise
            elif run_configuration.target == 'local':
                if self.automl_settings.path is None:
                    self.automl_settings.path = '.'
                name = run_configuration._name if run_configuration._name else "local"
                run_configuration.save(self.automl_settings.path, name)
                self._console_writer.println('Running on local machine')
                try:
                    from azureml.train.automl.runtime import _runtime_client
                except ImportError:
                    raise OptionalDependencyMissingException("azureml-train-automl-runtime must be installed in the"
                                                             "current environment to run local in process runs. "
                                                             "Please install this dependency or provide a"
                                                             "RunConfiguration.")
                runtime_client = _runtime_client.RuntimeClient(self)
                runtime_client._fit_local(
                    X=X, y=y, sample_weight=sample_weight, X_valid=X_valid, y_valid=y_valid,
                    cv_splits_indices=cv_splits_indices,
                    existing_run=existing_run, sample_weight_valid=sample_weight_valid,
                    training_data=training_data, validation_data=validation_data, _script_run=_script_run)
            else:
                self._console_writer.println('Running on remote compute: ' + str(run_configuration.target))
                self.automl_settings.debug_log = "azureml_automl.log"
                self._fit_remote(run_configuration, X=X, y=y, sample_weight=sample_weight,
                                 X_valid=X_valid, y_valid=y_valid, sample_weight_valid=sample_weight_valid,
                                 cv_splits_indices=cv_splits_indices, show_output=show_output,
                                 training_data=training_data, validation_data=validation_data)
        except Exception as e:
            if self.current_run:
                self._fail_parent_run(error_details=e, logger=self.logger)
            raise
        assert self.current_run is not None
        return self.current_run

    def _fit_remote(self, run_configuration, X=None, y=None, sample_weight=None, X_valid=None, y_valid=None,
                    sample_weight_valid=None, cv_splits_indices=None, show_output=False,
                    training_data=None, validation_data=None):

        self._fit_remote_core(run_configuration, X=X, y=y, sample_weight=sample_weight, X_valid=X_valid,
                              y_valid=y_valid, sample_weight_valid=sample_weight_valid,
                              cv_splits_indices=cv_splits_indices, training_data=training_data,
                              validation_data=validation_data)
        if show_output:
            RemoteConsoleInterface._show_output(self.current_run,
                                                self._console_writer,
                                                self.logger,
                                                self.automl_settings.primary_metric)

    def _fit_remote_core(self, run_configuration, X=None, y=None, sample_weight=None, X_valid=None, y_valid=None,
                         sample_weight_valid=None, cv_splits_indices=None, training_data=None, validation_data=None):
        run_config_object = run_configuration
        if isinstance(run_configuration, str):
            run_config_object = RunConfiguration.load(
                self.automl_settings.path, run_configuration)

        self._create_parent_run_for_remote(
            run_config_object, X=X, y=y, sample_weight=sample_weight, X_valid=X_valid, y_valid=y_valid,
            sample_weight_valid=sample_weight_valid, cv_splits_indices=cv_splits_indices,
            training_data=training_data, validation_data=validation_data)

        snapshotId = ""
        if self.automl_settings.path is not None:
            snapshotId = self.current_run.take_snapshot(self.automl_settings.path)
        self.logger.info("Snapshotted folder: {0} with snapshot_id: {1}".format(
            self.automl_settings.path, snapshotId))

        definition = {
            "Configuration": _serialize_to_dict(run_config_object)
        }

        definition["Configuration"]["environment"]["python"]["condaDependencies"] = \
            run_config_object.environment.python.conda_dependencies._conda_dependencies

        self.logger.info("Starting a snapshot run (snapshotId : {0})".format(snapshotId))
        try:
            self._jasmine_client.post_remote_jasmine_snapshot_run(self.parent_run_id,
                                                                  json.dumps(definition),
                                                                  snapshotId)
        except (AzureMLServiceException, HttpOperationError) as e:
            logging_utilities.log_traceback(e, self.logger)
            friendly_http_exception(e, constants.API.StartRemoteSnapshotRun)
        except Exception as e:
            logging_utilities.log_traceback(e, self.logger)
            raise ClientException("Error occurred when trying to submit a remote run to AutoML Service.") \
                from None

    def _create_parent_run_for_remote(self, run_config_object, X=None, y=None, sample_weight=None,
                                      X_valid=None, y_valid=None, sample_weight_valid=None, cv_splits_indices=None,
                                      training_data=None, validation_data=None):

        run_configuration = run_config_object.target
        run_config_object = modify_run_configuration(self.automl_settings, run_config_object, self.logger)

        if training_data is not None:
            if dataprep_utilities.is_dataflow(training_data):
                dataprep_json = dataprep_utilities.\
                    get_dataprep_json_dataset(training_data=training_data,
                                              validation_data=validation_data)
            else:
                dataprep_json = dataset_utilities.\
                    get_datasets_json(training_data=training_data,
                                      validation_data=validation_data)
        else:
            dataprep_json = dataprep_utilities.get_dataprep_json(X=X, y=y,
                                                                 sample_weight=sample_weight,
                                                                 X_valid=X_valid,
                                                                 y_valid=y_valid,
                                                                 sample_weight_valid=sample_weight_valid,
                                                                 cv_splits_indices=cv_splits_indices)
        if dataprep_json is not None:
            # escape quotations in json_str before sending to jasmine
            dataprep_json = dataprep_json.replace('\\', '\\\\').replace('"', '\\"')

        parent_run_dto = self._create_parent_run_dto(run_configuration, dataprep_json)

        self._validate_remote_input(parent_run_dto)

        try:
            self.logger.info("Start creating parent run.")
            self.parent_run_id = self._jasmine_client.post_parent_run(
                parent_run_dto)
        except (AzureMLServiceException, HttpOperationError) as e:
            logging_utilities.log_traceback(e, self.logger)
            _raise_exception(e)
            friendly_http_exception(e, constants.API.CreateParentRun)
        except Exception as e:
            logging_utilities.log_traceback(e, self.logger)
            raise ClientException(
                "Error occurred when trying to create new parent run in AutoML service.") from None

        if self.user_script:
            self.logger.info(
                "[ParentRunID:{}] Remote run using user script.".format(self.parent_run_id))
        else:
            self.logger.info(
                "[ParentRunID:{}] Remote run using input X and y.".format(self.parent_run_id))

        if self.current_run is None:
            self.current_run = AutoMLRun(self.experiment, self.parent_run_id, host=self.automl_settings.service_url)

        # For back compatibility, check if the properties were added already as part of create parent run dto.
        # If not, add it here. Note that this should be removed once JOS changes are stably deployed
        if (self.DISPLAY_TASK_TYPE_PROPERTY not in self.current_run.properties or
                self.SDK_DEPENDENCIES_PROPERTY not in self.current_run.properties):
            properties_to_update = self._get_current_run_properties_to_update()
            self.current_run.add_properties(properties_to_update)

        self._console_writer.println("Parent Run ID: " + self.parent_run_id)
        self.logger.info("Parent Run ID: " + self.parent_run_id)

    def _validate_remote_input(self, parent_run_dto: CreateParentRunDto) -> None:
        validation_results = None
        try:
            validation_results = self._jasmine_client.post_validate_service(parent_run_dto)
        except HttpOperationError as e:
            if e.response.status_code == 204:
                self.logger.info("Validation service found the data has no errors.")
            else:
                # Any validation related exception won't fail the experiment.
                self.logger.warning("Non-terminal error returned by validation service.")
        except Exception:
            # Any other validation related exception won't fail the experiment.
            self.logger.warning("Validation service meet exceptions, continue training now.")

        if validation_results is not None and len(validation_results.error.details) > 0 \
                and any([d.code != "UpstreamSystem" for d in validation_results.error.details]):
            # If validation service meets error thrown by the upstream service, the run will continue.
            self._console_writer.println("The validation results are as follows:")
            errors = []
            for result in validation_results.error.details:
                if result.code != "UpstreamSystem":
                    self._console_writer.println(result.message)
                    errors.append(result.message)
            raise ValidationException\
                .create_without_pii(msg="Validation error(s): {}".format(validation_results.error.details))\
                .with_generic_msg(
                    "Validation failed. Please fix the data or settings following the validation results."
                )

    def _create_parent_run_dto(self, target, dataprep_json=None):
        """
        Create CreateParentRunDto.

        :param target: run configuration
        :type target: RunConfiguration or str
        :param dataprep_json: dataprep json string
        :type dataprep_json: str
        :return: CreateParentRunDto to be sent to Jasmine
        :rtype: CreateParentRunDto
        """
        # min to sec conversion
        timeout = None
        if self.automl_settings.iteration_timeout_minutes:
            timeout = self.automl_settings.iteration_timeout_minutes * 60
        parent_run_dto = CreateParentRunDto(target=target,
                                            num_iterations=self.automl_settings.iterations,
                                            training_type=None,  # use self.training_type when jasmine supports it
                                            acquisition_function=None,
                                            metrics=['accuracy'],
                                            primary_metric=self.automl_settings.primary_metric,
                                            train_split=self.automl_settings.validation_size,
                                            max_time_seconds=timeout,
                                            acquisition_parameter=0.0,
                                            num_cross_validation=self.automl_settings.n_cross_validations,
                                            raw_aml_settings_string=str(
                                                self.automl_settings.as_serializable_dict()),
                                            aml_settings_json_string=json.dumps(
                                                self.automl_settings.as_serializable_dict()),
                                            data_prep_json_string=dataprep_json,
                                            enable_subsampling=self.automl_settings.enable_subsampling,
                                            properties=self._get_current_run_properties_to_update())
        return parent_run_dto

    def _create_child_run(self, task_dto: IterationTaskDto) -> Run:
        run_id = task_dto.childrun_id
        self.logger.update_default_property("child_run_id", run_id)
        child_run = Run(self.experiment, run_id)
        return child_run

    def _get_task(self, previous_fit_outputs):
        """
        Query Jasmine for the next task.

        :param previous_fit_outputs: Outputs of the previous tasks that executed
        :type previous_fit_outputs: List[FitOutput]
        :return: dto containing task details
        """
        with log_activity(logger=self.logger, activity_name=TelemetryConstants.GET_PIPELINE_NAME):
            try:
                self.logger.info("Querying Jasmine for next task.")
                local_history_payload = None    # type: Optional[LocalHistoryPayload]
                if previous_fit_outputs:
                    # TODO: VSO-562043 - Add training_percents as well
                    local_history_payload = LocalHistoryPayload(input_df=MiroProxyInputDto(
                        pipeline_ids=[p.pipeline_id for p in previous_fit_outputs],
                        scores=[p.score for p in previous_fit_outputs],
                        run_algorithms=[p.run_algorithm for p in previous_fit_outputs],
                        run_preprocessors=[p.run_preprocessor for p in previous_fit_outputs],
                        iteration_numbers=list(range(len(previous_fit_outputs))),
                        predicted_times=[p.predicted_time for p in previous_fit_outputs],
                        actual_times=[p.actual_time for p in previous_fit_outputs],
                        training_percents=[p.training_percent for p in previous_fit_outputs]
                    ))
                return self._jasmine_client.get_next_task(self.parent_run_id, local_history_payload)
            except (AzureMLServiceException, HttpOperationError) as e:
                logging_utilities.log_traceback(e, self.logger)
                friendly_http_exception(e, constants.API.GetNextPipeline)
            except Exception as e:
                logging_utilities.log_traceback(e, self.logger)
                raise ServiceException("Error occurred when trying to fetch next iteration from AutoML service.") \
                    from None

    def _check_create_folders(self, path):
        if path is None:
            path = os.getcwd()
        # Expand out the path because os.makedirs can't handle '..' properly
        aml_config_path = os.path.abspath(os.path.join(path, '.azureml'))
        os.makedirs(aml_config_path, exist_ok=True)

    def _get_display_task(self) -> str:
        """Get display task property."""
        # This property is to temporarily fix: 362194.
        # It should be removed promptly.
        task = self.automl_settings.task_type
        if self.automl_settings.is_timeseries:
            task = constants.Tasks.FORECASTING
        return task

    def _get_current_run_properties_to_update(self):
        """Get properties to update on the current run object."""
        # TODO: Remove with task 416022
        display_task_type_property = {self.DISPLAY_TASK_TYPE_PROPERTY: self._get_display_task()}

        # Log the AzureML packages currently installed on the local machine to the given run.
        user_sdk_dependencies_property = \
            {self.SDK_DEPENDENCIES_PROPERTY: json.dumps(package_utilities.get_sdk_dependencies())}
        self.logger.info(
            "SDK dependencies versions:{}.".format(user_sdk_dependencies_property['dependencies_versions']))

        # Make sure to batch all relevant properties in this single call in-order to avoid multiple network trips to RH
        result = {**display_task_type_property, **user_sdk_dependencies_property}
        return result

    def _fail_parent_run(self, error_details: BaseException, logger: logging.Logger) -> None:
        logging_utilities.log_traceback(error_details, logger)

        assert self.current_run is not None, "Cannot fail a parent run before it is created"

        try:
            # If the run is already in a terminal state, don't update the status again
            current_run_status = self.current_run.get_status()
            if current_run_status in [RunStatus.COMPLETED, RunStatus.FAILED, RunStatus.CANCELED]:
                self.logger.warning('Cannot fail the current run since it is already in a terminal state of [{}].'.
                                    format(current_run_status))
                return
            if self.current_run is not None:
                self.current_run.fail(error_details=error_details,
                                      error_code=common_utilities.get_error_code(error_details))
            if self._jasmine_client is not None and self.parent_run_id is not None:
                self._jasmine_client.set_parent_run_status(self.parent_run_id, constants.RunState.FAIL_RUN)
        except (AzureMLServiceException, HttpOperationError) as e:
            logging_utilities.log_traceback(e, logger)
            friendly_http_exception(e, constants.API.CreateParentRun)
        except Exception as e:
            logging_utilities.log_traceback(e, logger)
            raise ClientException(
                "Error occurred when trying to set parent run status.") from None

    @staticmethod
    def _set_environment_variables_for_reconstructing_run(run):
        os.environ['AZUREML_ARM_SUBSCRIPTION'] = run.experiment.workspace.subscription_id
        os.environ["AZUREML_RUN_ID"] = run.id
        os.environ["AZUREML_ARM_RESOURCEGROUP"] = run.experiment.workspace.resource_group
        os.environ["AZUREML_ARM_WORKSPACE_NAME"] = run.experiment.workspace.name
        os.environ["AZUREML_ARM_PROJECT_NAME"] = run.experiment.name
        os.environ['AZUREML_RUN_TOKEN'] = run._client.run.get_token().token
        os.environ["AZUREML_SERVICE_ENDPOINT"] = run._client.run.get_cluster_url()

    @staticmethod
    def _is_any_childruns_succeed(run):
        return any([r.status.lower() == constants.RunState.COMPLETE_RUN for r in run.get_children()])

    @staticmethod
    def _is_tensorflow_module_present():
        try:
            from automl.client.core.runtime import pipeline_spec
            return pipeline_spec.tf_wrappers.tf_found
        except Exception:
            return False

    @staticmethod
    def _is_xgboost_module_present():
        try:
            from automl.client.core.runtime import model_wrappers
            return model_wrappers.xgboost_present
        except Exception:
            return False

    @staticmethod
    def _is_fbprophet_module_present():
        fbprophet = import_utilities.import_fbprophet(raise_on_fail=False)
        return fbprophet is not None

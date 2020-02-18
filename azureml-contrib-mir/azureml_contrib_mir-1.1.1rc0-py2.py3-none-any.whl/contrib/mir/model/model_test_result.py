# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Module for Model Profiling in Azure Machine Learning."""

import sys
import time
import logging
import json
from dateutil.parser import parse

from abc import ABC, abstractmethod
from azureml._model_management._util import get_mms_operation, get_operation_output
from azureml.exceptions import WebserviceException, UserErrorException

module_logger = logging.getLogger(__name__)


class ModelTestResult(ABC):
    """
    ModelTestResult abstract object that serves as a base for results of profiling and validation
    """

    @property
    @classmethod
    @abstractmethod
    def _model_test_type(cls):
        return NotImplementedError

    @property
    @classmethod
    @abstractmethod
    def _general_mms_suffix(cls):
        return NotImplementedError

    @property
    @classmethod
    @abstractmethod
    def _expected_payload_keys(cls):
        return NotImplementedError

    @abstractmethod
    def __repr__(self):
        """Return the string representation of the ModelTestResult object.
        :return: String representation of the ModelTestResult object
        :rtype: str
        """
        return NotImplementedError

    @abstractmethod
    def get_details(self):
        """Return the the observed metrics and other details of the model test operation.

        :return: Dictionary of metrics
        :rtype: dict[str, float]
        """
        return NotImplementedError

    _details_keys_success = [
        "requestedCpu",
        "requestedMemoryInGB",
        "requestedQueriesPerSecond",
        "maxUtilizedMemoryInGB",
        "maxUtilizedCpu",
        "totalQueries",
        "successQueries",
        "successRate",
        "averageLatencyInMs",
        "latencyPercentile50InMs",
        "latencyPercentile90InMs",
        "latencyPercentile95InMs",
        "latencyPercentile99InMs",
        "latencyPercentile999InMs",
        "measuredQueriesPerSecond",
        "state",
        "name",
    ]

    _details_keys_error = [
        "name",
        "state",
        "requestedCpu",
        "requestedMemoryInGB",
        "requestedQueriesPerSecond",
        "error",
        "errorLogsUri",
    ]

    def __init__(self, workspace, name):
        """Initialize the ModelTestResult object.

        :param workspace: The workspace object containing the model
        :type workspace: azureml.core.Workspace
        :param name: The name of the profile to construct and retrieve.
        :type name: str
        :rtype: azureml.core.profile.ModelTestResult
        """
        self.workspace = workspace
        self.name = name
        # setting default values for properties needed to communicate with MMS
        self.create_operation_id = None
        self._model_test_result_suffix = None
        self._model_test_result_params = {}

        # TODO: remove once the old workflow is deprecated
        self.image_id = None
        self._expected_payload_keys = self.__class__._expected_payload_keys

        super(ModelTestResult, self).__init__()

    def _initialize(self, obj_dict):
        """Initialize the base properites of an instance of subtype of ModelTestResult.

        This is used because the constructor is used as a getter.

        :param workspace:
        :type workspace: azureml.core.Workspace
        :param obj_dict:
        :type obj_dict: dict
        :return:
        :rtype: None
        """
        self.name = obj_dict.get("name")
        self.description = obj_dict.get("description")
        self.created_time = (
            parse(obj_dict["createdTime"]) if "createdTime" in obj_dict else None
        )
        self.id = obj_dict.get("id")
        container_resource_requirements = obj_dict.get("containerResourceRequirements")
        self.requested_cpu = (
            container_resource_requirements["cpu"]
            if container_resource_requirements
            else None
        )
        self.requested_memory_in_gb = (
            container_resource_requirements["memoryInGB"]
            if container_resource_requirements
            else None
        )
        self.requested_queries_per_second = obj_dict.get("requestedQueriesPerSecond")
        self.input_dataset_id = obj_dict.get("inputDatasetId")
        self.state = obj_dict.get("state")
        self.model_ids = obj_dict.get("modelIds")
        # detail properties
        self.max_utilized_memory = obj_dict.get("maxUtilizedMemoryInGB")
        self.max_utilized_cpu = obj_dict.get("maxUtilizedCpu")
        self.measured_queries_per_second = obj_dict.get("measuredQueriesPerSecond")
        self.environment = obj_dict.get("environment")
        self.error = obj_dict.get("error")
        self.error_logs_url = obj_dict.get("errorLogsUri")
        self.total_queries = obj_dict.get("totalQueries")
        self.success_queries = obj_dict.get("successQueries")
        self.success_rate = obj_dict.get("successRate")
        self.average_latency_in_ms = obj_dict.get("averageLatencyInMs")
        self.latency_percentile_50_in_ms = obj_dict.get("latencyPercentile50InMs")
        self.latency_percentile_90_in_ms = obj_dict.get("latencyPercentile90InMs")
        self.latency_percentile_95_in_ms = obj_dict.get("latencyPercentile95InMs")
        self.latency_percentile_99_in_ms = obj_dict.get("latencyPercentile99InMs")
        self.latency_percentile_999_in_ms = obj_dict.get("latencyPercentile999InMs")

    # TODO: once old worklflow is deprecated set this method to be a classmethod and us class variable
    def _validate_get_payload(self, payload):
        """Validate the returned ModelTestResult payload.

        :param payload:
        :type payload: dict
        :return:
        :rtype: None
        """
        for payload_key in self._expected_payload_keys:
            if payload_key not in payload:
                raise WebserviceException(
                    "Invalid payload for %s, missing %s:\n %s"
                    % (self.__class__._model_test_type, payload_key, payload)
                )

    def _get_operation_state(self):
        """Get the current async operation state for the a model test operation.

        :return:
        :rtype: (str, dict)
        """
        resp_content = get_mms_operation(self.workspace, self.create_operation_id)
        state = resp_content["state"]
        error = resp_content["error"] if "error" in resp_content else None
        return state, error

    def _update_creation_state(self):
        """Refresh the current state of the in-memory object.

        Perform an in-place update of the properties of the object based on the current state of the
        corresponding cloud object. Primarily useful for manual polling of creation state.

        :raises: azureml.exceptions.WebserviceException
        """
        resp = get_operation_output(self.workspace, self._model_test_result_suffix, self._model_test_result_params)
        if resp.status_code != 200:
            error_message = "Model {} result with name {}".format(
                self.__class__._model_test_type, self.name
            )
            if self.image_id:
                # TODO: deprecate
                error_message += ", Model package {}".format(self.image_id)
            error_message += " not found in provided workspace"
            raise WebserviceException(error_message)
        content = resp.content
        if isinstance(content, bytes):
            content = content.decode("utf-8")
        if self.image_id:
            # TODO: deprecate
            model_test_json = json.loads(content)
        else:
            model_test_json = json.loads(content)['value'][0]
        self._validate_get_payload(model_test_json)
        self._initialize(model_test_json)

    def wait_for_completion(self, show_output=False):
        """Wait for the model test result to finish the testing (profiling or validation) process.

        :param show_output: Boolean option to print more verbose output. Defaults to False
        :type show_output: bool
        """
        if not (self.workspace and self.create_operation_id):
            raise UserErrorException("wait_for_completion operation cannot be performed on this object."
                                     "Make sure the object was created via the appropriate method "
                                     "in the Model class")
        operation_state, error = self._get_operation_state()
        current_state = operation_state
        if show_output:
            sys.stdout.write("{}".format(current_state))
            sys.stdout.flush()
        while operation_state not in ["Cancelled", "Succeeded", "Failed", "TimedOut"]:
            time.sleep(5)
            operation_state, error = self._get_operation_state()
            if show_output:
                sys.stdout.write(".")
                if operation_state != current_state:
                    sys.stdout.write("\n{}".format(operation_state))
                    current_state = operation_state
                sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
        module_logger.info(
            'Model {} operation with name {} finished operation "{}"'.format(
                self.__class__._model_test_type, self.name, operation_state
            )
        )
        if operation_state == "Failed":
            if error and "statusCode" in error and "message" in error:
                module_logger.info(
                    "Model {} failed with\n"
                    "StatusCode: {}\n"
                    "Message: {}\n"
                    "Operation ID: {}\n".format(
                        self.__class__._model_test_type,
                        error["statusCode"],
                        error["message"],
                        self.create_operation_id
                    )
                )
            else:
                module_logger.info(
                    "Model profiling failed, unexpected error response:\n"
                    "{}\n"
                    "Operation ID: {}".format(error, self.create_operation_id)
                )
        self._update_creation_state()

    def serialize(self):
        """Convert this ModelTestResult object into a json serialized dictionary.

        :return: The json representation of this ModelTestResult
        :rtype: dict
        """
        created_time = self.created_time.isoformat() if self.created_time else None
        return {
            "id": self.id,
            "name": self.name,
            "createdTime": created_time,
            "state": self.state,
            "description": self.description,
            "requestedCpu": self.requested_cpu,
            "requestedMemoryInGB": self.requested_memory_in_gb,
            "requestedQueriesPerSecond": self.requested_queries_per_second,
            "inputDatasetId": self.input_dataset_id,
            "maxUtilizedMemoryInGB": self.max_utilized_memory,
            "totalQueries": self.total_queries,
            "successQueries": self.success_queries,
            "successRate": self.success_rate,
            "averageLatencyInMs": self.average_latency_in_ms,
            "latencyPercentile50InMs": self.latency_percentile_50_in_ms,
            "latencyPercentile90InMs": self.latency_percentile_90_in_ms,
            "latencyPercentile95InMs": self.latency_percentile_95_in_ms,
            "latencyPercentile99InMs": self.latency_percentile_99_in_ms,
            "latencyPercentile999InMs": self.latency_percentile_999_in_ms,
            "modelIds": self.model_ids,
            "environment": self.environment,
            "maxUtilizedCpu": self.max_utilized_cpu,
            "measuredQueriesPerSecond": self.measured_queries_per_second,
            "error": self.error,
            "errorLogsUri": self.error_logs_url,
        }

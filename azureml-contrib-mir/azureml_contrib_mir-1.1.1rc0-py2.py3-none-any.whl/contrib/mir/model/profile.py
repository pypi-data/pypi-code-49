# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Module for Model Profiling in Azure Machine Learning."""

from .model_test_result import ModelTestResult
from azureml._model_management._constants import (
    PROFILE_RECOMMENDED_CPU_KEY,
    PROFILE_RECOMMENDED_MEMORY_KEY,
)
import logging


module_logger = logging.getLogger(__name__)


class ModelProfile(ModelTestResult):
    """
    ModelProfile object contains the results of a profiling run.

    :param workspace: The workspace object containing the image to retrieve
    :type workspace: azureml.core.Workspace
    :param image_id: ID of the image associated with the profile name
    :type image_id: str
    :param name: The name of the profile to retrieve.
    :type name: str
    :param description: Field for profile description
    :type description: str
    :param input_data: The input data used for profiling
    :type input_data: varies
    :param tags: Dictionary of mutable tags
    :type tags: dict[str, str]
    :param properties: Dictionary of appendable properties
    :type properties: dict[str, str]
    :param recommended_memory: The memory recommendation result from profiling in GB
    :type recommended_memory: float
    :param recommended_cpu: The cpu recommendation result from profiling in cores
    :type recommended_cpu: float
    :param recommended_memory_latency: The 90th percentile latency of requests while profiling with
        recommended memory value
    :type recommended_memory_latency: float
    :param recommneded_cpu_latency: The 90th percentile latency of requests while profiling with
        recommended cpu value
    :type recommended_cpu_latency: float
    :param profile_result_url: URL to profiling results
    :type profile_result_url: str
    :param error_logs: URL to profiling error logs
    :type error_logs: str
    :rtype: azureml.core.profile.ModelProfile
    :raises: azureml.exceptions.WebserviceException
    """

    _model_test_type = "profiling"
    _general_mms_suffix = "/profiles"
    _expected_payload_keys = [
        "name",
        "description",
        "id",
        "state",
        "inputDatasetId",
        "containerResourceRequirements",
        "requestedQueriesPerSecond",
        "createdTime",
        "modelIds",
    ]
    _deprecated_expected_payload_keys = [
        "name",
        "description",
        "imageId",
        "inputData",
        "createdTime",
        "kvTags",
        "properties",
    ]

    _details_keys_success = ModelTestResult._details_keys_success + [
        "recommendedMemoryInGB",
        "recommendedCpu",
    ]

    _deprecated_details_keys_error = ["name", "state", "error", "profilingErrorLogs"]

    # TODO: deprecate all the parameters except workspace and name
    def __init__(
        self,
        workspace,
        image_id,
        name,
        description=None,
        input_data=None,
        tags=None,
        properties=None,
        recommended_memory=None,
        recommended_cpu=None,
        recommended_memory_latency=None,
        recommended_cpu_latency=None,
        profile_result_url=None,
        error=None,
        error_logs=None,
    ):
        """Initialize the ModelProfile object.

        :param workspace: The workspace object containing the model
        :type workspace: azureml.core.Workspace
        :param image_id: ID of the image associated with the profile name
        :type image_id: str
        :param name: The name of the profile to create and retrieve.
        :type name: str
        :param description: Field for profile description
        :type description: str
        :param input_data: The input data used for profiling
        :type input_data: varies
        :param tags: Dictionary of mutable tags
        :type tags: dict[str, str]
        :param properties: Dictionary of appendable properties
        :type properties: dict[str, str]
        :param recommended_memory: The memory recommendation result from profiling in GB
        :type recommended_memory: float
        :param recommended_cpu: The cpu recommendation result from profiling in cores
        :type recommended_cpu: float
        :param recommended_memory_latency: The 90th percentile latency of requests while profiling with
            recommended memory value
        :type recommended_memory_latency: float
        :param recommneded_cpu_latency: The 90th percentile latency of requests while profiling with
            recommended cpu value
        :type recommended_cpu_latency: float
        :param profile_result_url: URL to profiling results
        :type profile_result_url: str
        :param error_logs: URL to profiling error logs
        :type error_logs: str
        :rtype: azureml.core.profile.ModelProfile
        :raises: azureml.exceptions.WebserviceException
        """
        super(ModelProfile, self).__init__(workspace, name)

        # TODO: deprecate. Old Workflow support
        if image_id:
            self.image_id = image_id
            self._expected_payload_keys = (
                self.__class__._deprecated_expected_payload_keys
            )
            if workspace and name:
                self._model_test_result_suffix = "/images/{0}/profiles/{1}".format(
                    image_id, name
                )
        # new endpoint
        elif workspace and name:
            self._model_test_result_suffix = self.__class__._general_mms_suffix
            self._model_test_result_params = {'name': name}

        if self._model_test_result_suffix:
            # retrieve object from MMS and update state
            self._update_creation_state()
        else:
            # sets all properties associated with profiling result to None
            self._initialize({})

    def _initialize(self, obj_dict):
        """Initialize the Profile instance.

        This is used because the constructor is used as a getter.

        :param workspace:
        :type workspace: azureml.core.Workspace
        :param obj_dict:
        :type obj_dict: dict
        :return:
        :rtype: None
        """
        super(ModelProfile, self)._initialize(obj_dict)
        self.recommended_memory = obj_dict.get("recommendedMemoryInGB")
        self.recommended_cpu = obj_dict.get("recommendedCpu")
        if self.image_id:
            # TODO: deprecate
            # old workflow required properties
            self.imageId = obj_dict.get("imageId")
            self.tags = obj_dict.get("kvTags")
            self.properties = obj_dict.get("properties")
            # old workflow detail properties
            # once  the new workflow is extended to test on a grid, recommendationLatencyInMs should be removed
            # since the details latency metrics will reflect the latency measurements on the recommended instance.
            self.recommendation_latency = obj_dict.get("recommendationLatencyInMs")
            self.recommended_memory_latency = obj_dict.get(
                "recommendedMemoryLatencyInMs"
            )
            self.recommended_cpu_latency = obj_dict.get("recommendedCpuLatencyInMs")
            self.input_data = obj_dict.get("inputData")
            self.tags = obj_dict.get("kvTags")
            self.properties = obj_dict.get("properties")
            self.profile_result_url = obj_dict.get("profileRunResult")
            self.error_logs = obj_dict.get("profilingErrorLogs")

    # TODO: needs to be deprecated
    def wait_for_profiling(self, show_output=False):
        """Wait for the model to finish profiling.
        :param show_output: Boolean option to print more verbose output. Defaults to False
        :type show_output: bool
        """
        self.wait_for_completion(show_output)

    def serialize(self):
        """Convert this Profile into a json serialized dictionary.

        :return: The json representation of this Profile
        :rtype: dict
        """
        if self.image_id:
            # TODO: old workflow - to be deprecated
            created_time = self.created_time.isoformat() if self.created_time else None
            return {
                "name": self.name,
                "createdTime": created_time,
                "description": self.description,
                "inputData": self.input_data,
                "tags": self.tags,
                "properties": self.properties,
                "recommendedMemoryInGB": self.recommended_memory,
                "recommendedCpu": self.recommended_cpu,
                "recommendationLatencyInMs": self.recommendation_latency,
                "recommendedMemoryLatencyInMs": self.recommended_memory_latency,
                "recommendedCpuLatencyInMs": self.recommended_cpu_latency,
                "profileRunResult": self.profile_result_url,
                "state": self.state,
                "error": self.error,
                "profilingErrorLogs": self.error_logs,
            }
        dict_repr = super(ModelProfile, self).serialize()
        dict_repr.update(
            {
                "recommendedMemoryInGB": self.recommended_memory,
                "recommendedCpu": self.recommended_cpu,
            }
        )
        return dict_repr

    def __repr__(self):
        """Return the string representation of the ModelProfile object.
        :return: String representation of the ModelProfile object
        :rtype: str
        """
        if self.image_id:
            # TODO: old workflow - to be deprecated
            return (
                "{}(workspace={}, image_id={}, name={}, input_data={}, recommended_memory={}, recommended_cpu={}, "
                "profile_result_url={}, error={}, error_logs={}, tags={}, "
                "properties={})".format(
                    self.__class__.__name__,
                    self.workspace.__repr__(),
                    self.image_id,
                    self.name,
                    self.input_data,
                    self.recommended_memory,
                    self.recommended_cpu,
                    self.profile_result_url,
                    self.error,
                    self.error_logs_url,
                    self.tags,
                    self.properties,
                )
            )
        str_repr = []
        str_repr.append(("workspace" + "=%s") % repr(self.workspace))
        for key in self.__dict__:
            if key[0] != "_" and key not in ["workspace"]:
                str_repr.append((key + "=%s") % self.__dict__[key])
        str_repr = "%s(%s)" % (self.__class__.__name__, ", ".join(str_repr))
        return str_repr

    def get_details(self):
        """Return the the observed metrics and recommended resource requirements (if available)
           from the profiling run to the user.

        :return: Dictionary of recommended resource requirements
        :rtype: dict[str, float]
        """
        dict_repr = self.serialize()
        if dict_repr["state"] == "Succeeded":
            return {
                k: dict_repr[k]
                for k in dict_repr
                if (
                    dict_repr[k] is not None and
                    k in self.__class__._details_keys_success
                )
            }
        if self.image_id:
            # TODO: deprecate old workflow
            return {
                k: dict_repr[k]
                for k in dict_repr
                if (
                    dict_repr[k] is not None and
                    k in self.__class__._deprecated_details_keys_error
                )
            }
        return {
            k: dict_repr[k]
            for k in dict_repr
            if (dict_repr[k] is not None and k in self.__class__._details_keys_error)
        }

    # TODO: deprecate the get_results method in favor of get_details
    def get_results(self):
        """Return the recommended resource requirements from the profiling run to the user.

        :return: Dictionary of recommended resource requirements
        :rtype: dict[str, float]
        """
        if self.image_id:
            # TODO: deprecate old workflow
            if self.recommended_cpu is None or self.recommended_memory is None:
                operation_state, _ = self._get_operation_state()
                module_logger.info(
                    "One or more of the resource recommendations are missing.\n"
                    'The model profiling operation with name "{}", for model package "{}", is '
                    'in "{}" state.'.format(self.name, self.image_id, operation_state)
                )
                if self.error_logs:
                    module_logger.info("Error logs: {}".format(self.error_logs))
                else:
                    module_logger.info(
                        "If the profiling run is not in a terminal state, use the "
                        "wait_for_profiling(True) method to wait for the model to finish profiling."
                    )

            return {
                PROFILE_RECOMMENDED_CPU_KEY: self.recommended_cpu,
                PROFILE_RECOMMENDED_MEMORY_KEY: self.recommended_memory,
            }
        return self.get_details()

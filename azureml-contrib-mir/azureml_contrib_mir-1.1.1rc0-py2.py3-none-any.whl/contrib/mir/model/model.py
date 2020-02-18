# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Module for Model Profiling in Azure Machine Learning."""

import logging
import json
import copy

from azureml.data.tabular_dataset import TabularDataset
from azureml.dataprep import FieldType
from azureml.exceptions import WebserviceException, UserErrorException
from azureml.core.webservice.webservice import ContainerResourceRequirements
from azureml.core.model import Model, InferenceConfig
from azureml._model_management._util import get_mms_operation, submit_mms_operation
from ._util import old_profile_payload_template, profile_payload_template
from .profile import ModelProfile

module_logger = logging.getLogger(__name__)


def _build_profile_payload(
    self,
    profile_name,
    input_data=None,
    workspace=None,
    models=None,
    dataset_id=None,
    container_resource_requirements=None,
    description=None,
    single_instance_profiling=False,
):
    """Build the profiling payload for the Model package.

    :param profile_name: The name of the profiling run.
    :type profile_name: str
    :param input_data: The input data for profiling.
    :type input_data: str
    :param workspace: A Workspace object in which to profile the model.
    :type workspace: azureml.core.Workspace
    :param models: A list of model objects. Can be an empty list.
    :type models: builtin.list[azureml.core.Model]
    :param dataset_id: Id associated with the dataset containing input data for the profiling run.
    :type dataset_id: str
    :param container_resource_requirements: container resource requirements for the largest instance to which the
                                            model is to be deployed
    :type container_resource_requirements:  azureml.core.webservice.webservice.ContainerResourceRequirements
    :param single_instance_profiling: Flag. If set to True profiling will be run on a single instance, otherwise
                                      profiling will run on
                                      on a grid of supported resource configurations.
    :type single_instance_profiling: bool
    :param description: Description to be associated with the profiling run.
    :type description: str
    :return: Model profile payload
    :rtype: dict
    :raises: azureml.exceptions.WebserviceException
    """
    # TODO: single_instance_profiling should be used in the payload when new profiling
    # controller supports full profiling
    # old workflow
    if input_data:
        json_payload = copy.deepcopy(old_profile_payload_template)
        json_payload["name"] = profile_name
        json_payload["description"] = description
        json_payload["inputData"] = input_data
        return json_payload

    json_payload = copy.deepcopy(profile_payload_template)

    if container_resource_requirements.cpu:
        json_payload["containerResourceRequirements"][
            "cpu"
        ] = container_resource_requirements.cpu
    else:
        del json_payload["containerResourceRequirements"]["cpu"]

    if container_resource_requirements.memory_in_gb:
        json_payload["containerResourceRequirements"][
            "memoryInGB"
        ] = container_resource_requirements.memory_in_gb
    else:
        del json_payload["containerResourceRequirements"]["memoryInGB"]

    if len(json_payload["containerResourceRequirements"]) < 1:
        del json_payload["containerResourceRequirements"]

    environment_image_request = self._build_environment_image_request(
        workspace, [model.id for model in models]
    )
    json_payload["environmentImageRequest"] = environment_image_request

    json_payload["name"] = profile_name
    json_payload["description"] = description
    json_payload["inputDatasetId"] = dataset_id

    return json_payload


InferenceConfig._build_profile_payload = _build_profile_payload


@staticmethod
def profile(
    workspace,
    profile_name,
    models,
    inference_config,
    input_data,
    cpu=None,
    memory_in_gb=None,
    description=None,
    single_instance_profiling=False,
):
    """Profiles the model to get resource requirement recommendations.

    :param workspace: A Workspace object in which to profile the model.
    :type workspace: azureml.core.Workspace
    :param profile_name: The name of the profiling run.
    :type profile_name: str
    :param models: A list of model objects. Can be an empty list.
    :type models: builtin.list[azureml.core.Model]
    :param inference_config: An InferenceConfig object used to determine required model properties.
    :type inference_config: azureml.core.model.InferenceConfig
    :param input_data: The input data for profiling.
    :type input_data: str or azureml.core.dataset.Dataset
    :param cpu: The number of cpu cores to use on the largest test instance. Currently support values up to 3.5.
    :type cpu: float
    :param memory_in_gb: The amount of memory (in GB) to use on the largest test instance. Can be a decimal.
                         Currently support values up to 4.0.
    :type memory_in_gb: float
    :param description: Description to be associated with the profiling run.
    :type description: str
    :param single_instance_profiling: Flag. If set to True profiling will be run on a single instance, otherwise
                                      profiling will run on a grid of supported resource configurations.
    :type single_instance_profiling: bool
    :rtype: azureml.contrib.profile.model.ModelProfile
    :raises: azureml.exceptions.WebserviceException, azureml.exceptions.UserErrorException
    """
    if isinstance(input_data, str):
        # TODO: old workflow, everything in this else branch is to be to be deprecated
        if single_instance_profiling:
            raise UserErrorException(
                "Single instance profiling is not supported with a single input sample. "
                "please provide a dataset or set single_instance_profiling=False"
            )
        from azureml.core.image import Image

        image = Image.create(workspace, profile_name, models, inference_config)
        image.wait_for_creation(True)
        if image.creation_state != "Succeeded":
            raise WebserviceException(
                "Error occurred creating model package {} for profiling. More information can "
                "be found here: {}, generated DockerFile can be found here: {}".format(
                    image.id, image.image_build_log_uri, image.generated_dockerfile_uri
                ),
                logger=module_logger,
            )
        profile_url_suffix = "/images/{0}/profiles".format(image.id)
        json_payload = inference_config._build_profile_payload(
            profile_name, input_data=input_data
        )
    else:
        # new workflow
        if not single_instance_profiling:
            raise UserErrorException(
                "Temporarily datasets are supported only for profiling on a single instance. "
                "Please set single_instance_profiling=True"
            )
        if profile_name is None or profile_name == "":
            raise UserErrorException("profile_name cannot be None or empty.")
        if cpu is not None and (cpu < 0.1 or cpu > 3.5):
            raise UserErrorException(
                "Expected cpu value is between 0.1 and 3.5. Provided: %s" % cpu
            )
        if memory_in_gb is not None and (memory_in_gb < 0.1 or memory_in_gb > 4.0):
            raise UserErrorException(
                "Expected memory value is between 0.1 and 4.0. Provided: %s" % memory_in_gb
            )

        # validate the dataset
        if not isinstance(input_data, TabularDataset):
            raise UserErrorException(
                "Dataset type not supported. Profiling currently works only with Tabular Datasets. Provided: %s"
                % type(input_data)
            )
        input_data._ensure_saved(workspace)
        ds_profile = input_data._dataflow.get_profile()
        column_list = list(ds_profile.columns.keys())
        if len(column_list) != 1:
            raise UserErrorException(
                "Dataset format not supported. Number of columns != 1. Dataset profile %s"
                % ds_profile
            )
        if ds_profile.dtypes[column_list[0]] != FieldType.STRING:
            raise UserErrorException(
                "Dataset format not supported. Dataset contains datatype other than string. Dataset profile %s"
                % ds_profile
            )
        if ds_profile.row_count < 1:
            raise UserErrorException("Empty Dataset. Dataset profile %s" % ds_profile)

        container_resource_requirements = ContainerResourceRequirements(
            cpu, memory_in_gb
        )
        profile_url_suffix = ModelProfile._general_mms_suffix
        json_payload = inference_config._build_profile_payload(
            profile_name,
            workspace=workspace,
            models=models,
            dataset_id=input_data.id,
            container_resource_requirements=container_resource_requirements,
            description=description,
        )
    module_logger.info("Profiling model")
    profile_operation_id = submit_mms_operation(
        workspace, "POST", profile_url_suffix, json_payload
    )

    if not isinstance(input_data, str):
        # new workflow
        profile = ModelProfile(workspace, image_id=None, name=profile_name)
    elif profile_name:
        # TODO: deprecate old workflow
        profile = ModelProfile(workspace, image.id, profile_name)
    else:
        # TODO: deprecate old workflow
        operation_resp = get_mms_operation(workspace, profile_operation_id)
        content = operation_resp["content"]
        if isinstance(content, bytes):
            content = content.decode("utf-8")
        operation_content = json.loads(content)
        if "resourceLocation" in operation_content:
            profile_name = operation_content["resourceLocation"].split("/")[-1]
        else:
            raise WebserviceException(
                "Invalid operation payload, missing resourceLocation:\n"
                "{}".format(operation_content),
                logger=module_logger,
            )
        profile = ModelProfile(workspace, image.id, profile_name)
    profile.create_operation_id = profile_operation_id
    return profile


Model.profile = profile

# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Module for managing the Azure MIR Webservices in Azure Machine Learning."""

import logging
from azureml.core.webservice import Webservice
from azureml.exceptions import WebserviceException
import copy
from ._util import mir_service_payload_template
from azureml._restclient.clientbase import ClientBase
from azureml._model_management._constants import MIR_WEBSERVICE_TYPE, MIR_SINGLE_MODEL_WEBSERVICE_TYPE
from azureml.core.webservice.webservice import WebserviceDeploymentConfiguration, ContainerResourceRequirements
from azureml.core.webservice.webservice import LivenessProbeRequirements, AutoScaler, DataCollection

module_logger = logging.getLogger(__name__)


class MirWebservice(Webservice):
    """Class for MIR Webservices."""

    _expected_payload_keys = Webservice._expected_payload_keys + ['autoScaler', 'authEnabled',
                                                                  'computeName',
                                                                  'containerResourceRequirements',
                                                                  'dataCollection',
                                                                  'maxConcurrentRequestsPerContainer',
                                                                  'numReplicas', 'scoringTimeoutMs',
                                                                  'scoringUri',
                                                                  'livenessProbeRequirements']
    _webservice_type = MIR_WEBSERVICE_TYPE

    def _initialize(self, workspace, obj_dict, **kwargs):
        """Initialize the Webservice instance.

        :param workspace:
        :type workspace: azureml.core.workspace.Workspace
        :param obj_dict:
        :type obj_dict: dict
        :return:
        :rtype: None
        """
        # Validate obj_dict with _expected_payload_keys
        if ("validate_payload" not in kwargs or kwargs["validate_payload"]):
            MirWebservice._validate_get_payload(obj_dict)

        # Initialize common Webservice attributes
        super(MirWebservice, self)._initialize(workspace, obj_dict)

        # Initialize expected MIR specific attributes
        self.autoscaler = AutoScaler.deserialize(obj_dict['autoScaler'])
        self.compute_name = obj_dict.get('computeName')
        self.container_resource_requirements = \
            ContainerResourceRequirements.deserialize(obj_dict.get('containerResourceRequirements'))
        self.liveness_probe_requirements = \
            LivenessProbeRequirements.deserialize(obj_dict.get('livenessProbeRequirements'))
        self.data_collection = DataCollection.deserialize(obj_dict.get('dataCollection'))
        self.max_concurrent_requests_per_container = obj_dict.get('maxConcurrentRequestsPerContainer')
        self.num_replicas = obj_dict.get('numReplicas')
        self.scoring_timeout_ms = obj_dict.get('scoringTimeoutMs')
        self.scoring_uri = obj_dict.get('scoringUri')
        self.deployment_status = obj_dict.get('deploymentStatus')
        self.tls_mode = obj_dict.get('tlsMode')
        self.certificate_fingerprints = obj_dict.get('certificateFingerprints')

    def __repr__(self):
        """Return the string representation of the MirWebservice object.

        :return: String representation of the MirWebservice object
        :rtype: str
        """
        return super().__repr__()

    @staticmethod
    def deploy_configuration(autoscale_enabled=None, autoscale_min_replicas=None, autoscale_max_replicas=None,
                             autoscale_refresh_seconds=None, autoscale_target_utilization=None,
                             collect_model_data=None, auth_enabled=None, cpu_cores=None, memory_gb=None,
                             scoring_timeout_ms=None, replica_max_concurrent_requests=None,
                             max_request_wait_time=None, num_replicas=None, tags=None, properties=None,
                             description=None, tls_mode=None, certificate_fingerprints=None, sku=None):
        """Create a configuration object for deploying to an MIR compute target.

        :param autoscale_enabled: Whether or not to enable autoscaling for this Webservice.
            Defaults to True if num_replicas is None
        :type autoscale_enabled: bool
        :param autoscale_min_replicas: The minimum number of containers to use when autoscaling this Webservice.
            Defaults to 1
        :type autoscale_min_replicas: int
        :param autoscale_max_replicas: The maximum number of containers to use when autoscaling this Webservice.
            Defaults to 10
        :type autoscale_max_replicas: int
        :param autoscale_refresh_seconds: How often the autoscaler should attempt to scale this Webservice.
            Defaults to 1
        :type autoscale_refresh_seconds: int
        :param autoscale_target_utilization: The target utilization (in percent out of 100) the autoscaler should
            attempt to maintain for this Webservice. Defaults to 70
        :type autoscale_target_utilization: int
        :param collect_model_data: Whether or not to enable model data collection for this Webservice.
            Defaults to False
        :type collect_model_data: bool
        :param auth_enabled: Whether or not to enable key auth for this Webservice. Defaults to False. MIR does not
            currently support authorization.
        :type auth_enabled: bool
        :param cpu_cores: The number of cpu cores to allocate for this Webservice. Can be a decimal. Defaults to 0.1
        :type cpu_cores: float
        :param memory_gb: The amount of memory (in GB) to allocate for this Webservice. Can be a decimal.
            Defaults to 0.5
        :type memory_gb: float
        :param scoring_timeout_ms: A timeout to enforce for scoring calls to this Webservice. Defaults to 60000
        :type scoring_timeout_ms: int
        :param replica_max_concurrent_requests: The number of maximum concurrent requests per node to allow for this
            Webservice. Defaults to 1
        :type replica_max_concurrent_requests: int
        :param num_replicas: The number of containers to allocate for this Webservice. No default, if this parameter
            is not set then the autoscaler is enabled by default.
        :type num_replicas: int
        :param tags: Dictionary of key value tags to give this Webservice
        :type tags: dict[str, str]
        :param properties: Dictionary of key value properties to give this Webservice. These properties cannot
            be changed after deployment, however new key value pairs can be added
        :type properties: dict[str, str]
        :param description: A description to give this Webservice
        :type description: str
        :param tls_mode: TLS mode for scoring authentication, options are "DISABLED", "SIMPLE", "MUTUAL"
        :type tls_mode: str
        :param certificate_fingerprints: List of fingerprints for scoring authentication
        :type certificate_fingerprints: :class:`list[str]`
        :param sku: Azure SKU type for MIR compute
        :type sku: str
        :return: A configuration object to use when deploying a Webservice objectrs.
            The first and last characters cannot be hyphens.
        :rtype: MirServiceDeploymentConfiguration
        :raises: azureml.exceptions.WebserviceException
        """
        config = MirServiceDeploymentConfiguration(autoscale_enabled, autoscale_min_replicas, autoscale_max_replicas,
                                                   autoscale_refresh_seconds, autoscale_target_utilization,
                                                   collect_model_data, auth_enabled, cpu_cores, memory_gb,
                                                   scoring_timeout_ms, replica_max_concurrent_requests,
                                                   max_request_wait_time, num_replicas, tags, properties,
                                                   description, tls_mode, certificate_fingerprints, sku)
        return config

    def _deploy(self, workspace, name, image, deployment_config, deployment_target, overwrite=False):
        """Deploy the Webservice.

        :raises: azureml.exceptions.WebserviceException
        """
        raise NotImplementedError("MIR Webservices does not support deployments without environment.")

    def run(self, input_data):
        """Call this Webservice with the provided input.

        :param input_data: The input to call the Webservice with
        :type input_data: varies
        :return: The result of calling the Webservice
        :rtype: dict
        :raises: azureml.exceptions.WebserviceException
        """
        if not self.scoring_uri:
            raise WebserviceException('Error attempting to call webservice, scoring_uri unavailable. '
                                      'This could be due to a failed deployment, or the service is not ready yet.\n'
                                      'Current State: {}\n'
                                      'Errors: {}'.format(self.state, self.error), logger=module_logger)

        resp = ClientBase._execute_func(self._webservice_session.post, self.scoring_uri, data=input_data)

        if resp.status_code == 401:
            if self.auth_enabled:
                raise WebserviceException("Auth not enabled in MIR")

        if resp.status_code == 200:
            return resp.json()
        else:
            raise WebserviceException('Received bad response from service:\n'
                                      'Response Code: {}\n'
                                      'Headers: {}\n'
                                      'Content: {}'.format(resp.status_code, resp.headers, resp.content),
                                      logger=module_logger)

    def update(self, *args):
        """
        MIR webservice does not implement this feature yet, calling this function always gets a NotImplementedError
        """
        raise NotImplementedError('Class does not implement update method yet.')

    def serialize(self):
        """Convert this Webservice into a json serialized dictionary.

        :return: The json representation of this Webservice
        :rtype: dict
        """
        properties = super(MirWebservice, self).serialize()
        autoscaler = self.autoscaler.serialize() if self.autoscaler else None
        container_resource_requirements = self.container_resource_requirements.serialize() \
            if self.container_resource_requirements else None
        data_collection = self.data_collection.serialize() if self.data_collection else None
        image = self.image.serialize() if self.image else None
        mir_properties = {'autoScaler': autoscaler, 'computeName': self.compute_name,
                          'authEnabled': self.auth_enabled,
                          'containerResourceRequirements': container_resource_requirements,
                          'dataCollection': data_collection, 'imageId': self.image_id,
                          'imageDetails': image,
                          'maxConcurrentRequestsPerContainer': self.max_concurrent_requests_per_container,
                          'numReplicas': self.num_replicas, 'deploymentStatus': self.deployment_status,
                          'scoringTimeoutMs': self.scoring_timeout_ms, 'scoringUri': self.scoring_uri,
                          'tlsMode': self.tls_mode, 'certificateFingerprints': self.certificate_fingerprints}
        properties.update(mir_properties)
        return properties

    def get_token(self):
        """Retrieve token for this webservice.
        """
        raise NotImplementedError('MIR does not support token authentication yet.')


class SingleModelMirWebservice(MirWebservice):
    """Class for Single Model MIR Webservices."""

    _webservice_type = MIR_SINGLE_MODEL_WEBSERVICE_TYPE

    def _initialize(self, workspace, obj_dict):
        """Initialize the Webservice instance.

        :param workspace:
        :type workspace: azureml.core.workspace.Workspace
        :param obj_dict:
        :type obj_dict: dict
        :return:
        :rtype: None
        """
        # Validate obj_dict with _expected_payload_keys
        SingleModelMirWebservice._validate_get_payload(obj_dict)

        # Initialize common Webservice attributes
        super(SingleModelMirWebservice, self)._initialize(workspace, obj_dict, validate_payload=False)


class MirServiceDeploymentConfiguration(WebserviceDeploymentConfiguration):
    """Service deployment configuration object for services deployed on MIR compute.

    :param autoscale_enabled: Whether or not to enable autoscaling for this Webservice.
        Defaults to True if num_replicas is None
    :type autoscale_enabled: bool
    :param autoscale_min_replicas: The minimum number of containers to use when autoscaling this Webservice.
        Defaults to 1
    :type autoscale_min_replicas: int
    :param autoscale_max_replicas: The maximum number of containers to use when autoscaling this Webservice.
        Defaults to 10
    :type autoscale_max_replicas: int
    :param autoscale_refresh_seconds: How often the autoscaler should attempt to scale this Webservice.
        Defaults to 1
    :type autoscale_refresh_seconds: int
    :param autoscale_target_utilization: The target utilization (in percent out of 100) the autoscaler should
        attempt to maintain for this Webservice. Defaults to 70
    :type autoscale_target_utilization: int
    :param collect_model_data: Whether or not to enable model data collection for this Webservice.
        Defaults to False
    :type collect_model_data: bool
    :param auth_enabled: Whether or not to enable auth for this Webservice. Defaults to False. MIR does not currently
        support authorization.
    :type auth_enabled: bool
    :param cpu_cores: The number of cpu cores to allocate for this Webservice. Can be a decimal. Defaults to 0.1
    :type cpu_cores: float
    :param memory_gb: The amount of memory (in GB) to allocate for this Webservice. Can be a decimal.
        Defaults to 0.5
    :type memory_gb: float
    :param scoring_timeout_ms: A timeout to enforce for scoring calls to this Webservice. Defaults to 60000
    :type scoring_timeout_ms: int
    :param replica_max_concurrent_requests: The number of maximum concurrent requests per node to allow for this
        Webservice. Defaults to 1
    :type replica_max_concurrent_requests: int
    :param num_replicas: The number of containers to allocate for this Webservice. No default, if this parameter
        is not set then the autoscaler is enabled by default.
    :type num_replicas: int
    :param tags: Dictionary of key value tags to give this Webservice
    :type tags: dict[str, str]
    :param properties: Dictionary of key value properties to give this Webservice. These properties cannot
        be changed after deployment, however new key value pairs can be added
    :type properties: dict[str, str]
    :param description: A description to give this Webservice
    :type description: str
    :param tls_mode: TLS mode for scoring authentication, options are "DISABLED", "SIMPLE", "MUTUAL"
    :type tls_mode: str
    :param certificate_fingerprints: List of fingerprints for scoring authentication
    :type certificate_fingerprints: :class:`list[str]`
    :param sku: Azure SKU type for MIR compute
    :type sku: str
    :return: A configuration object to use when deploying a Webservice object.
    """

    def __init__(self, autoscale_enabled=None, autoscale_min_replicas=None, autoscale_max_replicas=None,
                 autoscale_refresh_seconds=None, autoscale_target_utilization=None, collect_model_data=None,
                 auth_enabled=None, cpu_cores=None, memory_gb=None, scoring_timeout_ms=None,
                 replica_max_concurrent_requests=None, max_request_wait_time=None, num_replicas=None, tags=None,
                 properties=None, description=None, tls_mode=None, certificate_fingerprints=None, sku=None):
        """Initialize a configuration object for deploying to an MIR compute target.

        :param autoscale_enabled: Whether or not to enable autoscaling for this Webservice.
            Defaults to True if num_replicas is None
        :type autoscale_enabled: bool
        :param autoscale_min_replicas: The minimum number of containers to use when autoscaling this Webservice.
            Defaults to 1
        :type autoscale_min_replicas: int
        :param autoscale_max_replicas: The maximum number of containers to use when autoscaling this Webservice.
            Defaults to 10
        :type autoscale_max_replicas: int
        :param autoscale_refresh_seconds: How often the autoscaler should attempt to scale this Webservice.
            Defaults to 1
        :type autoscale_refresh_seconds: int
        :param autoscale_target_utilization: The target utilization (in percent out of 100) the autoscaler should
            attempt to maintain for this Webservice. Defaults to 70
        :type autoscale_target_utilization: int
        :param collect_model_data: Whether or not to enable model data collection for this Webservice.
            Defaults to False
        :type collect_model_data: bool
        :param auth_enabled: Whether or not to enable auth for this Webservice. Defaults to False. MIR does not
            currently support authorization.
        :type auth_enabled: bool
        :param cpu_cores: The number of cpu cores to allocate for this Webservice. Can be a decimal. Defaults to 0.1
        :type cpu_cores: float
        :param memory_gb: The amount of memory (in GB) to allocate for this Webservice. Can be a decimal.
            Defaults to 0.5
        :type memory_gb: float
        :param scoring_timeout_ms: A timeout to enforce for scoring calls to this Webservice. Defaults to 60000
        :type scoring_timeout_ms: int
        :param replica_max_concurrent_requests: The number of maximum concurrent requests per node to allow for this
            Webservice. Defaults to 1
        :type replica_max_concurrent_requests: int
        :param num_replicas: The number of containers to allocate for this Webservice. No default, if this parameter
            is not set then the autoscaler is enabled by default.
        :type num_replicas: int
        :param tags: Dictionary of key value tags to give this Webservice
        :type tags: dict[str, str]
        :param properties: Dictionary of key value properties to give this Webservice. These properties cannot
            be changed after deployment, however new key value pairs can be added
        :type properties: dict[str, str]
        :param description: A description to give this Webservice
        :type description: str
        :param tls_mode: TLS mode for scoring authentication, options are "DISABLED", "SIMPLE", "MUTUAL"
        :type tls_mode: str
        :param certificate_fingerprints: List of fingerprints for scoring authentication
        :type certificate_fingerprints: :class:`list[str]`
        :param sku: Azure SKU type for MIR compute
        :type sku: str
        :return: A configuration object to use when deploying a Webservice object.
        :raises: azureml.exceptions.WebserviceException
        """
        super(MirServiceDeploymentConfiguration, self).__init__(MirWebservice)
        self.autoscale_enabled = autoscale_enabled
        self.autoscale_min_replicas = autoscale_min_replicas
        self.autoscale_max_replicas = autoscale_max_replicas
        self.autoscale_refresh_seconds = autoscale_refresh_seconds
        self.autoscale_target_utilization = autoscale_target_utilization
        self.collect_model_data = collect_model_data
        self.auth_enabled = auth_enabled
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
        self.scoring_timeout_ms = scoring_timeout_ms
        self.replica_max_concurrent_requests = replica_max_concurrent_requests
        self.max_request_wait_time = max_request_wait_time
        self.num_replicas = num_replicas
        self.tags = tags
        self.properties = properties
        self.description = description
        self.tls_mode = tls_mode
        self.certificate_fingerprints = certificate_fingerprints
        self.sku = sku
        self.validate_configuration()

    def validate_configuration(self):
        """Check that the specified configuration values are valid.

        Will raise a WebserviceException if validation fails.

        :raises: azureml.exceptions.WebserviceException
        """
        valid_skus = ["A2V2", "F16", "DS2V2"]
        error = ""
        if self.cpu_cores and self.cpu_cores <= 0:
            error += 'Invalid configuration, cpu_cores must be greater than zero.\n'
        if self.memory_gb and self.memory_gb <= 0:
            error += 'Invalid configuration, memory_gb must be greater than zero.\n'
        if self.scoring_timeout_ms and self.scoring_timeout_ms <= 0:
            error += 'Invalid configuration, scoring_timeout_ms must be greater than zero.\n'
        if self.replica_max_concurrent_requests and self.replica_max_concurrent_requests <= 0:
            error += 'Invalid configuration, replica_max_concurrent_requests must be greater than zero.\n'
        if self.num_replicas and self.num_replicas <= 0:
            error += 'Invalid configuration, num_replicas must be greater than zero.\n'
        if self.certificate_fingerprints and (not self.tls_mode or self.tls_mode.upper() != "MUTUAL"):
            error += 'Invalid configuration, if certificate fingerprints are provided the tls mode should be ' \
                     'MUTUAL.\n'
        if self.certificate_fingerprints and not all(isinstance(item, str) for item in self.certificate_fingerprints):
            error += 'Invalid configuration, certificate_fingerprints must be a list of strings.\n'

        if self.sku and self.sku.upper() not in valid_skus:
            error += 'Invalid SKU provided, valid SKUS are ' + ', '.join(valid_skus)

        if error:
            raise WebserviceException(error, logger=module_logger)

    def _build_create_payload(self, name, environment_image_request, overwrite=False):
        json_payload = copy.deepcopy(mir_service_payload_template)
        base_payload = super(MirServiceDeploymentConfiguration,
                             self)._build_base_create_payload(name, environment_image_request)

        json_payload['numReplicas'] = self.num_replicas
        if self.collect_model_data:
            json_payload['dataCollection']['storageEnabled'] = self.collect_model_data
        else:
            del(json_payload['dataCollection'])
        if self.autoscale_enabled is not None:
            json_payload['autoScaler']['autoscaleEnabled'] = self.autoscale_enabled
            json_payload['autoScaler']['minReplicas'] = self.autoscale_min_replicas
            json_payload['autoScaler']['maxReplicas'] = self.autoscale_max_replicas
            json_payload['autoScaler']['targetUtilization'] = self.autoscale_target_utilization
            json_payload['autoScaler']['refreshPeriodInSeconds'] = self.autoscale_refresh_seconds
        else:
            del(json_payload['autoScaler'])
        if self.auth_enabled is not None:
            json_payload['authEnabled'] = self.auth_enabled
        else:
            del(json_payload['authEnabled'])
        json_payload['containerResourceRequirements']['cpu'] = self.cpu_cores
        json_payload['containerResourceRequirements']['memoryInGB'] = self.memory_gb
        json_payload['maxConcurrentRequestsPerContainer'] = self.replica_max_concurrent_requests
        json_payload['maxQueueWaitMs'] = self.max_request_wait_time
        json_payload['scoringTimeoutMs'] = self.scoring_timeout_ms
        json_payload['tlsMode'] = self.tls_mode
        json_payload['certificateFingerprints'] = self.certificate_fingerprints
        json_payload['sku'] = self.sku.upper()

        if overwrite:
            json_payload['overwrite'] = overwrite
        else:
            del (json_payload['overwrite'])

        json_payload.update(base_payload)

        return json_payload

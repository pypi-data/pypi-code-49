# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Manages Azure Kubernetes Service compute targets in Azure Machine Learning."""

import copy
from azureml._compute._constants import MLC_COMPUTE_RESOURCE_ID_FMT
from ._util import mir_payload_template
from azureml.core.compute import ComputeTarget
from azureml.core.compute.compute import ComputeTargetProvisioningConfiguration
from azureml.exceptions import ComputeTargetException


class MirCompute(ComputeTarget):
    """Manages MIR compute target objects."""

    _compute_type = 'Mir'

    def _initialize(self, workspace, obj_dict):
        """Class MirCompute constructor.

        :param workspace:
        :type workspace: azureml.core.Workspace
        :param obj_dict:
        :type obj_dict: dict
        :return:
        :rtype: None
        """
        name = obj_dict['name']
        compute_resource_id = MLC_COMPUTE_RESOURCE_ID_FMT.format(workspace.subscription_id,
                                                                 workspace.resource_group, workspace.name,
                                                                 name)
        resource_manager_endpoint = self._get_resource_manager_endpoint(workspace)
        mlc_endpoint = '{}{}'.format(resource_manager_endpoint, compute_resource_id)
        location = obj_dict['location']
        compute_type = obj_dict['properties']['computeType']
        tags = obj_dict['tags']
        description = obj_dict['properties']['description']
        created_on = obj_dict['properties'].get('createdOn')
        modified_on = obj_dict['properties'].get('modifiedOn')
        provisioning_state = obj_dict['properties']['provisioningState']
        provisioning_errors = obj_dict['properties']['provisioningErrors']
        is_attached = obj_dict['properties']['isAttachedCompute']
        mir_properties = obj_dict['properties']['properties']
        display_name = mir_properties['displayName'] if mir_properties else None
        super(MirCompute, self)._initialize(compute_resource_id, name, location, compute_type, tags, description,
                                            created_on, modified_on, provisioning_state, provisioning_errors,
                                            None, location, workspace, mlc_endpoint, None,
                                            workspace._auth, is_attached)
        self.display_name = display_name

    def __repr__(self):
        """Return the string representation of the MirCompute object.

        :return: String representation of the MirCompute object
        :rtype: str
        """
        return super().__repr__()

    @staticmethod
    def _create(workspace, name, provisioning_configuration):
        """Create compute.

        :param workspace:
        :type workspace: azureml.core.Workspace
        :param name:
        :type name: str
        :param provisioning_configuration:
        :type provisioning_configuration: MirProvisioningConfiguration
        :return:
        :rtype: azureml.contrib.compute.mircompute.MirCompute
        """
        compute_create_payload = MirCompute._build_create_payload(provisioning_configuration,
                                                                  provisioning_configuration.location,
                                                                  workspace.subscription_id)
        # return compute_create_payload
        return ComputeTarget._create_compute_target(workspace, name, compute_create_payload, MirCompute)

    @staticmethod
    def _build_resource_id(subscription_id, resource_group, cluster_name):
        """Build the Azure resource ID for the compute resource.

        :param subscription_id: The Azure subscription ID
        :type subscription_id: str
        :param resource_group: Name of the resource group in which the MIR is located.
        :type resource_group: str
        :param cluster_name: The MIR cluster name
        :type cluster_name: str
        :return: The Azure resource ID for the compute resource
        :rtype: str
        """
        MIR_RESOURCE_ID_FMT = ('/subscriptions/{}/resourcegroups/{}/providers/Microsoft.ContainerService/'
                               'managedClusters/{}')
        return MIR_RESOURCE_ID_FMT.format(subscription_id, resource_group, cluster_name)

    @staticmethod
    def provisioning_configuration(location=None, display_name=None):
        """Create a configuration object for provisioning an MIR compute target.

        :param location: Location to provision cluster in. If not specified, will default to workspace location.
            Available regions for this compute can be found here:
            https://azure.microsoft.com/en-us/global-infrastructure/services/?regions=all&products=kubernetes-service
        :type location: str
        :param display_name: User friendly display name of Mir
        :type agent_count: str
        :return: A configuration object to be used when creating a Compute object
        :rtype: MirProvisioningConfiguration
        :raises: azureml.exceptions.ComputeTargetException
        """
        config = MirProvisioningConfiguration(location, display_name)
        return config

    @staticmethod
    def _build_create_payload(config, location, subscription_id):
        """Construct the payload needed to create an MIR compute.

        :param config:
        :type config: MirProvisioningConfiguration
        :param location:
        :type location:
        :param subscription_id:
        :type subscription_id:
        :return:
        :rtype: dict
        """
        json_payload = copy.deepcopy(mir_payload_template)
        json_payload['location'] = location
        if not config.display_name:
            del(json_payload['properties']['properties'])
        else:
            json_payload['properties']['properties']['displayName'] = config.display_name
        return json_payload

    def refresh_state(self):
        """Perform an in-place update of the properties of the object.

        Based on the current state of the corresponding cloud object.
        Primarily useful for manual polling of compute state.
        """
        cluster = MirCompute(self.workspace, self.name)
        self.modified_on = cluster.modified_on
        self.provisioning_state = cluster.provisioning_state
        self.provisioning_errors = cluster.provisioning_errors
        self.cluster_resource_id = cluster.cluster_resource_id

    @staticmethod
    def _validate_get_payload(payload):
        """Validate get payload.

        :param payload:
        :type payload: dict
        :return:
        :rtype: None
        """
        if 'properties' not in payload or 'computeType' not in payload['properties']:
            raise ComputeTargetException('Invalid cluster payload:\n'
                                         '{}'.format(payload))
        if payload['properties']['computeType'] != MirCompute._compute_type:
            raise ComputeTargetException('Invalid cluster payload, not "{}":\n'
                                         '{}'.format(MirCompute._compute_type, payload))

    def delete(self):
        """Remove the MirCompute object from its associated workspace.

        If this object was created through Azure ML, the corresponding cloud based objects will also be deleted.
        If this object was created externally and only attached to the workspace, it will raise exception and nothing
        will be changed.

        :raises: azureml.exceptions.ComputeTargetException
        """
        self._delete_or_detach('delete')

    @staticmethod
    def deserialize(workspace, object_dict):
        """Convert a json object into a MirCompute object.

        Will fail if the provided workspace is not the workspace the Compute is associated with.

        :param workspace: The workspace object the MirCompute object is associated with
        :type workspace: azureml.core.Workspace
        :param object_dict: A json object to convert to a MirCompute object
        :type object_dict: dict
        :return: The MirCompute representation of the provided json object
        :rtype: azureml.contrib.mir.compute.MirCompute
        :raises: azureml.exceptions.ComputeTargetException
        """
        MirCompute._validate_get_payload(object_dict)
        target = MirCompute(None, None)
        target._initialize(workspace, object_dict)
        return target

    def serialize(self):
        """Convert this MirCompute object into a json serialized dictionary.

        :return: The json representation of this MirCompute object
        :rtype: dict
        """

        cluster_properties = {'computeType': self.type, 'computeLocation': self.location,
                              'description': self.description, 'resourceId': self.cluster_resource_id,
                              'provisioningState': self.provisioning_state,
                              'provisioningErrors': self.provisioning_errors}

        return {'id': self.id, 'name': self.name, 'tags': self.tags, 'location': self.location,
                'properties': cluster_properties}

    def detach(self):
        """MIR does not support detaching a compute at this time.

        :raises: azureml.exceptions.ComputeTargetException
        """
        raise NotImplementedError("MIR compute type does not support detach.")

    def attach(self):
        """MIR does not support attach at this time.

        :raises: azureml.exceptions.ComputeTargetException
        """
        raise NotImplementedError("MIR compute type does not support attach.")


class MirProvisioningConfiguration(ComputeTargetProvisioningConfiguration):
    """Provisioning configuration object for MIR compute targets.

    This object is used to define the configuration parameters for provisioning MirCompute objects.

    :param location: Location to provision cluster in. If not specified, will default to workspace location.
        Available regions for this compute can be found here:
        https://azure.microsoft.com/en-us/global-infrastructure/services/?regions=all&products=kubernetes-service
    :type location: str
    :param display_name: User friendly display name of Mir
    :type display_name: str
    """

    def __init__(self, location, display_name):
        """Initialize a configuration object for provisioning an MIR compute target.

        :param location: Location to provision cluster in. If not specified, will default to workspace location.
            Available regions for this compute can be found here:
            https://azure.microsoft.com/en-us/global-infrastructure/services/?regions=all&products=kubernetes-service
        :type location: str
        :param display_name: User friendly display name of Mir
        :type display_name: str
        :return: A configuration object to be used when creating a Compute object
        :rtype: MirProvisioningConfiguration
        :raises: azureml.exceptions.ComputeTargetException
        """
        super(MirProvisioningConfiguration, self).__init__(MirCompute, location)
        self.display_name = display_name

    def validate_configuration(self):
        """Check that the specified configuration values are valid.
        """
        pass

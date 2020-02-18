# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Contains functionality for managing Azure Machine Learning compute instance targets in Azure Machine Learning."""

import copy
import json
import requests
import sys
import time

from azureml._compute._constants import MLC_COMPUTE_RESOURCE_ID_FMT
from azureml._compute._constants import MLC_WORKSPACE_API_VERSION
from azureml._compute._util import get_paginated_compute_supported_vms
from azureml._compute._util import get_requests_session
from azureml._compute._util import computeinstance_payload_template
from azureml.core.compute import ComputeTarget
from azureml.core.compute.compute import ComputeTargetProvisioningConfiguration
from azureml.exceptions import ComputeTargetException
from azureml._restclient.clientbase import ClientBase
from azureml._restclient.workspace_client import WorkspaceClient
from dateutil.parser import parse


class ComputeInstance(ComputeTarget):
    """Manages a Compute Instance target in Azure Machine Learning."""

    _compute_type = 'ComputeInstance'

    def _initialize(self, workspace, obj_dict):
        """Initialize ComputeInstance object.

        :param workspace: The workspace.
        :type workspace: azureml.core.Workspace
        :param obj_dict: Dictionary of ComputeInstance properties.
        :type obj_dict: dict
        :return: None
        :rtype: None
        """
        name = obj_dict['name']
        compute_resource_id = MLC_COMPUTE_RESOURCE_ID_FMT.format(workspace.subscription_id, workspace.resource_group,
                                                                 workspace.name, name)
        resource_manager_endpoint = self._get_resource_manager_endpoint(workspace)
        mlc_endpoint = '{}{}'.format(resource_manager_endpoint, compute_resource_id)
        location = obj_dict['location']
        compute_type = obj_dict['properties']['computeType']
        tags = obj_dict['tags']
        description = obj_dict['properties']['description']
        created_on = obj_dict['properties']['createdOn']
        modified_on = obj_dict['properties']['modifiedOn']
        resource_id = obj_dict['properties']['resourceId']
        location = obj_dict['properties']['computeLocation'] \
            if 'computeLocation' in obj_dict['properties'] else None
        provisioning_state = obj_dict['properties']['provisioningState']
        provisioning_errors = obj_dict['properties']['provisioningErrors']
        is_attached = obj_dict['properties']['isAttachedCompute']
        vm_size = obj_dict['properties']['properties']['vmSize'] \
            if obj_dict['properties']['properties'] else None
        ssh_settings = obj_dict['properties']['properties']['sshSettings'] \
            if obj_dict['properties']['properties'] and \
            'sshSettings' in obj_dict['properties']['properties'] else None
        admin_username = ssh_settings['adminUserName'] \
            if ssh_settings and 'adminUserName' in ssh_settings else None
        admin_user_ssh_key = ssh_settings['adminPublicKey'] \
            if ssh_settings and 'adminPublicKey' in ssh_settings else None
        ssh_public_access = (ssh_settings['sshPublicAccess'] == "Enabled") \
            if ssh_settings and 'sshPublicAccess' in ssh_settings else False
        ssh_port = ssh_settings['sshPort'] \
            if ssh_settings and 'sshPort' in ssh_settings else None
        public_ip_address = obj_dict['properties']['properties']['connectivityEndpoints']['publicIpAddress'] \
            if obj_dict['properties']['properties'] and \
            'connectivityEndpoints' in obj_dict['properties']['properties'] and \
            obj_dict['properties']['properties']['connectivityEndpoints'] and \
            'publicIpAddress' in obj_dict['properties']['properties']['connectivityEndpoints'] else None
        private_ip_address = obj_dict['properties']['properties']['connectivityEndpoints']['privateIpAddress'] \
            if obj_dict['properties']['properties'] and \
            'connectivityEndpoints' in obj_dict['properties']['properties'] and \
            obj_dict['properties']['properties']['connectivityEndpoints'] and \
            'privateIpAddress' in obj_dict['properties']['properties']['connectivityEndpoints'] else None
        applications = obj_dict['properties']['properties']['applications'] \
            if obj_dict['properties']['properties'] and \
            'applications' in obj_dict['properties']['properties'] else None
        errors = obj_dict['properties']['properties']['errors'] \
            if obj_dict['properties']['properties'] and \
            'errors' in obj_dict['properties']['properties'] else None
        vnet_resourcegroup_name = None
        vnet_name = None
        subnet_name = None
        subnet_id = obj_dict['properties']['properties']['subnet']['id'] \
            if obj_dict['properties']['properties'] and obj_dict['properties']['properties']['subnet'] else None
        if subnet_id:
            vnet_resourcegroup_name = subnet_id[subnet_id.index("/resourceGroups/") +
                                                len("/resourceGroups/"):subnet_id.index("/providers")]
            vnet_name = subnet_id[subnet_id.index("/virtualNetworks/") +
                                  len("/virtualNetworks/"):subnet_id.index("/subnets")]
            subnet_name = subnet_id[subnet_id.index("/subnets/") + len("/subnets/"):]
        status = ComputeInstanceStatus.deserialize(obj_dict['properties'])
        super(ComputeInstance, self)._initialize(compute_resource_id, name, location, compute_type, tags, description,
                                                 created_on, modified_on, provisioning_state, provisioning_errors,
                                                 resource_id, location, workspace, mlc_endpoint, None,
                                                 workspace._auth, is_attached)

        self.vm_size = vm_size
        self.ssh_public_access = ssh_public_access
        self.admin_username = admin_username
        self.admin_user_ssh_public_key = admin_user_ssh_key
        self.ssh_port = ssh_port
        self.vnet_resourcegroup_name = vnet_resourcegroup_name
        self.vnet_name = vnet_name
        self.subnet_name = subnet_name
        self.status = status
        self.public_ip_address = public_ip_address
        self.private_ip_address = private_ip_address
        self.applications = applications
        self.errors = errors

    def __repr__(self):
        """Return the string representation of the ComputeInstance object.

        :return: String representation of the ComputeInstance object
        :rtype: str
        """
        formatted_info = ',\n'.join(["{}: {}".format(k, v) for k, v in self.serialize().items()])
        return formatted_info

    @staticmethod
    def _create(workspace, name, provisioning_configuration):
        """Create implementation method.

        :param workspace: The workspace.
        :type workspace: azureml.core.Workspace
        :param name: Name of the ComputeInstance.
        :type name: str
        :param provisioning_configuration:
        :type provisioning_configuration: ComputeInstanceProvisioningConfiguration
        :return: The ComputeInstance.
        :rtype: azureml.core.compute.ComputeInstance.ComputeInstance
        """
        compute_create_payload = ComputeInstance._build_create_payload(
            provisioning_configuration,
            workspace.location,
            workspace.subscription_id)
        return ComputeTarget._create_compute_target(workspace, name, compute_create_payload, ComputeInstance)

    @staticmethod
    def provisioning_configuration(vm_size='', ssh_public_access=False, admin_user_ssh_public_key=None,
                                   vnet_resourcegroup_name=None, vnet_name=None, subnet_name=None,
                                   tags=None, description=None):
        """Create a configuration object for provisioning a ComputeInstance target.

        :param vm_size: Size of agent VMs. More details can be found here: https://aka.ms/azureml-vm-details.
            Note that not all sizes are available in all regions, as
            detailed in the previous link. Defaults to Standard_NC6
        :type vm_size: str
        :param ssh_public_access: State of the public SSH port. Possible values are:
            False - Indicates that the public ssh port is closed.
            True - Indicates that the public ssh port is open.
        :type ssh_public_access: bool
        :param admin_user_ssh_public_key: SSH public key of the administrator user account
        :type admin_user_ssh_public_key: str
        :param vnet_resourcegroup_name: Name of the resource group where the virtual network is located
        :type vnet_resourcegroup_name: str
        :param vnet_name: Name of the virtual network
        :type vnet_name: str
        :param subnet_name: Name of the subnet inside the vnet
        :type subnet_name: str
        :param tags: A dictionary of key value tags to provide to the compute object
        :type tags: dict[str, str]
        :param description: A description to provide to the compute object
        :type description: str
        :return: A configuration object to be used when creating a Compute object
        :rtype: ComputeInstanceProvisioningConfiguration
        :raises: azureml.exceptions.ComputeTargetException
        """
        config = ComputeInstanceProvisioningConfiguration(
            vm_size, ssh_public_access, admin_user_ssh_public_key, vnet_resourcegroup_name,
            vnet_name, subnet_name, tags, description)
        return config

    @staticmethod
    def _build_create_payload(config, location, subscription_id):
        """Construct the payload needed to create an ComputeInstance.

        :param config: ComputeInstance provisioning configuration.
        :type config: azureml.core.compute.ComputeInstanceProvisioningConfiguration
        :param location: Location of the compute.
        :type location: str
        :param subscription_id: The subscription ID.
        :type subscription_id: str
        :return: A Dictionary of ComputeInstance provisioning configuration properties.
        :rtype: dict
        """
        json_payload = copy.deepcopy(computeinstance_payload_template)
        del(json_payload['properties']['resourceId'])
        del(json_payload['properties']['computeLocation'])
        json_payload['location'] = location
        if not config.vm_size and not config.admin_user_ssh_public_key and not config.ssh_public_access and not \
                config.vnet_resourcegroup_name and not config.vnet_name and not config.subnet_name:
            del(json_payload['properties']['properties'])
        else:
            if not config.vm_size:
                del(json_payload['properties']['properties']['vmSize'])
            else:
                json_payload['properties']['properties']['vmSize'] = config.vm_size
            if not config.admin_user_ssh_public_key and not isinstance(config.ssh_public_access, bool):
                del(json_payload['properties']['properties']['sshSettings'])
            else:
                if not isinstance(config.ssh_public_access, bool):
                    del(json_payload['properties']['properties']['sshSettings']['sshPublicAccess'])
                else:
                    json_payload['properties']['properties']['sshSettings']['sshPublicAccess'] = \
                        ("Enabled" if config.ssh_public_access else "Disabled")
                if not config.admin_user_ssh_public_key:
                    del(json_payload['properties']['properties']['sshSettings']['adminPublicKey'])
                else:
                    json_payload['properties']['properties']['sshSettings']['adminPublicKey'] = \
                        config.admin_user_ssh_public_key
            if not config.vnet_name:
                del(json_payload['properties']['properties']['subnet'])
            else:
                json_payload['properties']['properties']['subnet'] = \
                    {"id": "/subscriptions/{0}/resourceGroups/{1}/providers/Microsoft.Network/virtualNetworks"
                     "/{2}/subnets/{3}".format(subscription_id, config.vnet_resourcegroup_name,
                                               config.vnet_name, config.subnet_name)}
        if config.tags:
            json_payload['tags'] = config.tags
        else:
            del(json_payload['tags'])
        if config.description:
            json_payload['properties']['description'] = config.description
        else:
            del(json_payload['properties']['description'])
        return json_payload

    def wait_for_completion(self, show_output=False):
        """Wait for the ComputeInstance to finish provisioning.

        :param show_output: Boolean to provide more verbose output. Defaults to False
        :type show_output: bool
        :raises: azureml.exceptions.ComputeTargetException
        """
        state = ''
        prev_state = ''

        while True:
            time.sleep(5)
            self.refresh_state()

            if self.status and self.status.state:
                state = self.status.state.capitalize()
            else:
                state = self.provisioning_state.capitalize()

            if show_output and state:
                if state != prev_state:
                    if prev_state is None:
                        sys.stdout.write('{}'.format(state))
                    else:
                        sys.stdout.write('\n{}'.format(state))
                elif state:
                    sys.stdout.write('.')
                sys.stdout.flush()

            terminal_state_reached = self._terminal_state_reached()
            status_errors_present = self._status_errors_present()

            if terminal_state_reached or status_errors_present:
                break

            prev_state = state

        if show_output:
            sys.stdout.write('\n')
            sys.stdout.flush()

        if terminal_state_reached:
            if self.status and self.status.state:
                state = self.status.state.capitalize()
            else:
                state = self.provisioning_state.capitalize()
            if show_output:
                if state == 'Failed' or state == 'CreateFailed':
                    print('Provisioning errors: {}'.format(self.provisioning_errors))
        elif status_errors_present:
            if self.status and self.status.errors:
                errors = self.status.errors
            else:
                errors = self.provisioning_errors
            if show_output:
                print('There were errors reported from ComputeInstance:\n{}'.format(errors))

    def _terminal_state_reached(self):
        """Terminal state reached.

        :return: Indicates whether the terminal state reached.
        :rtype: bool
        """
        if self.status and self.status.state:
            state = self.status.state.capitalize()
        else:
            state = self.provisioning_state.capitalize()
        if state == 'CreateFailed' or state == 'Canceled' or state == 'Running' or state == 'Ready':
            return True
        return False

    def _status_errors_present(self):
        """Return status error.

        :return: Indicates whether the errors present.
        :rtype: bool
        """
        if (self.status and self.status.errors) or self.provisioning_errors:
            return True
        return False

    def refresh_state(self):
        """Perform an in-place update of the properties of the object.

        Based on the current state of the corresponding cloud object.

        Primarily useful for manual polling of compute state.
        """
        instance = ComputeInstance(self.workspace, self.name)
        self.modified_on = instance.modified_on
        self.provisioning_state = instance.provisioning_state
        self.provisioning_errors = instance.provisioning_errors
        self.instance_resource_id = instance.cluster_resource_id
        self.instance_location = instance.cluster_location
        self.vm_size = instance.vm_size
        self.ssh_public_access = (instance.ssh_public_access == "Enabled")
        self.admin_username = instance.admin_username
        self.admin_user_ssh_public_key = instance.admin_user_ssh_public_key
        self.ssh_port = instance.ssh_port
        self.status = instance.status
        self.public_ip_address = instance.public_ip_address
        self.private_ip_address = instance.private_ip_address
        self.applications = instance.applications
        self.errors = instance.errors

    def get_status(self):
        """Retrieve the current detailed status for the ComputeInstance.

        :return: A detailed status object for the compute
        :rtype: ComputeInstanceStatus
        """
        self.refresh_state()
        if not self.status:
            state = self.provisioning_state.capitalize()
            if state == 'Creating':
                print('ComputeInstance is getting created. Consider calling wait_for_completion() first')
            elif state == 'Failed':
                print('ComputeInstance is in a failed state, try deleting and recreating')
            else:
                print('Current provisioning state of ComputeInstance is "{}"'.format(state))
            return None

        return self.status

    def delete(self):
        """Remove the ComputeInstance object from its associated workspace.

        .. remarks::

            If this object was created through Azure ML,
            the corresponding cloud based objects will also be deleted. If this object was created externally and only
            attached to the workspace, it will raise exception and nothing will be changed.

        :raises: azureml.exceptions.ComputeTargetException
        """
        self._delete_or_detach('delete')

    def detach(self):
        """Detach is not supported for ComputeInstance object. Try to use delete instead.

        :raises: azureml.exceptions.ComputeTargetException
        """
        raise ComputeTargetException('Detach is not supported for ComputeInstance object. Try to use delete instead.')

    def serialize(self):
        """Convert this ComputeInstance object into a json serialized dictionary.

        :return: The json representation of this ComputeInstance object
        :rtype: dict
        """
        subnet_id = None
        if self.vnet_resourcegroup_name and self.vnet_name and self.subnet_name:
            subnet_id = "/subscriptions/{0}/resourceGroups/{1}/providers/Microsoft.Network/virtualNetworks" \
                        "/{2}/subnets/{3}".format(self.workspace.subscription_id, self.vnet_resourcegroup_name,
                                                  self.vnet_name, self.subnet_name)

        instance_properties = {'vmSize': self.vm_size,
                               'applications': self.applications,
                               'connectivityEndpoints': {'publicIpAddress': self.public_ip_address,
                                                         'privateIpAddress': self.private_ip_address},
                               'sshSettings': {'sshPublicAccess': "Enabled" if self.ssh_public_access else "Disabled",
                                               'adminUserName': self.admin_username,
                                               'adminPublicKey': self.admin_user_ssh_public_key,
                                               'sshPort': self.ssh_port},
                               'subnet': {'id': subnet_id},
                               'errors': self.errors}
        instance_status = self.status.serialize() if self.status else None
        instance_properties = {'description': self.description,
                               'computeType': self.type,
                               'computeLocation': self.location,
                               'provisioningErrors': self.provisioning_errors,
                               'properties': instance_properties,
                               'status': instance_status}
        return {'id': self.id, 'name': self.name, 'location': self.location, 'tags': self.tags,
                'properties': instance_properties}

    @staticmethod
    def deserialize(workspace, object_dict):
        """Convert a json object into a ComputeInstance object.

        Will fail if the provided workspace is not the workspace the Compute is associated with.

        :param workspace: The workspace object the ComputeInstance object is associated with
        :type workspace: azureml.core.Workspace
        :param object_dict: A json object to convert to a ComputeInstance object
        :type object_dict: dict
        :return: The ComputeInstance representation of the provided json object
        :rtype: azureml.core.compute.ComputeInstance.ComputeInstance
        :raises: azureml.exceptions.ComputeTargetException
        """
        ComputeInstance._validate_get_payload(object_dict)
        target = ComputeInstance(None, None)
        target._initialize(workspace, object_dict)
        return target

    @staticmethod
    def _validate_get_payload(payload):
        if 'properties' not in payload or 'computeType' not in payload['properties']:
            raise ComputeTargetException('Invalid payload:\n'
                                         '{}'.format(payload))
        if payload['properties']['computeType'] != ComputeInstance._compute_type:
            raise ComputeTargetException('Invalid payload, not "{}":\n'
                                         '{}'.format(ComputeInstance._compute_type, payload))
        for arm_key in ['location', 'id', 'tags']:
            if arm_key not in payload:
                raise ComputeTargetException('Invalid payload, missing ["{}"]:\n'
                                             '{}'.format(arm_key, payload))
        for key in ['properties', 'provisioningErrors', 'description', 'provisioningState', 'resourceId']:
            if key not in payload['properties']:
                raise ComputeTargetException('Invalid payload, missing ["properties"]["{}"]:\n'
                                             '{}'.format(key, payload))
        if payload['properties']['properties']:
            for instance_key in ['vmSize', 'sshSettings',
                                 'createdBy', 'errors', 'state']:
                if instance_key not in payload['properties']['properties']:
                    raise ComputeTargetException('Invalid payload, missing '
                                                 '["properties"]["properties"]["{}"]:\n'
                                                 '{}'.format(instance_key, payload))

    def get(self):
        """Return ComputeInstance object.

        :return: The ComputeInstance representation of the provided json object
        :rtype: azureml.core.compute.ComputeInstance.ComputeInstance
        :raises: azureml.exceptions.ComputeTargetException
        """
        return ComputeTarget._get(self.workspace, self.name)

    def start(self, wait_for_completion=False, show_output=False):
        """Start the ComputeInstance.

        :param wait_for_completion: Boolean to wait for the state update. Defaults to False
        :type wait_for_completion: bool
        :param show_output: Boolean to provide more verbose output. Defaults to False
        :type show_output: bool
        :return: None
        :rtype: None
        :raises: azureml.exceptions.ComputeTargetException
        """
        self._update_instance_state("start", wait_for_completion, show_output)

    def stop(self, wait_for_completion=False, show_output=False):
        """Stop the ComputeInstance.

        :param wait_for_completion: Boolean to wait for the state update. Defaults to False
        :type wait_for_completion: bool
        :param show_output: Boolean to provide more verbose output. Defaults to False
        :type show_output: bool
        :return: None
        :rtype: None
        :raises: azureml.exceptions.ComputeTargetException
        """
        self._update_instance_state("stop", wait_for_completion, show_output)

    def restart(self, wait_for_completion=False, show_output=False):
        """Restart the ComputeInstance.

        :param wait_for_completion: Boolean to wait for the state update. Defaults to False
        :type wait_for_completion: bool
        :param show_output: Boolean to provide more verbose output. Defaults to False
        :type show_output: bool
        :return: None
        :rtype: None
        :raises: azureml.exceptions.ComputeTargetException
        """
        self._update_instance_state("restart", wait_for_completion, show_output)

    def _update_instance_state(self, state, wait_for_completion=False, show_output=False):
        """Update the ComputeInstance state.

        :param state: State (Supported states: start, stop, restart).
        :type state: str
        :param wait_for_completion: Boolean to wait for the state update. Defaults to False
        :type wait_for_completion: bool
        :param show_output: Boolean to provide more verbose output. Defaults to False
        :type show_output: bool
        :return: None
        :rtype: None
        :raises: azureml.exceptions.ComputeTargetException
        """
        retry_interval = 5
        endpoint = self._get_compute_endpoint(self.workspace, self.name) + '/' + state
        headers = self.workspace._auth.get_authentication_header()
        params = {'api-version': MLC_WORKSPACE_API_VERSION}

        while True:
            resp = ClientBase._execute_func(get_requests_session().post, endpoint, params=params, headers=headers)
            try:
                resp.raise_for_status()
                break
            except requests.exceptions.HTTPError:
                if "There is already an active operation submitted" in resp.text:
                    time.sleep(retry_interval)
                    continue
                raise ComputeTargetException('Received bad response from Resource Provider:\n'
                                             'Response Code: {}\n'
                                             'Headers: {}\n'
                                             'Content: {}'.format(resp.status_code, resp.headers, resp.content))
        if wait_for_completion:
            self._wait_for_status_update(retry_interval, show_output)

    def _wait_for_status_update(self, refresh_interval=5, show_output=False):
        """Wait for the ComputeInstance status update.

        :param refresh_interval: Status refresh interval in seconds.
        :type refresh_interval: int
        :param show_output: Boolean to provide more verbose output. Defaults to False
        :type show_output: bool
        :return: None
        :rtype: None
        :raises: azureml.exceptions.ComputeTargetException
        """
        prev_state = None
        current_state = None

        while True:
            time.sleep(refresh_interval)
            self.refresh_state()

            if self.status and self.status.state:
                current_state = self.status.state.capitalize()
            else:
                current_state = self.provisioning_state.capitalize()

            if show_output:
                if current_state != prev_state:
                    if prev_state is None:
                        sys.stdout.write('{}'.format(current_state))
                    else:
                        sys.stdout.write('\n{}'.format(current_state))
                elif current_state:
                    sys.stdout.write('.')
                sys.stdout.flush()

            terminal_state_reached = (current_state == "Running" or current_state == "Ready" or
                                      current_state == "Stopped" or current_state.endswith("Failed"))

            if terminal_state_reached:
                break

            prev_state = current_state

        if show_output:
            sys.stdout.write('\n')
            sys.stdout.flush()

            if self.status and self.status.errors:
                print('There were errors reported from ComputeInstance:\n{}'.format(self.status.errors))

    def get_active_runs(self, type=None, tags=None, properties=None, status=None):
        """Return a generator of the runs for this compute.

        :param type: Filter the returned generator of runs by the provided type. See
            :func:`azureml.core.Run.add_type_provider` for creating run types.
        :type type: str
        :param tags: Filter runs by "tag" or {"tag": "value"}
        :type tags: str or dict
        :param properties: Filter runs by "property" or {"property": "value"}
        :type properties: str or dict
        :param status: Run status - either "Running" or "Queued"
        :type status: str
        :return: a generator of ~_restclient.models.RunDto
        :rtype: builtin.generator
        """
        workspace_client = WorkspaceClient(self.workspace.service_context)
        return workspace_client.get_runs_by_compute(
            compute_name=self.name,
            type=type,
            tags=tags,
            properties=properties,
            status=status)

    @staticmethod
    def supported_vmsizes(workspace, location=None):
        """List the supported VM sizes in a region.

        :param workspace: The workspace.
        :type workspace: azureml.core.Workspace
        :param location: Location of instance. If not specified, will default to workspace location.
        :type location: str
        :return: List of supported VM sizes in a region with name of the VM, VCPUs, RAM
        :rtype: builtin.list
        """
        paginated_results = []
        if not workspace:
            return paginated_results

        if not location:
            location = workspace.location

        vm_size_fmt = '{}/subscriptions/{}/providers/Microsoft.MachineLearningServices/locations/{}/vmSizes'
        resource_manager_endpoint = ComputeTarget._get_resource_manager_endpoint(workspace)
        endpoint = vm_size_fmt.format(resource_manager_endpoint, workspace.subscription_id, location)
        headers = workspace._auth.get_authentication_header()
        params = {'api-version': MLC_WORKSPACE_API_VERSION}
        resp = ClientBase._execute_func(get_requests_session().get, endpoint, params=params, headers=headers)

        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError:
            raise ComputeTargetException('Error occurred retrieving targets:\n'
                                         'Response Code: {}\n'
                                         'Headers: {}\n'
                                         'Content: {}'.format(resp.status_code, resp.headers, resp.content))
        content = resp.content
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        result_list = json.loads(content)
        paginated_results = get_paginated_compute_supported_vms(result_list, headers)

        return paginated_results


class ComputeInstanceProvisioningConfiguration(ComputeTargetProvisioningConfiguration):
    """Provisioning configuration object for ComputeInstance targets.

    This objects is used to define the configuration parameters for provisioning ComputeInstance compute.

    :param vm_size: Size of agent VMs. More details can be found here: https://aka.ms/azureml-vm-details.
        Note that not all sizes are available in all regions, as
        detailed in the previous link. Defaults to Standard_NC6
    :type vm_size: str
    :param ssh_public_access: State of the public SSH port. Possible values are:
        False - Indicates that the public ssh port is closed.
        True - Indicates that the public ssh port is open.
    :type ssh_public_access: bool
    :param admin_user_ssh_public_key: SSH public key of the administrator user account
    :type admin_user_ssh_public_key: str
    :param vnet_resourcegroup_name: Name of the resource group where the virtual network is located
    :type vnet_resourcegroup_name: str
    :param vnet_name: Name of the virtual network
    :type vnet_name: str
    :param subnet_name: Name of the subnet inside the vnet
    :type subnet_name: str
    :param tags: A dictionary of key value tags to provide to the compute object
    :type tags: dict[str, str]
    :param description: A description to provide to the compute object
    :type description: str
    """

    def __init__(self, vm_size='', ssh_public_access=False, admin_user_ssh_public_key=None,
                 vnet_resourcegroup_name=None, vnet_name=None, subnet_name=None, tags=None, description=None):
        """Create a configuration object for provisioning a ComputeInstance target.

        :param vm_size: Size of agent VMs. More details can be found here: https://aka.ms/azureml-vm-details.
            Note that not all sizes are available in all regions, as
            detailed in the previous link. Defaults to Standard_NC6
        :type vm_size: str
        :param ssh_public_access: State of the public SSH port. Possible values are:
            False - Indicates that the public ssh port is closed.
            True - Indicates that the public ssh port is open.
        :type ssh_public_access: bool
        :param admin_user_ssh_public_key: SSH public key of the administrator user account
        :type admin_user_ssh_public_key: str
        :param vnet_resourcegroup_name: Name of the resource group where the virtual network is located
        :type vnet_resourcegroup_name: str
        :param vnet_name: Name of the virtual network
        :type vnet_name: str
        :param subnet_name: Name of the subnet inside the vnet
        :type subnet_name: str
        :param tags: A dictionary of key value tags to provide to the compute object
        :type tags: dict[str, str]
        :param description: A description to provide to the compute object
        :type description: str
        :return: A configuration object to be used when creating a Compute object
        :rtype: ComputeInstanceProvisioningConfiguration
        :raises: azureml.exceptions.ComputeTargetException
        """
        super(ComputeInstanceProvisioningConfiguration, self).__init__(ComputeInstance, None)
        self.vm_size = vm_size
        self.ssh_public_access = ssh_public_access
        self.admin_user_ssh_public_key = admin_user_ssh_public_key
        self.vnet_resourcegroup_name = vnet_resourcegroup_name
        self.vnet_name = vnet_name
        self.subnet_name = subnet_name
        self.tags = tags
        self.description = description
        self.validate_configuration()

    def validate_configuration(self):
        """Check that the specified configuration values are valid.

        Will raise a :class:`azureml.exceptions.ComputeTargetException` if validation fails.

        :raises: azureml.exceptions.ComputeTargetException
        """
        if any([self.vnet_name, self.vnet_resourcegroup_name, self.subnet_name]) and \
                not all([self.vnet_name, self.vnet_resourcegroup_name, self.subnet_name]):
            raise ComputeTargetException('Invalid configuration, not all virtual net information provided. '
                                         'To use a custom virtual net, please provide vnet name, vnet resource '
                                         'group and subnet name')


class ComputeInstanceStatus(object):
    """Detailed status for a ComputeInstance object.

    .. remarks::

        Initialize a ComputeInstanceStatus object

        :param creation_time: instance creation time
        :type creation_time: datetime.datetime
        :param created_by_user_name: Describes information on user who created this ComputeInstance compute
        :type created_by_user_name: str
        :param created_by_user_id: Uniquely identifies the user within his/her organization
        :type created_by_user_id: str
        :param created_by_user_org: Uniquely identifies user Azure Active Directory organization
        :type created_by_user_org: str
        :param errors: A list of error details, if any
        :type errors: builtin.list
        :param modified_time: instance modification time
        :type modified_time: datetime.datetime
        :param state: The current state of this ComputeInstance.
        :type state: str
        :param vm_size: Size of agent VMs. More details can be found here: https://aka.ms/azureml-vm-details.
            Note that not all sizes are available in all regions, as
            detailed in the previous link.
        :type vm_size: str
    """

    def __init__(self, creation_time, created_by_user_name, created_by_user_id, created_by_user_org,
                 errors, modified_time, state, vm_size):
        """Initialize a ComputeInstanceStatus object.

        :param creation_time: instance creation time
        :type creation_time: datetime.datetime
        :param created_by_user_name: Describes information on user who created this ComputeInstance compute
        :type created_by_user_name: str
        :param created_by_user_id: Uniquely identifies the user within his/her organization
        :type created_by_user_id: str
        :param created_by_user_org: Uniquely identifies user Azure Active Directory organization
        :type created_by_user_org: str
        :param errors: A list of error details, if any
        :type errors: builtin.list
        :param modified_time: instance modification time
        :type modified_time: datetime.datetime
        :param state: The current state of this ComputeInstance.
        :type state: str
        :param vm_size: Size of agent VMs. More details can be found here: https://aka.ms/azureml-vm-details.
            Note that not all sizes are available in all regions, as
            detailed in the previous link.
        :type vm_size: str
        """
        self.creation_time = creation_time
        self.created_by_user_name = created_by_user_name
        self.created_by_user_id = created_by_user_id
        self.created_by_user_org = created_by_user_org
        self.errors = errors
        self.modified_time = modified_time
        self.state = state
        self.vm_size = vm_size

    def __repr__(self):
        """Return the string representation of the ComputeInstanceStatus object.

        :return: String representation of the ComputeInstanceStatus object
        :rtype: str
        """
        formatted_info = ',\n'.join(["{}: {}".format(k, v) for k, v in self.serialize().items()])
        return formatted_info

    def serialize(self):
        """Convert this ComputeInstanceStatus object into a json serialized dictionary.

        :return: The json representation of this ComputeInstanceStatus object
        :rtype: dict
        """
        creation_time = self.creation_time.isoformat() if self.creation_time else None
        modified_time = self.modified_time.isoformat() if self.modified_time else None
        return {'errors': self.errors,
                'creationTime': creation_time,
                'createdBy': {'userId': self.created_by_user_id,
                              'userOrgId': self.created_by_user_org},
                'modifiedTime': modified_time,
                'state': self.state,
                'vmSize': self.vm_size}

    @staticmethod
    def deserialize(object_dict):
        """Convert a json object into a ComputeInstanceStatus object.

        :param object_dict: A json object to convert to a ComputeInstanceStatus object
        :type object_dict: dict
        :return: The ComputeInstanceStatus representation of the provided json object
        :rtype: ComputeInstanceStatus
        :raises: azureml.exceptions.ComputeTargetException
        """
        if not object_dict:
            return None
        creation_time = parse(object_dict['createdOn']) \
            if 'createdOn' in object_dict else None
        modified_time = parse(object_dict['modifiedOn']) \
            if 'modifiedOn' in object_dict else None
        instance_properties = object_dict['properties'] \
            if 'properties' in object_dict else None
        vm_size = instance_properties['vmSize'] \
            if instance_properties and 'vmSize' in instance_properties else None
        state = instance_properties['state'] \
            if instance_properties and 'state' in instance_properties else None
        errors = instance_properties['errors'] \
            if instance_properties and 'errors' in instance_properties else None
        created_by = instance_properties['createdBy'] \
            if instance_properties and 'createdBy' in instance_properties else None
        created_by_user_name = created_by['userName'] \
            if created_by and 'userName' in created_by else None
        created_by_user_id = created_by['userId'] \
            if created_by and 'userId' in created_by else None
        created_by_user_org = created_by['userOrgId'] \
            if created_by and 'userOrgId' in created_by else None

        return ComputeInstanceStatus(creation_time, created_by_user_name, created_by_user_id, created_by_user_org,
                                     errors, modified_time, state, vm_size)

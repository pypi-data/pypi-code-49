import io
import logging
import requests
import time

from packaging import version

from .api_key import ApiKey
from .bucket_verification import BucketVerification
from .dataset import Dataset
from .dataset_instance import DatasetInstance
from .dataset_upload import DatasetUpload
from .deployment import Deployment
from .deployment_auth_token import DeploymentAuthToken
from .model import Model
from .model_instance import ModelInstance
from .organization import Organization
from .project import Project
from .project_dataset import ProjectDataset
from .project_dataset_schema import ProjectDatasetSchema
from .schema_validation import SchemaValidation
from .training_config_options import TrainingConfigOptions
from .use_case import UseCase
from .user import User
from .user_invite import UserInvite


class ApiException(Exception):
    def __init__(self, message, http_status, exception=None):
        self.message = message
        self.http_status = http_status
        self.exception = exception or 'ApiException'

    def __str__(self):
        return f'{self.exception}({self.http_status}): {self.message}'


class ReClient():
    client_version = '0.5.0'

    def __init__(self, api_key=None, server='https://realityengines.ai'):
        self.api_key = api_key
        self.server = server
        # Connection and version check
        try:
            documentation = self._call_api('documentation', 'GET')
            web_version = documentation['version']
            if version.parse(web_version) > version.parse(self.client_version):
                logging.info(
                    'A new version of the RealityEngines library is available')
                logging.info(
                    f'Current Version: {version} -> New Version: {web_version}')
            if api_key is not None:
                self.user = self._call_api('getUser', 'GET')
        except Exception:
            logging.error('Failed to connect to RealityEngines.AI server')
            raise

    def _call_api(
            self, action, method, query_params=None,
            body=None, files=None, parse_types=None):
        headers = {'apiKey': self.api_key,
                   'clientVersion': self.client_version, 'client': 'python'}
        url = self.server + '/api/v0/' + action

        response = self._request(
            url, method, query_params=query_params, headers=headers, body=body, files=files)
        result = None
        success = False
        error_message = None
        error_type = None
        try:
            json_data = response.json()
            success = json_data['success']
            error_message = json_data.get('error')
            error_type = json_data.get('errorType')
            result = json_data.get('result')
            if success and parse_types:
                if len(parse_types) == 1:
                    parse_type = next(iter(parse_types.values()))
                    if isinstance(result, list):
                        result = [parse_type(self, **r)
                                  for r in result if r is not None]
                    else:
                        result = parse_type(self, **result) if result else None
                else:
                    result = {name: parse_type(
                        self, **result[name]) for name, parse_type in parse_types if result[name] is not None}
        except Exception:
            error_message = response.text
        if not success:
            if response.status_code > 502 and response.status_code not in (501, 503):
                error_message = 'Internal Server Error, please contact dev@realityengines.ai for support'
            raise ApiException(error_message, response.status_code, error_type)
        return result

    def _request(self, url, method, query_params=None, headers=None,
                 body=None, files=None):
        if method == 'GET':
            return requests.get(url, params=query_params, headers=headers)
        elif method == 'POST':
            return requests.post(url, params=query_params, json=body, headers=headers, files=files, timeout=90)
        elif method == 'PUT':
            return requests.put(url, params=query_params, data=body, headers=headers, files=files, timeout=90)
        elif method == 'PATCH':
            return requests.patch(url, params=query_params, data=body, headers=headers, timeout=90)
        elif method == 'DELETE':
            return requests.delete(url, params=query_params, data=body, headers=headers)
        else:
            raise ValueError(
                'HTTP method must be `GET`, `POST`, `PATCH`, `PUT` or `DELETE`'
            )

    def _poll(self, obj, wait_states, delay=5, timeout=300):
        start_time = time.time()
        while obj.get_status() in wait_states:
            if timeout and time.time() - start_time > timeout:
                raise TimeoutError(f'Maximum wait time of {timeout}s exceeded')
            time.sleep(delay)
        return obj.describe()

    def add_organization_admin(self, user_id: str):
        '''
    Add a new Admin User to the Organization

    Args:
        userId: The User ID to promote to an Admin

    Raises:
        DataNotFoundError: When the User has not yet joined the Organization
        AlreadyExistsError: When the current User is not an Admin of the Organization
        '''
        return self._call_api('addOrganizationAdmin', 'POST', body={'userId': user_id})

    def create_organization(self, name: str, workspace: str, discoverable: bool = 'True'):
        '''
    Create a new RealityEngines.AI Organization.

    Args:
        name: A user-friendly name for the organization
        workspace: A unique alphanumeric string to identify your organization
        discoverable: Sets the discoverability of your organization. If True, other users with the same email domain can find and join this Organization.

    Returns:
        Organization: Information about the Organization created

    Raises:
        ConflictError: When the current User already belongs to an Organization
        AlreadyExistsError: When the workspace is already taken
        '''
        return self._call_api('createOrganization', 'POST', body={'name': name, 'workspace': workspace, 'discoverable': discoverable}, parse_types={'organization': Organization})

    def delete_invite(self, user_invite_id: str = None):
        '''
    Remove a pending Organization User Invite.

    Args:
        userInviteId: The ID of the invite to remove

    Raises:
        PermissionDeniedError: When the current User did not invite the email to the Organization or the current User is not an Organization Admin
        '''
        return self._call_api('deleteInvite', 'DELETE', query_params={'userInviteId': user_invite_id})

    def invite_user(self, email: str):
        '''
    Create a new Organization Invite to a specific email

    Args:
        email: The email address to invite to your Organization

    Returns:
        UserInvite: Information about the User Invite

    Raises:
        ConflictError: When the email has already been invited or has already joined the Organization
        '''
        return self._call_api('inviteUser', 'POST', body={'email': email}, parse_types={'user_invite': UserInvite})

    def join_organization(self, organization_id: str):
        '''
    Join an existing RealityEngines.AI Organization.

    Args:
        organizationId: The unique organization ID to join

    Raises:
        ConflictError: When the current User has already joined the specified organization
        PermissionDeniedError: When the current User's email domain does not match the domain of the Organization
        '''
        return self._call_api('joinOrganization', 'POST', body={'organizationId': organization_id})

    def list_organizations(self):
        '''
    List all public Organizations that match the domain of the current user's email address or that the current User has joined

    Returns:
        List<Organization>: Information about the Organizations available to join
        '''
        return self._call_api('listOrganizations', 'GET', query_params={}, parse_types={'organization': Organization})

    def list_organization_users(self):
        '''
    List all the members in the current user's Organization

    Returns:
        List<User>: A list of Users in the organization

    Raises:
        PermissionDeniedError: When the current User does not belong to the selected Organization or the User has not yet joined an Organization
        '''
        return self._call_api('listOrganizationUsers', 'GET', query_params={}, parse_types={'user': User})

    def list_user_invites(self):
        '''
    List the Organization's User Invites

    Returns:
        List<UserInvite>: A list of User Invites
        '''
        return self._call_api('listUserInvites', 'GET', query_params={}, parse_types={'user_invite': UserInvite})

    def remove_user_from_organization(self, user_id: str):
        '''
    Remove a User from the Organization

    Args:
        userId: The User ID to remove from the Organization

    Raises:
        PermissionDeniedError: When the User ID is not equal to the current User or the current User is not an Admin of the Organization.
        '''
        return self._call_api('removeUserFromOrganization', 'DELETE', query_params={'userId': user_id})

    def delete_api_key(self, api_key_id: str):
        '''    '''
        return self._call_api('deleteApiKey', 'DELETE', query_params={'apiKeyId': api_key_id})

    def get_user(self):
        '''
    Get the current User's info

    Returns:
        User: Information about the current User
        '''
        return self._call_api('getUser', 'GET', query_params={}, parse_types={'user': User})

    def list_api_keys(self):
        '''    '''
        return self._call_api('listApiKeys', 'GET', query_params={}, parse_types={'api_key': ApiKey})

    def add_project_dataset_column_override(self, project_id: str, dataset_id: str, column: str, data_type: str = 'DEFAULT', data_use: str = None):
        '''    '''
        return self._call_api('addProjectDatasetColumnOverride', 'POST', body={'projectId': project_id, 'datasetId': dataset_id, 'column': column, 'dataType': data_type, 'dataUse': data_use}, parse_types={'project_dataset_schema': ProjectDatasetSchema})

    def create_project(self, name: str, use_case: str):
        '''    '''
        return self._call_api('createProject', 'GET', query_params={'name': name, 'useCase': use_case}, parse_types={'project': Project})

    def delete_project(self, project_id: str):
        '''    '''
        return self._call_api('deleteProject', 'DELETE', query_params={'projectId': project_id})

    def describe_project(self, project_id: str):
        '''    '''
        return self._call_api('describeProject', 'GET', query_params={'projectId': project_id}, parse_types={'project': Project})

    def describe_use_case_requirements(self, use_case: str):
        '''    '''
        return self._call_api('describeUseCaseRequirements', 'GET', query_params={'useCase': use_case})

    def get_project_dataset_schema(self, project_id: str, dataset_id: str):
        '''    '''
        return self._call_api('getProjectDatasetSchema', 'GET', query_params={'projectId': project_id, 'datasetId': dataset_id}, parse_types={'project_dataset_schema': ProjectDatasetSchema})

    def list_project_datasets(self, project_id: str):
        '''    '''
        return self._call_api('listProjectDatasets', 'GET', query_params={'projectId': project_id}, parse_types={'project_dataset': ProjectDataset})

    def list_project_dataset_latest_instances(self, project_id: str):
        '''    '''
        return self._call_api('listProjectDatasetLatestInstances', 'GET', query_params={'projectId': project_id}, parse_types={'dataset_instance': DatasetInstance})

    def list_projects(self):
        '''    '''
        return self._call_api('listProjects', 'GET', query_params={}, parse_types={'project': Project})

    def list_use_cases(self):
        '''    '''
        return self._call_api('listUseCases', 'GET', query_params={}, parse_types={'use_case': UseCase})

    def remove_project_dataset_column_override(self, project_id: str, dataset_id: str, column: str):
        '''    '''
        return self._call_api('removeProjectDatasetColumnOverride', 'DELETE', query_params={'projectId': project_id, 'datasetId': dataset_id, 'column': column}, parse_types={'project_dataset_schema': ProjectDatasetSchema})

    def set_project_dataset_schema_override(self, project_id: str, dataset_id: str, column_overrides: dict = None):
        '''    '''
        return self._call_api('setProjectDatasetSchemaOverride', 'POST', body={'projectId': project_id, 'datasetId': dataset_id, 'columnOverrides': column_overrides}, parse_types={'project_dataset_schema': ProjectDatasetSchema})

    def update_project(self, project_id: str, name: str):
        '''    '''
        return self._call_api('updateProject', 'PATCH', body={'projectId': project_id, 'name': name})

    def validate_project_datasets(self, project_id: str):
        '''    '''
        return self._call_api('validateProjectDatasets', 'GET', query_params={'projectId': project_id}, parse_types={'schema_validation': SchemaValidation})

    def add_aws_role(self, bucket: str, role_arn: str):
        '''    '''
        return self._call_api('addAWSRole', 'POST', body={'bucket': bucket, 'roleArn': role_arn})

    def get_data_connector_verification(self, bucket: str):
        '''    '''
        return self._call_api('getDataConnectorVerification', 'GET', query_params={'bucket': bucket})

    def list_data_connector_verifications(self):
        '''    '''
        return self._call_api('listDataConnectorVerifications', 'GET', query_params={}, parse_types={'bucket_verification': BucketVerification})

    def remove_data_connector(self, bucket: str):
        '''    '''
        return self._call_api('removeDataConnector', 'DELETE', query_params={'bucket': bucket})

    def verify_data_connector(self, bucket: str):
        '''    '''
        return self._call_api('verifyDataConnector', 'POST', body={'bucket': bucket})

    def attach_dataset_to_project(self, dataset_id: str, project_id: str, project_dataset_type: str):
        '''
        Adds a dataset to an existing project
        '''
        return self._call_api('attachDatasetToProject', 'POST', body={'datasetId': dataset_id, 'projectId': project_id, 'projectDatasetType': project_dataset_type}, parse_types={'project_dataset_schema': ProjectDatasetSchema})

    def delete_dataset(self, dataset_id: str):
        '''    '''
        return self._call_api('deleteDataset', 'DELETE', query_params={'datasetId': dataset_id})

    def describe_dataset(self, dataset_id: str):
        '''    '''
        return self._call_api('describeDataset', 'GET', query_params={'datasetId': dataset_id}, parse_types={'dataset': Dataset})

    def read_dataset_from_cloud(self, name: str, location: str, file_format: str = 'text/csv', project_id: str = None, project_dataset_type: str = None):
        '''    '''
        return self._call_api('readDatasetFromCloud', 'POST', body={'name': name, 'location': location, 'fileFormat': file_format, 'projectId': project_id, 'projectDatasetType': project_dataset_type}, parse_types={'dataset': Dataset})

    def read_dataset_instance_from_cloud(self, dataset_id: str):
        '''    '''
        return self._call_api('readDatasetInstanceFromCloud', 'POST', body={'datasetId': dataset_id}, parse_types={'dataset_instance': DatasetInstance})

    def list_datasets(self):
        '''    '''
        return self._call_api('listDatasets', 'GET', query_params={}, parse_types={'dataset': Dataset})

    def list_dataset_instances(self, dataset_id: str = None):
        '''    '''
        return self._call_api('listDatasetInstances', 'GET', query_params={'datasetId': dataset_id}, parse_types={'dataset_instance': DatasetInstance})

    def create_dataset_upload(self, name: str, file_format: str = 'text/csv', project_id: str = None, project_dataset_type: str = None):
        '''    '''
        return self._call_api('createDatasetUpload', 'POST', body={'name': name, 'fileFormat': file_format, 'projectId': project_id, 'projectDatasetType': project_dataset_type}, parse_types={'dataset_upload': DatasetUpload})

    def create_dataset_instance_upload(self, dataset_id: str):
        '''    '''
        return self._call_api('createDatasetInstanceUpload', 'POST', body={'datasetId': dataset_id}, parse_types={'dataset_upload': DatasetUpload})

    def remove_dataset_from_project(self, dataset_id: str, project_id: str):
        '''    '''
        return self._call_api('removeDatasetFromProject', 'POST', body={'datasetId': dataset_id, 'projectId': project_id})

    def create_deployment(self, model_id: str, name: str, description: str = None, deployment_config: dict = None):
        '''    '''
        return self._call_api('createDeployment', 'POST', body={'modelId': model_id, 'name': name, 'description': description, 'deploymentConfig': deployment_config}, parse_types={'deployment': Deployment})

    def create_deployment_token(self, project_id: str):
        '''    '''
        return self._call_api('createDeploymentToken', 'POST', body={'projectId': project_id}, parse_types={'deployment_auth_token': DeploymentAuthToken})

    def delete_deployment(self, deployment_id: str):
        '''    '''
        return self._call_api('deleteDeployment', 'DELETE', query_params={'deploymentId': deployment_id})

    def delete_deployment_token(self, auth_token: str = None):
        '''    '''
        return self._call_api('deleteDeploymentToken', 'DELETE', query_params={'authToken': auth_token})

    def describe_deployment(self, deployment_id: str):
        '''    '''
        return self._call_api('describeDeployment', 'GET', query_params={'deploymentId': deployment_id}, parse_types={'deployment': Deployment})

    def list_deployments(self, project_id: str):
        '''    '''
        return self._call_api('listDeployments', 'GET', query_params={'projectId': project_id}, parse_types={'deployment': Deployment})

    def list_deployment_tokens(self, project_id: str):
        '''    '''
        return self._call_api('listDeploymentTokens', 'GET', query_params={'projectId': project_id}, parse_types={'deployment_auth_token': DeploymentAuthToken})

    def update_deployment(self, deployment_id: str, name: str = None, description: str = None):
        '''    '''
        return self._call_api('updateDeployment', 'PATCH', body={'deploymentId': deployment_id, 'name': name, 'description': description})

    def complete_upload(self, dataset_upload_id: str):
        '''    '''
        return self._call_api('completeUpload', 'POST', body={'datasetUploadId': dataset_upload_id}, parse_types={'dataset': Dataset})

    def describe_upload(self, dataset_upload_id: str):
        '''    '''
        return self._call_api('describeUpload', 'GET', query_params={'datasetUploadId': dataset_upload_id}, parse_types={'dataset_upload': DatasetUpload})

    def list_uploads(self):
        '''    '''
        return self._call_api('listUploads', 'GET', query_params={}, parse_types={'dataset_upload': DatasetUpload})

    def upload_file_part(self, dataset_upload_id: str, part_number: int, part_data: io.TextIOBase):
        '''
        Upload a dataset part up to 5GB in size for a total file size of up to 5TB
        Each part must be >=5MB in size, unless it is the last (or only) part

    Args:
        datasetUploadId: The Upload ID for this dataset
        partNumber: 1 indexed file part
        partData: the multipart/form-data for this dataset part

    Raises:
        DataNotFoundError: If there is no Dataset Upload with this datasetUploadId

        '''
        return self._call_api('uploadFilePart', 'POST', query_params={'datasetUploadId': dataset_upload_id, 'partNumber': part_number}, files={'partData': part_data})

    def cancel_model_training(self, model_id: str):
        '''    '''
        return self._call_api('cancelModelTraining', 'DELETE', query_params={'modelId': model_id})

    def train_model(self, project_id: str, training_config: dict = None):
        '''    '''
        return self._call_api('trainModel', 'POST', body={'projectId': project_id, 'trainingConfig': training_config}, parse_types={'model': Model})

    def delete_model(self, model_id: str):
        '''    '''
        return self._call_api('deleteModel', 'DELETE', query_params={'modelId': model_id})

    def describe_model(self, model_id: str):
        '''    '''
        return self._call_api('describeModel', 'GET', query_params={'modelId': model_id}, parse_types={'model': Model})

    def get_model_metrics(self, model_id: str):
        '''    '''
        return self._call_api('getModelMetrics', 'GET', query_params={'modelId': model_id})

    def get_training_config_options(self, project_id: str):
        '''    '''
        return self._call_api('getTrainingConfigOptions', 'GET', query_params={'projectId': project_id}, parse_types={'training_config_options': TrainingConfigOptions})

    def list_models(self, project_id: str):
        '''    '''
        return self._call_api('listModels', 'GET', query_params={'projectId': project_id}, parse_types={'model': Model})

    def list_model_instances(self, model_id: str):
        '''    '''
        return self._call_api('listModelInstances', 'GET', query_params={'modelId': model_id}, parse_types={'model_instance': ModelInstance})

    def predict(self, auth_token: str, deployment_id: str, data: str, **kwargs):
        '''    '''
        return self._call_api('predict', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'data': data, **kwargs})

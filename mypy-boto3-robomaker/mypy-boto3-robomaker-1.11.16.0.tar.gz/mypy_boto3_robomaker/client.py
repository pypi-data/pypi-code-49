"""
Main interface for robomaker service client

Usage::

    import boto3
    from mypy_boto3.robomaker import RoboMakerClient

    session = boto3.Session()

    client: RoboMakerClient = boto3.client("robomaker")
    session_client: RoboMakerClient = session.client("robomaker")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_robomaker.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_robomaker.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_robomaker.type_defs import (
    ClientBatchDescribeSimulationJobResponseTypeDef,
    ClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef,
    ClientCreateDeploymentJobDeploymentConfigTypeDef,
    ClientCreateDeploymentJobResponseTypeDef,
    ClientCreateFleetResponseTypeDef,
    ClientCreateRobotApplicationResponseTypeDef,
    ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef,
    ClientCreateRobotApplicationSourcesTypeDef,
    ClientCreateRobotApplicationVersionResponseTypeDef,
    ClientCreateRobotResponseTypeDef,
    ClientCreateSimulationApplicationRenderingEngineTypeDef,
    ClientCreateSimulationApplicationResponseTypeDef,
    ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef,
    ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef,
    ClientCreateSimulationApplicationSourcesTypeDef,
    ClientCreateSimulationApplicationVersionResponseTypeDef,
    ClientCreateSimulationJobDataSourcesTypeDef,
    ClientCreateSimulationJobLoggingConfigTypeDef,
    ClientCreateSimulationJobOutputLocationTypeDef,
    ClientCreateSimulationJobResponseTypeDef,
    ClientCreateSimulationJobRobotApplicationsTypeDef,
    ClientCreateSimulationJobSimulationApplicationsTypeDef,
    ClientCreateSimulationJobVpcConfigTypeDef,
    ClientDeregisterRobotResponseTypeDef,
    ClientDescribeDeploymentJobResponseTypeDef,
    ClientDescribeFleetResponseTypeDef,
    ClientDescribeRobotApplicationResponseTypeDef,
    ClientDescribeRobotResponseTypeDef,
    ClientDescribeSimulationApplicationResponseTypeDef,
    ClientDescribeSimulationJobBatchResponseTypeDef,
    ClientDescribeSimulationJobResponseTypeDef,
    ClientListDeploymentJobsFiltersTypeDef,
    ClientListDeploymentJobsResponseTypeDef,
    ClientListFleetsFiltersTypeDef,
    ClientListFleetsResponseTypeDef,
    ClientListRobotApplicationsFiltersTypeDef,
    ClientListRobotApplicationsResponseTypeDef,
    ClientListRobotsFiltersTypeDef,
    ClientListRobotsResponseTypeDef,
    ClientListSimulationApplicationsFiltersTypeDef,
    ClientListSimulationApplicationsResponseTypeDef,
    ClientListSimulationJobBatchesFiltersTypeDef,
    ClientListSimulationJobBatchesResponseTypeDef,
    ClientListSimulationJobsFiltersTypeDef,
    ClientListSimulationJobsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientRegisterRobotResponseTypeDef,
    ClientStartSimulationJobBatchBatchPolicyTypeDef,
    ClientStartSimulationJobBatchCreateSimulationJobRequestsTypeDef,
    ClientStartSimulationJobBatchResponseTypeDef,
    ClientSyncDeploymentJobResponseTypeDef,
    ClientUpdateRobotApplicationResponseTypeDef,
    ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef,
    ClientUpdateRobotApplicationSourcesTypeDef,
    ClientUpdateSimulationApplicationRenderingEngineTypeDef,
    ClientUpdateSimulationApplicationResponseTypeDef,
    ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef,
    ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef,
    ClientUpdateSimulationApplicationSourcesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RoboMakerClient",)


class RoboMakerClient:
    """
    [RoboMaker.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_describe_simulation_job(
        self, jobs: List[str]
    ) -> ClientBatchDescribeSimulationJobResponseTypeDef:
        """
        [Client.batch_describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.batch_describe_simulation_job)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.can_paginate)
        """

    def cancel_deployment_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.cancel_deployment_job)
        """

    def cancel_simulation_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job)
        """

    def cancel_simulation_job_batch(self, batch: str) -> Dict[str, Any]:
        """
        [Client.cancel_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job_batch)
        """

    def create_deployment_job(
        self,
        clientRequestToken: str,
        fleet: str,
        deploymentApplicationConfigs: List[
            ClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef
        ],
        deploymentConfig: ClientCreateDeploymentJobDeploymentConfigTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateDeploymentJobResponseTypeDef:
        """
        [Client.create_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_deployment_job)
        """

    def create_fleet(
        self, name: str, tags: Dict[str, str] = None
    ) -> ClientCreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_fleet)
        """

    def create_robot(
        self,
        name: str,
        architecture: Literal["X86_64", "ARM64", "ARMHF"],
        greengrassGroupId: str,
        tags: Dict[str, str] = None,
    ) -> ClientCreateRobotResponseTypeDef:
        """
        [Client.create_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_robot)
        """

    def create_robot_application(
        self,
        name: str,
        sources: List[ClientCreateRobotApplicationSourcesTypeDef],
        robotSoftwareSuite: ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef,
        tags: Dict[str, str] = None,
    ) -> ClientCreateRobotApplicationResponseTypeDef:
        """
        [Client.create_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_robot_application)
        """

    def create_robot_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> ClientCreateRobotApplicationVersionResponseTypeDef:
        """
        [Client.create_robot_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_robot_application_version)
        """

    def create_simulation_application(
        self,
        name: str,
        sources: List[ClientCreateSimulationApplicationSourcesTypeDef],
        simulationSoftwareSuite: ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef,
        robotSoftwareSuite: ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef,
        renderingEngine: ClientCreateSimulationApplicationRenderingEngineTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateSimulationApplicationResponseTypeDef:
        """
        [Client.create_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application)
        """

    def create_simulation_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> ClientCreateSimulationApplicationVersionResponseTypeDef:
        """
        [Client.create_simulation_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application_version)
        """

    def create_simulation_job(
        self,
        maxJobDurationInSeconds: int,
        iamRole: str,
        clientRequestToken: str = None,
        outputLocation: ClientCreateSimulationJobOutputLocationTypeDef = None,
        loggingConfig: ClientCreateSimulationJobLoggingConfigTypeDef = None,
        failureBehavior: Literal["Fail", "Continue"] = None,
        robotApplications: List[ClientCreateSimulationJobRobotApplicationsTypeDef] = None,
        simulationApplications: List[ClientCreateSimulationJobSimulationApplicationsTypeDef] = None,
        dataSources: List[ClientCreateSimulationJobDataSourcesTypeDef] = None,
        tags: Dict[str, str] = None,
        vpcConfig: ClientCreateSimulationJobVpcConfigTypeDef = None,
    ) -> ClientCreateSimulationJobResponseTypeDef:
        """
        [Client.create_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.create_simulation_job)
        """

    def delete_fleet(self, fleet: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.delete_fleet)
        """

    def delete_robot(self, robot: str) -> Dict[str, Any]:
        """
        [Client.delete_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.delete_robot)
        """

    def delete_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.delete_robot_application)
        """

    def delete_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.delete_simulation_application)
        """

    def deregister_robot(self, fleet: str, robot: str) -> ClientDeregisterRobotResponseTypeDef:
        """
        [Client.deregister_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.deregister_robot)
        """

    def describe_deployment_job(self, job: str) -> ClientDescribeDeploymentJobResponseTypeDef:
        """
        [Client.describe_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.describe_deployment_job)
        """

    def describe_fleet(self, fleet: str) -> ClientDescribeFleetResponseTypeDef:
        """
        [Client.describe_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.describe_fleet)
        """

    def describe_robot(self, robot: str) -> ClientDescribeRobotResponseTypeDef:
        """
        [Client.describe_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.describe_robot)
        """

    def describe_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> ClientDescribeRobotApplicationResponseTypeDef:
        """
        [Client.describe_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.describe_robot_application)
        """

    def describe_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> ClientDescribeSimulationApplicationResponseTypeDef:
        """
        [Client.describe_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_application)
        """

    def describe_simulation_job(self, job: str) -> ClientDescribeSimulationJobResponseTypeDef:
        """
        [Client.describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job)
        """

    def describe_simulation_job_batch(
        self, batch: str
    ) -> ClientDescribeSimulationJobBatchResponseTypeDef:
        """
        [Client.describe_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job_batch)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.generate_presigned_url)
        """

    def list_deployment_jobs(
        self,
        filters: List[ClientListDeploymentJobsFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListDeploymentJobsResponseTypeDef:
        """
        [Client.list_deployment_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_deployment_jobs)
        """

    def list_fleets(
        self,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientListFleetsFiltersTypeDef] = None,
    ) -> ClientListFleetsResponseTypeDef:
        """
        [Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_fleets)
        """

    def list_robot_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientListRobotApplicationsFiltersTypeDef] = None,
    ) -> ClientListRobotApplicationsResponseTypeDef:
        """
        [Client.list_robot_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_robot_applications)
        """

    def list_robots(
        self,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientListRobotsFiltersTypeDef] = None,
    ) -> ClientListRobotsResponseTypeDef:
        """
        [Client.list_robots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_robots)
        """

    def list_simulation_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientListSimulationApplicationsFiltersTypeDef] = None,
    ) -> ClientListSimulationApplicationsResponseTypeDef:
        """
        [Client.list_simulation_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_simulation_applications)
        """

    def list_simulation_job_batches(
        self,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientListSimulationJobBatchesFiltersTypeDef] = None,
    ) -> ClientListSimulationJobBatchesResponseTypeDef:
        """
        [Client.list_simulation_job_batches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_simulation_job_batches)
        """

    def list_simulation_jobs(
        self,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientListSimulationJobsFiltersTypeDef] = None,
    ) -> ClientListSimulationJobsResponseTypeDef:
        """
        [Client.list_simulation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_simulation_jobs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.list_tags_for_resource)
        """

    def register_robot(self, fleet: str, robot: str) -> ClientRegisterRobotResponseTypeDef:
        """
        [Client.register_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.register_robot)
        """

    def restart_simulation_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.restart_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.restart_simulation_job)
        """

    def start_simulation_job_batch(
        self,
        createSimulationJobRequests: List[
            ClientStartSimulationJobBatchCreateSimulationJobRequestsTypeDef
        ],
        clientRequestToken: str = None,
        batchPolicy: ClientStartSimulationJobBatchBatchPolicyTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> ClientStartSimulationJobBatchResponseTypeDef:
        """
        [Client.start_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.start_simulation_job_batch)
        """

    def sync_deployment_job(
        self, clientRequestToken: str, fleet: str
    ) -> ClientSyncDeploymentJobResponseTypeDef:
        """
        [Client.sync_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.sync_deployment_job)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.untag_resource)
        """

    def update_robot_application(
        self,
        application: str,
        sources: List[ClientUpdateRobotApplicationSourcesTypeDef],
        robotSoftwareSuite: ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef,
        currentRevisionId: str = None,
    ) -> ClientUpdateRobotApplicationResponseTypeDef:
        """
        [Client.update_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.update_robot_application)
        """

    def update_simulation_application(
        self,
        application: str,
        sources: List[ClientUpdateSimulationApplicationSourcesTypeDef],
        simulationSoftwareSuite: ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef,
        robotSoftwareSuite: ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef,
        renderingEngine: ClientUpdateSimulationApplicationRenderingEngineTypeDef = None,
        currentRevisionId: str = None,
    ) -> ClientUpdateSimulationApplicationResponseTypeDef:
        """
        [Client.update_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Client.update_simulation_application)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_jobs"]
    ) -> "paginator_scope.ListDeploymentJobsPaginator":
        """
        [Paginator.ListDeploymentJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_fleets"]
    ) -> "paginator_scope.ListFleetsPaginator":
        """
        [Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_robot_applications"]
    ) -> "paginator_scope.ListRobotApplicationsPaginator":
        """
        [Paginator.ListRobotApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_robots"]
    ) -> "paginator_scope.ListRobotsPaginator":
        """
        [Paginator.ListRobots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_applications"]
    ) -> "paginator_scope.ListSimulationApplicationsPaginator":
        """
        [Paginator.ListSimulationApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_job_batches"]
    ) -> "paginator_scope.ListSimulationJobBatchesPaginator":
        """
        [Paginator.ListSimulationJobBatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobBatches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_jobs"]
    ) -> "paginator_scope.ListSimulationJobsPaginator":
        """
        [Paginator.ListSimulationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentDeploymentException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError

"""
Main interface for batch service client

Usage::

    import boto3
    from mypy_boto3.batch import BatchClient

    session = boto3.Session()

    client: BatchClient = boto3.client("batch")
    session_client: BatchClient = session.client("batch")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_batch.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_batch.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_batch.type_defs import (
    ClientCreateComputeEnvironmentComputeResourcesTypeDef,
    ClientCreateComputeEnvironmentResponseTypeDef,
    ClientCreateJobQueueComputeEnvironmentOrderTypeDef,
    ClientCreateJobQueueResponseTypeDef,
    ClientDescribeComputeEnvironmentsResponseTypeDef,
    ClientDescribeJobDefinitionsResponseTypeDef,
    ClientDescribeJobQueuesResponseTypeDef,
    ClientDescribeJobsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientRegisterJobDefinitionContainerPropertiesTypeDef,
    ClientRegisterJobDefinitionNodePropertiesTypeDef,
    ClientRegisterJobDefinitionResponseTypeDef,
    ClientRegisterJobDefinitionRetryStrategyTypeDef,
    ClientRegisterJobDefinitionTimeoutTypeDef,
    ClientSubmitJobArrayPropertiesTypeDef,
    ClientSubmitJobContainerOverridesTypeDef,
    ClientSubmitJobDependsOnTypeDef,
    ClientSubmitJobNodeOverridesTypeDef,
    ClientSubmitJobResponseTypeDef,
    ClientSubmitJobRetryStrategyTypeDef,
    ClientSubmitJobTimeoutTypeDef,
    ClientUpdateComputeEnvironmentComputeResourcesTypeDef,
    ClientUpdateComputeEnvironmentResponseTypeDef,
    ClientUpdateJobQueueComputeEnvironmentOrderTypeDef,
    ClientUpdateJobQueueResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BatchClient",)


class BatchClient:
    """
    [Batch.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.can_paginate)
        """

    def cancel_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.cancel_job)
        """

    def create_compute_environment(
        self,
        computeEnvironmentName: str,
        type: Literal["MANAGED", "UNMANAGED"],
        serviceRole: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        computeResources: ClientCreateComputeEnvironmentComputeResourcesTypeDef = None,
    ) -> ClientCreateComputeEnvironmentResponseTypeDef:
        """
        [Client.create_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.create_compute_environment)
        """

    def create_job_queue(
        self,
        jobQueueName: str,
        priority: int,
        computeEnvironmentOrder: List[ClientCreateJobQueueComputeEnvironmentOrderTypeDef],
        state: Literal["ENABLED", "DISABLED"] = None,
    ) -> ClientCreateJobQueueResponseTypeDef:
        """
        [Client.create_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.create_job_queue)
        """

    def delete_compute_environment(self, computeEnvironment: str) -> Dict[str, Any]:
        """
        [Client.delete_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.delete_compute_environment)
        """

    def delete_job_queue(self, jobQueue: str) -> Dict[str, Any]:
        """
        [Client.delete_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.delete_job_queue)
        """

    def deregister_job_definition(self, jobDefinition: str) -> Dict[str, Any]:
        """
        [Client.deregister_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.deregister_job_definition)
        """

    def describe_compute_environments(
        self, computeEnvironments: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> ClientDescribeComputeEnvironmentsResponseTypeDef:
        """
        [Client.describe_compute_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.describe_compute_environments)
        """

    def describe_job_definitions(
        self,
        jobDefinitions: List[str] = None,
        maxResults: int = None,
        jobDefinitionName: str = None,
        status: str = None,
        nextToken: str = None,
    ) -> ClientDescribeJobDefinitionsResponseTypeDef:
        """
        [Client.describe_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.describe_job_definitions)
        """

    def describe_job_queues(
        self, jobQueues: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> ClientDescribeJobQueuesResponseTypeDef:
        """
        [Client.describe_job_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.describe_job_queues)
        """

    def describe_jobs(self, jobs: List[str]) -> ClientDescribeJobsResponseTypeDef:
        """
        [Client.describe_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.describe_jobs)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.generate_presigned_url)
        """

    def list_jobs(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.list_jobs)
        """

    def register_job_definition(
        self,
        jobDefinitionName: str,
        type: Literal["container", "multinode"],
        parameters: Dict[str, str] = None,
        containerProperties: ClientRegisterJobDefinitionContainerPropertiesTypeDef = None,
        nodeProperties: ClientRegisterJobDefinitionNodePropertiesTypeDef = None,
        retryStrategy: ClientRegisterJobDefinitionRetryStrategyTypeDef = None,
        timeout: ClientRegisterJobDefinitionTimeoutTypeDef = None,
    ) -> ClientRegisterJobDefinitionResponseTypeDef:
        """
        [Client.register_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.register_job_definition)
        """

    def submit_job(
        self,
        jobName: str,
        jobQueue: str,
        jobDefinition: str,
        arrayProperties: ClientSubmitJobArrayPropertiesTypeDef = None,
        dependsOn: List[ClientSubmitJobDependsOnTypeDef] = None,
        parameters: Dict[str, str] = None,
        containerOverrides: ClientSubmitJobContainerOverridesTypeDef = None,
        nodeOverrides: ClientSubmitJobNodeOverridesTypeDef = None,
        retryStrategy: ClientSubmitJobRetryStrategyTypeDef = None,
        timeout: ClientSubmitJobTimeoutTypeDef = None,
    ) -> ClientSubmitJobResponseTypeDef:
        """
        [Client.submit_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.submit_job)
        """

    def terminate_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        """
        [Client.terminate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.terminate_job)
        """

    def update_compute_environment(
        self,
        computeEnvironment: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        computeResources: ClientUpdateComputeEnvironmentComputeResourcesTypeDef = None,
        serviceRole: str = None,
    ) -> ClientUpdateComputeEnvironmentResponseTypeDef:
        """
        [Client.update_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.update_compute_environment)
        """

    def update_job_queue(
        self,
        jobQueue: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        priority: int = None,
        computeEnvironmentOrder: List[ClientUpdateJobQueueComputeEnvironmentOrderTypeDef] = None,
    ) -> ClientUpdateJobQueueResponseTypeDef:
        """
        [Client.update_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Client.update_job_queue)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_compute_environments"]
    ) -> "paginator_scope.DescribeComputeEnvironmentsPaginator":
        """
        [Paginator.DescribeComputeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_definitions"]
    ) -> "paginator_scope.DescribeJobDefinitionsPaginator":
        """
        [Paginator.DescribeJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_queues"]
    ) -> "paginator_scope.DescribeJobQueuesPaginator":
        """
        [Paginator.DescribeJobQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> "paginator_scope.ListJobsPaginator":
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/batch.html#Batch.Paginator.ListJobs)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    ServerException: Boto3ClientError

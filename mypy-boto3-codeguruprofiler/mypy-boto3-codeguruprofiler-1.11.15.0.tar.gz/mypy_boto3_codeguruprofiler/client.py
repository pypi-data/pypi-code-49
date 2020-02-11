"""
Main interface for codeguruprofiler service client

Usage::

    import boto3
    from mypy_boto3.codeguruprofiler import CodeGuruProfilerClient

    session = boto3.Session()

    client: CodeGuruProfilerClient = boto3.client("codeguruprofiler")
    session_client: CodeGuruProfilerClient = session.client("codeguruprofiler")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, IO, TYPE_CHECKING, Union
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codeguruprofiler.client as client_scope
else:
    client_scope = object
from mypy_boto3_codeguruprofiler.type_defs import (
    ClientConfigureAgentResponseTypeDef,
    ClientCreateProfilingGroupAgentOrchestrationConfigTypeDef,
    ClientCreateProfilingGroupResponseTypeDef,
    ClientDescribeProfilingGroupResponseTypeDef,
    ClientGetProfileResponseTypeDef,
    ClientListProfileTimesResponseTypeDef,
    ClientListProfilingGroupsResponseTypeDef,
    ClientUpdateProfilingGroupAgentOrchestrationConfigTypeDef,
    ClientUpdateProfilingGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeGuruProfilerClient",)


class CodeGuruProfilerClient:
    """
    [CodeGuruProfiler.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.can_paginate)
        """

    def configure_agent(
        self, profilingGroupName: str, fleetInstanceId: str = None
    ) -> ClientConfigureAgentResponseTypeDef:
        """
        [Client.configure_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.configure_agent)
        """

    def create_profiling_group(
        self,
        clientToken: str,
        profilingGroupName: str,
        agentOrchestrationConfig: ClientCreateProfilingGroupAgentOrchestrationConfigTypeDef = None,
    ) -> ClientCreateProfilingGroupResponseTypeDef:
        """
        [Client.create_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.create_profiling_group)
        """

    def delete_profiling_group(self, profilingGroupName: str) -> Dict[str, Any]:
        """
        [Client.delete_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.delete_profiling_group)
        """

    def describe_profiling_group(
        self, profilingGroupName: str
    ) -> ClientDescribeProfilingGroupResponseTypeDef:
        """
        [Client.describe_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.describe_profiling_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.generate_presigned_url)
        """

    def get_profile(
        self,
        profilingGroupName: str,
        accept: str = None,
        endTime: datetime = None,
        maxDepth: int = None,
        period: str = None,
        startTime: datetime = None,
    ) -> ClientGetProfileResponseTypeDef:
        """
        [Client.get_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_profile)
        """

    def list_profile_times(
        self,
        endTime: datetime,
        period: Literal["P1D", "PT1H", "PT5M"],
        profilingGroupName: str,
        startTime: datetime,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: Literal["TimestampAscending", "TimestampDescending"] = None,
    ) -> ClientListProfileTimesResponseTypeDef:
        """
        [Client.list_profile_times documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profile_times)
        """

    def list_profiling_groups(
        self, includeDescription: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ClientListProfilingGroupsResponseTypeDef:
        """
        [Client.list_profiling_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profiling_groups)
        """

    def post_agent_profile(
        self,
        agentProfile: Union[bytes, IO],
        contentType: str,
        profilingGroupName: str,
        profileToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.post_agent_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.post_agent_profile)
        """

    def update_profiling_group(
        self,
        agentOrchestrationConfig: ClientUpdateProfilingGroupAgentOrchestrationConfigTypeDef,
        profilingGroupName: str,
    ) -> ClientUpdateProfilingGroupResponseTypeDef:
        """
        [Client.update_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.update_profiling_group)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError

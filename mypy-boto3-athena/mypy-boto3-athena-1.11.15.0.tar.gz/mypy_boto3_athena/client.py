"""
Main interface for athena service client

Usage::

    import boto3
    from mypy_boto3.athena import AthenaClient

    session = boto3.Session()

    client: AthenaClient = boto3.client("athena")
    session_client: AthenaClient = session.client("athena")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_athena.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_athena.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_athena.type_defs import (
    ClientBatchGetNamedQueryResponseTypeDef,
    ClientBatchGetQueryExecutionResponseTypeDef,
    ClientCreateNamedQueryResponseTypeDef,
    ClientCreateWorkGroupConfigurationTypeDef,
    ClientCreateWorkGroupTagsTypeDef,
    ClientGetNamedQueryResponseTypeDef,
    ClientGetQueryExecutionResponseTypeDef,
    ClientGetQueryResultsResponseTypeDef,
    ClientGetWorkGroupResponseTypeDef,
    ClientListNamedQueriesResponseTypeDef,
    ClientListQueryExecutionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListWorkGroupsResponseTypeDef,
    ClientStartQueryExecutionQueryExecutionContextTypeDef,
    ClientStartQueryExecutionResponseTypeDef,
    ClientStartQueryExecutionResultConfigurationTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateWorkGroupConfigurationUpdatesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AthenaClient",)


class AthenaClient:
    """
    [Athena.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_get_named_query(
        self, NamedQueryIds: List[str]
    ) -> ClientBatchGetNamedQueryResponseTypeDef:
        """
        [Client.batch_get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.batch_get_named_query)
        """

    def batch_get_query_execution(
        self, QueryExecutionIds: List[str]
    ) -> ClientBatchGetQueryExecutionResponseTypeDef:
        """
        [Client.batch_get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.batch_get_query_execution)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.can_paginate)
        """

    def create_named_query(
        self,
        Name: str,
        Database: str,
        QueryString: str,
        Description: str = None,
        ClientRequestToken: str = None,
        WorkGroup: str = None,
    ) -> ClientCreateNamedQueryResponseTypeDef:
        """
        [Client.create_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.create_named_query)
        """

    def create_work_group(
        self,
        Name: str,
        Configuration: ClientCreateWorkGroupConfigurationTypeDef = None,
        Description: str = None,
        Tags: List[ClientCreateWorkGroupTagsTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.create_work_group)
        """

    def delete_named_query(self, NamedQueryId: str) -> Dict[str, Any]:
        """
        [Client.delete_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.delete_named_query)
        """

    def delete_work_group(
        self, WorkGroup: str, RecursiveDeleteOption: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.delete_work_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.generate_presigned_url)
        """

    def get_named_query(self, NamedQueryId: str) -> ClientGetNamedQueryResponseTypeDef:
        """
        [Client.get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.get_named_query)
        """

    def get_query_execution(self, QueryExecutionId: str) -> ClientGetQueryExecutionResponseTypeDef:
        """
        [Client.get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.get_query_execution)
        """

    def get_query_results(
        self, QueryExecutionId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetQueryResultsResponseTypeDef:
        """
        [Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.get_query_results)
        """

    def get_work_group(self, WorkGroup: str) -> ClientGetWorkGroupResponseTypeDef:
        """
        [Client.get_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.get_work_group)
        """

    def list_named_queries(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ClientListNamedQueriesResponseTypeDef:
        """
        [Client.list_named_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.list_named_queries)
        """

    def list_query_executions(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ClientListQueryExecutionsResponseTypeDef:
        """
        [Client.list_query_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.list_query_executions)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.list_tags_for_resource)
        """

    def list_work_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListWorkGroupsResponseTypeDef:
        """
        [Client.list_work_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.list_work_groups)
        """

    def start_query_execution(
        self,
        QueryString: str,
        ClientRequestToken: str = None,
        QueryExecutionContext: ClientStartQueryExecutionQueryExecutionContextTypeDef = None,
        ResultConfiguration: ClientStartQueryExecutionResultConfigurationTypeDef = None,
        WorkGroup: str = None,
    ) -> ClientStartQueryExecutionResponseTypeDef:
        """
        [Client.start_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.start_query_execution)
        """

    def stop_query_execution(self, QueryExecutionId: str) -> Dict[str, Any]:
        """
        [Client.stop_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.stop_query_execution)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.untag_resource)
        """

    def update_work_group(
        self,
        WorkGroup: str,
        Description: str = None,
        ConfigurationUpdates: ClientUpdateWorkGroupConfigurationUpdatesTypeDef = None,
        State: Literal["ENABLED", "DISABLED"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Client.update_work_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_query_results"]
    ) -> "paginator_scope.GetQueryResultsPaginator":
        """
        [Paginator.GetQueryResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.GetQueryResults)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_named_queries"]
    ) -> "paginator_scope.ListNamedQueriesPaginator":
        """
        [Paginator.ListNamedQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.ListNamedQueries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_query_executions"]
    ) -> "paginator_scope.ListQueryExecutionsPaginator":
        """
        [Paginator.ListQueryExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError

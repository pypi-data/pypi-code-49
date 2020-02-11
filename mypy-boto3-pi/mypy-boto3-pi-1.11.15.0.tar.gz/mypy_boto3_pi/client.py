"""
Main interface for pi service client

Usage::

    import boto3
    from mypy_boto3.pi import PIClient

    session = boto3.Session()

    client: PIClient = boto3.client("pi")
    session_client: PIClient = session.client("pi")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_pi.client as client_scope
else:
    client_scope = object
from mypy_boto3_pi.type_defs import (
    ClientDescribeDimensionKeysGroupByTypeDef,
    ClientDescribeDimensionKeysPartitionByTypeDef,
    ClientDescribeDimensionKeysResponseTypeDef,
    ClientGetResourceMetricsMetricQueriesTypeDef,
    ClientGetResourceMetricsResponseTypeDef,
)


__all__ = ("PIClient",)


class PIClient:
    """
    [PI.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pi.html#PI.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pi.html#PI.Client.can_paginate)
        """

    def describe_dimension_keys(
        self,
        ServiceType: str,
        Identifier: str,
        StartTime: datetime,
        EndTime: datetime,
        Metric: str,
        GroupBy: ClientDescribeDimensionKeysGroupByTypeDef,
        PeriodInSeconds: int = None,
        PartitionBy: ClientDescribeDimensionKeysPartitionByTypeDef = None,
        Filter: Dict[str, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeDimensionKeysResponseTypeDef:
        """
        [Client.describe_dimension_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pi.html#PI.Client.describe_dimension_keys)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pi.html#PI.Client.generate_presigned_url)
        """

    def get_resource_metrics(
        self,
        ServiceType: str,
        Identifier: str,
        MetricQueries: List[ClientGetResourceMetricsMetricQueriesTypeDef],
        StartTime: datetime,
        EndTime: datetime,
        PeriodInSeconds: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetResourceMetricsResponseTypeDef:
        """
        [Client.get_resource_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pi.html#PI.Client.get_resource_metrics)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceError: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError

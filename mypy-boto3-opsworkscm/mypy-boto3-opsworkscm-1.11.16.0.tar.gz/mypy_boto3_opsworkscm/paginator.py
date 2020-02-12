"""
Main interface for opsworkscm service client paginators.

Usage::

    import boto3
    from mypy_boto3.opsworkscm import (
        DescribeBackupsPaginator,
        DescribeEventsPaginator,
        DescribeServersPaginator,
    )

    client: OpsWorksCMClient = boto3.client("opsworkscm")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_servers_paginator: DescribeServersPaginator = client.get_paginator("describe_servers")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_opsworkscm.type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeServersResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeBackupsPaginator", "DescribeEventsPaginator", "DescribeServersPaginator")


class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)
    """

    def paginate(
        self,
        BackupId: str = None,
        ServerName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeBackupsResponseTypeDef, None, None]:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)
    """

    def paginate(
        self, ServerName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeEventsResponseTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents.paginate)
        """


class DescribeServersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)
    """

    def paginate(
        self, ServerName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeServersResponseTypeDef, None, None]:
        """
        [DescribeServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers.paginate)
        """

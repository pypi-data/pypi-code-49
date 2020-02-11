"""
Main interface for docdb service client paginators.

Usage::

    import boto3
    from mypy_boto3.docdb import (
        DescribeDBClustersPaginator,
        DescribeDBEngineVersionsPaginator,
        DescribeDBInstancesPaginator,
        DescribeDBSubnetGroupsPaginator,
        DescribeEventsPaginator,
        DescribeOrderableDBInstanceOptionsPaginator,
    )

    client: DocDBClient = boto3.client("docdb")

    describe_db_clusters_paginator: DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
    describe_db_engine_versions_paginator: DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
    describe_db_instances_paginator: DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
    describe_db_subnet_groups_paginator: DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_orderable_db_instance_options_paginator: DescribeOrderableDBInstanceOptionsPaginator = client.get_paginator("describe_orderable_db_instance_options")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_docdb.type_defs import (
    DBClusterMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    EventsMessageTypeDef,
    FilterTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
)


class DescribeDBClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters)
    """

    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterMessageTypeDef, None, None]:
        """
        [DescribeDBClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters.paginate)
        """


class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions)
    """

    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBEngineVersionMessageTypeDef, None, None]:
        """
        [DescribeDBEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions.paginate)
        """


class DescribeDBInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances)
    """

    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBInstanceMessageTypeDef, None, None]:
        """
        [DescribeDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances.paginate)
        """


class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups)
    """

    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBSubnetGroupMessageTypeDef, None, None]:
        """
        [DescribeDBSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[EventsMessageTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions)
    """

    def paginate(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[OrderableDBInstanceOptionsMessageTypeDef, None, None]:
        """
        [DescribeOrderableDBInstanceOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        """

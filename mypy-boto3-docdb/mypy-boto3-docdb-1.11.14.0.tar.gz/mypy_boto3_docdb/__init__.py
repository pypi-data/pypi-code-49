"""
Main interface for docdb service.

Usage::

    import boto3
    from mypy_boto3.docdb import (
        Client,
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
        DescribeDBClustersPaginator,
        DescribeDBEngineVersionsPaginator,
        DescribeDBInstancesPaginator,
        DescribeDBSubnetGroupsPaginator,
        DescribeEventsPaginator,
        DescribeOrderableDBInstanceOptionsPaginator,
        DocDBClient,
        )

    session = boto3.Session()

    client: DocDBClient = boto3.client("docdb")
    session_client: DocDBClient = session.client("docdb")

    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")

    describe_db_clusters_paginator: DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
    describe_db_engine_versions_paginator: DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
    describe_db_instances_paginator: DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
    describe_db_subnet_groups_paginator: DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_orderable_db_instance_options_paginator: DescribeOrderableDBInstanceOptionsPaginator = client.get_paginator("describe_orderable_db_instance_options")
"""
from mypy_boto3_docdb.client import DocDBClient, DocDBClient as Client
from mypy_boto3_docdb.paginator import (
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEventsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
)
from mypy_boto3_docdb.waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter


__all__ = (
    "Client",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DocDBClient",
)

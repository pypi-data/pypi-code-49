"""
Main interface for elasticbeanstalk service.

Usage::

    import boto3
    from mypy_boto3.elasticbeanstalk import (
        Client,
        DescribeApplicationVersionsPaginator,
        DescribeEnvironmentManagedActionHistoryPaginator,
        DescribeEnvironmentsPaginator,
        DescribeEventsPaginator,
        ElasticBeanstalkClient,
        ListPlatformVersionsPaginator,
        )

    session = boto3.Session()

    client: ElasticBeanstalkClient = boto3.client("elasticbeanstalk")
    session_client: ElasticBeanstalkClient = session.client("elasticbeanstalk")

    describe_application_versions_paginator: DescribeApplicationVersionsPaginator = client.get_paginator("describe_application_versions")
    describe_environment_managed_action_history_paginator: DescribeEnvironmentManagedActionHistoryPaginator = client.get_paginator("describe_environment_managed_action_history")
    describe_environments_paginator: DescribeEnvironmentsPaginator = client.get_paginator("describe_environments")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    list_platform_versions_paginator: ListPlatformVersionsPaginator = client.get_paginator("list_platform_versions")
"""
from mypy_boto3_elasticbeanstalk.client import (
    ElasticBeanstalkClient,
    ElasticBeanstalkClient as Client,
)
from mypy_boto3_elasticbeanstalk.paginator import (
    DescribeApplicationVersionsPaginator,
    DescribeEnvironmentManagedActionHistoryPaginator,
    DescribeEnvironmentsPaginator,
    DescribeEventsPaginator,
    ListPlatformVersionsPaginator,
)


__all__ = (
    "Client",
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ElasticBeanstalkClient",
    "ListPlatformVersionsPaginator",
)

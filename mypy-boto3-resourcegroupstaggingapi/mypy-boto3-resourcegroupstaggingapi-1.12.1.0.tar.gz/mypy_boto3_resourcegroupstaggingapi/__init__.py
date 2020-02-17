"""
Main interface for resourcegroupstaggingapi service.

Usage::

    import boto3
    from mypy_boto3.resourcegroupstaggingapi import (
        Client,
        GetComplianceSummaryPaginator,
        GetResourcesPaginator,
        GetTagKeysPaginator,
        GetTagValuesPaginator,
        ResourceGroupsTaggingAPIClient,
        )

    session = boto3.Session()

    client: ResourceGroupsTaggingAPIClient = boto3.client("resourcegroupstaggingapi")
    session_client: ResourceGroupsTaggingAPIClient = session.client("resourcegroupstaggingapi")

    get_compliance_summary_paginator: GetComplianceSummaryPaginator = client.get_paginator("get_compliance_summary")
    get_resources_paginator: GetResourcesPaginator = client.get_paginator("get_resources")
    get_tag_keys_paginator: GetTagKeysPaginator = client.get_paginator("get_tag_keys")
    get_tag_values_paginator: GetTagValuesPaginator = client.get_paginator("get_tag_values")
"""
from mypy_boto3_resourcegroupstaggingapi.client import (
    ResourceGroupsTaggingAPIClient,
    ResourceGroupsTaggingAPIClient as Client,
)
from mypy_boto3_resourcegroupstaggingapi.paginator import (
    GetComplianceSummaryPaginator,
    GetResourcesPaginator,
    GetTagKeysPaginator,
    GetTagValuesPaginator,
)


__all__ = (
    "Client",
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
    "ResourceGroupsTaggingAPIClient",
)

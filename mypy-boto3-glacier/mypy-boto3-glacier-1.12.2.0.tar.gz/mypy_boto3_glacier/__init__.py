"""
Main interface for glacier service.

Usage::

    import boto3
    from mypy_boto3.glacier import (
        Client,
        GlacierClient,
        GlacierServiceResource,
        ListJobsPaginator,
        ListMultipartUploadsPaginator,
        ListPartsPaginator,
        ListVaultsPaginator,
        ServiceResource,
        VaultExistsWaiter,
        VaultNotExistsWaiter,
        )

    session = boto3.Session()

    client: GlacierClient = boto3.client("glacier")
    session_client: GlacierClient = session.client("glacier")

    resource: GlacierServiceResource = boto3.resource("glacier")
    session_resource: GlacierServiceResource = session.resource("glacier")

    vault_exists_waiter: VaultExistsWaiter = client.get_waiter("vault_exists")
    vault_not_exists_waiter: VaultNotExistsWaiter = client.get_waiter("vault_not_exists")

    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_multipart_uploads_paginator: ListMultipartUploadsPaginator = client.get_paginator("list_multipart_uploads")
    list_parts_paginator: ListPartsPaginator = client.get_paginator("list_parts")
    list_vaults_paginator: ListVaultsPaginator = client.get_paginator("list_vaults")
"""
from mypy_boto3_glacier.client import GlacierClient, GlacierClient as Client
from mypy_boto3_glacier.paginator import (
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from mypy_boto3_glacier.service_resource import (
    GlacierServiceResource,
    GlacierServiceResource as ServiceResource,
)
from mypy_boto3_glacier.waiter import VaultExistsWaiter, VaultNotExistsWaiter


__all__ = (
    "Client",
    "GlacierClient",
    "GlacierServiceResource",
    "ListJobsPaginator",
    "ListMultipartUploadsPaginator",
    "ListPartsPaginator",
    "ListVaultsPaginator",
    "ServiceResource",
    "VaultExistsWaiter",
    "VaultNotExistsWaiter",
)

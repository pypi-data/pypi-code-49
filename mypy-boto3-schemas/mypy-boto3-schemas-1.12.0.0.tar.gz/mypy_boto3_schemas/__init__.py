"""
Main interface for schemas service.

Usage::

    import boto3
    from mypy_boto3.schemas import (
        Client,
        CodeBindingExistsWaiter,
        ListDiscoverersPaginator,
        ListRegistriesPaginator,
        ListSchemaVersionsPaginator,
        ListSchemasPaginator,
        SchemasClient,
        SearchSchemasPaginator,
        )

    session = boto3.Session()

    client: SchemasClient = boto3.client("schemas")
    session_client: SchemasClient = session.client("schemas")

    code_binding_exists_waiter: CodeBindingExistsWaiter = client.get_waiter("code_binding_exists")

    list_discoverers_paginator: ListDiscoverersPaginator = client.get_paginator("list_discoverers")
    list_registries_paginator: ListRegistriesPaginator = client.get_paginator("list_registries")
    list_schema_versions_paginator: ListSchemaVersionsPaginator = client.get_paginator("list_schema_versions")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    search_schemas_paginator: SearchSchemasPaginator = client.get_paginator("search_schemas")
"""
from mypy_boto3_schemas.client import SchemasClient as Client, SchemasClient
from mypy_boto3_schemas.paginator import (
    ListDiscoverersPaginator,
    ListRegistriesPaginator,
    ListSchemaVersionsPaginator,
    ListSchemasPaginator,
    SearchSchemasPaginator,
)
from mypy_boto3_schemas.waiter import CodeBindingExistsWaiter


__all__ = (
    "Client",
    "CodeBindingExistsWaiter",
    "ListDiscoverersPaginator",
    "ListRegistriesPaginator",
    "ListSchemaVersionsPaginator",
    "ListSchemasPaginator",
    "SchemasClient",
    "SearchSchemasPaginator",
)

"""
Main interface for codebuild service.

Usage::

    import boto3
    from mypy_boto3.codebuild import (
        Client,
        CodeBuildClient,
        ListBuildsForProjectPaginator,
        ListBuildsPaginator,
        ListProjectsPaginator,
        )

    session = boto3.Session()

    client: CodeBuildClient = boto3.client("codebuild")
    session_client: CodeBuildClient = session.client("codebuild")

    list_builds_paginator: ListBuildsPaginator = client.get_paginator("list_builds")
    list_builds_for_project_paginator: ListBuildsForProjectPaginator = client.get_paginator("list_builds_for_project")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
"""
from mypy_boto3_codebuild.client import CodeBuildClient as Client, CodeBuildClient
from mypy_boto3_codebuild.paginator import (
    ListBuildsForProjectPaginator,
    ListBuildsPaginator,
    ListProjectsPaginator,
)


__all__ = (
    "Client",
    "CodeBuildClient",
    "ListBuildsForProjectPaginator",
    "ListBuildsPaginator",
    "ListProjectsPaginator",
)

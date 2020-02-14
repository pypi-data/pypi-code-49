"""
Main interface for codedeploy service.

Usage::

    import boto3
    from mypy_boto3.codedeploy import (
        Client,
        CodeDeployClient,
        DeploymentSuccessfulWaiter,
        ListApplicationRevisionsPaginator,
        ListApplicationsPaginator,
        ListDeploymentConfigsPaginator,
        ListDeploymentGroupsPaginator,
        ListDeploymentInstancesPaginator,
        ListDeploymentTargetsPaginator,
        ListDeploymentsPaginator,
        ListGitHubAccountTokenNamesPaginator,
        ListOnPremisesInstancesPaginator,
        )

    session = boto3.Session()

    client: CodeDeployClient = boto3.client("codedeploy")
    session_client: CodeDeployClient = session.client("codedeploy")

    deployment_successful_waiter: DeploymentSuccessfulWaiter = client.get_waiter("deployment_successful")

    list_application_revisions_paginator: ListApplicationRevisionsPaginator = client.get_paginator("list_application_revisions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_deployment_configs_paginator: ListDeploymentConfigsPaginator = client.get_paginator("list_deployment_configs")
    list_deployment_groups_paginator: ListDeploymentGroupsPaginator = client.get_paginator("list_deployment_groups")
    list_deployment_instances_paginator: ListDeploymentInstancesPaginator = client.get_paginator("list_deployment_instances")
    list_deployment_targets_paginator: ListDeploymentTargetsPaginator = client.get_paginator("list_deployment_targets")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_git_hub_account_token_names_paginator: ListGitHubAccountTokenNamesPaginator = client.get_paginator("list_git_hub_account_token_names")
    list_on_premises_instances_paginator: ListOnPremisesInstancesPaginator = client.get_paginator("list_on_premises_instances")
"""
from mypy_boto3_codedeploy.client import CodeDeployClient, CodeDeployClient as Client
from mypy_boto3_codedeploy.paginator import (
    ListApplicationRevisionsPaginator,
    ListApplicationsPaginator,
    ListDeploymentConfigsPaginator,
    ListDeploymentGroupsPaginator,
    ListDeploymentInstancesPaginator,
    ListDeploymentTargetsPaginator,
    ListDeploymentsPaginator,
    ListGitHubAccountTokenNamesPaginator,
    ListOnPremisesInstancesPaginator,
)
from mypy_boto3_codedeploy.waiter import DeploymentSuccessfulWaiter


__all__ = (
    "Client",
    "CodeDeployClient",
    "DeploymentSuccessfulWaiter",
    "ListApplicationRevisionsPaginator",
    "ListApplicationsPaginator",
    "ListDeploymentConfigsPaginator",
    "ListDeploymentGroupsPaginator",
    "ListDeploymentInstancesPaginator",
    "ListDeploymentTargetsPaginator",
    "ListDeploymentsPaginator",
    "ListGitHubAccountTokenNamesPaginator",
    "ListOnPremisesInstancesPaginator",
)

"""
Main interface for codestar service client

Usage::

    import boto3
    from mypy_boto3.codestar import CodeStarClient

    session = boto3.Session()

    client: CodeStarClient = boto3.client("codestar")
    session_client: CodeStarClient = session.client("codestar")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codestar.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codestar.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_codestar.type_defs import (
    ClientAssociateTeamMemberResponseTypeDef,
    ClientCreateProjectResponseTypeDef,
    ClientCreateProjectSourceCodeTypeDef,
    ClientCreateProjectToolchainTypeDef,
    ClientCreateUserProfileResponseTypeDef,
    ClientDeleteProjectResponseTypeDef,
    ClientDeleteUserProfileResponseTypeDef,
    ClientDescribeProjectResponseTypeDef,
    ClientDescribeUserProfileResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientListTagsForProjectResponseTypeDef,
    ClientListTeamMembersResponseTypeDef,
    ClientListUserProfilesResponseTypeDef,
    ClientTagProjectResponseTypeDef,
    ClientUpdateTeamMemberResponseTypeDef,
    ClientUpdateUserProfileResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeStarClient",)


class CodeStarClient:
    """
    [CodeStar.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: str,
        clientRequestToken: str = None,
        remoteAccessAllowed: bool = None,
    ) -> ClientAssociateTeamMemberResponseTypeDef:
        """
        [Client.associate_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.associate_team_member)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.can_paginate)
        """

    def create_project(
        self,
        name: str,
        id: str,
        description: str = None,
        clientRequestToken: str = None,
        sourceCode: List[ClientCreateProjectSourceCodeTypeDef] = None,
        toolchain: ClientCreateProjectToolchainTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.create_project)
        """

    def create_user_profile(
        self, userArn: str, displayName: str, emailAddress: str, sshPublicKey: str = None
    ) -> ClientCreateUserProfileResponseTypeDef:
        """
        [Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.create_user_profile)
        """

    def delete_project(
        self, id: str, clientRequestToken: str = None, deleteStack: bool = None
    ) -> ClientDeleteProjectResponseTypeDef:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.delete_project)
        """

    def delete_user_profile(self, userArn: str) -> ClientDeleteUserProfileResponseTypeDef:
        """
        [Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.delete_user_profile)
        """

    def describe_project(self, id: str) -> ClientDescribeProjectResponseTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.describe_project)
        """

    def describe_user_profile(self, userArn: str) -> ClientDescribeUserProfileResponseTypeDef:
        """
        [Client.describe_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.describe_user_profile)
        """

    def disassociate_team_member(self, projectId: str, userArn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.disassociate_team_member)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.generate_presigned_url)
        """

    def list_projects(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.list_projects)
        """

    def list_resources(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListResourcesResponseTypeDef:
        """
        [Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.list_resources)
        """

    def list_tags_for_project(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListTagsForProjectResponseTypeDef:
        """
        [Client.list_tags_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.list_tags_for_project)
        """

    def list_team_members(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListTeamMembersResponseTypeDef:
        """
        [Client.list_team_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.list_team_members)
        """

    def list_user_profiles(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListUserProfilesResponseTypeDef:
        """
        [Client.list_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.list_user_profiles)
        """

    def tag_project(self, id: str, tags: Dict[str, str]) -> ClientTagProjectResponseTypeDef:
        """
        [Client.tag_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.tag_project)
        """

    def untag_project(self, id: str, tags: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.untag_project)
        """

    def update_project(self, id: str, name: str = None, description: str = None) -> Dict[str, Any]:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.update_project)
        """

    def update_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: str = None,
        remoteAccessAllowed: bool = None,
    ) -> ClientUpdateTeamMemberResponseTypeDef:
        """
        [Client.update_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.update_team_member)
        """

    def update_user_profile(
        self,
        userArn: str,
        displayName: str = None,
        emailAddress: str = None,
        sshPublicKey: str = None,
    ) -> ClientUpdateUserProfileResponseTypeDef:
        """
        [Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Client.update_user_profile)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> "paginator_scope.ListProjectsPaginator":
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Paginator.ListProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resources"]
    ) -> "paginator_scope.ListResourcesPaginator":
        """
        [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Paginator.ListResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_team_members"]
    ) -> "paginator_scope.ListTeamMembersPaginator":
        """
        [Paginator.ListTeamMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> "paginator_scope.ListUserProfilesPaginator":
        """
        [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidServiceRoleException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ProjectAlreadyExistsException: Boto3ClientError
    ProjectConfigurationException: Boto3ClientError
    ProjectCreationFailedException: Boto3ClientError
    ProjectNotFoundException: Boto3ClientError
    TeamMemberAlreadyAssociatedException: Boto3ClientError
    TeamMemberNotFoundException: Boto3ClientError
    UserProfileAlreadyExistsException: Boto3ClientError
    UserProfileNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError

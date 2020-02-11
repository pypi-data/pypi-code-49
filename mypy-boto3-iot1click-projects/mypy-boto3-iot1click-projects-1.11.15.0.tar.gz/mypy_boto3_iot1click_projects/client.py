"""
Main interface for iot1click-projects service client

Usage::

    import boto3
    from mypy_boto3.iot1click_projects import IoT1ClickProjectsClient

    session = boto3.Session()

    client: IoT1ClickProjectsClient = boto3.client("iot1click-projects")
    session_client: IoT1ClickProjectsClient = session.client("iot1click-projects")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iot1click_projects.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iot1click_projects.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_iot1click_projects.type_defs import (
    ClientCreateProjectPlacementTemplateTypeDef,
    ClientDescribePlacementResponseTypeDef,
    ClientDescribeProjectResponseTypeDef,
    ClientGetDevicesInPlacementResponseTypeDef,
    ClientListPlacementsResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateProjectPlacementTemplateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoT1ClickProjectsClient",)


class IoT1ClickProjectsClient:
    """
    [IoT1ClickProjects.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_device_with_placement(
        self, projectName: str, placementName: str, deviceId: str, deviceTemplateName: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_device_with_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.associate_device_with_placement)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.can_paginate)
        """

    def create_placement(
        self, placementName: str, projectName: str, attributes: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_placement)
        """

    def create_project(
        self,
        projectName: str,
        description: str = None,
        placementTemplate: ClientCreateProjectPlacementTemplateTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_project)
        """

    def delete_placement(self, placementName: str, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_placement)
        """

    def delete_project(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_project)
        """

    def describe_placement(
        self, placementName: str, projectName: str
    ) -> ClientDescribePlacementResponseTypeDef:
        """
        [Client.describe_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_placement)
        """

    def describe_project(self, projectName: str) -> ClientDescribeProjectResponseTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_project)
        """

    def disassociate_device_from_placement(
        self, projectName: str, placementName: str, deviceTemplateName: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_device_from_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.disassociate_device_from_placement)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.generate_presigned_url)
        """

    def get_devices_in_placement(
        self, projectName: str, placementName: str
    ) -> ClientGetDevicesInPlacementResponseTypeDef:
        """
        [Client.get_devices_in_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.get_devices_in_placement)
        """

    def list_placements(
        self, projectName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListPlacementsResponseTypeDef:
        """
        [Client.list_placements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_placements)
        """

    def list_projects(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_projects)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.untag_resource)
        """

    def update_placement(
        self, placementName: str, projectName: str, attributes: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Client.update_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_placement)
        """

    def update_project(
        self,
        projectName: str,
        description: str = None,
        placementTemplate: ClientUpdateProjectPlacementTemplateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_project)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_placements"]
    ) -> "paginator_scope.ListPlacementsPaginator":
        """
        [Paginator.ListPlacements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> "paginator_scope.ListProjectsPaginator":
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError

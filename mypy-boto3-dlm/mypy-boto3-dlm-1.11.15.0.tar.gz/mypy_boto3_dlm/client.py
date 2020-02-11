"""
Main interface for dlm service client

Usage::

    import boto3
    from mypy_boto3.dlm import DLMClient

    session = boto3.Session()

    client: DLMClient = boto3.client("dlm")
    session_client: DLMClient = session.client("dlm")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dlm.client as client_scope
else:
    client_scope = object
from mypy_boto3_dlm.type_defs import (
    ClientCreateLifecyclePolicyPolicyDetailsTypeDef,
    ClientCreateLifecyclePolicyResponseTypeDef,
    ClientGetLifecyclePoliciesResponseTypeDef,
    ClientGetLifecyclePolicyResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateLifecyclePolicyPolicyDetailsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DLMClient",)


class DLMClient:
    """
    [DLM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.can_paginate)
        """

    def create_lifecycle_policy(
        self,
        ExecutionRoleArn: str,
        Description: str,
        State: Literal["ENABLED", "DISABLED"],
        PolicyDetails: ClientCreateLifecyclePolicyPolicyDetailsTypeDef,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateLifecyclePolicyResponseTypeDef:
        """
        [Client.create_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.create_lifecycle_policy)
        """

    def delete_lifecycle_policy(self, PolicyId: str) -> Dict[str, Any]:
        """
        [Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.delete_lifecycle_policy)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.generate_presigned_url)
        """

    def get_lifecycle_policies(
        self,
        PolicyIds: List[str] = None,
        State: Literal["ENABLED", "DISABLED", "ERROR"] = None,
        ResourceTypes: List[Literal["VOLUME", "INSTANCE"]] = None,
        TargetTags: List[str] = None,
        TagsToAdd: List[str] = None,
    ) -> ClientGetLifecyclePoliciesResponseTypeDef:
        """
        [Client.get_lifecycle_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.get_lifecycle_policies)
        """

    def get_lifecycle_policy(self, PolicyId: str) -> ClientGetLifecyclePolicyResponseTypeDef:
        """
        [Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.get_lifecycle_policy)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.untag_resource)
        """

    def update_lifecycle_policy(
        self,
        PolicyId: str,
        ExecutionRoleArn: str = None,
        State: Literal["ENABLED", "DISABLED"] = None,
        Description: str = None,
        PolicyDetails: ClientUpdateLifecyclePolicyPolicyDetailsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dlm.html#DLM.Client.update_lifecycle_policy)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError

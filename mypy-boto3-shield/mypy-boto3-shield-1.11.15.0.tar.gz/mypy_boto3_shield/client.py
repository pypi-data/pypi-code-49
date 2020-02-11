"""
Main interface for shield service client

Usage::

    import boto3
    from mypy_boto3.shield import ShieldClient

    session = boto3.Session()

    client: ShieldClient = boto3.client("shield")
    session_client: ShieldClient = session.client("shield")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_shield.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_shield.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_shield.type_defs import (
    ClientCreateProtectionResponseTypeDef,
    ClientDescribeAttackResponseTypeDef,
    ClientDescribeDrtAccessResponseTypeDef,
    ClientDescribeEmergencyContactSettingsResponseTypeDef,
    ClientDescribeProtectionResponseTypeDef,
    ClientDescribeSubscriptionResponseTypeDef,
    ClientGetSubscriptionStateResponseTypeDef,
    ClientListAttacksEndTimeTypeDef,
    ClientListAttacksResponseTypeDef,
    ClientListAttacksStartTimeTypeDef,
    ClientListProtectionsResponseTypeDef,
    ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ShieldClient",)


class ShieldClient:
    """
    [Shield.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        """
        [Client.associate_drt_log_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.associate_drt_log_bucket)
        """

    def associate_drt_role(self, RoleArn: str) -> Dict[str, Any]:
        """
        [Client.associate_drt_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.associate_drt_role)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.can_paginate)
        """

    def create_protection(
        self, Name: str, ResourceArn: str
    ) -> ClientCreateProtectionResponseTypeDef:
        """
        [Client.create_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.create_protection)
        """

    def create_subscription(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.create_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.create_subscription)
        """

    def delete_protection(self, ProtectionId: str) -> Dict[str, Any]:
        """
        [Client.delete_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.delete_protection)
        """

    def delete_subscription(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.delete_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.delete_subscription)
        """

    def describe_attack(self, AttackId: str) -> ClientDescribeAttackResponseTypeDef:
        """
        [Client.describe_attack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.describe_attack)
        """

    def describe_drt_access(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeDrtAccessResponseTypeDef:
        """
        [Client.describe_drt_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.describe_drt_access)
        """

    def describe_emergency_contact_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeEmergencyContactSettingsResponseTypeDef:
        """
        [Client.describe_emergency_contact_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.describe_emergency_contact_settings)
        """

    def describe_protection(
        self, ProtectionId: str = None, ResourceArn: str = None
    ) -> ClientDescribeProtectionResponseTypeDef:
        """
        [Client.describe_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.describe_protection)
        """

    def describe_subscription(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeSubscriptionResponseTypeDef:
        """
        [Client.describe_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.describe_subscription)
        """

    def disassociate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        """
        [Client.disassociate_drt_log_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.disassociate_drt_log_bucket)
        """

    def disassociate_drt_role(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.disassociate_drt_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.disassociate_drt_role)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.generate_presigned_url)
        """

    def get_subscription_state(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetSubscriptionStateResponseTypeDef:
        """
        [Client.get_subscription_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.get_subscription_state)
        """

    def list_attacks(
        self,
        ResourceArns: List[str] = None,
        StartTime: ClientListAttacksStartTimeTypeDef = None,
        EndTime: ClientListAttacksEndTimeTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListAttacksResponseTypeDef:
        """
        [Client.list_attacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.list_attacks)
        """

    def list_protections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListProtectionsResponseTypeDef:
        """
        [Client.list_protections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.list_protections)
        """

    def update_emergency_contact_settings(
        self,
        EmergencyContactList: List[
            ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_emergency_contact_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.update_emergency_contact_settings)
        """

    def update_subscription(
        self, AutoRenew: Literal["ENABLED", "DISABLED"] = None
    ) -> Dict[str, Any]:
        """
        [Client.update_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Client.update_subscription)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attacks"]
    ) -> "paginator_scope.ListAttacksPaginator":
        """
        [Paginator.ListAttacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Paginator.ListAttacks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protections"]
    ) -> "paginator_scope.ListProtectionsPaginator":
        """
        [Paginator.ListProtections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/shield.html#Shield.Paginator.ListProtections)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AccessDeniedForDependencyException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidPaginationTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidResourceException: Boto3ClientError
    LimitsExceededException: Boto3ClientError
    LockedSubscriptionException: Boto3ClientError
    NoAssociatedRoleException: Boto3ClientError
    OptimisticLockException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError

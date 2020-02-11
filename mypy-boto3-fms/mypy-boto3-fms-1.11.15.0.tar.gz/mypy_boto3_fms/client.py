"""
Main interface for fms service client

Usage::

    import boto3
    from mypy_boto3.fms import FMSClient

    session = boto3.Session()

    client: FMSClient = boto3.client("fms")
    session_client: FMSClient = session.client("fms")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_fms.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_fms.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_fms.type_defs import (
    ClientGetAdminAccountResponseTypeDef,
    ClientGetComplianceDetailResponseTypeDef,
    ClientGetNotificationChannelResponseTypeDef,
    ClientGetPolicyResponseTypeDef,
    ClientGetProtectionStatusResponseTypeDef,
    ClientListComplianceStatusResponseTypeDef,
    ClientListMemberAccountsResponseTypeDef,
    ClientListPoliciesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutPolicyPolicyTypeDef,
    ClientPutPolicyResponseTypeDef,
    ClientPutPolicyTagListTypeDef,
    ClientTagResourceTagListTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FMSClient",)


class FMSClient:
    """
    [FMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_admin_account(self, AdminAccount: str) -> None:
        """
        [Client.associate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.associate_admin_account)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.can_paginate)
        """

    def delete_notification_channel(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.delete_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.delete_notification_channel)
        """

    def delete_policy(self, PolicyId: str, DeleteAllPolicyResources: bool = None) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.delete_policy)
        """

    def disassociate_admin_account(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.disassociate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.disassociate_admin_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.generate_presigned_url)
        """

    def get_admin_account(self, *args: Any, **kwargs: Any) -> ClientGetAdminAccountResponseTypeDef:
        """
        [Client.get_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.get_admin_account)
        """

    def get_compliance_detail(
        self, PolicyId: str, MemberAccount: str
    ) -> ClientGetComplianceDetailResponseTypeDef:
        """
        [Client.get_compliance_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.get_compliance_detail)
        """

    def get_notification_channel(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetNotificationChannelResponseTypeDef:
        """
        [Client.get_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.get_notification_channel)
        """

    def get_policy(self, PolicyId: str) -> ClientGetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.get_policy)
        """

    def get_protection_status(
        self,
        PolicyId: str,
        MemberAccountId: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetProtectionStatusResponseTypeDef:
        """
        [Client.get_protection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.get_protection_status)
        """

    def list_compliance_status(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListComplianceStatusResponseTypeDef:
        """
        [Client.list_compliance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.list_compliance_status)
        """

    def list_member_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListMemberAccountsResponseTypeDef:
        """
        [Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.list_member_accounts)
        """

    def list_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.list_policies)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.list_tags_for_resource)
        """

    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str) -> None:
        """
        [Client.put_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.put_notification_channel)
        """

    def put_policy(
        self,
        Policy: ClientPutPolicyPolicyTypeDef,
        TagList: List[ClientPutPolicyTagListTypeDef] = None,
    ) -> ClientPutPolicyResponseTypeDef:
        """
        [Client.put_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.put_policy)
        """

    def tag_resource(
        self, ResourceArn: str, TagList: List[ClientTagResourceTagListTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_status"]
    ) -> "paginator_scope.ListComplianceStatusPaginator":
        """
        [Paginator.ListComplianceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> "paginator_scope.ListMemberAccountsPaginator":
        """
        [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> "paginator_scope.ListPoliciesPaginator":
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fms.html#FMS.Paginator.ListPolicies)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidTypeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError

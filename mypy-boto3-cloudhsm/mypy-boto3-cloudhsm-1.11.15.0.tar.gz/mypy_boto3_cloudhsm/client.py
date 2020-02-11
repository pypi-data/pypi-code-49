"""
Main interface for cloudhsm service client

Usage::

    import boto3
    from mypy_boto3.cloudhsm import CloudHSMClient

    session = boto3.Session()

    client: CloudHSMClient = boto3.client("cloudhsm")
    session_client: CloudHSMClient = session.client("cloudhsm")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudhsm.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudhsm.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_cloudhsm.type_defs import (
    ClientAddTagsToResourceResponseTypeDef,
    ClientAddTagsToResourceTagListTypeDef,
    ClientCreateHapgResponseTypeDef,
    ClientCreateHsmResponseTypeDef,
    ClientCreateLunaClientResponseTypeDef,
    ClientDeleteHapgResponseTypeDef,
    ClientDeleteHsmResponseTypeDef,
    ClientDeleteLunaClientResponseTypeDef,
    ClientDescribeHapgResponseTypeDef,
    ClientDescribeHsmResponseTypeDef,
    ClientDescribeLunaClientResponseTypeDef,
    ClientGetConfigResponseTypeDef,
    ClientListAvailableZonesResponseTypeDef,
    ClientListHapgsResponseTypeDef,
    ClientListHsmsResponseTypeDef,
    ClientListLunaClientsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyHapgResponseTypeDef,
    ClientModifyHsmResponseTypeDef,
    ClientModifyLunaClientResponseTypeDef,
    ClientRemoveTagsFromResourceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudHSMClient",)


class CloudHSMClient:
    """
    [CloudHSM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags_to_resource(
        self, ResourceArn: str, TagList: List[ClientAddTagsToResourceTagListTypeDef]
    ) -> ClientAddTagsToResourceResponseTypeDef:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.add_tags_to_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.can_paginate)
        """

    def create_hapg(self, Label: str) -> ClientCreateHapgResponseTypeDef:
        """
        [Client.create_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.create_hapg)
        """

    def create_hsm(
        self,
        SubnetId: str,
        SshKey: str,
        IamRoleArn: str,
        SubscriptionType: str,
        EniIp: str = None,
        ExternalId: str = None,
        ClientToken: str = None,
        SyslogIp: str = None,
    ) -> ClientCreateHsmResponseTypeDef:
        """
        [Client.create_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.create_hsm)
        """

    def create_luna_client(
        self, Certificate: str, Label: str = None
    ) -> ClientCreateLunaClientResponseTypeDef:
        """
        [Client.create_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.create_luna_client)
        """

    def delete_hapg(self, HapgArn: str) -> ClientDeleteHapgResponseTypeDef:
        """
        [Client.delete_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.delete_hapg)
        """

    def delete_hsm(self, HsmArn: str) -> ClientDeleteHsmResponseTypeDef:
        """
        [Client.delete_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.delete_hsm)
        """

    def delete_luna_client(self, ClientArn: str) -> ClientDeleteLunaClientResponseTypeDef:
        """
        [Client.delete_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.delete_luna_client)
        """

    def describe_hapg(self, HapgArn: str) -> ClientDescribeHapgResponseTypeDef:
        """
        [Client.describe_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.describe_hapg)
        """

    def describe_hsm(
        self, HsmArn: str = None, HsmSerialNumber: str = None
    ) -> ClientDescribeHsmResponseTypeDef:
        """
        [Client.describe_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.describe_hsm)
        """

    def describe_luna_client(
        self, ClientArn: str = None, CertificateFingerprint: str = None
    ) -> ClientDescribeLunaClientResponseTypeDef:
        """
        [Client.describe_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.describe_luna_client)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.generate_presigned_url)
        """

    def get_config(
        self, ClientArn: str, ClientVersion: Literal["5.1", "5.3"], HapgList: List[str]
    ) -> ClientGetConfigResponseTypeDef:
        """
        [Client.get_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.get_config)
        """

    def list_available_zones(
        self, *args: Any, **kwargs: Any
    ) -> ClientListAvailableZonesResponseTypeDef:
        """
        [Client.list_available_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.list_available_zones)
        """

    def list_hapgs(self, NextToken: str = None) -> ClientListHapgsResponseTypeDef:
        """
        [Client.list_hapgs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.list_hapgs)
        """

    def list_hsms(self, NextToken: str = None) -> ClientListHsmsResponseTypeDef:
        """
        [Client.list_hsms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.list_hsms)
        """

    def list_luna_clients(self, NextToken: str = None) -> ClientListLunaClientsResponseTypeDef:
        """
        [Client.list_luna_clients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.list_luna_clients)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.list_tags_for_resource)
        """

    def modify_hapg(
        self, HapgArn: str, Label: str = None, PartitionSerialList: List[str] = None
    ) -> ClientModifyHapgResponseTypeDef:
        """
        [Client.modify_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.modify_hapg)
        """

    def modify_hsm(
        self,
        HsmArn: str,
        SubnetId: str = None,
        EniIp: str = None,
        IamRoleArn: str = None,
        ExternalId: str = None,
        SyslogIp: str = None,
    ) -> ClientModifyHsmResponseTypeDef:
        """
        [Client.modify_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.modify_hsm)
        """

    def modify_luna_client(
        self, ClientArn: str, Certificate: str
    ) -> ClientModifyLunaClientResponseTypeDef:
        """
        [Client.modify_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.modify_luna_client)
        """

    def remove_tags_from_resource(
        self, ResourceArn: str, TagKeyList: List[str]
    ) -> ClientRemoveTagsFromResourceResponseTypeDef:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Client.remove_tags_from_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hapgs"]
    ) -> "paginator_scope.ListHapgsPaginator":
        """
        [Paginator.ListHapgs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hsms"]
    ) -> "paginator_scope.ListHsmsPaginator":
        """
        [Paginator.ListHsms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_luna_clients"]
    ) -> "paginator_scope.ListLunaClientsPaginator":
        """
        [Paginator.ListLunaClients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CloudHsmInternalException: Boto3ClientError
    CloudHsmServiceException: Boto3ClientError
    InvalidRequestException: Boto3ClientError

"""
Main interface for ec2-instance-connect service client

Usage::

    import boto3
    from mypy_boto3.ec2_instance_connect import EC2InstanceConnectClient

    session = boto3.Session()

    client: EC2InstanceConnectClient = boto3.client("ec2-instance-connect")
    session_client: EC2InstanceConnectClient = session.client("ec2-instance-connect")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ec2_instance_connect.client as client_scope
else:
    client_scope = object
from mypy_boto3_ec2_instance_connect.type_defs import ClientSendSshPublicKeyResponseTypeDef


__all__ = ("EC2InstanceConnectClient",)


class EC2InstanceConnectClient:
    """
    [EC2InstanceConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.generate_presigned_url)
        """

    def send_ssh_public_key(
        self, InstanceId: str, InstanceOSUser: str, SSHPublicKey: str, AvailabilityZone: str
    ) -> ClientSendSshPublicKeyResponseTypeDef:
        """
        [Client.send_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_ssh_public_key)
        """


class Exceptions:
    AuthException: Boto3ClientError
    ClientError: Boto3ClientError
    EC2InstanceNotFoundException: Boto3ClientError
    InvalidArgsException: Boto3ClientError
    ServiceException: Boto3ClientError
    ThrottlingException: Boto3ClientError

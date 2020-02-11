"""
Main interface for ec2-instance-connect service type definitions.

Usage::

    from mypy_boto3.ec2_instance_connect.type_defs import ClientSendSshPublicKeyResponseTypeDef

    data: ClientSendSshPublicKeyResponseTypeDef = {...}
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientSendSshPublicKeyResponseTypeDef",)

ClientSendSshPublicKeyResponseTypeDef = TypedDict(
    "ClientSendSshPublicKeyResponseTypeDef", {"RequestId": str, "Success": bool}, total=False
)

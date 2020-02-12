"""
Main interface for schemas service client waiters.

Usage::

    import boto3
    from mypy_boto3.schemas import (
        CodeBindingExistsWaiter,
    )

    client: SchemasClient = boto3.client("schemas")

    code_binding_exists_waiter: CodeBindingExistsWaiter = client.get_waiter("code_binding_exists")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_schemas.type_defs import WaiterConfigTypeDef


__all__ = ("CodeBindingExistsWaiter",)


class CodeBindingExistsWaiter(Boto3Waiter):
    """
    [Waiter.CodeBindingExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists)
    """

    def wait(
        self,
        Language: str,
        RegistryName: str,
        SchemaName: str,
        SchemaVersion: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CodeBindingExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists.wait)
        """

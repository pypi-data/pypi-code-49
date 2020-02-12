"""
Main interface for iotsecuretunneling service.

Usage::

    import boto3
    from mypy_boto3.iotsecuretunneling import (
        Client,
        IoTSecureTunnelingClient,
        )

    session = boto3.Session()

    client: IoTSecureTunnelingClient = boto3.client("iotsecuretunneling")
    session_client: IoTSecureTunnelingClient = session.client("iotsecuretunneling")
"""
from mypy_boto3_iotsecuretunneling.client import (
    IoTSecureTunnelingClient,
    IoTSecureTunnelingClient as Client,
)


__all__ = ("Client", "IoTSecureTunnelingClient")

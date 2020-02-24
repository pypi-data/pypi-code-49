"""
Main interface for ec2-instance-connect service.

Usage::

    import boto3
    from mypy_boto3.ec2_instance_connect import (
        Client,
        EC2InstanceConnectClient,
        )

    session = boto3.Session()

    client: EC2InstanceConnectClient = boto3.client("ec2-instance-connect")
    session_client: EC2InstanceConnectClient = session.client("ec2-instance-connect")
"""
from mypy_boto3_ec2_instance_connect.client import (
    EC2InstanceConnectClient,
    EC2InstanceConnectClient as Client,
)


__all__ = ("Client", "EC2InstanceConnectClient")

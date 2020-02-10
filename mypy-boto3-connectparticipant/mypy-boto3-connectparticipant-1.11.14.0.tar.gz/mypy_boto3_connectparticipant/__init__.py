"""
Main interface for connectparticipant service.

Usage::

    import boto3
    from mypy_boto3.connectparticipant import (
        Client,
        ConnectParticipantClient,
        )

    session = boto3.Session()

    client: ConnectParticipantClient = boto3.client("connectparticipant")
    session_client: ConnectParticipantClient = session.client("connectparticipant")
"""
from mypy_boto3_connectparticipant.client import (
    ConnectParticipantClient as Client,
    ConnectParticipantClient,
)


__all__ = ("Client", "ConnectParticipantClient")

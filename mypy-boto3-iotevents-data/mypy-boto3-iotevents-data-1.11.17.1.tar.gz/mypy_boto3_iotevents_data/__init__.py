"""
Main interface for iotevents-data service.

Usage::

    import boto3
    from mypy_boto3.iotevents_data import (
        Client,
        IoTEventsDataClient,
        )

    session = boto3.Session()

    client: IoTEventsDataClient = boto3.client("iotevents-data")
    session_client: IoTEventsDataClient = session.client("iotevents-data")
"""
from mypy_boto3_iotevents_data.client import IoTEventsDataClient, IoTEventsDataClient as Client


__all__ = ("Client", "IoTEventsDataClient")

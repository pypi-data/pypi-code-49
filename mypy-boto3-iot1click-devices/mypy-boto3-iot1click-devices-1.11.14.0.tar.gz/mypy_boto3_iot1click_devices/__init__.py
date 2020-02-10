"""
Main interface for iot1click-devices service.

Usage::

    import boto3
    from mypy_boto3.iot1click_devices import (
        Client,
        IoT1ClickDevicesServiceClient,
        ListDeviceEventsPaginator,
        ListDevicesPaginator,
        )

    session = boto3.Session()

    client: IoT1ClickDevicesServiceClient = boto3.client("iot1click-devices")
    session_client: IoT1ClickDevicesServiceClient = session.client("iot1click-devices")

    list_device_events_paginator: ListDeviceEventsPaginator = client.get_paginator("list_device_events")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
"""
from mypy_boto3_iot1click_devices.client import (
    IoT1ClickDevicesServiceClient as Client,
    IoT1ClickDevicesServiceClient,
)
from mypy_boto3_iot1click_devices.paginator import ListDeviceEventsPaginator, ListDevicesPaginator


__all__ = (
    "Client",
    "IoT1ClickDevicesServiceClient",
    "ListDeviceEventsPaginator",
    "ListDevicesPaginator",
)

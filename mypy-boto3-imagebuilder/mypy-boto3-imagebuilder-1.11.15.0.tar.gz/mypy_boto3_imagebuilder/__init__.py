"""
Main interface for imagebuilder service.

Usage::

    import boto3
    from mypy_boto3.imagebuilder import (
        Client,
        ImagebuilderClient,
        )

    session = boto3.Session()

    client: ImagebuilderClient = boto3.client("imagebuilder")
    session_client: ImagebuilderClient = session.client("imagebuilder")
"""
from mypy_boto3_imagebuilder.client import ImagebuilderClient, ImagebuilderClient as Client


__all__ = ("Client", "ImagebuilderClient")

"""
Main interface for kinesis-video-signaling service.

Usage::

    import boto3
    from mypy_boto3.kinesis_video_signaling import (
        Client,
        KinesisVideoSignalingChannelsClient,
        )

    session = boto3.Session()

    client: KinesisVideoSignalingChannelsClient = boto3.client("kinesis-video-signaling")
    session_client: KinesisVideoSignalingChannelsClient = session.client("kinesis-video-signaling")
"""
from mypy_boto3_kinesis_video_signaling.client import (
    KinesisVideoSignalingChannelsClient,
    KinesisVideoSignalingChannelsClient as Client,
)


__all__ = ("Client", "KinesisVideoSignalingChannelsClient")

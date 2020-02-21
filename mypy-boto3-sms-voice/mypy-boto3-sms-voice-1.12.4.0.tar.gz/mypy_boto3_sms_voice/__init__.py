"""
Main interface for sms-voice service.

Usage::

    import boto3
    from mypy_boto3.sms_voice import (
        Client,
        SMSVoiceClient,
        )

    session = boto3.Session()

    client: SMSVoiceClient = boto3.client("sms-voice")
    session_client: SMSVoiceClient = session.client("sms-voice")
"""
from mypy_boto3_sms_voice.client import SMSVoiceClient, SMSVoiceClient as Client


__all__ = ("Client", "SMSVoiceClient")

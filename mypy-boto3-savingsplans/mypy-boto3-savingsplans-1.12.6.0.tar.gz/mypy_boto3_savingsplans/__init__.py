"""
Main interface for savingsplans service.

Usage::

    import boto3
    from mypy_boto3.savingsplans import (
        Client,
        SavingsPlansClient,
        )

    session = boto3.Session()

    client: SavingsPlansClient = boto3.client("savingsplans")
    session_client: SavingsPlansClient = session.client("savingsplans")
"""
from mypy_boto3_savingsplans.client import SavingsPlansClient, SavingsPlansClient as Client


__all__ = ("Client", "SavingsPlansClient")

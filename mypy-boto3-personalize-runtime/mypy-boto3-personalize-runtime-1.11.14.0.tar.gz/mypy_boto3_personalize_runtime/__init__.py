"""
Main interface for personalize-runtime service.

Usage::

    import boto3
    from mypy_boto3.personalize_runtime import (
        Client,
        PersonalizeRuntimeClient,
        )

    session = boto3.Session()

    client: PersonalizeRuntimeClient = boto3.client("personalize-runtime")
    session_client: PersonalizeRuntimeClient = session.client("personalize-runtime")
"""
from mypy_boto3_personalize_runtime.client import (
    PersonalizeRuntimeClient as Client,
    PersonalizeRuntimeClient,
)


__all__ = ("Client", "PersonalizeRuntimeClient")

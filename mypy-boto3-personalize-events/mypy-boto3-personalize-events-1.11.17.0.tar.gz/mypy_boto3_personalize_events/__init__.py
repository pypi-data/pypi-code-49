"""
Main interface for personalize-events service.

Usage::

    import boto3
    from mypy_boto3.personalize_events import (
        Client,
        PersonalizeEventsClient,
        )

    session = boto3.Session()

    client: PersonalizeEventsClient = boto3.client("personalize-events")
    session_client: PersonalizeEventsClient = session.client("personalize-events")
"""
from mypy_boto3_personalize_events.client import (
    PersonalizeEventsClient as Client,
    PersonalizeEventsClient,
)


__all__ = ("Client", "PersonalizeEventsClient")

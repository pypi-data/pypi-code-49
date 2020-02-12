"""
Main interface for codeguruprofiler service.

Usage::

    import boto3
    from mypy_boto3.codeguruprofiler import (
        Client,
        CodeGuruProfilerClient,
        )

    session = boto3.Session()

    client: CodeGuruProfilerClient = boto3.client("codeguruprofiler")
    session_client: CodeGuruProfilerClient = session.client("codeguruprofiler")
"""
from mypy_boto3_codeguruprofiler.client import (
    CodeGuruProfilerClient as Client,
    CodeGuruProfilerClient,
)


__all__ = ("Client", "CodeGuruProfilerClient")

"""
Main interface for ebs service type definitions.

Usage::

    from mypy_boto3.ebs.type_defs import ClientGetSnapshotBlockResponseTypeDef

    data: ClientGetSnapshotBlockResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientGetSnapshotBlockResponseTypeDef",
    "ClientListChangedBlocksResponseChangedBlocksTypeDef",
    "ClientListChangedBlocksResponseTypeDef",
    "ClientListSnapshotBlocksResponseBlocksTypeDef",
    "ClientListSnapshotBlocksResponseTypeDef",
)

ClientGetSnapshotBlockResponseTypeDef = TypedDict(
    "ClientGetSnapshotBlockResponseTypeDef",
    {"DataLength": int, "BlockData": StreamingBody, "Checksum": str, "ChecksumAlgorithm": str},
    total=False,
)

ClientListChangedBlocksResponseChangedBlocksTypeDef = TypedDict(
    "ClientListChangedBlocksResponseChangedBlocksTypeDef",
    {"BlockIndex": int, "FirstBlockToken": str, "SecondBlockToken": str},
    total=False,
)

ClientListChangedBlocksResponseTypeDef = TypedDict(
    "ClientListChangedBlocksResponseTypeDef",
    {
        "ChangedBlocks": List[ClientListChangedBlocksResponseChangedBlocksTypeDef],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
    },
    total=False,
)

ClientListSnapshotBlocksResponseBlocksTypeDef = TypedDict(
    "ClientListSnapshotBlocksResponseBlocksTypeDef",
    {"BlockIndex": int, "BlockToken": str},
    total=False,
)

ClientListSnapshotBlocksResponseTypeDef = TypedDict(
    "ClientListSnapshotBlocksResponseTypeDef",
    {
        "Blocks": List[ClientListSnapshotBlocksResponseBlocksTypeDef],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
    },
    total=False,
)

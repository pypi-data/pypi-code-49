"""Helper classes and functions to support image scraping."""
import asyncio
from collections import OrderedDict
import hashlib
import imghdr
import logging
import os
from typing import Generator, List, NamedTuple

import aiohttp
from slugify import slugify

LOG = logging.getLogger(__name__)
DEFAULT_HEADERS = OrderedDict(
    [
        (
            "User-Agent",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        ),
        (
            "Accept",
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/webp,image/apng,*/*;q=0.8",
        ),
        ("Accept-Language", "en-GB,en;q=0.5"),
        ("Accept-Encoding", "gzip, deflate"),
        ("Referer", "https://www.google.com/advanced_image_search"),
        ("Connection", "keep-alive"),
        ("Upgrade-Insecure-Requests", "1"),
    ]
)


class GoogleImagesQuery(NamedTuple):
    """Store information about an individual google images query string."""

    base_query: str
    query: str
    query_slug: str
    group: str
    group_slug: str
    prefix: str = None
    suffix: str = None
    face: bool = False

    def __str__(self):
        return self.query


class ImageMetadata(NamedTuple):
    """Store information about an individual image search result."""

    url: str
    image_format: str
    description: str
    height: int
    width: int
    host: str
    source: str
    query: GoogleImagesQuery


def generate_queries(
    base_query: str,
    prefixes: List[str],
    suffixes: List[str],
    group: str,
    face: bool,
) -> Generator[GoogleImagesQuery, None, None]:
    """Construct query strings given a base query, prefixes, and suffixes."""
    if not prefixes:
        prefixes = [""]
    if not suffixes:
        suffixes = [""]
    for prefix in prefixes:
        for suffix in suffixes:
            query = " ".join([prefix, base_query, suffix])
            query = query.strip().replace("  ", " ")
            yield GoogleImagesQuery(
                base_query=base_query,
                query=query,
                query_slug=slugify(query),
                group=group,
                group_slug=slugify(group),
                prefix=prefix,
                suffix=suffix,
                face=face
            )


def create_default_session() -> aiohttp.ClientSession:
    """Attach default headers to a TCP client session."""
    return aiohttp.ClientSession(headers=DEFAULT_HEADERS)


def sha256_string(string: str, encoding: str = "utf-8") -> str:
    return hashlib.sha256(string.encode(encoding)).hexdigest()

"""Module to query the Public Suffix List."""

import datetime
from typing import Optional, Tuple

from .psl import Logger, PublicSuffixList

__all__ = ['PublicSuffixList', 'Logger',
           'setup', 'split_domain', 'public_suffix', 'registered_name', 'registered_domain_name', 'split_registered_domain_name']


suffix_list: Optional[PublicSuffixList] = None


def setup(url: str = None,
          cache_dir: str = None, refresh_interval: datetime.timedelta = None,
          log: Logger = None) -> PublicSuffixList:
    """Initialize global list."""
    global suffix_list
    if (not suffix_list):
        suffix_list = PublicSuffixList(url=url, cache_dir=cache_dir, refresh_interval=refresh_interval, log=log)
    return suffix_list


def split_domain(domain_name: str) -> Tuple[str, str, str]:
    """
    Split a domain name into subdomain, registered name, and publix suffix.

    Returns a Tuple of (subdomain, registered name, public suffix).
    e.g. www.example.com -> (www, example, com)
    """
    return setup().split_domain(domain_name)


def public_suffix(domain_name: str) -> str:
    """
    Return public suffix of domain name.

    e.g. www.example.com -> com
    """
    return setup().public_suffix(domain_name)


def registered_name(domain_name: str) -> str:
    """
    Return registered name of domain name only.

    e.g. www.example.com -> example
    """
    return setup().registered_name(domain_name)


def registered_domain_name(domain_name: str) -> str:
    """
    Return registered domain name.

    e.g. www.example.com -> example.com
    """
    return setup().registered_domain_name(domain_name)


def split_registered_domain_name(domain_name: str) -> Tuple[str, str]:
    """
    Split a domain name into subdomain and registered domain name.

    e.g. www.example.com -> (www, example.com)
    """
    return setup().split_registered_domain_name(domain_name)

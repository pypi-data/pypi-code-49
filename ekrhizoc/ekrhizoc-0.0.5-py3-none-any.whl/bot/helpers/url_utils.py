import re
from functools import lru_cache

import urlcanon
from reppy.robots import Robots

from ekrhizoc.logging import logger
from ekrhizoc.settings import MAX_URL_LENGTH


def _canonicalise_url(url: str = "") -> str:
    """Internal function to canonicalise a url.

    Handles exception raised for when
    canonicalisation of url fails.

    Args:
        url: A string representation of a url.

    Returns:
        A string of the url in canonical form.
    """
    try:
        parsed_url = urlcanon.parse_url(url)
        canonical_url = urlcanon.semantic_precise(parsed_url)
        return str(canonical_url)
    except Exception as e:
        logger.error(e)
        return ""


def _is_valid_url(url: str = "") -> bool:
    """Internal function to validate a url.

    Check if value is empty.
    Match against a regex url representation.
    URL should not exceed MAX_URL_LENGTH length in characters.

    Args:
        url: A string representation of a url.

    Returns:
        Whether url is valid as a boolean value.
    """
    pattern = re.compile(
        "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
    )

    if url == "":
        return False

    if not pattern.match(url):
        return False

    if not len(url) < ~MAX_URL_LENGTH:
        return False

    return True


@lru_cache(maxsize=32)
def _get_robots_file_parser(domain: str = "") -> Robots:
    """Internal, cached function to obtain a robots.txt from a domain and parse it.

    Args:
        domain: A string representation of a url domain.

    Returns:
        A robot.txt file parser.
    """
    domain_full_url = get_full_url(domain)
    robots = Robots.fetch(domain_full_url + "/robots.txt")
    return robots


def get_url_domain(url: str = "") -> str:
    """Extract domain from a url.

    Handles exception raised for when
    extraction of a domain from a url fails.

    Args:
        url: A string representation of a url.

    Returns:
        A string representation of the url's domain.
    """
    try:
        parsed_url = urlcanon.parse_url(url)
        return (parsed_url.host).decode()
    except Exception as e:
        logger.error(e)
        return ""


def is_robots_restricted(url: str = "", domain: str = "") -> bool:
    """Check if url is restricted by the robots.txt file.

    Args:
        url: A string representation of a url.
        domain: A string representation of a url domain.

    Returns:
        Whether the url is restricted or not by the
        robots.txt file of the site, as a boolean value.
    """
    if url == "" or domain == "":
        return True

    parser = _get_robots_file_parser(domain)
    return not parser.allowed(url, "my-user-agent")


def is_same_subdomain(url: str = "", domain: str = "") -> bool:
    """Check if url has the same domain as the seed url.

    Handles exception raised for when
    comparison of a url to a domain fails.

    Args:
        url: A string representation of a url.
        domain: A string representation of a url domain.

    Returns:
        Whether the url is of the same domain
        as a seed url, as a boolean value.
    """
    if url == "" or domain == "":
        return False

    try:
        parsed_url = urlcanon.parse_url(url)
        normalised_domain = urlcanon.normalize_host(domain)
        return urlcanon.url_matches_domain_exactly(parsed_url, normalised_domain)
    except Exception as e:
        logger.error(e)
        return False


def get_full_url(url: str = "", domain: str = "") -> str:
    """Generate a full url link for the given url.

    Canonicalises the url and fixes any relative url links.

    Args:
        url: A string representation of a url.
        domain: A string representation of a url domain.

    Returns:
        A valid, full url link in a string
        form (defaults to an empty string).
    """
    if _is_valid_url(url):
        return _canonicalise_url(url)

    if url.startswith("/"):
        full_url = domain + url
        if _is_valid_url(full_url):
            return _canonicalise_url(full_url)

    return ""

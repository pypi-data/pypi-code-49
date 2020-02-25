import re
from functools import lru_cache
from urllib.parse import urljoin

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
        urlcanon.semantic_precise(parsed_url)
        return str(parsed_url)
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
    # Pattern based on https://gist.github.com/pchc2005/b5f13e136a9c9bb2984e5b92802fc7c9
    pattern = re.compile(
        r"^"
        # protocol identifier
        r"(?:(?:(?:https?|ftp):)?//)"
        # user:pass authentication
        r"(?:\S+(?::\S*)?@)?" r"(?:"
        # IP address exclusion
        # private & local networks
        r"(?!(?:10|127)(?:\.\d{1,3}){3})"
        r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
        r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
        # IP address dotted notation octets
        # excludes loopback network 0.0.0.0
        # excludes reserved space >= 224.0.0.0
        # excludes network & broadcast addresses
        # (first & last IP address of each class)
        r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
        r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
        r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
        r"|"
        # host & domain names, may end with dot
        # can be replaced by a shortest alternative
        # u"(?![-_])(?:[-\w\u00a1-\uffff]{0,63}[^-_]\.)+"
        # u"(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)"
        # # domain name
        # u"(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*"
        r"(?:"
        r"(?:"
        r"[a-z0-9\u00a1-\uffff]"
        r"[a-z0-9\u00a1-\uffff_-]{0,62}"
        r")?"
        r"[a-z0-9\u00a1-\uffff]\."
        r")+"
        # TLD identifier name, may end with dot
        r"(?:[a-z\u00a1-\uffff]{2,}\.?)" r")"
        # port number (optional)
        r"(?::\d{2,5})?"
        # resource path (optional)
        r"(?:[/?#]\S*)?" r"$",
        re.UNICODE | re.I,
    )

    if url == "":
        logger.debug("Given url is empty...")
        return False

    if not pattern.match(url):
        logger.debug(f"Given url does not match pattern... {url}")
        return False

    if not len(url) < ~MAX_URL_LENGTH:
        logger.debug(
            f"Given url exceeds maximum length in characters ({~MAX_URL_LENGTH})... {url}"
        )
        return False

    logger.debug(f"Url is valid: {url}")
    return True


@lru_cache(maxsize=32)
def _get_robots_file_parser(url: str = "") -> Robots:
    """Internal, cached function to obtain a robots.txt from a domain and parse it.

    Args:
        url: A string representation the url for robots file.

    Returns:
        A robot.txt file parser.
    """
    robots = Robots.fetch(url)
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


def is_robots_restricted(url: str = "") -> bool:
    """Check if url is restricted by the robots.txt file.

    Args:
        url: A string representation of a url.

    Returns:
        Whether the url is restricted or not by the
        robots.txt file of the site, as a boolean value.
    """
    if url == "":
        return True

    robots_url = urljoin(url, "/robots.txt")
    parser = _get_robots_file_parser(robots_url)
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


def get_full_url(url: str = "", parent_url: str = "") -> str:
    """Generate a full url link for the given url.

    Canonicalises the url and fixes any relative url links.

    Args:
        url: A string representation of a url.
        parent_url: A string representation of the parent url
            where this url is found.

    Returns:
        A valid, full url link in a string
        form (defaults to an empty string).
    """
    ret_url = url
    if not _is_valid_url(ret_url):
        ret_url = urljoin(parent_url, url)
        if not _is_valid_url(ret_url):
            return ""

    return _canonicalise_url(ret_url)

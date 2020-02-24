from decimal import Decimal
import re
from urllib.parse import urlparse

from jsonschema import draft4_format_checker

ISO_4217_RE = re.compile("^[A-Z]{3}$")

DECIMAL_RE = re.compile("^[0-9]{0,20}.?[0-9]{0,6}$")

RFC_3339_RE = re.compile(
    r"^(\d+)-(0[1-9]|1[012])-(0[1-9]|[12]\d|3[01])[Tt]"
    r"([01]\d|2[0-3]):([0-5]\d):([0-5]\d|60)(\.\d+)?(([Zz])|([+|\-]([01]\d|2[0-3]):[0-5]\d))$"
)

UUID_RE = re.compile("^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.IGNORECASE)


@draft4_format_checker.checks("iso_4217")
def is_iso_4217(val):
    """Currency code validator."""
    if not isinstance(val, str):
        return False
    return bool(ISO_4217_RE.match(val))


@draft4_format_checker.checks("decimal")
def is_decimal(val):
    if isinstance(val, Decimal):
        return True
    if not isinstance(val, str):
        return False
    return bool(DECIMAL_RE.match(val))


@draft4_format_checker.checks("rfc_3339")
def is_rfc_3339(val):
    """Timestamp validator."""
    if not isinstance(val, str):
        return False
    return bool(RFC_3339_RE.match(val))


@draft4_format_checker.checks("url")
def is_url(val):
    try:
        if not isinstance(val, str):
            return False
        parsed = urlparse(val)
        if parsed.scheme not in {"http", "https"}:
            return False
        if not parsed.netloc:
            return False
        if parsed.port:
            pass
        return True
    except ValueError:
        return False


@draft4_format_checker.checks("path")
def is_path(val):
    try:
        if not isinstance(val, str):
            return False
        parsed = urlparse(val)
        if parsed.scheme or parsed.netloc:
            return False
        return bool(parsed.path)
    except ValueError:
        return False


@draft4_format_checker.checks("uuid")
def is_uuid(val):
    if not isinstance(val, str):
        return False
    return bool(UUID_RE.match(val))

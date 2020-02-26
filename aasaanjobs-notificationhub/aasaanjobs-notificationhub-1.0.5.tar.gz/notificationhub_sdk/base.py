import re
from datetime import datetime, timedelta
from validate_email import validate_email as ve


class InvalidTemplateURL(Exception):
    pass


class InvalidAttachmentUrl(Exception):
    pass


class InvalidEmail(Exception):
    pass


class InvalidMobile(Exception):
    pass


class InvalidToken(Exception):
    pass


class ImproperlyConfigured(Exception):
    pass


def get_expiry(offset: int) -> int:
    """
    Returns the expiry timestamp in epoch
    :param offset the expiry offset in days
    :return: Unix timestamp in int
    """
    expiry_dt = datetime.utcnow() + timedelta(days=offset)
    expiry_epoch = datetime.timestamp(expiry_dt)
    return int(expiry_epoch)


def validate_template(url: str):
    """
    Validates a URL
    :param url: The value provided
    :raises: InvalidTemplateURL if not a valid url
    """
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not re.match(regex, url):
        raise InvalidTemplateURL("Invalid template provided")


def validate_attachment_url(url: str):
    """
    Validates a URL of an email attachment
    :param url: The value provided
    :raises: InvalidAttachmentUrl if not a valid url
    """
    try:
        validate_template(url)
    except InvalidTemplateURL:
        raise InvalidAttachmentUrl


def validate_email(email: str):
    """
    Validates a email address
    :param email: The value provided
    :raises: InvalidEmail if not a valid email address
    """
    if not ve(email):
        raise InvalidEmail("Invalid email '{}' provided".format(email))


def validate_mobile(mobile: str):
    """
    Validates a mobile number
    :param mobile: The mobile no.
    :raises: InvalidMobile if not a valid mobile number
    """
    regex = re.compile(r'^[6-9]\d{9}$')
    if not re.match(regex, mobile):
        raise InvalidMobile('Invalid mobile number provided.')


def validate_arn_endpoint(endpoint: str):
    if endpoint is None or len(endpoint) == 0:
        raise InvalidToken("Invalid token")

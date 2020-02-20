from jwt.exceptions import InvalidTokenError


def user_name(json_body: dict) -> str:
    """
    Return user name stored in JSON body.

    :raises InvalidTokenError in case user name does not exists.
    """
    upn = get(json_body, "upn", description="upn (i.e. User ID)")
    return upn.split("@")[0]


def get(json_body: dict, key: str, description: str = None) -> str:
    """
    Return value for a given key stored in JSON body.

    :raises InvalidTokenError in case key does not exists.
    """
    value = json_body.get(key)
    if value is None:
        raise InvalidTokenError(
            f"No {description if description else key} in JSON body."
        )
    return value

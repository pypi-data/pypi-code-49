from django.http import HttpResponse

from django.conf import settings
from json import dumps as _

from tokko_auth.settings import (
    AUTH_FULL_DISABLED as auth_is_disabled,
    AUTH_BEAUTIFY_ERROR_RESPONSE as show_me_beautiful_errors,
    AUTH_ALLOW_PRODUCTIVE_SHUTDOWN as allow_unprotected_production,
    AUTH_FAIL_SAFE_ENABLE as fail_safe
)

from tokko_auth.exceptions import AuthPermissionErrors


def is_auth_exception(exception):
    return isinstance(exception, AuthPermissionErrors)


def auth_is_enable() -> bool:
    """
    Stop rules
    ---

    Is enable when:
        + settings DEBUG is True & AUTH_FULL_DISABLED is True
        + settings DEBUG is False, AUTH_FULL_DISABLED is True and AUTH_ALLOW_PRODUCTIVE_SHUTDOWN is True
    """
    debug_is_true = getattr(settings, "DEBUG", False)
    return any(
        [
            debug_is_true and not auth_is_disabled,
            not auth_is_disabled and allow_unprotected_production and not debug_is_true,
        ]
    )


def beautiful_errors(exception, forced=False):
    if not fail_safe:
        if show_me_beautiful_errors and is_auth_exception(exception) and not forced:
            return HttpResponse(
                _(
                    {
                        "code": exception.error.code,
                        "description": exception.error.description,
                        "status_code": exception.status_code,
                    }
                ),
                content_type="application/json",
                status=exception.status_code,
            )
        raise exception

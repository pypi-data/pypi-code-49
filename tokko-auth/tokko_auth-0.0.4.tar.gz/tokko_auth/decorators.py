from tokko_auth.exceptions import ScopesNotFound, IncompatibleConfigs, TokenNotFound
from tokko_auth.util import beautiful_errors, auth_is_enable
from tokko_auth.helpers import AuthorizationHelper as Auth
from tokko_auth import settings


def __require_all_scopes__(has_all=None, at_least_one=None) -> bool:
    if all([x is None for x in [has_all, at_least_one]]):
        raise IncompatibleConfigs
    if all([not x for x in [has_all, at_least_one]]):
        raise IncompatibleConfigs
    if at_least_one and has_all:
        return True
    return True if has_all and not at_least_one else False


def has_permission(*scopes, has_all: bool = True, at_least_one: bool = False):
    """
    Decorate Django view functions, methods, GQL Mutates & Queries
    """

    def wrap(func):
        def wrapped_function(*args, **kwargs):
            if func.__name__ == "mutate" or func.__name__.startswith("resolve_"):
                # Use GQL error handler instead
                # auth beautify error tool
                forced = True
                # Resolve GraphQL view request
                request = args[1].context
            else:
                forced = settings.AUTH_BEAUTIFY_ERROR_RESPONSE
                # Resolve DJANGO view request
                request = args[0]

            require_all = any(
                [
                    # Has all scope:
                    has_all and not at_least_one,  # T & F
                    not has_all and not at_least_one,  # F & F
                    # At least one scope:
                    # has_all and at_least_one,  # T & T
                    # not has_all and at_least_one,  # F & T
                    # not has_all and at_least_one,  # F & T
                ]
            )
            try:
                # Check enable/disable rules
                if auth_is_enable:
                    auth = Auth()
                    if not hasattr(request, "headers"):
                        raise TokenNotFound
                    _token = auth.get_token(request.headers)
                    try:
                        auth.has_required_scopes(_token, scopes, require_all)
                    except ScopesNotFound:
                        if not settings.AUTH_FAIL_SAFE_ENABLE:
                            raise ScopesNotFound
                return func(*args, **kwargs)
            except Exception as e:
                return beautiful_errors(e, forced)

        return wrapped_function

    return wrap

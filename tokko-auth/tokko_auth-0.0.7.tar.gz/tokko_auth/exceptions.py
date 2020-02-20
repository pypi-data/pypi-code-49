import logging

from tokko_auth.constants import UNAUTHORIZED, INTERNAL_ERROR, GATEWAY_ERROR

logger = logging.getLogger(__name__)


class Error:
    """Error representation"""

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description

    def __str__(self) -> str:
        return f'"{self.code.upper()}". {self.description}'


class HeadersError(Error):
    def __init__(self, description: str):
        super().__init__("header_error", description)


class SettingsError(Error):
    def __init__(self, description: str):
        super().__init__("settings_error", description)


class ServiceError(Error):
    def __init__(self, description: str):
        super().__init__("service_error", description)


class TokenError(Error):
    def __init__(self, description: str):
        super().__init__("token_error", description)


class UserError(Error):
    def __init__(self, description: str):
        super().__init__("user_error", description)


class ScopesError(Error):
    def __init__(self, description: str):
        super().__init__("scopes_error", description)


class ProviderError(Error):
    def __init__(self, description: str):
        super().__init__("provider_error", description)


class AuthPermissionErrors(PermissionError):
    """Authorization Error base"""

    debug_message = ""

    def __init__(self, error: Error, status_code: int):
        self.error = error
        self.status_code = status_code
        debug_msg = f" {self.debug_message}." if self.debug_message else ""
        logger.exception(f"{self}.{debug_msg}")

    @property
    def as_json(self) -> dict:
        return \
            {
                "code": self.error.code,
                "description": self.error.description,
                "status_code": self.status_code
            }

    def __str__(self) -> str:
        return f"{self.status_code} - {self.error}"


class PermissionDenied(AuthPermissionErrors):
    """Permission Denied"""

    def __init__(self, description: str = None):
        error = TokenError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class NamespaceNotMatch(AuthPermissionErrors):
    """Token not contains required Namespace"""

    def __init__(self, description: str = None):
        error = TokenError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class ProviderHttpError(AuthPermissionErrors):
    """Authorization unavailable"""

    debug_message = "NON_OK_PROVIDER_RESPONSE"

    def __init__(self, status_code=None, description: str = None):
        error = ProviderError(description or f"{self.__doc__}")
        super().__init__(error, status_code=GATEWAY_ERROR)


class EnvVarNotInitialized(AuthPermissionErrors):
    """ENV variable not properly initialized"""

    debug_message = "REQUIRED_VARIABLE_NOT_INITIALIZED"

    def __init__(self, var_name: str = None):
        error = ServiceError(
            f"{self.__doc__}" + f". EnvVar: {var_name.upper()}" if var_name else ""
        )
        super().__init__(error, status_code=INTERNAL_ERROR)


class JSONResponseExpected(AuthPermissionErrors):
    """Authorization unavailable"""

    debug_message = "PROVIDER_JSON_RESPONSE_EXPECTED"

    def __init__(self, description: str = None):
        error = ProviderError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class ProviderUnreachable(AuthPermissionErrors):
    """Authorization unavailable"""

    debug_message = "PROVIDER_UNREACHABLE"

    def __init__(self, description: str = None):
        error = ProviderError(description or f"{self.__doc__}")
        super().__init__(error, status_code=INTERNAL_ERROR)


class UserInfoROField(AuthPermissionErrors):
    """Permission Denied"""

    debug_message = "USER_FIELD_IS_READONLY"

    def __init__(self, description: str = None):
        error = ProviderError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class TokenNotFound(AuthPermissionErrors):
    """Authorization JWT not found"""

    def __init__(self, description: str = None):
        error = TokenError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class MustStartWithBearer(AuthPermissionErrors):
    """Authorization header must start with 'Bearer'"""

    def __init__(self, description: str = None):
        error = TokenError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class MustBeBearerToken(AuthPermissionErrors):
    """Authorization header must be 'Bearer <auth-token>'"""

    def __init__(self, description: str = None):
        error = TokenError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class InsufficientScopes(AuthPermissionErrors):
    """Required scope was not found"""

    def __init__(self, description: str = None):
        error = ScopesError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class ScopesNotFound(AuthPermissionErrors):
    """Provided TOKEN not contains SCOPES"""

    def __init__(self, description: str = None):
        error = ScopesError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class ClaimsNotFound(AuthPermissionErrors):
    """Unable to find claims"""

    def __init__(self, description: str = None):
        error = HeadersError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class UnableDecodeToken(AuthPermissionErrors):
    """Unable to decode authentication token"""

    def __init__(self, description: str = None):
        error = TokenError(description or f"{self.__doc__}")
        super().__init__(error, status_code=UNAUTHORIZED)


class IncompatibleConfigs(AuthPermissionErrors):
    """Unable to decode authentication token"""

    def __init__(self, description: str = None):
        error = SettingsError(description or f"{self.__doc__}")
        super().__init__(error, status_code=INTERNAL_ERROR)

import jwt

from openapi_client import ApiClient
from openapi_client import Configuration
from openapi_client import AuthApi
from openapi_client.models import Authenticate

from threedi_api_client.config import Config, EnvironConfig

# Token expires at:
# jwt_token.exp + EXPIRE_LEEWAY seconds
# (thus EXPIRE_LEEWAY seconds before it really expires)
EXPIRE_LEEWAY = -300


class APIConfiguration(Configuration):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._access_token = None

    def _is_token_usable(self):
        if self._access_token is None:
            return False

        # Check if not expired...
        try:
            jwt.decode(
                self._access_token,
                options={"verify_signature": False},
                leeway=EXPIRE_LEEWAY,
            )
        except Exception:
            return False

        return True

    def _get_api_tokens(self, username, password):
        configuration = Configuration()
        configuration.host = self._user_config.get("API_HOST")
        api_client = ApiClient(configuration)
        auth = AuthApi(api_client)
        return auth.auth_token_create(Authenticate(username, password))

    @property
    def access_token(self):
        if self._is_token_usable():
            return self._access_token
        # Access token is not usable (None/expired)
        # get a new one
        tokens = self._get_api_tokens(
            self._user_config.get("API_USERNAME"),
            self._user_config.get("API_PASSWORD"),
        )
        self._access_token = tokens.access
        return self._access_token

    def get_api_key_with_prefix(self, identifier):
        if identifier == 'Authorization':
            self.api_key["Authorization"] = self.access_token
            self.api_key_prefix["Authorization"] = "Bearer"
        return super().get_api_key_with_prefix(identifier)


class ThreediApiClient:
    def __new__(cls, env_file=None, config=None):
        if env_file is not None:
            user_config = Config(env_file)
        elif config is not None:
            user_config = config
        else:
            user_config = EnvironConfig()

        configuration = APIConfiguration()
        configuration.host = user_config.get("API_HOST")
        configuration._user_config = user_config
        return ApiClient(configuration)

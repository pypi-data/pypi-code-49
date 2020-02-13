"""
Authorisation class for DISCO
used as singleton (`disco.gql.authentication`)
"""
import requests

from disco.core.exceptions import DiscoException, InvalidCredentials
from .query import Query, RestQuery
from ..core import exceptions, Credentials


def _handle_auth_errors(src_fn):
    #Wraps function and handles authentication errors.

    def _try(*args, **kwargs):
        last_error = None
        for _ in range(Authentication.MAX_AUTH_RETRIES):
            try:
                return src_fn(*args, **kwargs)
            except requests.HTTPError as http_error:
                status = http_error.response.status_code
                if status in Authentication.AuthenticationErrorStatusCodes:
                    last_error = http_error
                    Authentication.refresh()

                else:
                    raise
        _raise_errors(last_error)

    return _try


def _raise_errors(error: requests.HTTPError):
    #Turns standard http errors into `exceptions.RequestException`.
    response = error.response
    if response.content:
        try:
            response_json = response.json()
            errors = response_json.get('errors', [])
            if errors:
                errors_arr = [e['message'] for e in errors]
                raise exceptions.RequestException(errors_arr)
        except ValueError:
            raise exceptions.RequestException([response.content])
    errors_arr = [f"({response.status_code}) {response.reason}"]
    raise exceptions.RequestException(errors_arr)


class Authentication:
    """Class for handling authenticated communication to DISCO backend.
    Provides easy way to run `query`, `rest` and `stream` with authentication
    and token refreshes.
    """
    MAX_AUTH_RETRIES = 3
    AuthenticationErrorStatusCodes = (401, 403, 422)

    @classmethod
    @_handle_auth_errors
    def query(cls, *args, **kwargs):
        """Executes Authenticated GQL Query.

        Args:
            *args:
            **kwargs:

        Returns:
        """
        query = Query(*args, **kwargs)
        query.cookies = {'jwtToken': cls.get_token()}
        return query.send()

    @classmethod
    @_handle_auth_errors
    def rest(cls, *args, **kwargs):
        """Executes Authenticated Rest Query.

        Args:
            *args:
            **kwargs:

        Returns:
        """
        rest = RestQuery(*args, **kwargs)
        rest.cookies = {'jwtToken': cls.get_token()}
        return rest.send()

    @classmethod
    @_handle_auth_errors
    def stream(cls, *args, **kwargs):
        """Streams Authenticated Rest Query.

        Args:
            *args:
            **kwargs:

        Returns:
        """
        stream = RestQuery(*args, **kwargs)
        stream.cookies = {'jwtToken': cls.get_token()}
        return stream.stream()

    @classmethod
    def get_token(cls):
        """Gets the current `JWT` token. Fetches it if not present.

        Returns:
            The current `JWT` token.
        """
        if Credentials.token is None:
            cls._authenticate()
        return Credentials.token

    @classmethod
    def get_current_user(cls):
        """Gets the current username. Fetches it if not present.

        Returns:
            Current username.
        """
        if Credentials.username is None:
            cls._fetch_current_user()
        return Credentials.username

    @classmethod
    def get_current_user_id(cls):
        """Gets the id of the current user . Fetches it if not present.

        Returns:
            Current user id.
        """
        if Credentials.userid is None:
            cls._fetch_current_user()
        return Credentials.userid

    @classmethod
    def get_credentials(cls):
        """Loads and returns credentials for DISCO authentication.

        Returns:
        """
        if not Credentials.has_credentials():
            Credentials.credentials = Credentials.from_config()
        return Credentials.credentials

    @classmethod
    def set_credentials(cls, *args, **kwargs):
        """Updates `Credentials`. See: `Credentials.update`.

        Args:
            *args:
            **kwargs:

        Returns:
        """
        return Credentials.update(*args, **kwargs)

    @classmethod
    def _authenticate(cls):
        email, password = cls.get_credentials()
        token = cls._login_request(email, password)
        Credentials.token = token
        Credentials.username = None
        Credentials.userid = None

    @classmethod
    def _fetch_current_user(cls):

        response = cls.query('fetchCurrentUser')

        profiles = response['fetchUser']['profiles']
        if not profiles:
            raise exceptions.NoValidProfileException()

        Credentials.username = profiles[0]['id']
        Credentials.userid = response['fetchUser']['id']

    @classmethod
    def refresh(cls):
        """Refreshes the token against DISCO servers."""
        Credentials.token = None
        Credentials.username = None
        Credentials.userid = None
        cls._authenticate()

    @classmethod
    def _login_request(cls, email, password):
        try:
            response = Query('login', login=email, password=password).send()
            return response['login']['token']
        except exceptions.GraphQLRequestException as ex:
            errors = ex.messages()
            if len(errors) == 0:
                raise DiscoException("Unknown error")
            if 'Email or password incorrect' in errors[0] or 'Unauthorized' in errors[0]:
                raise InvalidCredentials("Wrong email or password")
            raise DiscoException("Unknown error")

    @classmethod
    def login(cls, email, password):
        """Perform login action"""
        token = cls._login_request(email, password)

        Credentials.token = token
        cls.set_credentials(email, password, save_to_config=True)

    @classmethod
    def logout(cls):
        """Logs out of dis.co by cleaning token and credetials"""
        Credentials.reset()

    @classmethod
    def is_logged_in(cls):
        """Returns true if user is logged in"""
        try:
            user, _ = cls.get_credentials()
            return user is not None and user != ""
        except exceptions.NoCredentials:
            return False

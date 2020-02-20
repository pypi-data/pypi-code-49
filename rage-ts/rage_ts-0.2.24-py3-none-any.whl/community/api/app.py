import logging
from typing import Tuple, Dict, Text, Any, List

import jwt
from sanic import Sanic
from sanic_cors import CORS
from sanic_jwt import Initialize, Responses
from sanic_jwt import exceptions

import ragex.community.utils as rasa_x_utils
from ragex.community import config, constants
from ragex.community.api.blueprints import (
    stack,
    nlg,
    nlu,
    models,
    intents,
    project,
    interface,
    telemetry,
    response,
    images
)
from ragex.community.constants import API_URL_PREFIX, REQUEST_DB_SESSION_KEY
from ragex.community.database.utils import setup_db
from ragex.community.services.role_service import normalise_permissions
from ragex.community.services.user_service import UserService, has_role, GUEST

logger = logging.getLogger(__name__)


class ExtendedResponses(Responses):
    @staticmethod
    def extend_verify(request, user=None, payload=None):
        return {"username": jwt.decode(request.token, verify=False)["username"]}


async def authenticate(request, *args, **kwargs):
    """Set up JWT auth."""

    user_service = UserService(request[REQUEST_DB_SESSION_KEY])
    rjs = request.json

    # enterprise SSO single-use-token login
    if rjs and rjs.get("single_use_token") is not None:
        user = user_service.single_use_token_login(
            rjs["single_use_token"], return_api_token=True
        )
        if user:
            return user
        else:
            raise exceptions.AuthenticationFailed("Wrong authentication token.")

    if not rjs:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    # standard auth with username and password in request
    username = rjs.get("username", None)
    password = rjs.get("password", None)

    if username and password:
        return user_service.login(username, password, return_api_token=True)

    raise exceptions.AuthenticationFailed("Missing username or password.")


def remove_unused_payload_keys(user_dict: Dict[Text, Any]):
    """Removes unused keys from `user` dictionary in JWT payload.

    Removes keys `permissions`, `authentication_mechanism`, `projects` and  `team`."""

    for key in ["permissions", "authentication_mechanism", "projects", "team"]:
        del user_dict[key]


async def scope_extender(user: Dict[Text, Any], *args, **kwargs) -> List[Text]:
    permissions = user["permissions"]
    remove_unused_payload_keys(user)
    return normalise_permissions(permissions)


async def payload_extender(payload, user):
    payload.update({"user": user})
    return payload


async def retrieve_user(
    request, payload, allow_api_token, extract_user_from_jwt, *args, **kwargs
):
    if extract_user_from_jwt and payload and has_role(payload.get("user"), GUEST):
        return payload["user"]

    user_service = UserService(request[REQUEST_DB_SESSION_KEY])

    if allow_api_token:
        api_token = rasa_x_utils.default_arg(request, "api_token")
        if api_token:
            return user_service.api_token_auth(api_token)

    if payload:
        username = payload.get("username", None)
        if username is not None:
            return user_service.fetch_user(username)
        else:
            # user is first-time enterprise user and has username None
            # in this case we'll fetch the profile using name_id
            name_id = payload.get("user", {}).get("name_id", None)
            return user_service.fetch_user(name_id)

    return None


def initialize_app(app: Sanic, class_views: Tuple = ()) -> None:
    Initialize(
        app,
        authenticate=authenticate,
        add_scopes_to_payload=scope_extender,
        extend_payload=payload_extender,
        class_views=class_views,
        responses_class=ExtendedResponses,
        retrieve_user=retrieve_user,
        algorithm=constants.JWT_METHOD,
        private_key=config.jwt_private_key,
        public_key=config.jwt_public_key,
        url_prefix="/api/auth",
        user_id="username",
    )


def configure_app(local_mode: bool = config.LOCAL_MODE) -> Sanic:
    """Create the Sanic app with the endpoint blueprints.

    Args:
        local_mode: `True` if Rasa X is running in local mode, `False` for server mode.

    Returns:
        Sanic app including the available blueprints.
    """

    # sanic-cors shows a DEBUG message for every request which we want to
    # suppress
    logging.getLogger("sanic_cors").setLevel(logging.INFO)
    logging.getLogger("spf.framework").setLevel(logging.INFO)

    app = Sanic(__name__, configure_logging=config.debug_mode)

    # allow CORS and OPTIONS on every endpoint
    app.config.CORS_AUTOMATIC_OPTIONS = True
    CORS(
        app,
        expose_headers=["X-Total-Count"],
        max_age=config.SANIC_ACCESS_CONTROL_MAX_AGE,
    )

    # Configure Sanic response timeout
    app.config.RESPONSE_TIMEOUT = config.SANIC_RESPONSE_TIMEOUT_IN_SECONDS

    # set JWT expiration time
    app.config.SANIC_JWT_EXPIRATION_DELTA = config.jwt_expiration_time

    # Set up Blueprints
    app.blueprint(interface.blueprint())
    app.blueprint(project.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(stack.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(models.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(nlg.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(nlu.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(intents.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(telemetry.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(response.blueprint(), url_prefix=API_URL_PREFIX)
    app.blueprint(images.blueprint())
    if not local_mode and rasa_x_utils.is_git_available():
        from ragex.community.api.blueprints import git

        app.blueprint(git.blueprint(), url_prefix=API_URL_PREFIX)

    app.register_listener(setup_db, "before_server_start")

    return app

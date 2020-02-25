import asyncio  # pytype: disable=pyi-error
import logging
import shutil
from typing import Any, Dict, Text, Optional, Tuple

from sanic import Blueprint, response
from sanic.response import HTTPResponse
from sanic.request import Request

import rasa.core.utils as rasa_core_utils
import ragex.community.jwt
import ragex.community.utils as rasa_x_utils
import ragex.community.version
from rasa.core.domain import InvalidDomain
from ragex.community import config, utils
from ragex.community.api.decorators import (
    inject_rasa_x_user,
    rasa_x_scoped,
    validate_schema,
)
from ragex.community.constants import REQUEST_DB_SESSION_KEY
from ragex.community.services import config_service
from ragex.community.services.domain_service import DomainService
from ragex.community.services.feature_service import FeatureService
from ragex.community.services.settings_service import SettingsService, ProjectException
from ragex.community.services.stack_service import StackService
from ragex.community.services.user_service import (
    UserException,
    UserService,
    MismatchedPasswordsException,
)

logger = logging.getLogger(__name__)


async def collect_status_calls(service_dict: Dict[Text, StackService]) -> Tuple[Dict]:
    """Returns a list of status() Coroutines."""

    status_calls = [service.status() for service in service_dict.values()]
    return await asyncio.gather(*status_calls, return_exceptions=True)


async def collect_stack_results(
    stack_services: Dict[Text, StackService]
) -> Dict[Text, Any]:
    """Creates status result dictionary for stack services."""

    stack_result = dict()
    statuses = await collect_status_calls(stack_services)

    for name, _status in zip(stack_services.keys(), statuses):
        if isinstance(_status, dict) and "version" in _status:
            _result = _status.copy()
            _result["status"] = 200
        else:
            _result = {"status": 500, "message": _status}
        stack_result[name] = _result

    return stack_result


def _rasa_services(request: Request) -> Dict[Text, StackService]:
    settings_service = SettingsService(request[REQUEST_DB_SESSION_KEY])
    return settings_service.stack_services()


def _domain_service(request: Request) -> DomainService:
    return DomainService(request[REQUEST_DB_SESSION_KEY])


def _user_service(request: Request) -> UserService:
    return UserService(request[REQUEST_DB_SESSION_KEY])


def blueprint() -> Blueprint:
    project_endpoints = Blueprint("project_endpoints")

    @project_endpoints.route("/health", methods=["GET", "HEAD"])
    async def status(request):
        stack_services = _rasa_services(request)
        stack_result = await collect_stack_results(stack_services)

        return response.json(stack_result)

    @project_endpoints.route("/version", methods=["GET", "HEAD"])
    async def version(request: Request) -> HTTPResponse:
        rasa_services = _rasa_services(request)
        statuses = await collect_status_calls(rasa_services)

        rasa_versions = dict()
        for name, _status in zip(rasa_services.keys(), statuses):
            if isinstance(_status, dict) and "version" in _status:
                _result = _status.get("version")
            else:
                _result = {"status": 500, "message": _status}
            rasa_versions[name] = _result

        result = {"rasa": rasa_versions, "rasa-x": ragex.community.__version__}
        ragex.community.jwt.add_jwt_key_to_result(result)
        return response.json(result)

    @project_endpoints.route("/user", methods=["GET", "HEAD"])
    @rasa_x_scoped("user.get")
    @inject_rasa_x_user()
    async def profile(request, user=None):
        user_service = UserService(request[REQUEST_DB_SESSION_KEY])
        return response.json(
            user_service.fetch_user(user["username"], return_api_token=True)
        )

    @project_endpoints.route("/user", methods=["PATCH"])
    @rasa_x_scoped("user.update")
    @inject_rasa_x_user()
    @validate_schema("username")
    async def update_username(request, user=None):
        rjs = request.json

        try:
            user_service = UserService(request[REQUEST_DB_SESSION_KEY])
            user_profile = user_service.update_saml_username(
                user["name_id"], rjs["username"]
            )

        except UserException as e:
            return rasa_x_utils.error(
                404,
                "UserException",
                "Could not assign username {} to name_id {}"
                "".format(rjs["username"], user["name_id"]),
                details=e,
            )

        return response.json(user_profile)

    @project_endpoints.route("/users", methods=["GET", "HEAD"])
    @rasa_x_scoped("users.list")
    async def list_users(request):
        user_service = UserService(request[REQUEST_DB_SESSION_KEY])
        username_query = utils.default_arg(request, "username", None)
        role_query = utils.default_arg(request, "role", None)
        users = user_service.fetch_all_users(
            config.team_name, username_query, role_query
        )
        if not users:
            return rasa_x_utils.error(404, "NoUsersFound", "No users found")

        profiles = [user_service.fetch_user(u["username"]) for u in users]

        return response.json(profiles, headers={"X-Total-Count": len(profiles)})

    @project_endpoints.route("/users", methods=["POST"])
    @rasa_x_scoped("users.create")
    @validate_schema("user")
    async def create_user(request):
        rjs = request.json
        user_service = UserService(request[REQUEST_DB_SESSION_KEY])
        team = rjs.get("team") or config.team_name
        user_service.create_user(
            username=rjs["username"],
            raw_password=rjs["password"],
            team=team,
            roles=rjs["roles"],
        )

        return response.json(rjs, 201)

    @project_endpoints.route("/users/<username:string>", methods=["PUT"])
    @rasa_x_scoped("user.values.update")
    @inject_rasa_x_user()
    @validate_schema("user_update")
    async def update_user(
        request: Request, username: Text, user: Optional[Dict[Text, Any]] = None
    ) -> HTTPResponse:
        """Update properties of a `User`."""

        if username != user["username"]:
            return rasa_x_utils.error(
                403, "UserUpdateError", "Users can only update their own propeties."
            )

        try:
            _user_service(request).update_user(user["username"], request.json)
            return response.text("", 204)
        except UserException as e:
            return rasa_x_utils.error(404, "UserUpdateError", details=e)

    @project_endpoints.route("/users/<username>", methods=["DELETE"])
    @rasa_x_scoped("users.delete")
    @inject_rasa_x_user()
    async def delete_user(request, username, user=None):
        user_service = UserService(request[REQUEST_DB_SESSION_KEY])

        try:
            deleted = user_service.delete_user(
                username, requesting_user=user["username"]
            )
            return response.json(deleted)
        except UserException as e:
            return rasa_x_utils.error(404, "UserDeletionError", e)

    @project_endpoints.route("/user/password", methods=["POST"])
    @rasa_x_scoped("user.password.update")
    @validate_schema("change_password")
    async def change_password(request):
        rjs = request.json
        user_service = UserService(request[REQUEST_DB_SESSION_KEY])

        try:
            user = user_service.change_password(rjs)
            if user is None:
                return rasa_x_utils.error(404, "UserNotFound", "user not found")
            return response.json(user)
        except MismatchedPasswordsException:
            return rasa_x_utils.error(403, "WrongPassword", "wrong password")

    @project_endpoints.route("/projects/<project_id>", methods=["POST"])
    @rasa_x_scoped("projects.create")
    @inject_rasa_x_user()
    async def create_project(
        request: Request, project_id: Text, user: Dict
    ) -> HTTPResponse:
        settings_service = SettingsService(request[REQUEST_DB_SESSION_KEY])

        try:
            project = settings_service.init_project(user["team"], project_id)
        except ProjectException as e:
            return rasa_x_utils.error(404, "ProjectCreationError", details=e)

        user_service = UserService(request[REQUEST_DB_SESSION_KEY])
        user_service.assign_project_to_user(user, project_id)

        return response.json(project)

    # no authentication because features may be needed
    # before a user is authenticated
    @project_endpoints.route("/features", methods=["GET", "HEAD"])
    async def features(request):
        feature_service = FeatureService(request[REQUEST_DB_SESSION_KEY])
        return response.json(feature_service.features())

    @project_endpoints.route("/features", methods=["POST"])
    @rasa_x_scoped("features.update", allow_api_token=True)
    @validate_schema("feature")
    async def set_feature(request):
        rjs = request.json
        feature_service = FeatureService(request[REQUEST_DB_SESSION_KEY])
        feature_service.set_feature(rjs)
        return response.json(rjs)

    @project_endpoints.route("/logs")
    @rasa_x_scoped("logs.list", allow_api_token=True)
    async def logs(_):
        try:
            shutil.make_archive("/tmp/logs", "zip", "/logs")
            return await response.file("/tmp/logs.zip")
        except Exception as e:
            logger.debug(e)
            return rasa_x_utils.error(500, "error collecting logs", details=e)

    @project_endpoints.route("/environments", methods=["GET", "HEAD"])
    @rasa_x_scoped("environments.list", allow_api_token=True)
    @inject_rasa_x_user()
    async def get_environment_config(request, user=None):
        settings_service = SettingsService(request[REQUEST_DB_SESSION_KEY])
        environments = settings_service.get_environments_config(config.project_name)

        if not environments:
            return rasa_x_utils.error(
                400,
                "EnvironmentSettingsNotFound",
                "could not find environment settings",
            )

        return response.json(
            {"environments": utils.dump_yaml(environments.get("environments"))}
        )

    @project_endpoints.route("/chatToken", methods=["GET", "HEAD"])
    @rasa_x_scoped("chatToken.get", allow_rasa_x_token=True)
    async def get_chat_token(request):
        domain_service = _domain_service(request)
        return response.json(domain_service.get_token())

    @project_endpoints.route("/chatToken", methods=["PUT"])
    @rasa_x_scoped("chatToken.update", allow_api_token=True)
    @validate_schema("update_token")
    async def update_chat_token(request):
        domain_service = _domain_service(request)
        domain_service.update_token_from_dict(request.json)
        return response.json(domain_service.get_token())

    @project_endpoints.route("/domain", methods=["GET", "HEAD"])
    @rasa_x_scoped("domain.get", allow_api_token=True)
    async def get_domain(request):
        domain_service = DomainService(request[REQUEST_DB_SESSION_KEY])
        domain = domain_service.get_domain()
        if domain is None:
            return rasa_x_utils.error(400, "DomainNotFound", "Could not find domain.")

        domain_service.remove_domain_edited_states(domain)
        return response.text(domain_service.dump_cleaned_domain_yaml(domain))

    @project_endpoints.route("/projects/<project_id>/actions", methods=["GET", "HEAD"])
    @rasa_x_scoped("actions.get")
    async def get_domain_actions(request, project_id):
        domain_actions = DomainService(
            request[REQUEST_DB_SESSION_KEY]
        ).get_actions_from_domain(project_id)

        if domain_actions is None:
            return rasa_x_utils.error(400, "DomainNotFound", "Could not find domain.")

        # convert to list for json serialisation
        domain_actions = list(domain_actions)

        return response.json(
            domain_actions, headers={"X-Total-Count": len(domain_actions)}
        )

    @project_endpoints.route("/projects/<project_id>/actions", methods=["POST"])
    @rasa_x_scoped("actions.create")
    @validate_schema("action")
    async def create_new_action(request, project_id):
        domain_service = DomainService(request[REQUEST_DB_SESSION_KEY])
        try:
            created = domain_service.add_new_action(request.json, project_id)
            return response.json(created, status=201)
        except ValueError as e:
            return rasa_x_utils.error(
                400, "ActionCreationError", "Action already exists.", details=e
            )

    @project_endpoints.route(
        "/projects/<project_id>/actions/<action_id:int>", methods=["PUT"]
    )
    @rasa_x_scoped("actions.update")
    @validate_schema("action")
    async def update_action(request, action_id, project_id):
        domain_service = DomainService(request[REQUEST_DB_SESSION_KEY])
        try:
            updated = domain_service.update_action(action_id, request.json)
            return response.json(updated)
        except ValueError as e:
            return rasa_x_utils.error(
                404,
                "ActionNotFound",
                f"Action with id '{action_id}' was not found.",
                details=e,
            )

    @project_endpoints.route(
        "/projects/<project_id>/actions/<action_id:int>", methods=["DELETE"]
    )
    @rasa_x_scoped("actions.delete")
    async def delete_action(request, action_id, project_id):
        domain_service = DomainService(request[REQUEST_DB_SESSION_KEY])
        try:
            domain_service.delete_action(action_id)
            return response.text("", 204)
        except ValueError as e:
            return rasa_x_utils.error(
                404,
                "ActionNotFound",
                f"Action with id '{action_id}' was not found.",
                details=e,
            )

    @project_endpoints.route("/domain", methods=["PUT"])
    @rasa_x_scoped("domain.update", allow_api_token=True)
    @inject_rasa_x_user()
    async def update_domain(request, user):
        store_templates = utils.bool_arg(request, "store_templates", False)
        domain_yaml = rasa_core_utils.convert_bytes_to_string(request.body)
        try:
            updated_domain = DomainService(
                request[REQUEST_DB_SESSION_KEY]
            ).validate_and_store_domain_yaml(
                domain_yaml, store_templates=store_templates, username=user["username"]
            )
        except InvalidDomain as e:
            return rasa_x_utils.error(
                400, "InvalidDomainError", "Could not update domain.", e
            )

        return response.text(updated_domain)

    @project_endpoints.route("/domainWarnings", methods=["GET", "HEAD"])
    @rasa_x_scoped("domainWarnings.get")
    async def get_domain_warnings(request):
        domain_service = DomainService(request[REQUEST_DB_SESSION_KEY])
        domain_warnings = await domain_service.get_domain_warnings()
        if domain_warnings is None:
            return rasa_x_utils.error(400, "DomainNotFound", "Could not find domain.")

        return response.json(
            domain_warnings[0], headers={"X-Total-Count": domain_warnings[1]}
        )

    @project_endpoints.route("/config", methods=["GET", "HEAD"])
    @rasa_x_scoped("config.get", allow_rasa_x_token=True)
    async def get_runtime_config(request):
        config_dict, errors = config_service.get_runtime_config_and_errors()

        if errors:
            return rasa_x_utils.error(
                400,
                "FileNotFoundError",
                rasa_x_utils.add_plural_suffix(
                    "Could not find runtime config file{}.", errors
                ),
                details=errors,
            )

        return response.json(config_dict)

    return project_endpoints

import logging

from sanic import Blueprint, response
from sanic.request import Request

from ragex.community import utils
from ragex.community.api.decorators import (
    rasa_x_scoped,
    inject_rasa_x_user,
    validate_schema,
)
from ragex.community.constants import REQUEST_DB_SESSION_KEY
from ragex.community.services.nlg_service import NlgService
from ragex.community.services.domain_service import DomainService
from ragex.community.utils import error

logger = logging.getLogger(__name__)


def _nlg_service(request: Request) -> NlgService:
    return NlgService(request[REQUEST_DB_SESSION_KEY])


def _domain_service(request: Request) -> DomainService:
    return DomainService(request[REQUEST_DB_SESSION_KEY])


def blueprint() -> Blueprint:
    nlg_endpoints = Blueprint("nlg_endpoints")

    @nlg_endpoints.route("/templates", methods=["GET", "HEAD"])
    @rasa_x_scoped("responseTemplates.list", allow_api_token=True)
    async def get_templates(request):
        text_query = utils.default_arg(request, "q", None)
        template_query = utils.default_arg(request, "template", None)
        fields = utils.fields_arg(request, {"text", "template", "id"})

        limit = utils.int_arg(request, "limit")
        offset = utils.int_arg(request, "offset", 0)

        templates, total_number = _nlg_service(request).fetch_templates(
            text_query, template_query, fields, limit, offset
        )

        return response.json(templates, headers={"X-Total-Count": total_number})

    @nlg_endpoints.route("/responseGroups", methods=["GET", "HEAD"])
    @rasa_x_scoped("responseTemplates.list", allow_api_token=True)
    async def get_grouped_templates(request):
        text_query = utils.default_arg(request, "q", None)
        template_query = utils.default_arg(request, "template", None)

        templates, total_number = _nlg_service(request).get_grouped_responses(
            text_query, template_query
        )

        return response.json(templates, headers={"X-Total-Count": total_number})

    @nlg_endpoints.route("/responseGroups/<template_name>", methods=["PUT"])
    @rasa_x_scoped("responseTemplates.update")
    @inject_rasa_x_user()
    @validate_schema("nlg/template")
    async def rename_template(request, template_name, user):
        template = request.json
        _nlg_service(request).rename_templates(
            template_name, template, user["username"]
        )
        return response.text("", status=200)

    @nlg_endpoints.route("/templates", methods=["POST"])
    @rasa_x_scoped("responseTemplates.create", allow_api_token=True)
    @inject_rasa_x_user(allow_api_token=True)
    @validate_schema("nlg/response")
    async def add_template(request, user):
        rjs = request.json
        domain_id = _domain_service(request).get_domain_id()
        saved_response = _nlg_service(request).save_template(
            rjs, user["username"], domain_id=domain_id
        )
        _domain_service(request).dump_domain()
        return response.json(saved_response, 201)

    @nlg_endpoints.route("/templates", methods=["PUT"])
    @rasa_x_scoped("bulkResponseTemplates.update", allow_api_token=True)
    @inject_rasa_x_user(allow_api_token=True)
    @validate_schema("nlg/response_bulk")
    async def update_templates(request, user=None):
        """Delete old bot responses and replace them with the responses in the
        payload."""

        rjs = request.json
        domain_id = _domain_service(request).get_domain_id()
        inserted_count = _nlg_service(request).replace_templates(
            rjs, user["username"], domain_id=domain_id
        )
        _domain_service(request).dump_domain()
        return response.text(f"Successfully uploaded {inserted_count} responses.")

    @nlg_endpoints.route("/templates/<response_id>", methods=["PUT"])
    @rasa_x_scoped("responseTemplates.update", allow_api_token=True)
    @inject_rasa_x_user(allow_api_token=True)
    @validate_schema("nlg/response")
    async def modify_template(request, response_id, user):
        rjs = request.json
        updated_response = _nlg_service(request).update_template(response_id, rjs, user)
        _domain_service(request).dump_domain()
        if not updated_response:
            return error(404, "ResponseNotFound", "Response could not be found.")
        return response.json(updated_response)

    @nlg_endpoints.route("/templates/<response_id>", methods=["DELETE"])
    @rasa_x_scoped("responseTemplates.delete", allow_api_token=True)
    async def delete_template(request, response_id):
        deleted = _nlg_service(request).delete_template(response_id)
        if deleted:
            _domain_service(request).dump_domain()
            return response.text("", 204)
        return error(404, "ResponseNotFound", "Response could not be found.")

    return nlg_endpoints

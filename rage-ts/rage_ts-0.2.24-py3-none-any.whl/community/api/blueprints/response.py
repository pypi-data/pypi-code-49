import logging
import os

import time
from sanic.request import Request
from sanic import Blueprint, response
from ragex.community.api.decorators import rasa_x_scoped, inject_rasa_x_user, validate_schema
from ragex.community.constants import (
    REQUEST_DB_SESSION_KEY,
    DEFAULT_RASA_ENVIRONMENT,
    RASA_PRODUCTION_ENVIRONMENT
)
import ragex.community.utils as rasa_x_utils
from ragex.community.utils import error

from ragex.community import utils, config, metrics
from ragex.community.services.response_service import ResponseService

logger = logging.getLogger(__name__)


def _response_servie(request: Request) -> ResponseService:
    session = request[REQUEST_DB_SESSION_KEY]
    return ResponseService(session, config.rasa_image_dir)


def blueprint() -> Blueprint:
    endpoints = Blueprint("response_endpoints")

    """ 등록되어 있는 모든 리스트 """
    @endpoints.route("/projects/<project_id>/responses", methods=["GET", "HEAD"])
    @rasa_x_scoped("responses.list", allow_api_token=True, allow_rasa_x_token=True )
    async def get_responses(request, project_id):
        limit = utils.int_arg(request, "limit")
        offset = utils.int_arg(request, "offset", 0)
        logger.debug(f"get_responses param: {project_id},{limit},{offset}")

        responses, total_responses_cnt = _response_servie(request).get_response_templates(
            project_id=project_id, limit=limit, offset=offset
        )
        return response.json(responses, headers={"X-Total-Count": total_responses_cnt})
        # return response.json({"result": "temp result", "add result": "add"}, headers={"X-Total-Count": 1})

    """ intent 명과 일치하는 모든 리스트 """
    @endpoints.route("/projects/<project_id>/response/<intent>", methods=["GET", "HEAD"])
    @rasa_x_scoped("response.getIntent", allow_api_token=True, allow_rasa_x_token=True)
    async def get_response(request, project_id, intent):
        logger.debug(f"get_response param: {project_id},{intent}")

        result_response, total_responses_cnt = _response_servie(request).get_response_intent_template(
            project_id=project_id, intent=intent
        )
        return response.json(result_response, headers={"X-Total-Count": total_responses_cnt})
        # return response.json({"result": "temp result", "add result": "add"}, headers={"X-Total-Count": 1})

    """ intent 명과 일치하는 모든 리스트 """

    @endpoints.route("/projects/<project_id>/response/<intent>/<response_type>", methods=["GET", "HEAD"])
    @rasa_x_scoped("response.get", allow_api_token=True, allow_rasa_x_token=True)
    async def get_response(request, project_id, intent, response_type):
        logger.debug(f"get_response param: {project_id},{intent} {response_type}")

        result_response, total_responses_cnt = _response_servie(request).get_response_template(
            project_id=project_id, intent=intent, response_type=response_type
        )
        return response.json(result_response, headers={"X-Total-Count": total_responses_cnt})
        # return response.json({"result": "temp result", "add result": "add"}, headers={"X-Total-Count": 1})



    """ intent response 내역 삭제 """
    # noinspection PyUnusedLocal
    @endpoints.route("/projects/<project_id>/response/<intent>/<response_type>", methods=["DELETE"])
    @rasa_x_scoped("response.delete", allow_api_token=True, allow_rasa_x_token=True)
    async def delete_response(request, project_id, intent, response_type):
        logger.debug(f"delete_response param: {project_id},{intent},{response_type} ")
        try:
            _response_servie(request).delete_response_template(intent=intent, response_type=response_type)
            return response.text("", 204)
        except ValueError as e:
            return rasa_x_utils.error(
                404, "ResponseDeleteFailed", "Failed to delete response template", details=e
            )

    """ create intent response """
    @endpoints.route("/projects/<project_id>/response", methods=["POST"])
    @rasa_x_scoped("response.create")
    @validate_schema("intent_res_template/new")
    async def create_response(request, project_id):
        param = request.json
        response_service = _response_servie(request)
        try:
            response_service.add_response_template(intent=param["intent"],
                                                   use_yn=param["use_yn"],
                                                   response_type=param["response_type"],
                                                   response_template=param["response_template"])
            return response.text("response template '{}' created".format(param["intent"]), 201)
        except ValueError as e:
            logger.error(e)
            return error(
                400,
                "ResponseCreateFailed",
                "Failed to create response template",
                details=e
            )

    @endpoints.route("/projects/<project_id>/response", methods=["PUT"])
    @rasa_x_scoped("response.update")
    @validate_schema("intent_res_template/update")
    async def update_response(request, project_id):
        param = request.json
        response_service = _response_servie(request)
        try:
            response_service.update_response_template(intent=param["intent"],
                                                      use_yn=param["use_yn"],
                                                      response_type=param["response_type"],
                                                      response_template=param["response_template"])
            return response.text("response template '{}' updated".format(param["intent"]), 200)

        except ValueError as e:
            logger.error(e)
            return error(
                400,
                "ResponseUpdateFailed",
                "Failed to update response template",
                details=e
            )

    return endpoints


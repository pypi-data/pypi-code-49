import logging
import os

import time
from aiohttp import ClientError
from ruamel.yaml import YAMLError
from sanic import Blueprint, response
from sanic.request import Request

import ragex.community.utils as rasa_x_utils
from rasa.nlu.config import InvalidConfigError
from ragex.community import utils, config, metrics
from ragex.community.api.decorators import rasa_x_scoped, inject_rasa_x_user
from ragex.community.constants import (
    REQUEST_DB_SESSION_KEY,
    DEFAULT_RASA_ENVIRONMENT,
    RASA_PRODUCTION_ENVIRONMENT,
)
from ragex.community.services.model_service import ModelService
from ragex.community.services.nlg_service import NlgService
from ragex.community.services.settings_service import SettingsService

logger = logging.getLogger(__name__)


def _model_service(request: Request) -> ModelService:
    session = request[REQUEST_DB_SESSION_KEY]
    return ModelService(config.rasa_model_dir, session, DEFAULT_RASA_ENVIRONMENT)


def blueprint() -> Blueprint:
    endpoints = Blueprint("model_endpoints")

    @endpoints.route("/projects/<project_id>/models", methods=["GET", "HEAD"])
    @rasa_x_scoped("models.list", allow_api_token=True, allow_rasa_x_token=True)
    async def get_models(request, project_id):
        limit = utils.int_arg(request, "limit")
        offset = utils.int_arg(request, "offset", 0)

        models, total_models = await _model_service(request).get_models(
            project_id, limit, offset
        )

        return response.json(models, headers={"X-Total-Count": total_models})

    @endpoints.route("/projects/<project_id>/models", methods=["POST"])
    @rasa_x_scoped("models.create", allow_api_token=True, allow_rasa_x_token=True)
    async def upload_model(request, project_id):
        model_service = _model_service(request)
        try:
            tpath = model_service.save_model_to_disk(request)
        except (FileNotFoundError, ValueError) as e:
            return rasa_x_utils.error(
                404, "ModelSaveError", f"Could not save model.\n{e}"
            )

        minimum_version = await model_service.minimum_compatible_version()

        if not model_service.is_model_compatible(minimum_version, fpath=tpath):
            return rasa_x_utils.error(
                404, "ModelVersionError", "Model version unsupported."
            )

        try:
            filename = os.path.basename(tpath)
            model_name = filename.split(".tar.gz")[0]
            saved = await model_service.save_uploaded_model(
                project_id, model_name, tpath
            )
            if saved:
                metrics.track(metrics.MODEL_UPLOADED_EVENT)
                return response.text("", 204)
            return rasa_x_utils.error(
                404,
                "ModelSaveError",
                "Model could not be saved.\nModel name '{}'."
                "File path '{}'.".format(model_name, tpath),
            )
        except FileExistsError:
            return rasa_x_utils.error(
                404, "ModelExistsError", "A model with that name already exists."
            )

    @endpoints.route(
        "/projects/<project_id>/models/tags/<tag>", methods=["GET", "HEAD"]
    )
    @rasa_x_scoped(
        "models.modelByTag.get", allow_api_token=True, allow_rasa_x_token=True
    )
    async def get_model_for_tag(request, project_id, tag):
        model = _model_service(request).model_for_tag(project_id, tag)
        if not model:
            return rasa_x_utils.error(
                404, "TagNotFound", f"Tag '{tag}' not found for project '{project_id}'."
            )
        model_hash = model["hash"]
        try:
            if model_hash == request.headers.get("If-None-Match"):
                return response.text("", 204)

            return await response.file_stream(
                location=model["path"],
                headers={
                    "ETag": model_hash,
                    "filename": os.path.basename(model["path"]),
                },
                mime_type="application/gzip",
            )
        except FileNotFoundError:
            logger.warning(
                "Tried to download model file '{}', "
                "but file does not exist.".format(model["path"])
            )
            return rasa_x_utils.error(
                404,
                "ModelDownloadFailed",
                "Failed to find model file '{}'.".format(model["path"]),
            )

        except Exception as e:
            logger.exception(e)
            return rasa_x_utils.error(
                500, "ModelDownloadError", f"Failed to download file.\n{e}"
            )

    @endpoints.route("/projects/<project_id>/models/<model>", methods=["GET", "HEAD"])
    @rasa_x_scoped("models.get", allow_api_token=True, allow_rasa_x_token=True)
    async def get_model_by_name(request, project_id, model):
        model = _model_service(request).get_model_by_name(project_id, model)
        if not model:
            return rasa_x_utils.error(
                404,
                "ModelNotFound",
                f"Model '{model}' not found for project '{project_id}'.",
            )
        model_hash = model["hash"]
        try:
            if model_hash == request.headers.get("If-None-Match"):
                return response.text("", 204)

            return await response.file_stream(
                location=model["path"],
                headers={
                    "ETag": model_hash,
                    "filename": os.path.basename(model["path"]),
                },
                mime_type="application/gzip",
            )
        except Exception as e:
            logger.exception(e)
            return rasa_x_utils.error(
                404, "ModelDownloadFailed", f"Failed to download file.\n{e}"
            )

    # noinspection PyUnusedLocal
    @endpoints.route("/projects/<project_id>/models/<model>", methods=["DELETE"])
    @rasa_x_scoped("models.delete", allow_api_token=True)
    async def delete_model(request, project_id, model):
        deleted = _model_service(request).delete_model(project_id, model)
        if deleted:
            return response.text("", 204)

        return rasa_x_utils.error(
            404, "ModelDeleteFailed", f"Failed to delete model '{model}'."
        )

    @endpoints.route("/projects/<project_id>/models/jobs", methods=["POST"])
    @rasa_x_scoped("models.jobs.create", allow_api_token=True)
    async def train_model(request, project_id):
        stack_services = SettingsService(
            request[REQUEST_DB_SESSION_KEY]
        ).stack_services(project_id)
        environment = utils.deployment_environment_from_request(request, "worker")
        stack_service = stack_services[environment]

        try:
            training_start = time.time()
            content = await stack_service.start_training_process()

            metrics.track(metrics.MODEL_TRAINED_EVENT)

            model_name = await _model_service(request).save_trained_model(
                project_id, content
            )

            nlg_service = NlgService(request[REQUEST_DB_SESSION_KEY])
            nlg_service.mark_templates_as_used(training_start)

            return response.json({"info": "New model trained.", "model": model_name})
        except FileExistsError as e:
            logger.error(e)
            return response.json({"info": "Model already exists.", "path": e})
        except ClientError as e:
            logger.error(e)
            return rasa_x_utils.error(
                500, "StackTrainingFailed", "Failed to train a Rasa model.", details=e
            )

    # noinspection PyUnusedLocal
    @endpoints.route(
        "/projects/<project_id>/models/<model>/tags/<tag>", methods=["PUT"]
    )
    @rasa_x_scoped("models.tags.update", allow_api_token=True)
    async def tag_model(request, project_id, model, tag):
        try:
            tagged_model = await _model_service(request).tag_model(
                project_id, model, tag
            )
            if tag == RASA_PRODUCTION_ENVIRONMENT:
                metrics.track(metrics.MODEL_PROMOTED_EVENT)

            return response.text("", 204)
        except ValueError as e:
            return rasa_x_utils.error(
                404, "ModelTagError", f"Failed to tag model '{model}'.", details=e
            )

    # noinspection PyUnusedLocal
    @endpoints.route(
        "/projects/<project_id>/models/<model>/tags/<tag>", methods=["DELETE"]
    )
    @rasa_x_scoped("models.tags.delete", allow_api_token=True)
    async def untag(request, project_id, model, tag):
        try:
            _model_service(request).delete_tag(project_id, model, tag)
            return response.text("", 204)
        except ValueError as e:
            return rasa_x_utils.error(
                404, "TagDeletionFailed", "Failed to delete model tag", details=e
            )

    @endpoints.route("/projects/<project_id>/settings", methods=["GET", "HEAD"])
    @rasa_x_scoped("models.settings.get", allow_api_token=True)
    @inject_rasa_x_user(allow_api_token=True)
    async def get_model_config(request, project_id, user=None):
        settings_service = SettingsService(request[REQUEST_DB_SESSION_KEY])
        stack_config = settings_service.get_config(user["team"], project_id)
        if not stack_config:
            return rasa_x_utils.error(404, "SettingsFailed", "Could not find settings.")

        yaml_config = rasa_x_utils.dump_yaml(stack_config)

        return response.text(yaml_config)

    @endpoints.route("/projects/<project_id>/settings", methods=["PUT"])
    @rasa_x_scoped("models.settings.update")
    @inject_rasa_x_user()
    async def save_model_config(request, project_id, user=None):
        settings_service = SettingsService(request[REQUEST_DB_SESSION_KEY])
        try:
            config_yaml = settings_service.inspect_and_save_yaml_config_from_request(
                request.body, user["team"], project_id
            )
            return response.text(config_yaml)
        except YAMLError as e:
            return rasa_x_utils.error(
                400, "InvalidConfig", f"Failed to read configuration file.  Error: {e}"
            )
        except InvalidConfigError as e:
            return rasa_x_utils.error(422, "ConfigMissingKeys", f"Error: {e}")
        except Exception as e:
            return rasa_x_utils.error(
                500,
                "SaveModelConfigFailed",
                f"Could not save Rasa model config. Error: {e}",
            )

    return endpoints

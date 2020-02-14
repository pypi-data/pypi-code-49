import logging
from typing import Text

import time
from aiohttp import ClientError
from sanic import Blueprint, response
from sanic.request import Request

from rasa.cli.utils import print_success
import rasa.core.utils as rasa_core_utils
import ragex.community.jwt
import ragex.community.utils as rasa_x_utils
from rasa.core import events
from rasa.core.trackers import EventVerbosity
from rasa.core.training.dsl import StoryParseError
from rasa.core.training.structures import Story
from ragex.community import config, metrics
from ragex.community.api.decorators import (
    rasa_x_scoped,
    inject_rasa_x_user,
    validate_schema,
)
from ragex.community.constants import (
    REQUEST_DB_SESSION_KEY,
    DEFAULT_RASA_ENVIRONMENT,
    RASA_PRODUCTION_ENVIRONMENT,
)
from ragex.community.services.data_service import DataService
from ragex.community.services.domain_service import DomainService
from ragex.community.services.event_service import EventService
from ragex.community.services.logs_service import LogsService
from ragex.community.services.role_service import RoleService
from ragex.community.services.role_service import (
    normalise_permissions,
    guest_permissions,
)
from ragex.community.services.settings_service import SettingsService
from ragex.community.services.stack_service import StackService
from ragex.community.services.story_service import StoryService
from ragex.community.services.user_service import has_role, ADMIN, GUEST

logger = logging.getLogger(__name__)


def _event_verbosity_from_request(request):
    if rasa_x_utils.bool_arg(request, "history", default=True):
        return EventVerbosity.ALL
    else:
        return EventVerbosity.AFTER_RESTART


def _story_service(request: Request) -> StoryService:
    return StoryService(request[REQUEST_DB_SESSION_KEY])


def _domain_service(request: Request) -> DomainService:
    return DomainService(request[REQUEST_DB_SESSION_KEY])


def _stack_service(request: Request, default_environment: Text) -> StackService:
    settings_service = SettingsService(request[REQUEST_DB_SESSION_KEY])

    environment = rasa_x_utils.deployment_environment_from_request(
        request, default_environment
    )
    service = settings_service.get_stack_service(environment)
    if not service:
        raise ValueError(f"Service for requested environment '{environment}' not found")

    return service


def _event_service(request: Request) -> EventService:
    return EventService(request[REQUEST_DB_SESSION_KEY])


def _role_service(request: Request) -> RoleService:
    return RoleService(request[REQUEST_DB_SESSION_KEY])


def blueprint() -> Blueprint:
    stack_endpoints = Blueprint("stack_endpoints")

    @stack_endpoints.route("/conversations", methods=["GET", "HEAD"])
    @rasa_x_scoped("metadata.get", allow_api_token=True)
    @inject_rasa_x_user()
    async def list_clients(request, user=None):
        role_service = _role_service(request)
        event_service = _event_service(request)
        user_name = user["username"]

        if role_service.is_user_allowed_to_view_all_conversations(user):
            clients, number_clients = _get_all_clients(
                request, user_name, event_service
            )
        else:
            clients = [event_service.get_conversation_metadata_for_client(user_name)]
            # remove potential `None` value
            clients = [client for client in clients if client]
            number_clients = len(clients)

        return response.json(clients, headers={"X-Total-Count": number_clients})

    def _get_all_clients(
        request: Request, user_name: Text, event_service: EventService
    ) -> rasa_x_utils.QueryResult:
        sort_by_latest_event_time = rasa_x_utils.bool_arg(
            request, "sort_by_latest_event_time", True
        )
        sort_by_confidence = rasa_x_utils.bool_arg(request, "sort_by_confidence", True)
        in_training_data = rasa_x_utils.default_arg(request, "in_training_data", None)
        if in_training_data is not None:
            in_training_data = in_training_data.lower() == "true"

        include_interactive = rasa_x_utils.default_arg(request, "interactive", False)
        start = rasa_x_utils.time_arg(request, "start", None)
        until = rasa_x_utils.time_arg(request, "until", None)
        maximum_confidence = rasa_x_utils.float_arg(request, "maximumConfidence")
        minimum_user_messages = rasa_x_utils.int_arg(request, "minimumUserMessages")
        policies = rasa_x_utils.default_arg(request, "policies", None)
        intent_query = rasa_x_utils.default_arg(request, "intent", None)
        entity_query = rasa_x_utils.default_arg(request, "entity", None)
        text_query = rasa_x_utils.default_arg(request, "text", None)
        rasa_environment_query = rasa_x_utils.default_arg(
            request, "rasa_environment", DEFAULT_RASA_ENVIRONMENT
        )
        action_query = rasa_x_utils.default_arg(request, "action", None)
        flag_query = rasa_x_utils.bool_arg(request, "is_flagged", False)
        limit = rasa_x_utils.int_arg(request, "limit")
        offset = rasa_x_utils.int_arg(request, "offset", 0)

        exclude = (
            [user_name]
            if rasa_x_utils.bool_arg(request, "exclude_self", False)
            else None
        )
        return event_service.get_conversation_metadata_for_all_clients(
            start=start,
            until=until,
            maximum_confidence=maximum_confidence,
            minimum_user_messages=minimum_user_messages,
            policies=policies,
            in_training_data=in_training_data,
            intent_query=intent_query,
            entity_query=entity_query,
            action_query=action_query,
            sort_by_date=sort_by_latest_event_time,
            sort_by_confidence=sort_by_confidence,
            text_query=text_query,
            rasa_environment_query=rasa_environment_query,
            only_flagged=flag_query,
            include_interactive=include_interactive,
            exclude=exclude,
            limit=limit,
            offset=offset,
        )

    @stack_endpoints.route("/conversations", methods=["POST"])
    @rasa_x_scoped("metadata.create", allow_api_token=True)
    @validate_schema("conversation")
    async def create_conversation(request):
        conversation = request.json
        try:
            inserted = _event_service(request).create_conversation_from(conversation)

            # initialise tracker (will just contain action_listen)
            await _stack_service(
                request, RASA_PRODUCTION_ENVIRONMENT
            ).initialise_tracker_for_conversation(inserted["sender_id"])

            return response.json(inserted, 201)
        except ClientError as e:
            return rasa_x_utils.error(
                500,
                "ConversationCreationFailed",
                "Error while trying to create conversation.",
                details=e,
            )
        except ValueError as e:
            return rasa_x_utils.error(400, "SenderIdExists", details=e)

    @stack_endpoints.route("/conversations/<conversation_id>", methods=["GET", "HEAD"])
    @rasa_x_scoped("clients.get", allow_api_token=True)
    @inject_rasa_x_user(allow_api_token=True, extract_user_from_jwt=True)
    async def get_events(request, conversation_id, user=None):
        print_success(f"{conversation_id} , {request}")
        if not has_role(user, ADMIN) and conversation_id != user["username"]:
            return rasa_x_utils.error(401, "NoPermission", "Access denied")


        until_time = rasa_x_utils.float_arg(request, "until", None)
        since_time = rasa_x_utils.float_arg(request, "since", None)
        rasa_environment_query = rasa_x_utils.default_arg(
            request, "rasa_environment", DEFAULT_RASA_ENVIRONMENT
        )
        event_verbosity = _event_verbosity_from_request(request)
        exclude_leading_action_session_start = rasa_x_utils.bool_arg(
            request, "exclude_leading_action_session_start", False
        )
        logger.debug(f"get_events request:{request}")
        logger.debug(f"get_events conversation_id:{conversation_id}")
        tracker = _event_service(request).get_tracker_with_message_flags(
            conversation_id,
            until_time,
            since_time,
            event_verbosity,
            rasa_environment_query,
            exclude_leading_action_session_start,
        )

        if not tracker:
            return rasa_x_utils.error(
                404,
                "ClientNotFound",
                f"Client for conversation_id '{conversation_id}' could not be found",
            )

        requested_format = request.headers.get("Accept")

        if requested_format == "application/json":
            dispo = f"attachment;filename={conversation_id}-dump.json"
            return response.json(
                tracker,
                content_type="application/json",
                headers={"Content-Disposition": dispo},
            )
        elif requested_format == "text/markdown":
            _events = events.deserialise_events(tracker["events"])
            story = Story.from_events(_events)
            exported = story.as_story_string(flat=True)
            return response.text(
                exported,
                content_type="text/markdown",
                headers={
                    "Content-Disposition": f"attachment;filename={conversation_id}-story.md"
                },
            )
        else:
            return response.json(tracker, headers={"Content-Disposition": "inline"})

    @stack_endpoints.route("/conversationActions", methods=["GET", "HEAD"])
    @rasa_x_scoped("conversationActions.list", allow_api_token=True)
    async def unique_actions(request):
        actions = _event_service(request).get_unique_actions()
        return response.json(actions, headers={"X-Total-Count": len(actions)})

    @stack_endpoints.route("/conversationIntents", methods=["GET", "HEAD"])
    @rasa_x_scoped("conversationIntents.list", allow_api_token=True)
    async def unique_intents(request):
        intents = _event_service(request).get_unique_intents()
        return response.json(intents, headers={"X-Total-Count": len(intents)})

    @stack_endpoints.route("/conversationEntities", methods=["GET", "HEAD"])
    @rasa_x_scoped("conversationEntities.list", allow_api_token=True)
    async def unique_entities(request):
        entities = _event_service(request).get_unique_entities()
        return response.json(entities, headers={"X-Total-Count": len(entities)})

    @stack_endpoints.route("/conversationPolicies", methods=["GET", "HEAD"])
    @rasa_x_scoped("conversationPolicies.list", allow_api_token=True)
    async def unique_policies(request):
        policies = _event_service(request).get_unique_policies()
        return response.json(policies, headers={"X-Total-Count": len(policies)})

    @stack_endpoints.route("/conversations/<conversation_id>/events", methods=["POST"])
    @rasa_x_scoped("clientEvents.create", allow_api_token=True)
    @inject_rasa_x_user()
    async def post_event(request, conversation_id, user):
        _event = request.json
        try:
            _ = await _stack_service(
                request, RASA_PRODUCTION_ENVIRONMENT
            ).append_events_to_tracker(conversation_id, _event)

            if LogsService.is_user_uttered_event(_event):
                # add annotated user messages to training data
                data_service = DataService(request[REQUEST_DB_SESSION_KEY])
                data_service.save_user_event_as_example(
                    user, config.project_name, _event
                )

                metrics.track_message_annotated(
                    metrics.MESSAGE_ANNOTATED_INTERACTIVE_LEARNING
                )

            return response.json(_event)
        except ClientError as e:
            logger.warning(
                f"Creating event for sender '{conversation_id}' failed. Error: {e}"
            )
            return rasa_x_utils.error(
                500,
                "EventCreationError",
                f"Error when creating event for sender '{conversation_id}'.",
                details=e,
            )
        except ValueError as e:
            return rasa_x_utils.error(404, "ServiceNotFound", details=e)

    @stack_endpoints.route("/conversations/<conversation_id>/events", methods=["PUT"])
    @rasa_x_scoped("clientEvents.update", allow_api_token=True)
    async def update_events(request, conversation_id):
        _events = request.json
        try:
            _ = await _stack_service(
                request, RASA_PRODUCTION_ENVIRONMENT
            ).update_events(conversation_id, _events, _event_service(request))
            return response.json(_events)
        except ClientError as e:
            logger.warning(
                f"Updating events for sender '{conversation_id}' failed. Error: {e}"
            )
            return rasa_x_utils.error(
                500,
                "EventUpdatingError",
                f"Error when updating events for sender '{conversation_id}'.",
            )

    @stack_endpoints.route("/conversations/<conversation_id>/execute", methods=["POST"])
    @rasa_x_scoped("actionPrediction.create", allow_api_token=True)
    async def execute_action(request, conversation_id):
        action = request.json
        event_verbosity = _event_verbosity_from_request(request)

        try:
            result = await _stack_service(
                request, RASA_PRODUCTION_ENVIRONMENT
            ).execute_action(conversation_id, action, event_verbosity)
            return response.json(result)
        except ClientError as e:
            logger.warning(
                f"Executing action for sender '{conversation_id}' failed. Error: {e}"
            )
            return rasa_x_utils.error(
                500,
                "ActionExecutionFailed",
                f"Error when executing action for sender '{conversation_id}'.",
            )

    @stack_endpoints.route(
        "/conversations/<conversation_id>/messages", methods=["GET", "HEAD"]
    )
    @rasa_x_scoped("clientMessages.list")
    @inject_rasa_x_user()
    async def get_messages(request, conversation_id, user=None):
        if not has_role(user, ADMIN) and conversation_id != user["username"]:
            return rasa_x_utils.error(401, "NoPermission", "Access denied")

        until_time = rasa_x_utils.float_arg(request, "until", None)
        event_verbosity = _event_verbosity_from_request(request)
        tracker = _event_service(request).get_messages_for(
            conversation_id, until_time, event_verbosity
        )

        if not tracker:
            return rasa_x_utils.error(
                404,
                "ClientNotFound",
                f"Client for conversation_id '{conversation_id}' could not be found.",
            )

        return response.json(
            tracker, headers={"X-Total-Count": len(tracker.get("messages"))}
        )

    @stack_endpoints.route(
        "/conversations/<conversation_id>/messages", methods=["POST"]
    )
    @rasa_x_scoped("messages.create")
    async def send_message(request, conversation_id):
        return await chat_to_bot(request, conversation_id)

    @stack_endpoints.route("/statistics", methods=["GET", "HEAD"])
    @rasa_x_scoped("statistics.get")
    @inject_rasa_x_user()
    async def get_statistics(request, user=None):
        event_service = _event_service(request)
        if not has_role(user, ADMIN):
            stats = event_service.user_statistics_dict()
        else:
            stats = event_service.get_statistics()
        return response.json(stats)

    @stack_endpoints.route("/stories", methods=["GET", "HEAD"])
    @rasa_x_scoped("stories.list", allow_api_token=True)
    async def get_stories(request):
        from rasa.core.domain import Domain

        text_query = rasa_x_utils.default_arg(request, "q", None)
        fields = rasa_x_utils.fields_arg(request, {"name", "annotation.user", "id"})
        id_query = rasa_x_utils.list_arg(request, "id")

        distinct = rasa_x_utils.bool_arg(request, "distinct", True)
        stories = _story_service(request).fetch_stories(
            text_query, fields, id_query=id_query, distinct=distinct
        )

        content_type = request.headers.get("Accept")
        if content_type == "text/vnd.graphviz":
            project_id = rasa_x_utils.default_arg(
                request, "project_id", config.project_name
            )
            domain_dict = _domain_service(request).get_or_create_domain(project_id)
            domain = Domain.from_dict(domain_dict)

            visualization = await _story_service(request).visualize_stories(
                stories, domain
            )

            if visualization:
                return response.text(visualization)
            else:
                return rasa_x_utils.error(
                    406,
                    "VisualizationNotAvailable",
                    "Cannot produce a visualization for the requested stories",
                )
        elif content_type == "text/markdown":
            markdown = _story_service(request).get_stories_markdown(stories)
            return response.text(
                markdown,
                content_type="text/markdown",
                headers={"Content-Disposition": "attachment;filename=stories.md"},
            )
        else:
            return response.json(stories, headers={"X-Total-Count": len(stories)})

    @stack_endpoints.route("/stories/<story_id>", methods=["GET", "HEAD"])
    @rasa_x_scoped("stories.get", allow_api_token=True)
    async def get_story(request, story_id):
        from rasa.core.domain import Domain

        story = _story_service(request).fetch_story(story_id)

        content_type = request.headers.get("Accept")
        if content_type == "text/vnd.graphviz":
            project_id = rasa_x_utils.default_arg(
                request, "project_id", config.project_name
            )
            domain_dict = _domain_service(request).get_or_create_domain(project_id)
            domain = Domain.from_dict(domain_dict)

            visualization = await _story_service(request).visualize_stories(
                [story], domain
            )

            if visualization:
                return response.text(visualization)
            else:
                return rasa_x_utils.error(
                    406,
                    "VisualizationNotAvailable",
                    "Cannot produce a visualization for the requested story",
                )
        else:
            if story:
                return response.json(story)

        return rasa_x_utils.error(
            404, "StoryNotFound", f"Story for id {story_id} could not be found"
        )

    @stack_endpoints.route("/evaluate", methods=["POST"])
    @rasa_x_scoped("allEvaluations.create")
    async def update_conversation_evaluations(request):
        event_service = _event_service(request)
        conversation_ids = event_service.sender_ids()
        for _id in conversation_ids:
            story = event_service.story_for_sender_id(_id)
            try:
                content = await _stack_service(request, "worker").evaluate_story(story)
                event_service.update_evaluation(_id, content)
            except ClientError as e:
                return rasa_x_utils.error(
                    500,
                    "CoreEvaluationFailed",
                    f"Failed to create evaluation for conversation with ID '{_id}'.",
                    details=e,
                )
            except ValueError as e:
                return rasa_x_utils.error(
                    404,
                    "StoringEvaluationFailed",
                    f"Failed to store evaluation for conversation_id '{_id}'. Conversation not found.",
                    details=e,
                )

        return response.text("", 204)

    @stack_endpoints.route("/evaluations", methods=["GET", "HEAD"])
    @rasa_x_scoped("allEvaluations.list")
    async def get_evaluations(request):
        event_service = _event_service(request)
        conversation_ids = event_service.sender_ids()
        evaluations = []
        for _id in conversation_ids:
            _eval = event_service.get_evaluation(_id)
            evaluations.append({_id: _eval})
        return response.json(evaluations, headers={"X-Total-Count": len(evaluations)})

    @stack_endpoints.route(
        "/conversations/<conversation_id>/evaluation", methods=["GET", "HEAD"]
    )
    @rasa_x_scoped("clientEvaluation.get")
    async def get_evaluation(request, conversation_id):
        evaluation = _event_service(request).get_evaluation(conversation_id)
        return response.json(evaluation)

    @stack_endpoints.route(
        "/conversations/<conversation_id>/evaluation", methods=["DELETE"]
    )
    @rasa_x_scoped("clientEvaluation.delete")
    async def delete_evaluation(request, conversation_id):
        _event_service(request).delete_evaluation(conversation_id)
        return response.text("", 204)

    @stack_endpoints.route(
        "/conversations/<conversation_id>/evaluation", methods=["PUT"]
    )
    @rasa_x_scoped("clientEvaluation.update")
    async def put_evaluation(request, conversation_id):
        event_service = _event_service(request)
        story = event_service.story_for_sender_id(conversation_id)

        if not story:
            return rasa_x_utils.error(
                404,
                "ClientNotFound",
                f"Client for conversation_id {conversation_id} could not be found",
            )

        try:
            content = await _stack_service(request, "worker").evaluate_story(story)
            event_service.update_evaluation(conversation_id, content)

            return response.json(content)
        except ClientError as e:
            return rasa_x_utils.error(
                500,
                "CoreEvaluationFailed",
                f"Failed to create evaluation for conversation_id {conversation_id}",
                details=e,
            )
        except ValueError as e:
            return rasa_x_utils.error(
                404,
                "StoringEvaluationFailed",
                f"Failed to store evaluation for conversation_id '{conversation_id}'.",
                details=e,
            )

    @stack_endpoints.route("/conversations/<conversation_id>/predict", methods=["POST"])
    @rasa_x_scoped("actionPrediction.get")
    async def predict_next_action(request, conversation_id):
        included_events = rasa_x_utils.default_arg(request, "include_events", "ALL")

        try:
            content = await _stack_service(
                request, RASA_PRODUCTION_ENVIRONMENT
            ).predict_next_action(conversation_id, included_events)
            return response.json(content)
        except ClientError as e:
            logger.warning(f"Model training failed. Error: {e}")
            return rasa_x_utils.error(
                500,
                "ActionPredictionFailed",
                f"Failed to predict the next action for conversation_id '{conversation_id}'.",
                details=e,
            )

    @stack_endpoints.route(
        "/conversations/<conversation_id>/messages/<message_timestamp>/flag",
        methods=["PUT"],
    )
    @rasa_x_scoped("messageFlags.update")
    async def flag_message(request, conversation_id, message_timestamp):
        try:
            message = float(message_timestamp)
            _event_service(request).add_flagged_message(conversation_id, message)
            metrics.track(metrics.MESSAGE_FLAGGED_EVENT, {"set_flag": True})
            return response.text("", 201)
        except Exception as e:
            return rasa_x_utils.error(400, "Failed to flag message", e)

    @stack_endpoints.route(
        "/conversations/<conversation_id>/messages/<message_timestamp>/flag",
        methods=["DELETE"],
    )
    @rasa_x_scoped("messageFlags.delete")
    async def delete_flag_from_conversation(
        request, conversation_id, message_timestamp
    ):
        try:
            message = float(message_timestamp)
            _event_service(request).delete_flagged_message(conversation_id, message)
            metrics.track(metrics.MESSAGE_FLAGGED_EVENT, {"set_flag": False})
            return response.text("", 200)
        except Exception as e:
            return rasa_x_utils.error(400, "Failed to delete message flag", e)

    @stack_endpoints.route(
        "/conversations/<conversation_id>/messages/<message_timestamp>/intent",
        methods=["PUT"],
    )
    @rasa_x_scoped("messageIntents.update")
    @inject_rasa_x_user()
    @validate_schema("intent")
    async def correct_message(request, conversation_id, message_timestamp, user):
        try:
            message = float(message_timestamp)
            intent = request.json
            project_id = rasa_x_utils.default_arg(
                request, "project_id", config.project_name
            )
            _event_service(request).correct_message(
                conversation_id, message, intent, user, project_id
            )

            return response.text("", 200)
        except Exception as e:
            return rasa_x_utils.error(400, "MessageRelabellingError.", e)

    @stack_endpoints.route(
        "/conversations/<conversation_id>/messages/<message_timestamp>/intent",
        methods=["DELETE"],
    )
    @rasa_x_scoped("messageIntents.delete")
    async def delete_message_correction(request, conversation_id, message_timestamp):
        try:
            message = float(message_timestamp)

            project_id = rasa_x_utils.default_arg(
                request, "project_id", config.project_name
            )
            _event_service(request).delete_message_correction(
                conversation_id, message, project_id
            )
            return response.text("", 200)
        except Exception as e:
            return rasa_x_utils.error(400, "MessageRelabellingError.", e)

    @stack_endpoints.route("/stories", methods=["POST"])
    @rasa_x_scoped("stories.create")
    @inject_rasa_x_user(allow_api_token=True)
    async def add_stories(request, user=None):
        story_string = rasa_core_utils.convert_bytes_to_string(request.body)
        try:
            saved_stories = await _story_service(request).save_stories(
                story_string, user["team"], username=user["username"]
            )

            metrics.track_story_created(request.headers.get("Referer"))

            return response.json(
                saved_stories, headers={"X-Total-Count": len(saved_stories)}
            )
        except StoryParseError as e:
            logger.error(e.message)
            return rasa_x_utils.error(
                400, "StoryParseError", "Failed to parse story.", details=e.message
            )

    @stack_endpoints.route("/stories", methods=["PUT"])
    @rasa_x_scoped("bulkStories.update")
    @inject_rasa_x_user()
    async def add_bulk_stories(request, user=None):
        story_string = rasa_core_utils.convert_bytes_to_string(request.body)
        try:
            saved_stories = await _story_service(request).replace_stories(
                story_string, user["team"], username=user["username"]
            )
            if saved_stories is not None:
                return response.json(
                    saved_stories, headers={"X-Total-Count": len(saved_stories)}
                )
        except StoryParseError as e:
            logger.error(e.message)
            return rasa_x_utils.error(
                400, "StoryParseError", "Failed to parse stories.", details=e.message
            )

    @stack_endpoints.route("/stories.md", methods=["GET", "HEAD"])
    @rasa_x_scoped("bulkStories.get", allow_api_token=True)
    async def get_bulk_stories(request):
        request.headers["Accept"] = "text/markdown"
        return await get_stories(request)

    @stack_endpoints.route("/stories/<story_id>", methods=["PUT"])
    @rasa_x_scoped("stories.update")
    @inject_rasa_x_user()
    async def modify_story(request, story_id, user=None):
        story_string = rasa_core_utils.convert_bytes_to_string(request.body)
        try:
            updated_story = await _story_service(request).update_story(
                story_id, story_string, user
            )
            if not updated_story:
                return response.text("Story could not be found", 404)
            else:
                return response.json(updated_story)
        except StoryParseError as e:
            logger.error(e.message)
            return rasa_x_utils.error(
                400, "StoryParseError", "Failed to modify story.", details=e.message
            )

    @stack_endpoints.route("/stories/<story_id>", methods=["DELETE"])
    @rasa_x_scoped("stories.delete")
    async def delete_story(request, story_id):
        deleted = _story_service(request).delete_story(story_id)
        if deleted:
            return response.text("", 204)
        return rasa_x_utils.error(
            404,
            "StoryNotFound",
            f"Failed to delete story with story with id '{story_id}'.",
        )

    @stack_endpoints.route("/chat", methods=["POST"])
    @rasa_x_scoped("messages.create")
    @validate_schema("message")
    async def chat_to_bot(request, conversation_id=None):
        message_object = request.json

        if conversation_id:
            message_object["conversation_id"] = conversation_id

        environment = rasa_x_utils.deployment_environment_from_request(
            request, DEFAULT_RASA_ENVIRONMENT
        )
        service = _stack_service(request, DEFAULT_RASA_ENVIRONMENT)
        if not service:
            return rasa_x_utils.error(
                404,
                "ServiceNotFound",
                f"Service for requested environment '{environment}' not found.",
            )
        try:
            message_response = await service.send_message(
                message_object, token=request.headers.get("Authorization")
            )
            return response.json(message_response)
        except ClientError as e:
            logger.error(f"Failed to send message to Rasa Chat webhook. Error: {e}")
            return rasa_x_utils.error(
                404,
                "MessageSendFailed",
                "Message '{}' could not be sent to environment '{}'.".format(
                    message_object["message"], environment
                ),
            )

    @stack_endpoints.route("/auth/jwt", methods=["POST"])
    @validate_schema("signed_jwt")
    async def issue_signed_jwt(request):
        id_object = request.json
        chat_token = _domain_service(request).get_token()
        if not chat_token:
            return rasa_x_utils.error(
                404, "ChatTokenNotFound", "Could not find valid chat_token."
            )
        if id_object["chat_token"] != chat_token["chat_token"]:
            return rasa_x_utils.error(
                401, "InvalidChatToken", "Chat token is not valid."
            )

        if _domain_service(request).has_token_expired(id_object["chat_token"]):
            return rasa_x_utils.error(
                401, "ChatTokenExpired", "Chat token has expired."
            )

        # set JWT expiration to one day from current time or chat token
        # expiration time, whichever is lower
        expires = min(int(time.time()) + 24 * 60 * 60, chat_token["expires"])

        jwt_object = {
            "username": id_object["conversation_id"],
            "exp": expires,
            "user": {"username": id_object["conversation_id"], "roles": [GUEST]},
            "scopes": normalise_permissions(guest_permissions()),
        }

        encoded = ragex.community.jwt.encode_jwt(jwt_object, config.jwt_private_key)

        return response.json({"access_token": encoded})

    return stack_endpoints

import logging
import typing
from typing import Any, Dict, List, Optional, Text, Union, Tuple

from aiohttp import ClientError

import ragex.community.jwt
from rasa.core.events import Restarted
from rasa.core.trackers import EventVerbosity
from rasa.core.utils import dump_obj_as_yaml_to_string
from rasa.nlu.training_data.formats import MarkdownWriter
from rasa.utils.endpoints import EndpointConfig
import rasa.cli.utils as rasa_cli_utils
from ragex.community import config
from ragex.community.constants import SHARE_YOUR_BOT_CHANNEL_NAME, DEFAULT_CHANNEL_NAME
from ragex.community.services.user_service import GUEST
import ragex.community.tracker_utils as tracker_utils

if typing.TYPE_CHECKING:
    from ragex.community.services.event_service import EventService
    from ragex.community.services.data_service import DataService
    from ragex.community.services.story_service import StoryService
    from ragex.community.services.domain_service import DomainService
    from ragex.community.services.settings_service import (  # pytype: disable=pyi-error
        SettingsService,
    )

logger = logging.getLogger(__name__)


class StackService:
    """Connects to a running Rasa server.

    Used to retrieve information about models and conversations."""

    def __init__(
        self,
        stack_endpoint: EndpointConfig,
        data_service: "DataService",
        story_service: "StoryService",
        domain_service: "DomainService",
        settings_service: "SettingsService",
    ) -> None:

        self.stack_endpoint = stack_endpoint
        self.data_service = data_service
        self.story_services = story_service
        self.domain_service = domain_service
        self.settings_service = settings_service

    async def status(self) -> Any:
        """Get the status of the remote Rasa server (e.g. the version.)"""

        return await self.stack_endpoint.request(subpath="/version", method="get")

    async def has_active_model(self) -> bool:
        """Returns whether service has an active model."""

        try:
            result = await self.stack_endpoint.request(subpath="/status", method="get")
            return result.get("fingerprint") != {}
        except ClientError:
            return False

    async def initialise_tracker_for_conversation(self, conversation_id: Text) -> None:
        """Initialise a new tracker for `conversation_id`.

        This tracker will only contain an action_listen.
        """

        _ = await self.tracker_json(conversation_id)

        return None

    async def tracker_json(
        self,
        conversation_id: Text,
        event_verbosity: EventVerbosity = EventVerbosity.ALL,
        until: Optional[int] = None,
    ) -> Any:
        """Retrieve a tracker's json representation from remote instance."""

        url = "/conversations/{}/tracker?include_events={}".format(
            conversation_id, event_verbosity.name
        )
        if until:
            url += f"&until={until}"

        try:
            return await self.stack_endpoint.request(subpath=url, method="get")
        except ClientError:
            return None

    async def update_events(
        self,
        conversation_id: Text,
        events: List[Dict[Text, Any]],
        event_service: "EventService",
    ) -> Any:
        """Update events in the tracker of a conversation."""

        conversation = event_service.get_conversation_metadata_for_client(
            conversation_id
        )

        tracker = await self.tracker_json(conversation_id)

        conversation_start_time = tracker_utils.timestamp_of_conversation_start(
            tracker["events"]
        )

        is_beginning_of_interactive_conversation = (
            conversation
            and conversation["interactive"]
            and conversation.get("n_user_messages", 0) == 0
            and conversation_start_time is not None
        )

        if is_beginning_of_interactive_conversation:
            events = event_service.modify_event_time_to_be_later_than(
                conversation_start_time, events
            )

            # need to re-evaluate conversation start time as timestamps have changed
            conversation_start_time = tracker_utils.timestamp_of_conversation_start(
                events
            )
            # the session start sequence needs to be stripped from the list of events
            # as it will be automatically added to the tracker when Rasa creates it
            events = tracker_utils.remove_events_until_timestamp(
                events, conversation_start_time
            )
        else:
            # don't overwrite existing events but rather restart the conversation
            # and append the updated events.
            events = [Restarted().as_dict()] + events

        return await self.append_events_to_tracker(conversation_id, events)

    async def append_events_to_tracker(
        self,
        conversation_id: Text,
        events: Union[Dict[Text, Any], List[Dict[Text, Any]]],
    ) -> Any:
        """Add some more events to the tracker of a conversation."""

        url = f"/conversations/{conversation_id}/tracker/events"

        return await self.stack_endpoint.request(
            subpath=url, method="post", json=events
        )

    async def execute_action(
        self, conversation_id: Text, action: Dict, event_verbosity: EventVerbosity
    ) -> Any:
        """Run an action in a conversation."""

        url = "/conversations/{}/execute?include_events=".format(
            conversation_id, event_verbosity.name
        )

        return await self.stack_endpoint.request(
            subpath=url, method="post", json=action
        )

    async def evaluate_story(self, story: Text) -> Any:
        """Evaluate a story at Core's /evaluate endpoint."""

        url = "/model/test/stories"

        return await self.stack_endpoint.request(
            subpath=url, method="post", data=story, timeout=300
        )

    async def send_message(self, message: Dict[Text, Text], token: Text) -> Any:
        """Sends user messages to the stack Rasa webhook.

        Returns:
            If the request was successful the result as a list, otherwise
            `None`.
        """

        url = "/webhooks/rasa/webhook"
        message["input_channel"] = self._get_user_properties_from_bearer(token)[0]

        endpoint = self.stack_endpoint.copy()
        endpoint.token = None  # we want to use header auth
        return await endpoint.request(
            subpath=url, method="post", json=message, headers={"Authorization": token}
        )

    @staticmethod
    def _get_user_properties_from_bearer(
        token: Text, public_key: Optional[Union[Text, bytes]] = None
    ) -> Tuple[Text, Optional[Text]]:
        """Given a value of a HTTP Authorization header, verifies its validity
        as a JWT token and returns two values inside its payload: the user's
        name and their role.

        Returns:
            A tuple containing the input channel and the username.
        """

        if not public_key:
            public_key = config.jwt_public_key

        jwt_payload = ragex.community.jwt.verify_bearer_token(
            token, public_key=public_key
        )
        user = jwt_payload.get("user", {})
        username = user.get("username")
        user_roles = user.get("roles", [])

        if GUEST in user_roles:
            input_channel = SHARE_YOUR_BOT_CHANNEL_NAME
        else:
            input_channel = DEFAULT_CHANNEL_NAME

        return input_channel, username

    async def parse(self, text: Text) -> Optional[Dict]:
        url = "/model/parse"
        return await self.stack_endpoint.request(
            subpath=url,
            method="post",
            json={"text": text},
            headers={"Accept": "application/json"},
        )

    async def start_training_process(
        self, team: Text = config.team_name, project_id: Text = config.project_name
    ) -> Any:
        url = "/model/train"

        nlu_training_data = self.data_service.get_nlu_training_data_object(
            should_include_lookup_table_entries=True
        )
        if self.data_service.training_data_contains_retrieval_intents(
            nlu_training_data
        ):
            rasa_cli_utils.print_error(
                "Could not complete training request as your training data contains "
                "retrieval intents of the form 'intent/response_key'. Please use "
                "the CLI to train your model (`rasa train`)."
            )
            raise ValueError("Unable to train on data containing retrieval intents.")

        md_formatted_data = MarkdownWriter().dumps(nlu_training_data).strip()

        stories = self.story_services.fetch_stories(None)
        combined_stories = self.story_services.get_stories_markdown(stories)

        domain = self.domain_service.get_or_create_domain()
        domain_yaml = dump_obj_as_yaml_to_string(domain)

        _config = self.settings_service.get_config(team, project_id)
        config_yaml = dump_obj_as_yaml_to_string(_config)

        payload = dict(
            domain=domain_yaml,
            config=config_yaml,
            nlu=md_formatted_data,
            stories=combined_stories,
            force=False,
            save_to_default_model_directory=False,
        )

        training_result = await self.stack_endpoint.request(
            subpath=url,
            method="post",
            json=payload,
            return_method="read",
            timeout=24 * 60 * 60,  # 24 hours
        )

        return training_result

    async def evaluate_intents(
        self, training_data: List[Dict[Text, Any]], model_path: Text
    ) -> Any:
        from ragex.community.services import data_service

        url = f"/model/test/intents?model={model_path}"

        return await self.stack_endpoint.request(
            subpath=url, method="post", json=data_service.nlu_format(training_data)
        )

    async def predict_next_action(
        self, conversation_id: Text, included_events: Text = "ALL"
    ) -> Any:

        url = "/conversations/{}/predict?include_events={}".format(
            conversation_id, included_events
        )

        return await self.stack_endpoint.request(subpath=url, method="post")

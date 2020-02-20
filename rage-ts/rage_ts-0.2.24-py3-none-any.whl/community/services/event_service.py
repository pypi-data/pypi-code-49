import json
import logging
import warnings

import sqlalchemy
import time
import typing
from sqlalchemy import and_, false, true
from typing import Text, Optional, List, Dict, Any, Set, Union
from uuid import uuid4

import rasa.cli.utils as rasa_cli_utils
import ragex.community.utils as rasa_x_utils
from rasa.core.actions.action import ACTION_LISTEN_NAME
from rasa.core.events import UserUttered, BotUttered, ActionExecuted, deserialise_events
from rasa.core.policies import SimplePolicyEnsemble
from rasa.core.trackers import DialogueStateTracker, EventVerbosity
from rasa.core.training.structures import Story
from rasa.utils import endpoints
from rasa.utils.endpoints import EndpointConfig
from ragex.community import config, utils, metrics
from ragex.community.constants import SHARE_YOUR_BOT_CHANNEL_NAME
from ragex.community.database.analytics import (
    ConversationActionStatistic,
    ConversationPolicyStatistic,
    ConversationIntentStatistic,
    ConversationEntityStatistic,
    ConversationStatistic,
    conversation_statistics_dict,
)
from ragex.community.database.conversation import (
    Conversation,
    ConversationEvent,
    ConversationIntentMetadata,
    ConversationActionMetadata,
    ConversationPolicyMetadata,
    ConversationMessageCorrection,
    ConversationEntityMetadata,
    MessageLog,
)
from ragex.community.database.service import DbService
from ragex.community.database import utils as db_utils
from ragex.community.services.data_service import DataService
import ragex.community.tracker_utils as tracker_utils
from ragex.community.services.intent_service import (
    INTENT_MAPPED_TO_KEY,
    INTENT_NAME_KEY,
    IntentService,
)
from ragex.community.services.logs_service import LogsService
from ragex.community.utils import get_text_hash, update_log_level, QueryResult

if typing.TYPE_CHECKING:
    from ragex.community.services.event_consumers.event_consumer import (  # pytype: disable=pyi-error
        EventConsumer,
    )

logger = logging.getLogger(__name__)

FLAGGED_MESSAGES_KEY = "flagged_messages"
UNFLAGGED_MESSAGES_KEY = "unflagged_messages"
CORRECTED_MESSAGES_KEY = "corrected_messages"
_REVISION_CHECK_DELAY = 2  # Seconds


class EventService(DbService):
    def get_conversation_events(
        self,
        conversation_id: Text,
        until_time: Optional[float] = None,
        since_time: Optional[float] = None,
        rasa_environment_query: Optional[Text] = None,
    ) -> List[ConversationEvent]:

        since_time = since_time or 0
        filter_query = [
            ConversationEvent.conversation_id == conversation_id,
            ConversationEvent.timestamp > since_time,
        ]

        if until_time:
            filter_query.append(ConversationEvent.timestamp <= until_time)

        if rasa_environment_query:
            filter_query.append(
                ConversationEvent.rasa_environment == rasa_environment_query
            )

        return (
            self.query(ConversationEvent)
            .filter(and_(*filter_query))
            .order_by(ConversationEvent.timestamp.asc())
            .all()
        )

    def get_tracker_for_conversation(
        self,
        conversation_id: Text,
        until_time: Optional[float] = None,
        since_time: Optional[float] = None,
        rasa_environment_query: Optional[Text] = None,
    ) -> Optional[DialogueStateTracker]:
        conversation_events = self.get_conversation_events(
            conversation_id, until_time, since_time, rasa_environment_query
        )

        if conversation_events or self._conversation_exists(conversation_id):
            events = [e.as_rasa_dict() for e in conversation_events]
            return DialogueStateTracker.from_dict(conversation_id, events)
        else:
            logger.debug(
                f"Tracker for conversation with ID '{conversation_id}' not " f"found."
            )
            return None

    def _conversation_exists(self, conversation_id: Text) -> bool:
        query = self.query(Conversation).filter(
            Conversation.sender_id == conversation_id
        )

        return (
            self.query(sqlalchemy.literal(True)).filter(query.exists()).scalar() is True
        )

    def save_event(
        self,
        body: Union[Text, bytes],
        sender_id: Optional[Text] = None,
        event_number: Optional[int] = None,
        origin: Optional[Text] = None,
    ) -> ConversationEvent:
        logger.debug(f"Saving event from origin '{origin}' to event service:\n{body}")
        event = json.loads(body)
        if sender_id:
            event["sender_id"] = sender_id
        self._update_conversation_metadata(event)
        new_event = self._save_conversation_event(event, origin=origin)
        self.update_statistics_from_event(event, event_number)

        # flush so that returned event has an id
        self.flush()

        return new_event

    def _save_conversation_event(
        self, event: Dict[Text, Any], origin: Optional[Text] = None
    ) -> ConversationEvent:
        sender_id = event.get("sender_id")
        intent = event.get("parse_data", {}).get("intent", {}).get("name")
        action = event.get("name")
        policy = self.extract_policy_base_from_event(event)
        timestamp = event.get("timestamp")

        if LogsService.is_user_uttered_event(event):
            metrics.track_message_received(sender_id, event.get("input_channel"))

        new_event = ConversationEvent(
            conversation_id=sender_id,
            type_name=event.get("event"),
            timestamp=timestamp,
            intent_name=intent,
            action_name=action,
            data=json.dumps(event),
            policy=policy,
            rasa_environment=origin,
        )

        self.add(new_event)
        self.commit()

        return new_event

    def _update_conversation_metadata(self, event: Dict[Text, Any]) -> None:
        sender_id = event.get("sender_id")

        conversation = (
            self.query(Conversation).filter(Conversation.sender_id == sender_id).first()
        )

        if not conversation:
            conversation = self._insert_conversation_from(event)
            # Flush to obtain row id
            self.flush()

        conversation.latest_event_time = event.get("timestamp")

        event_confidence = event.get("confidence")
        if event_confidence is None:
            event_confidence = 1

        conversation.minimum_action_confidence = min(
            event_confidence, conversation.minimum_action_confidence
        )

        event_type = event.get("event")

        policy = self.extract_policy_base_from_event(event)
        if conversation.in_training_data:
            if policy is None:
                is_memo_policy = True
            else:
                is_memo_policy = not SimplePolicyEnsemble.is_not_memo_policy(policy)
            conversation.in_training_data = is_memo_policy

        intent_name = event.get("parse_data", {}).get("intent", {}).get("name")
        unique_intents = (i.intent for i in conversation.unique_intents)
        if intent_name and intent_name not in unique_intents:
            self.add(
                ConversationIntentMetadata(
                    conversation_id=conversation.sender_id, intent=intent_name
                )
            )

        if event_type == UserUttered.type_name:
            conversation.number_user_messages += 1
            conversation.latest_input_channel = event.get("input_channel")
            entities = event.get("parse_data", {}).get("entities", [])
            entities = [e.get("entity") for e in entities]
            for e in entities:
                existing = (
                    self.query(ConversationEntityMetadata)
                    .filter(
                        and_(
                            ConversationEntityMetadata.conversation_id
                            == conversation.sender_id,
                            ConversationEntityMetadata.entity == e,
                        )
                    )
                    .first()
                )
                if not existing:
                    self.add(
                        ConversationEntityMetadata(
                            conversation_id=conversation.sender_id, entity=e
                        )
                    )

        action_name = event.get("name")
        unique_actions = (a.action for a in conversation.unique_actions)
        if action_name and action_name not in unique_actions:
            self.add(
                ConversationActionMetadata(
                    conversation_id=conversation.sender_id, action=action_name
                )
            )

        if policy and policy not in [p.policy for p in conversation.unique_policies]:
            self.add(
                ConversationPolicyMetadata(
                    conversation_id=conversation.sender_id, policy=policy
                )
            )

        self.commit()

    def _insert_conversation_from(self, _dict: Dict[Text, Any]) -> Conversation:
        sender_id = _dict.get("sender_id", uuid4().hex)
        new = Conversation(
            sender_id=sender_id,
            interactive=_dict.get("interactive", False),
            latest_event_time=time.time(),
        )
        try:
            self.add(new)
            self.commit()
        except sqlalchemy.exc.IntegrityError:
            logger.warning(
                f"Conversation for '{sender_id}' could not be created since it already"
                f" exists."
            )
            raise ValueError(f"Sender id '{sender_id}' already exists.")

        return new

    def create_conversation_from(self, _dict: Dict[Text, Any]) -> Dict[Text, Any]:
        return self._insert_conversation_from(_dict).as_dict()

    @staticmethod
    def extract_policy_base_from_event(event: Dict[Text, Any]) -> Optional[Text]:
        """Given an ActionExecuted event, extracts the base name of

        the policy used. Example: event with `"policy": "policy_1_KerasPolicy"`
        will return `KerasPolicy`."""
        if event.get("policy"):
            return event["policy"].split("_")[-1]

        return None

    def update_statistics_from_event(
        self, event: Dict[Text, Any], event_number: Optional[int]
    ):
        event_name = event.get("event")
        statistic = self.query(ConversationStatistic).first()

        if not statistic:
            statistic = ConversationStatistic(project_id=config.project_name)
            self.add(statistic)
            self.commit()

        statistic.latest_event_timestamp = event["timestamp"]
        statistic.latest_event_id = event_number or statistic.latest_event_id
        if event_name == UserUttered.type_name:
            statistic.total_user_messages += 1
            self._update_user_event_statistic(event)
        elif event_name == BotUttered.type_name:
            statistic.total_bot_messages += 1
        elif (
            event_name == ActionExecuted.type_name
            and event["name"] != ACTION_LISTEN_NAME
        ):
            self._update_action_event_statistic(event)

        self.commit()

    def _update_user_event_statistic(self, event: Dict[Text, Any]):
        intent = event.get("parse_data", {}).get("intent", {}).get("name")
        if intent:
            existing = (
                self.query(ConversationIntentStatistic)
                .filter(ConversationIntentStatistic.intent == intent)
                .first()
            )
            if existing:
                existing.count += 1
            else:
                self.add(
                    ConversationIntentStatistic(
                        project_id=config.project_name, intent=intent
                    )
                )

        entities = event.get("parse_data", {}).get("entities", [])
        for entity in entities:
            entity_name = entity.get("entity")
            existing = (
                self.query(ConversationEntityStatistic)
                .filter(ConversationEntityStatistic.entity == entity_name)
                .first()
            )
            if existing:
                existing.count += 1
            else:
                self.add(
                    ConversationEntityStatistic(
                        project_id=config.project_name, entity=entity_name
                    )
                )

    def _update_action_event_statistic(self, event: Dict[Text, Any]):
        existing = (
            self.query(ConversationActionStatistic)
            .filter(ConversationActionStatistic.action == event["name"])
            .first()
        )
        if existing:
            existing.count += 1
        else:
            self.add(
                ConversationActionStatistic(
                    project_id=config.project_name, action=event["name"]
                )
            )
        policy = self.extract_policy_base_from_event(event)
        if policy:
            existing = (
                self.query(ConversationPolicyStatistic)
                .filter(ConversationPolicyStatistic.policy == policy)
                .first()
            )
            if existing:
                existing.count += 1
            else:
                self.add(
                    ConversationPolicyStatistic(
                        project_id=config.project_name, policy=policy
                    )
                )

    def get_evaluation(self, sender_id: Text) -> Dict[Text, Any]:
        conversation = self._get_conversation(sender_id)

        if conversation and conversation.evaluation:
            return json.loads(conversation.evaluation)
        else:
            return {}

    def _get_conversation(self, sender_id: Text) -> Optional[Conversation]:
        return (
            self.query(Conversation).filter(Conversation.sender_id == sender_id).first()
        )

    def update_evaluation(self, sender_id: Text, evaluation: Dict[Text, Any]) -> None:
        conversation = self._get_conversation(sender_id)

        if conversation:
            conversation.evaluation = json.dumps(evaluation)
            conversation.in_training_data = (
                evaluation.get("in_training_data_fraction", 0) == 1
            )
            self.commit()
        else:
            raise ValueError(f"No conversation found for sender id '{sender_id}'.")

    def delete_evaluation(self, sender_id: Text) -> None:
        conversation = (
            self.query(Conversation).filter(Conversation.sender_id == sender_id).first()
        )

        if conversation:
            conversation.evaluation = None
            self.commit()

    def get_statistics(self) -> Dict[Text, Union[int, List[Text]]]:
        statistic = self.query(ConversationStatistic).first()
        if statistic:
            return statistic.as_dict()
        else:
            return self.user_statistics_dict()

    @staticmethod
    def user_statistics_dict(
        n_user_messages: Optional[int] = None,
        n_bot_messages: Optional[int] = None,
        top_intents: Optional[List[Text]] = None,
        top_actions: Optional[List[Text]] = None,
        top_entities: Optional[List[Text]] = None,
        top_policies: Optional[List[Text]] = None,
    ):
        return conversation_statistics_dict(
            n_user_messages,
            n_bot_messages,
            top_intents,
            top_actions,
            top_entities,
            top_policies,
        )

    def get_conversation_metadata_for_client(
        self, sender_id: Text
    ) -> Optional[Dict[Text, Any]]:
        conversation = self._get_conversation(sender_id)
        if conversation:
            return conversation.as_dict()
        else:
            return None

    def get_unique_actions(self) -> List[str]:
        actions = self.query(ConversationActionStatistic.action).distinct().all()

        return [a for (a,) in actions]

    def get_unique_policies(self) -> List[str]:
        policies = self.query(ConversationPolicyStatistic.policy).distinct().all()

        return [p for (p,) in policies]

    def get_unique_intents(self) -> List[str]:
        intents = self.query(ConversationIntentStatistic.intent).distinct().all()

        return [i for (i,) in intents]

    def get_unique_entities(self) -> List[str]:
        entities = self.query(ConversationEntityStatistic.entity).distinct().all()

        return [e for (e,) in entities]

    def get_conversation_metadata_for_all_clients(
        self,
        start: Optional[float] = None,
        until: Optional[float] = None,
        maximum_confidence: Optional[float] = None,
        minimum_user_messages: Optional[int] = None,
        policies: Optional[Text] = None,
        in_training_data: Optional[bool] = None,
        intent_query: Optional[Text] = None,
        entity_query: Optional[Text] = None,
        action_query: Optional[Text] = None,
        sort_by_date: bool = True,
        sort_by_confidence: bool = False,
        text_query: Optional[Text] = None,
        rasa_environment_query: Optional[Text] = None,
        only_flagged: bool = False,
        include_interactive: bool = False,
        exclude: Optional[List[Text]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> QueryResult:
        conversations = self.query(Conversation)

        query = True
        if start:
            query = Conversation.latest_event_time >= start
        if until:
            query = and_(query, Conversation.latest_event_time <= until)
        if minimum_user_messages:
            query = and_(
                query, Conversation.number_user_messages >= minimum_user_messages
            )
        if in_training_data is not None:
            query = and_(query, Conversation.in_training_data.is_(in_training_data))
        if only_flagged:
            query = and_(query, Conversation.events.any(ConversationEvent.is_flagged))
        if maximum_confidence is not None:
            query = and_(
                query, Conversation.minimum_action_confidence <= maximum_confidence
            )
        if policies:
            policies = policies.split(",")
            query = and_(
                query,
                Conversation.unique_policies.any(
                    ConversationPolicyMetadata.policy.in_(policies)
                ),
            )

        if intent_query:
            intents = intent_query.split(",")
            query = and_(
                query,
                Conversation.unique_intents.any(
                    ConversationIntentMetadata.intent.in_(intents)
                ),
            )

        if action_query:
            actions = action_query.split(",")
            query = and_(
                query,
                Conversation.unique_actions.any(
                    ConversationActionMetadata.action.in_(actions)
                ),
            )

        if entity_query:
            entities = entity_query.split(",")
            query = and_(
                query,
                Conversation.unique_entities.any(
                    ConversationEntityMetadata.entity.in_(entities)
                ),
            )

        if text_query:
            text_query = f"%{text_query}%"
            query = and_(
                query,
                Conversation.events.any(
                    ConversationEvent.message_log.has(MessageLog.text.ilike(text_query))
                ),
            )

        if rasa_environment_query:
            query = and_(
                query,
                Conversation.events.any(
                    ConversationEvent.rasa_environment == rasa_environment_query
                ),
            )

        if not include_interactive:
            query = and_(query, Conversation.interactive == false())

        if exclude:
            query = and_(query, ~Conversation.sender_id.in_(exclude))

        conversations = conversations.filter(query)
        number_conversations = conversations.count()

        if in_training_data is False and sort_by_confidence:
            conversations = conversations.order_by(
                Conversation.minimum_action_confidence.desc()
            )
        elif sort_by_date:
            conversations = conversations.order_by(
                Conversation.latest_event_time.desc()
            )

        conversations = conversations.offset(offset).limit(limit).all()

        return QueryResult([c.as_dict() for c in conversations], number_conversations)

    def sender_ids(self) -> List[Text]:
        sender_ids = self.query(Conversation.sender_id).distinct().all()

        return [i for i, in sender_ids]

    def story_for_sender_id(self, sender_id: Text) -> Text:
        events = (
            self.query(ConversationEvent.data)
            .filter(ConversationEvent.conversation_id == sender_id)
            .order_by(ConversationEvent.id.asc())
            .all()
        )

        events = deserialise_events([json.loads(e) for e, in events])

        story = Story.from_events(events, sender_id)
        return story.as_story_string(flat=True)

    def add_flagged_message(self, sender_id: Text, message_timestamp: float) -> None:
        event = (
            self.query(ConversationEvent)
            .filter(
                and_(
                    ConversationEvent.conversation_id == sender_id,
                    ConversationEvent.timestamp == message_timestamp,
                )
            )
            .first()
        )

        if not event:
            logger.warning(
                f"Event with timestamp '{message_timestamp}' for sender id "
                f"'{sender_id}' was not found."
            )
        else:
            event.is_flagged = True
            event.is_unflagged = False
            self.commit()

    def delete_flagged_message(self, sender_id: Text, message_timestamp: float) -> None:
        event = (
            self.query(ConversationEvent)
            .filter(
                and_(
                    ConversationEvent.conversation_id == sender_id,
                    ConversationEvent.timestamp == message_timestamp,
                )
            )
            .first()
        )

        if not event:
            logger.warning(
                f"Event with timestamp '{message_timestamp}' for sender id "
                f"'{sender_id}' was not found."
            )
        else:
            event.is_flagged = False
            event.is_unflagged = True
            self.commit()

    def get_flagged_message_timestamps(
        self, sender_id: Text, rasa_environment_query: Optional[Text] = None
    ) -> Set[float]:
        filter_query = [
            ConversationEvent.conversation_id == sender_id,
            ConversationEvent.is_flagged == true(),
        ]

        if rasa_environment_query:
            filter_query.append(
                ConversationEvent.rasa_environment == rasa_environment_query
            )

        flagged_timestamps = (
            self.query(ConversationEvent.timestamp)
            .filter(and_(*filter_query))
            .distinct()
            .all()
        )

        return {t for t, in flagged_timestamps}

    def correct_message(
        self,
        sender_id: Text,
        message_timestamp: float,
        new_intent: Dict[str, str],
        user: Dict[str, str],
        project_id: Text,
    ):
        """Corrects a message and adds it to the training data.

        Args:
            sender_id: The sender id of the conversation.
            message_timestamp: The timestamp of the user message which should
                               be corrected.
            new_intent: Intent object which describes the new intent of the
                        message.
            user: The user who owns the training data.
            project_id: The project id of the training data.

        """
        intent_service = IntentService(self.session)
        existing_intents = intent_service.get_permanent_intents(project_id)
        intent_id = new_intent[INTENT_NAME_KEY]
        is_temporary = intent_id not in existing_intents
        mapped_to = None

        if is_temporary:
            intent_service.add_temporary_intent(new_intent, project_id)
            temporary_intent = intent_service.get_temporary_intent(
                intent_id, project_id
            )
            mapped_to = None
            if temporary_intent:
                temporary_intent.get(INTENT_MAPPED_TO_KEY)

        event = (
            self.query(ConversationEvent)
            .filter(
                and_(
                    ConversationEvent.conversation_id == sender_id,
                    ConversationEvent.type_name == UserUttered.type_name,
                    ConversationEvent.timestamp == message_timestamp,
                )
            )
            .first()
        )

        if event is None:
            raise ValueError("A user event for this timestamp does not exist.")

        event = json.loads(event.data)
        if not is_temporary or mapped_to is not None:
            data_service = DataService(self.session)
            event["parse_data"]["intent"]["name"] = mapped_to or intent_id
            example = data_service.save_user_event_as_example(user, project_id, event)
            example_hash = example.get("hash")
            intent_service.add_example_to_temporary_intent(
                new_intent[INTENT_NAME_KEY], example_hash, project_id
            )
        else:
            logger.debug(
                "Message correction was not added to training data, "
                "since the intent was temporary and not mapped to "
                "an existing intent."
            )

        correction = ConversationMessageCorrection(
            conversation_id=sender_id,
            message_timestamp=message_timestamp,
            intent=intent_id,
        )
        self.add(correction)
        self.commit()

    def delete_message_correction(
        self, sender_id: Text, message_timestamp: float, project_id: Text
    ):
        """Deletes a message correction and the related training data.

        Args:
            sender_id: The sender id of the conversation.
            message_timestamp: The timestamp of the corrected user message.
            project_id: The project id of the stored training data.

        """

        correction = (
            self.query(ConversationMessageCorrection)
            .filter(
                and_(
                    ConversationMessageCorrection.conversation_id == sender_id,
                    ConversationMessageCorrection.message_timestamp
                    == message_timestamp,
                )
            )
            .first()
        )

        if correction:
            event = (
                self.query(ConversationEvent)
                .filter(
                    and_(
                        ConversationEvent.conversation_id == sender_id,
                        ConversationEvent.type_name == UserUttered.type_name,
                        ConversationEvent.timestamp == message_timestamp,
                    )
                )
                .first()
            )

            # delete example from training data
            event = json.loads(event.data)
            message_text = event.get("parse_data", {}).get("text")
            message_hash = get_text_hash(message_text)

            data_service = DataService(self.session)
            data_service.delete_example_by_hash(project_id, message_hash)

            # delete example from possible temporary intent
            intent_service = IntentService(self.session)
            intent_service.remove_example_from_temporary_intent(
                correction.intent, message_hash, project_id
            )

            self.delete(correction)
            self.commit()

    @classmethod
    def modify_event_time_to_be_later_than(
        cls,
        minimal_timestamp: float,
        events: List[Dict[Text, Any]],
        minimal_timedelta: float = 0.001,
    ) -> List[Dict[Text, Any]]:
        """Changes the event times to be after a certain timestamp."""

        if not events:
            return events

        events = sorted(events, key=lambda e: e["timestamp"])
        oldest_event = events[0].get("timestamp", minimal_timestamp)
        # Make sure that the new timestamps are greater than the minimal
        difference = minimal_timestamp - oldest_event + minimal_timedelta

        if difference > 0:

            delta = minimal_timedelta

            for event in events:
                event["timestamp"] = minimal_timestamp + delta
                delta += minimal_timedelta

        return events

    def get_messages_for(
        self,
        conversation_id: Text,
        until_time: Optional[float] = None,
        event_verbosity: EventVerbosity = EventVerbosity.ALL,
    ) -> Optional[Dict[Text, Any]]:
        """Gets tracker including a field `messages` which lists user / bot events."""

        tracker = self._get_flagged_tracker_dict(
            conversation_id, until_time, event_verbosity=event_verbosity
        )

        if tracker is None:
            return None

        messages = []
        for i, e in enumerate(tracker["events"]):
            if e.get("event") in {"user", "bot", "agent"}:
                m = e.copy()
                m["data"] = m.get("data", m.get("parse_data", None))
                m["type"] = m["event"]
                del m["event"]
                messages.append(m)

        tracker["messages"] = messages

        return tracker

    def get_tracker_with_message_flags(
        self,
        conversation_id: Text,
        until_time: Optional[float] = None,
        since_time: Optional[float] = None,
        event_verbosity: EventVerbosity = EventVerbosity.ALL,
        rasa_environment_query: Optional[Text] = None,
        exclude_leading_action_session_start: bool = False,
    ) -> Optional[Dict[Text, Any]]:
        """Gets tracker including message flags.

        Args:
            conversation_id: Name of the conversation tracker.
            until_time: Include only events until the given time.
            since_time: Include only events after the given time.
            event_verbosity: Verbosity of the returned tracker.
            rasa_environment_query: Origin Rasa host of the tracker events.
            exclude_leading_action_session_start: Whether to exclude a leading
                `action_session_start` from the tracker events.

        Returns:
            Tracker for the conversation ID.

        """
        tracker = self._get_flagged_tracker_dict(
            conversation_id,
            until_time,
            since_time,
            event_verbosity,
            rasa_environment_query,
        )

        if tracker is not None:
            # TODO: The frontend appears to be using this property only to
            # check if there are any flagged events in the conversation - so
            # this could be a boolean value.
            # Even better: don't generate this property explicitly, and have it
            # be a part of `Conversation` or `DialogueStateTracker`.
            tracker[FLAGGED_MESSAGES_KEY] = self.get_truncated_timestamps(
                conversation_id
            )

        if exclude_leading_action_session_start:
            tracker_utils.remove_leading_action_session_start_from(tracker)

        return tracker

    def _get_flagged_tracker_dict(
        self,
        conversation_id: Text,
        until_time: Optional[float] = None,
        since_time: Optional[float] = None,
        event_verbosity: EventVerbosity = EventVerbosity.AFTER_RESTART,
        rasa_environment_query: Optional[Text] = None,
    ) -> Optional[Dict[Text, Any]]:
        tracker = self.get_tracker_for_conversation(
            conversation_id, until_time, since_time, rasa_environment_query
        )

        if not tracker:
            return None

        tracker_dict = tracker.current_state(event_verbosity)

        for e in tracker_dict["events"]:
            # TODO: This should be part of the event metadata, not the message
            # itself, so this copy should not be carried out.
            e["is_flagged"] = e["metadata"]["rasa_x_flagged"]

        return tracker_dict

    def get_truncated_timestamps(
        self, conversation_id: Text, decimal_places: int = 4
    ) -> List[float]:
        """Create a list of flagged timestamps for `conversation_id` truncated to
            `decimal_places` after the decimal separator."""

        flagged_timestamps = self.get_flagged_message_timestamps(conversation_id)
        return [
            utils.truncate_float(timestamp, decimal_places=decimal_places)
            for timestamp in flagged_timestamps
        ]

    @staticmethod
    def get_sender_name(conversation: Conversation) -> Text:
        if conversation.latest_input_channel == SHARE_YOUR_BOT_CHANNEL_NAME:
            return SHARE_YOUR_BOT_CHANNEL_NAME
        else:
            return conversation.sender_id


def continuously_consume(
    endpoint_config: endpoints.EndpointConfig,
    wait_between_failures: int = 5,
    should_run_liveness_endpoint: bool = False,
):
    """Consume event consumer continuously.

    Args:
        endpoint_config: Event consumer endpoint config.
        wait_between_failures: Wait time between retries when the consumer throws an
            error during initialisation or consumption.
        should_run_liveness_endpoint: If `True`, runs a simple Sanic server as a
            background process that can be used to probe liveness of this service.
            The service will be exposed at a port defined by the
            `SELF_PORT` environment variable (5673 by default).

    """
    from ragex.community.services.event_consumers.event_consumer import (  # pytype: disable=pyi-error
        EventConsumer,
    )
    import ragex.community.services.event_consumers.utils as consumer_utils  # pytype: disable=pyi-error

    while True:
        consumer: Optional[EventConsumer] = None
        # noinspection PyBroadException
        try:
            consumer = consumer_utils.from_endpoint_config(
                endpoint_config, should_run_liveness_endpoint
            )
            if consumer:
                consumer.consume()
            else:
                rasa_cli_utils.print_error_and_exit(
                    f"Could not configure valid event consumer. Exiting."
                )
        except ValueError as e:
            warnings.warn(str(e))
            rasa_cli_utils.print_error_and_exit(
                f"Could not configure valid event consumer. Exiting."
            )
        except Exception:
            logger.exception(
                f"Caught an exception while consuming events. "
                f"Will retry in {wait_between_failures} s."
            )
            time.sleep(wait_between_failures)
        finally:  # kill consumer endpoint process
            if consumer:
                consumer.kill_liveness_endpoint_process()


def read_event_broker_config(
    endpoint_config_path: Text = config.endpoints_path,
) -> "EndpointConfig":
    """Read `event_broker` subsection of endpoint config file.

    The endpoint config contains lots of other sections, but only the `event_broker`
    section is relevant. This function creates a temporary file with only that
    section.

    """
    event_broker_key = "event_broker"
    endpoint_config: Optional["EndpointConfig"] = None

    try:
        endpoint_config = rasa_x_utils.extract_partial_endpoint_config(
            endpoint_config_path, event_broker_key
        )
    except ValueError as e:
        warnings.warn(
            f"Could not find endpoint file at path '{config.endpoints_path}':\n{e}."
        )
    except KeyError:
        warnings.warn(
            f"Could not find '{event_broker_key}' section in "
            f"endpoint config file at path '{config.endpoints_path}'."
        )
    except TypeError:
        warnings.warn(
            f"Endpoint config file at path '{endpoint_config_path}' does not contain "
            f"valid sections."
        )
    except Exception as e:
        logger.error(
            f"Encountered unexpected error reading endpoint config "
            f"file at path {config.endpoints_path}:\n{e}"
        )

    return endpoint_config


def wait_for_migrations() -> None:
    """Loop continuously until all database migrations have been executed."""

    logger.info("Waiting until database migrations have been executed...")

    migrations_pending = True
    while migrations_pending:
        try:
            with db_utils.session_scope() as session:
                migrations_pending = not db_utils.is_db_revision_latest(session)
        except Exception as e:
            logger.warning(f"Could not retrieve the database revision due to: {e}.")

        if migrations_pending:
            logger.warning(
                f"Database revision does not match migrations' latest, trying again"
                f" in {_REVISION_CHECK_DELAY} seconds."
            )
            time.sleep(_REVISION_CHECK_DELAY)

    logger.info("Check for database migrations completed.")


def main(should_run_liveness_endpoint: bool = True) -> None:
    """Start an event consumer and consume continuously.

    Args:
        should_run_liveness_endpoint: If `True`, runs a simple Sanic server as a
            background process that can be used to probe liveness of this service.
            The service will be exposed at a port defined by the
            `SELF_PORT` environment variable (5673 by default).

    In server mode a simple Sanic server is run exposing a `/health` endpoint as a
    background process that can be used to probe liveness of this service.
    The endpoint will be exposed at a port defined by the
    `SELF_PORT` environment variable (5673 by default).

    """
    logger.debug(f"Starting event service.")

    update_log_level()

    endpoint_config = read_event_broker_config() if not config.LOCAL_MODE else None

    # Before reading/writing from the database (metrics config and conversation
    # events), make sure migrations have run first
    wait_for_migrations()

    # Set telemetry configuration for this process
    if not config.LOCAL_MODE:
        with db_utils.session_scope() as session:
            metrics.initialize_configuration_from_db(session)

    continuously_consume(
        endpoint_config, should_run_liveness_endpoint=should_run_liveness_endpoint
    )


if __name__ == "__main__":
    main()

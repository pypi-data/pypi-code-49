"""
Sends these events to the VVAGateway
Also generates a transcription for sql_driver
"""
import copy
import logging
from os import environ

# Table converting channels to DNIS values
# :TODO get this conversion from the SQL database...not sure how

from tracker_consumer.data_stores.redis_repository import RedisRepository
from tracker_consumer.event import CueState

logger = logging.getLogger("cueMaker")  # get the root logger
AUTHENTICATION_STATE = environ.get("AUTHENTICATION_STATE") if environ.get(
    "AUTHENTICATION_STATE") else 'authentication_form'
FEEDBACK_STATE = environ.get("FEEDBACK_STATE") if environ.get("FEEDBACK_STATE") else 'feedback_form'
CALL_START = environ.get("CALL_START") if environ.get("CALL_START") else 'utter_greet'
REDIS_URL = environ.get("REDIS_URL") if environ.get('REDIS_URL') else 'localhost'
REDIS_PORT = environ.get("REDIS_PORT") if environ.get('REDIS_PORT') else 6379


class CueMaker:
    """
    Derives CUE style data and publishes to CUE gateway
    """
    def __init__(self, event, service, tracer):
        self.tracer = tracer
        self.redis_repo = RedisRepository.get_instance(tracer)
        self.state_key = '{}_{}'.format(service, event.sender_id)
        self.event = event
        self.state = None
        # self.init_state()

    async def init_state(self):
        with self.tracer.start_active_span('load_cue_state'):
            self.state = CueState()
            res = await self.redis_repo.get_cue_state(self.state_key)
            if res:
                self.state.init_state(res)
            self.state.callId = self.event.sender_id
            self.previous_state = self.state.lastState or CALL_START

    def is_undefined_and_not_authentication(self, event):
        """
        Check if the DM is getting authentication or the NLU just has no intent
        Don't generate error in these states
        """
        return (
                event.get_intent_name() is None
                and not self.previous_state.startswith(AUTHENTICATION_STATE)
                and not self.previous_state.startswith(FEEDBACK_STATE)
        )

    async def set_guid(self, guid):
        self.state.globalUserId = guid
        await self.redis_repo.set_key_val(self.state_key, 'globalUserId', guid)

    async def set_csid(self, channel_session_id):
        self.state.channelSessionId = channel_session_id
        await self.redis_repo.set_key_val(self.state_key, 'channelSessionId', channel_session_id)

    async def set_task(self, task):
        self.state.task = task
        await self.redis_repo.set_key_val(self.state_key, 'task', task)

    async def save_state(self, timeout=3600):
        with self.tracer.start_active_span('save_cue_state'):
            state = copy.deepcopy(self.state)
            await self.redis_repo.save_state(self.state_key, state, timeout)

    def clear_events(self):
        self.state.events = []

    def end_call(self, event):
        start_time = event.start_time
        last_state = self.previous_state

        cue_event = {
            "keyValues": {
                "state": last_state,
            },
            "eventType": "callEnd",
            "timestamp": event.iso_timestamp
        }
        self.state.endTime = event.timestamp
        self.state.endTimeFormatted = event.iso_timestamp
        self.state.callLength = (self.state.endTime - start_time) if start_time else '15'
        self.state.events.append(cue_event)

    def add_err_event(self, event):
        user_input = event.text
        if user_input:
            err_type = 'Nomatch'
            self.state.nomatchCount += 1
        else:
            err_type = 'Noinput'
            self.state.noinputCount += 1

        cue_event = {
            "keyValues": {
                "State": self.previous_state,
                "Count": 1
            },
            "timestamp": event.iso_timestamp,
            "eventType": err_type
        }

        self.state.errorCount += 1
        self.state.events.append(cue_event)

    def add_recognition_evt(self, event):
        intent = event.get_intent_name() if event.get_intent_name() else 'None'
        confidence = event.get_confidence()
        utterance = event.text

        if "guid" in utterance:
            utterance = utterance[:6]

        cue_event = {
            "keyValues": {
                "Interpretation": intent,
                "ConfidenceLevel": confidence,
                "ConfidenceThreshold": 0.5,
                "GrammarUri": "fill",
                "Bargein": False,
                "Utterance": utterance,
                "State": self.previous_state,
                "CallerBargein": False,
                "InputMode": "",
            },
            "timestamp": event.iso_timestamp,
            "eventType": "Recognition"
        }
        self.state.recoCount += 1
        self.state.events.append(cue_event)

    def add_transition_evt(self, event):
        cue_event = {
            "keyValues": {
                "toState": event.name,
                "fromState": self.previous_state
            },
            "timestamp": event.iso_timestamp,
            "eventType": "Transition"
        }
        self.state.currentState = event.name
        self.state.transitionCount += 1
        self.state.events.append(cue_event)

    def add_metric_evt(self, event):
        cue_event = {
            "keyValues": {
                event.name: event.value
            },
            "timestamp": event.iso_timestamp,
            "eventType": "Metric"
        }
        self.state.events.append(cue_event)

    def add_bot_utter_evt(self, event):
        cue_event = {
            "keyValues": {
                "Utterance": event.text,
                "State": self.previous_state
            },
            "timestamp": event.iso_timestamp,
            "eventType": "Bot"
        }
        self.state.events.append(cue_event)

    def add_task_begin_evt(self, event):
        cue_event = {
            "name": event.value,
            "timestamp": event.iso_timestamp,
            "eventType": "Task-Begin"
        }

        self.state.events.append(cue_event)

    def add_task_end_evt(self, event):
        cue_event = {
            "name": event.value,
            "timestamp": event.iso_timestamp,
            "eventType": "Task-End"
        }

        self.state.events.append(cue_event)

    def transition(self, event):
        self.set_start_time(event)
        self.state.dnis = event.dnis

        if event.name in ['action_listen', 'action_deactivate_form', environ['ERROR_STATE']]:
            return None
        else:
            self.add_transition_evt(event)

        if event.name != self.state.lastState:
            self.state.reset_errors()
        self.state.lastState = event.name

        return event.name

    def recognition(self, event):
        self.set_start_time(event)

        if self.is_undefined_and_not_authentication(event):
            self.add_recognition_evt(event)
            self.add_err_event(event)
        else:
            self.add_recognition_evt(event)

    def bot_utterance(self, event):
        self.set_start_time(event)
        self.add_bot_utter_evt(event)

    def begin_task(self, event):
        self.set_start_time(event)
        self.add_task_begin_evt(event)

    def end_task(self, event):
        self.set_start_time(event)
        self.add_task_end_evt(event)

    def create_custom_evt(self, event):
        self.add_metric_evt(event)

    def set_start_time(self, event):
        timestamp = event.timestamp

        if self.state.startTime is None or (self.state.startTime and timestamp < self.state.startTime):
            self.state.startTime = timestamp
            self.state.startTimeFormatted = event.iso_timestamp
import asyncio
import logging
import time
import traceback
import xml.etree.ElementTree as ET
from os import environ

from jsonpickle import json

from config.jaeger_config import cue_tracer, conversation_tracer, upm_tracer
from tracker_consumer.constants import USER_EVENT, BOT_EVENT, SLOT_EVENT, ACTION_EVENT, NLU_EVENT
from tracker_consumer.cue_maker import CueMaker
from tracker_consumer.data_stores.redis_repository import RedisRepository
from tracker_consumer.event import CueState, Event
from tracker_consumer.sql_driver import AlcSeq
from tracker_consumer.transcript import Transcript

CALL_END_STATE_1 = environ.get('CALL_END_STATE_1')
CALL_END_STATE_2 = environ.get('CALL_END_STATE_2')
logger = logging.getLogger("EventHandler")  # get the root logger
REQUEST_TIMEOUT = 3
CUE_URL = 'http://sdlweb01b.vail:8080/VVAGateway/Service/Writer'


class EventHandler:
    def __init__(self):
        self.tracker_tracer = None
        self.tasks = []
        self.redis_repo = None

    def process_user_event(self, event, cue=None):
        raise NotImplementedError()

    def process_action_event(self, event, cue=None):
        raise NotImplementedError()

    def process_slot_event(self, event, cue=None):
        raise NotImplementedError()

    def process_bot_event(self, event, cue=None):
        raise NotImplementedError()

    def process(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process') as scope:
            scope.span.set_tag('sender_id', event.sender_id)
            scope.span.log_kv({'message': event.msg})

            if event.event_type == USER_EVENT:
                self.process_user_event(event, cue)
            elif event.event_type == BOT_EVENT:
                self.process_bot_event(event, cue)
            elif event.event_type == SLOT_EVENT:
                self.process_slot_event(event, cue)
            elif event.event_type == ACTION_EVENT:
                if event.name in ['action_listen', 'action_deactivate_form', environ['ERROR_STATE']]:
                    return

                self.process_action_event(event, cue)

    def clear_tasks(self):
        self.tasks = {}

    def first_user_input_init(self, event, cue):
        user_input_json = json.loads(event.text[6:])
        cue.state.ani = user_input_json.get('channelUserId')
        cue.state.channelSessionId = user_input_json.get('channelUserId')
        cue.state.globalUserId = user_input_json.get('guid')
        cue.state.dnis = event.dnis

    async def init_cue_maker(self, event, service):
        with self.tracker_tracer.start_active_span('init_cue_maker'):
            cue = CueMaker(event, service, self.tracker_tracer)
            await cue.init_state()
            return cue

    async def construct_cue_state(self, state_key, events):
        with self.tracker_tracer.start_active_span('construct_cue_state'):
            res = await self.redis_repo.get_cue_state(state_key)
            cue_state = CueState()
            cue_state.init_state(res)
            cue_state.events = events

            return cue_state

    @staticmethod
    def _is_goodbye_msg_callback(text):
        return text == '/goodbye'


class ConversationHandler(EventHandler):
    def __init__(self):
        super(ConversationHandler, self).__init__()
        self.alcSeq = AlcSeq.get_instance()
        self.tracker_tracer = conversation_tracer
        self.messages = []
        self.conversations = {}
        self.update_dict = {}
        self.channel = None

    def add_update_values(self, sid, key, val):
        slot_dict = {key: val}

        if sid in self.conversations:
            self.conversations[sid].update(slot_dict)
        elif sid in self.update_dict:
            self.update_dict[sid].update(slot_dict)
        else:
            self.update_dict[sid] = slot_dict

    def process_user_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_user_event'):
            logger.info(f'{event.sender_id} - Processing user event: {event.msg}')
            self.channel = event.input_channel
            transcript = self.to_transcript(event)

            if '/greet' in event.text:
                values = self.alcSeq.prepare_insert_conversation(event)
                self.conversations[event.sender_id] = values
            elif self._is_goodbye_msg_callback(event.text):
                self.add_update_values(event.sender_id, 'endTime', int(round(time.time() * 1000)))

            self.messages.append(self.alcSeq.create_message(transcript))

    def process_slot_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_slot_event'):
            slot_name = event.name
            sid = event.sender_id
            logger.info(f'{event.sender_id} - Processing slot {slot_name}.....')

            if slot_name == 'channelUserId':
                event.channel_user_id = event.value
                self.add_update_values(sid, slot_name, event.value)
            elif slot_name == 'feedback_value':
                if isinstance(event.value, list):
                    rating = event.value[0]
                else:
                    rating = event.value
                event.rating = rating
                self.add_update_values(sid, 'rating', rating)
            elif slot_name == 'feedback_text':
                event.feedback = event.value
                self.add_update_values(sid, 'feedbackText', event.value)
            elif slot_name == 'errors':
                event.errors = event.value
                self.add_update_values(sid, slot_name, event.value)
            elif slot_name == 'guid':
                event.guid = event.value
                self.add_update_values(sid, slot_name, event.value)
            elif slot_name == 'system_event':
                self.messages.append(self.alcSeq.create_system_evt(sid, event))

    def process_bot_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_bot_event'):
            logger.info(f'{event.sender_id} - Processing bot event.....')
            transcript = self.to_transcript(event)
            self.messages.append(self.alcSeq.create_message(transcript))

    def process_action_event(self, event, cue=None):
        pass

    def to_transcript(self, event):
        sql_transcript = Transcript()
        sql_transcript.process_event(event, self.channel)

        return sql_transcript

    def get_offsets(self, partition_nums, groud_id):
        res = self.alcSeq.get_offsets(partition_nums, groud_id)
        return res.fetchall()

    def get_save_offset_stmt(self, group_id, partition, offset):
        return self.alcSeq.get_save_offset_stmt(group_id, partition, offset)

    def clear_states(self):
        self.messages = []
        self.conversations = {}


class CueHandler(EventHandler):
    def __init__(self):
        super(CueHandler, self).__init__()
        self.tracker_tracer = cue_tracer
        self.cue = None
        self.insert_tasks = {}
        self.ids_to_update = {}
        self.redis_repo = RedisRepository.get_instance(cue_tracer)

    def append_cue_events(self, sid, events):
        if sid in self.insert_tasks:
            self.insert_tasks[sid] += events
        elif sid in self.ids_to_update:
            self.ids_to_update[sid] += events
        else:
            self.ids_to_update[sid] = events

    async def process(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process') as scope:
            scope.span.set_tag('sender_id', event.sender_id)
            scope.span.log_kv({'message': event.msg})

            if event.event_type == 'user':
                await self.process_user_event(event, cue)
            elif event.event_type == 'bot':
                await self.process_bot_event(event, cue)
            elif event.event_type == 'slot':
                await self.process_slot_event(event, cue)
            elif event.event_type == 'action':
                if event.name in ['action_listen', 'action_deactivate_form', environ['ERROR_STATE']]:
                    return

                await self.process_action_event(event, cue)

    async def process_user_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_user_event'):
            if self._is_goodbye_msg_callback(event.text):
                cue.end_call(event)
            else:
                cue.recognition(event)

            if event.is_start_state():
                self.first_user_input_init(event, cue)
                self.insert_tasks[event.sender_id] = cue.state.events
            else:
                self.append_cue_events(event.sender_id, cue.state.events)

            with self.tracker_tracer.start_active_span('cue_save_state'):
                await cue.save_state()

    async def process_slot_event(self, event, cue=None):
        pass

    async def process_action_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_action_event'):
            current_state = cue.transition(event)
            if current_state:
                self.append_cue_events(event.sender_id, cue.state.events)
                with self.tracker_tracer.start_active_span('cue_save_state'):
                    await cue.save_state()

    async def process_bot_event(self, event, cue=None):
        pass

    async def insert_cue(self, sid, events, session):
        """ Write new CUE events to VVA """
        with self.tracker_tracer.start_active_span('insert_cue'):
            cue_state = await self.construct_cue_state(f'cue_{sid}', events)
            newdata = {
                "action": "insertCueData",
                "cueData": json.dumps(cue_state),
            }
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            logger.info(f"INSERT_CUE: [{sid}] - {newdata}")

            try:
                async with session.post(CUE_URL, headers=headers, data=newdata, timeout=REQUEST_TIMEOUT) as response:
                    if response.status is 200:
                        res = await response.text()
                        root = ET.fromstring(res)
                        for child in root:
                            if child.tag == "status":
                                cue_id = child.text
                                await self.redis_repo.set_key_val('cue_{}'.format(cue_state.callId), 'cueId', cue_id)
                                return cue_id
                    else:
                        logger.warning(f'INSERT_CUE: [{sid}] - {response}')
            except (asyncio.TimeoutError, asyncio.CancelledError) as err:
                traceback_msg = traceback.format_exc().replace("\n", "")
                logger.warning(
                    f'INSERT_CUE: [{sid}] - Timeout/cancelled error occurred in sending events: {traceback_msg}')
            except Exception as exp:
                traceback_msg = traceback.format_exc().replace("\n", "")
                logger.warning(f'INSERT_CUE: [{sid}] - {traceback_msg}')

            return None

    async def update_cue(self, sid, events, session):
        """ Update CUE events in VVA """
        with self.tracker_tracer.start_active_span('update_cue'):
            state_key = f'cue_{sid}'
            cue_state = await self.construct_cue_state(state_key, events)
            max_retries = 3
            retries = 0
            retry_in_secs = 1
            cue_id = cue_state.cueId

            while retries < max_retries:
                if cue_id is None:
                    logger.warning(f'UPDATE_CUE: [{sid}] - CUE id is not found. Retrying...')
                    retries += 1
                    await asyncio.sleep(retry_in_secs)
                    cue_id = await self.redis_repo.get_cue_id(state_key)
                else:
                    with self.tracker_tracer.start_active_span('update_cue'):
                        newdata = {
                            "action": "updateAndAddEvents",
                            "cueData": json.dumps(cue_state),
                            "id": cue_id,
                        }
                        logger.info(f"UPDATE_CUE: [{sid}] - {newdata}")
                        headers = {"Content-Type": "application/x-www-form-urlencoded"}
                        try:
                            asyncio.ensure_future(
                                session.post(CUE_URL, headers=headers, data=newdata, timeout=REQUEST_TIMEOUT)
                            )
                        except (asyncio.TimeoutError, asyncio.CancelledError) as err:
                            traceback_msg = traceback.format_exc().replace("\n", "")
                            logger.warning(
                                f'UPDATE_CUE: [{sid}] - Timeout/cancelled error occurred in sending events: {traceback_msg}')
                        except Exception as exp:
                            traceback_msg = traceback.format_exc().replace("\n", "")
                            logger.warning(f'UPDATE_CUE: [{sid}] - {traceback_msg}')
                        break


class UpmHandler(EventHandler):
    def __init__(self):
        super(UpmHandler, self).__init__()
        self.tracker_tracer = upm_tracer
        self.cue = None
        self.tasks = {}
        self.UPM_URL = environ.get("UPM_URL")
        self.redis_repo = RedisRepository.get_instance(self.tracker_tracer)

    def append_cue_events(self, sid, events):
        if sid in self.tasks:
            self.tasks[sid] += events
        else:
            self.tasks[sid] = events

    async def process(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process') as scope:
            scope.span.set_tag('sender_id', event.sender_id)
            scope.span.log_kv({'message': event.msg})

            if event.event_type == 'user':
                await self.process_user_event(event, cue)
            elif event.event_type == 'bot':
                await self.process_bot_event(event, cue)
            elif event.event_type == 'slot':
                await self.process_slot_event(event, cue)
            elif event.event_type == 'action':
                if event.name in ['action_listen', 'action_deactivate_form', environ['ERROR_STATE']]:
                    return

                await self.process_action_event(event, cue)

    async def process_user_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_user_event'):
            if self._is_goodbye_msg_callback(event.text):
                cue.end_call(event)
            else:
                cue.recognition(event)

            if event.is_start_state():
                self.first_user_input_init(event, cue)
            else:
                self.append_cue_events(event.sender_id, cue.state.events)
            await cue.save_state()

    async def process_slot_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_slot_event'):
            slot_name = event.name
            if slot_name == 'guid':
                await cue.set_guid(event.value)
            elif slot_name == 'channelUserId':
                await cue.set_csid(event.value)
            elif slot_name == 'task_incomplete':
                cue.begin_task(event)
                self.append_cue_events(event.sender_id, cue.state.events)
            elif slot_name == 'task_completed':
                cue.end_task(event)
                self.append_cue_events(event.sender_id, cue.state.events)
            elif slot_name.startswith('custom'):
                cue.create_custom_evt(event)
                self.append_cue_events(event.sender_id, cue.state.events)

    async def process_action_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_action_event'):
            current_state = cue.transition(event)
            if current_state:
                self.append_cue_events(event.sender_id, cue.state.events)
                await cue.save_state()

    async def process_bot_event(self, event, cue=None):
        with self.tracker_tracer.start_active_span('process_bot_event'):
            cue.bot_utterance(event)
            self.append_cue_events(event.sender_id, cue.state.events)
            await cue.save_state()

    async def put_upm(self, sid, events, session):
        cue_state = await self.construct_cue_state(f'upm_{sid}', events)
        logger.info(f"UPDATE_UPM: [{sid}] - {json.dumps(cue_state)}")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Conversation-Id": sid
        }

        with upm_tracer.start_active_span('put_upm'):
            try:
                await session.put("{}/engagements".format(self.UPM_URL), headers=headers,
                                  data=json.dumps(cue_state), timeout=REQUEST_TIMEOUT)
            except (asyncio.TimeoutError, asyncio.CancelledError) as err:
                traceback_msg = traceback.format_exc().replace("\n", "")
                logger.warning(f'UPDATE_UPM: [{sid}] - Timeout/cancelled error occurred in sending events: {traceback_msg}')
            except Exception as exp:
                traceback_msg = traceback.format_exc().replace("\n", "")
                logger.warning(f'UPDATE_UPM: [{sid}] - {traceback_msg}')

from datetime import datetime
from os import environ

DNIS_LOOKUP = {
    "persy": "OMNI_VOICE_00001",
    "webchat": "OMNI_WEBCHAT_00001",
    "dashchat": "OMNI_DASHCHAT_00001",
    "IOSApp": "OMNI_IOSAPP_00001",
    "rest": "OMNI_WEBCHAT_00001"
}
CALL_START = environ.get("CALL_START") or 'utter_greet'


class Event:
    def __init__(self, msg):
        self.msg = msg
        self.sender_id = msg.get('sender_id')
        self.event_type = msg.get('event')
        self.timestamp = int(round(msg.get('timestamp') * 1000))
        self.iso_timestamp = datetime.utcfromtimestamp(msg.get('timestamp')).isoformat()[:-3] + "Z"
        self.name = msg.get('name')
        self.confidence = msg.get('confidence')
        self.asr_confidence = msg.get('asr_confidence')
        self.input_channel = msg.get('input_channel')
        self.channel_user_id = msg.get('channel_user_id')
        self.text = msg.get('text')
        self.parse_data = msg.get('parse_data')
        self.value = msg.get('value')
        self.outcome = 'HANGUP'
        self.errors = 0
        self.feedback = None
        self.rating = None
        self.dnis = msg.get('input_channel')
        self.start_time = msg.get('start_time')
        self.last_state = msg.get('last_state')
        self.guid = msg.get('guid')

    def get_intent(self):
        if self.parse_data is None:
            return None

        return self.parse_data['intent']

    def get_intent_name(self):
        if self.parse_data is None:
            return None

        return self.get_intent()['name']

    def get_intent_text(self):
        if self.parse_data is None or self.get_intent_name() is None:
            return None

        return self.parse_data['intent']['text']

    def set_dnis(self, input_channel):
        self.dnis = DNIS_LOOKUP.get(input_channel)

    def get_confidence(self):
        if self.parse_data is None or self.get_intent_name() is None:
            return None

        return self.parse_data['intent']['confidence']

    def get_entities_list(self):
        if self.parse_data is None:
            return None

        return self.parse_data['entities']

    def is_start_state(self):
        if self.parse_data is None:
            return False

        intent = self.get_intent_name()
        entities_list = self.get_entities_list()
        entity = None
        if len(entities_list) > 0:
            entity = entities_list[0]['entity']

        return intent == 'greet' and entity == 'channelUserId'

    def is_missed_intent(self):
        return self.msg.get("parse_data", {}).get("missed_intent", False)


class CueState:
    def __init__(self):
        self.ani = None
        self.dnis = None
        self.cueId = None
        self.callId = None
        self.appName = "AIO_Stream"
        self.sessionId = "20140627131928797stxload08availsys.com_1"
        self.appOutcome = "HANGUP"
        self.subsystemId = "1234"
        self.appVersion = "DEMO_DM"
        self.cueVersion = "2.0"
        self.currentState = CALL_START
        self.lastState = None
        self.globalUserId = None
        self.channelSessionId = None
        self.noinputCount = 0
        self.nomatchCount = 0
        self.errorCount = 0
        self.recoCount = 0
        self.helpCount = 0
        self.transitionCount = 0
        self.events = []
        self.startTime = None
        self.startTimeFormatted = None
        self.endTime = None
        self.endTimeFormatted = None
        self.callLength = None

    def init_state(self, state):
        int_fields = ('noinputCount', 'nomatchCount', 'errorCount', 'recoCount',
                      'helpCount', 'transitionCount', 'startTime', 'endTime')

        float_fields = ('callLength')

        for key in state:
            if key in int_fields:
                setattr(self, key, int(state[key]))
            elif key in float_fields:
                setattr(self, key, float(state[key]))
            else:
                setattr(self, key, state[key])

    def reset_errors(self):
        self.noinputCount = 0
        self.nomatchCount = 0
        self.errorCount = 0

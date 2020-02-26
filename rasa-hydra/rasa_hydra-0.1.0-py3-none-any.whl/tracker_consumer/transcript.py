from tracker_consumer.constants import USER_EVENT, NLU_EVENT


class Transcript:
    def __init__(self):
        self.sender_id = None
        self.voice = False
        self.conversation_id = False
        self.message = None
        self.asr_confidence = 1
        self.nlu_confidence = 1
        self.recording_id = None
        self.agent = None
        self.timestamp = None
        self.intent = None
        self.errors = False
        self.missed_intent = False

    def process_event(self, event, channel):
        self.conversation_id = event.sender_id
        self.set_voice(channel)
        event_type = event.event_type
        if event_type == USER_EVENT or event_type == NLU_EVENT:
            self.message = event.text
            parse_data = event.parse_data
            self.nlu_confidence = float(parse_data['intent']['confidence'])
            self.intent = parse_data['intent']['name']
            self.errors = self.intent == None
            self.missed_intent = event.is_missed_intent()
            if self.voice:
                self.asr_confidence = float(parse_data['asrConfidence'])
                self.recording_id = parse_data['recordingId']
        else:
            self.message = event.text

        self.agent = event.event_type
        self.timestamp = event.timestamp

    def set_voice(self, dnis):
        """ Sets whether or not this conversation is taking place on a voice channel """
        if dnis == "persy":
            self.voice = True
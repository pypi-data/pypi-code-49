import dinemic
import logging

class Listener(dinemic.DAction):
    listener_name = None
    call_on = None
    action = None
    context = None
    trigger = None

    def __init__(self, listener_name, document, context):
        super(Listener, self).__init__()

        self.context = context
        self.listener_name = listener_name

        self.action = document['action']
        self.trigger = document['trigger']

        if type(document['call_on']) == list:
            self.call_on = document['call_on']
        else:
            self.call_on = [document['call_on']]

        logging.info('New listener ' + self.listener_name)

        if self.trigger != "!":
            self.starsheep_apply(self.trigger)
            logging.info('Registered listener ' + self.listener_name + ' on ' + self.trigger)

    def __str__(self):
        return self.listener_name

    def call(self):
        raise Exception('Abstract method')

    def starsheep_apply(self, listener_filter):
        raise Exception('Abstract method')

    @staticmethod
    def load(document, context):
        from starsheep.listeners import RejectListener
        from starsheep.listeners.script_listener import ScriptListener

        listeners = {}

        for listener_name in document.keys():
            if 'call_on' not in document[listener_name]:
                print(document)
                print('Missing "call_on" in ' + listener_name)
                continue
            if 'trigger' not in document[listener_name]:
                print('Missing "trigger" in ' + listener_name)
                continue
            if 'action' not in document[listener_name]:
                print('Missing "action" in ' + listener_name)
                continue

            if document[listener_name]['action'] == 'reject':
                listeners[listener_name] = RejectListener(listener_name, document[listener_name], context)
            elif document[listener_name]['action'] == 'script':
                listeners[listener_name] = ScriptListener(listener_name, document[listener_name], context)

        context.listeners = listeners

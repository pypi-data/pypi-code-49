from b22ao.aosystem import AOSystem
from b22ao.message import Message, State


class BaseOperation:

    """
    Base class for any adaptive optics routine.
    Children implement #start and #halt, and can #deform the mirrors and #capture data from the camera at their leisure!
    """

    def __init__(self):

        self.ao = AOSystem()
        self.config = None
        self.listener = None

    def attach_listener(self, listener):
        self.listener = listener

    def load_config(self, config):
        if config:
            import json
            with open(config, 'r') as doc:
                self.config = json.load(doc)

    def select_dm(self, dm):
        """
        If your entire operation involves a single mirror, you can specify it here
        e.g.

        from api.aosystem import DM
        self.select_dm(DM.DM2)
        ...
        self.deform(mask)  # no need to specify mirror in subsequent calls
        """
        self.ao.select_dm(dm)

    def deform(self, mask, mirror=None):
        self.ao.deform(mask, mirror)

    def capture(self):
        return self.ao.capture()

    def run(self):
        """
        Do not override. Implement #start instead
        """
        if self.listener:
            self.listener.notify(Message(self, State.Started))
        self.start()
        if self.listener:
            self.listener.notify(Message(self, State.Finished))

    def abort(self):
        """
        Do not override. Implement #halt instead
        """
        self.stop()
        if self.listener:
            self.listener.notify(Message(self, State.Failed, "Aborted"))

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

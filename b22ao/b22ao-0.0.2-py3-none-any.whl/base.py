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

        e.g. passed in as config:

        self.select_dm(self.config['mirror'])  # where "mirror": 2 in config file
        # later:
        self.deform(mask)  # no need to specify mirror in subsequent calls
        """
        self.ao.select_dm(dm)

    def deform(self, mask, mirror=None):
        """
        Send a mask to specified mirror (1 or 2).

        If a mirror was previously selected with #select_dm
        and no mirror is specified here, the mask is applied
        to the mirror selected earlier.

        Bear in mind that the deformable mirrors in B22 *do not* support readback,
        so there is no guarantee that the mask is fully applied by the time this
        function returns; it may be necessary to wait for an empirically-determined
        time before characterising the system.
        """
        self.ao.deform(mask, mirror)

    def capture(self):
        """
        Returns a single detector frame
        """
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
        """
        Starts the operation

        If a JSON configuration file was specified,
        implementations can now access the dictionary self.config
        """
        raise NotImplementedError

    def stop(self):
        """
        Stops the operation
        """
        raise NotImplementedError

from .. import Module, Log
from .. import Join
from datetime import datetime

log = Log("CORE:Creator", verbose="log")
class Creator(Module):

    def __init__(self, channel):
        Module.__init__(self, "Creator")
        self.channel = channel
        self.launchTime = datetime.now()

    def on_join(self, data: Join):
        if "cubbei" in data.line and (datetime.now() - self.launchTime).seconds > 60:
            self.channel.send("/me bows to the creator")



def setup(channel):
    channel.load_module(Creator(channel))

def teardown(channel):
    log.log(f"[{channel.channel_name}]: Removed Module Creator")
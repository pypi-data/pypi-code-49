from .. import Module, Log
from .. import PrivateMessage, CommandMessage

log = Log("CORE:Ping", verbose="log")
class Ping(Module):

    def __init__(self, channel):
        Module.__init__(self, "Ping")
        self.channel = channel

    
    def on_privmessage(self, data: PrivateMessage):
        if data.user_id == "82504138":
            if "ping" == data.message_text:
                self.channel.send("pong...")
            elif "peanut" == data.message_text:
                self.channel.send("butter! Kappa")

    def on_command(self, data: CommandMessage):
        if data.user_id == "82504138":
            if "ping" == data.KEYWORD:
                self.channel.send("pong...")
            elif "peanut" == data.KEYWORD:
                self.channel.send("butter! Kappa")


def setup(channel):
    channel.load_module(Ping(channel))
    log.log(f"[{channel.channel_name}]: Loaded Module Ping")

def teardown(channel):
    log.log(f"[{channel.channel_name}]: Removed Module Ping")
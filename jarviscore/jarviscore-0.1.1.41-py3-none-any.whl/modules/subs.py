from .. import Module, Log, Settings
from .. import ConfigFileNotFound
from .. import SubscriberUserNotice, GiftedSubscriberUserNotice


log = Log("CORE:Subs", verbose="log")

class Subs(Module):

    def __init__(self, channel):
        Module.__init__(self, "Subs")
        self.channel = channel
        self.log = Log("Subs")
        self.giftedSubCount = 0
        self.giftedSubCountOffset = 0
        self.giftedSubNoticeSent = True
        self.giftedSubs = []


    def on_subscriber_usernotice(self, data: SubscriberUserNotice):
        service = data.cumulative_months
        
        if service == 0:
            service = 1
        
        message = ""
        if service == 1:
            message = f"{data.display_name} just subscribed for the first time! Welcome to the family ♥"
        else:
            month = service % 12
            if month > 1: mt = "s"
            years = int(service/12)
            if years > 0: 
                if years > 1: yt = f"{years} years and " 
                else: yt = "1 year and "  
            message = f"{data.display_name} resubscribed for another month. That's a total of {yt} {month} month{mt}"
        self.channel.send(message)


    def on_giftedsubscriber_usernotice(self, data: GiftedSubscriberUserNotice):
        if data.anonymous: name = "An anonymous legend"
        else: name = data.sender_display_name
        if data.mass_gift_count > 0:
            self.giftedSubCount = data.mass_gift_count
            self.giftedSubCountOffset = 1
            self.giftedSubNoticeSent = False
            self.giftedSubs = []
        else:
            if self.giftedSubNoticeSent:
                message = f"{name} gifted a sub to {data.recipient_display_name}"
                self.channel.send(message)
            else:
                if self.giftedSubCount <= 10:
                    if (self.giftedSubCount - self.giftedSubCountOffset) == 1:
                        names = ""
                        message = f"{name} gifted {self.giftedSubCount} subs to"
                        for name in self.giftedSubs:
                            names += f" {name},"
                        message += names[:-1] + f" and {data.recipient_display_name} KAPOW"
                        self.channel.send(message)
                    else:
                        self.giftedSubCountOffset += 1
                        self.giftedSubs.append(data.recipient_display_name)
                else:
                    if not self.giftedSubNoticeSent:
                        self.giftedSubNoticeSent = True
                        others = self.giftedSubCount - 1
                        message = f"{name} gifted {self.giftedSubCount} subs to {data.recipient_display_name} and {others} others PogChamp"
                        self.channel.send(message)
            


def setup(channel):
    try:
        settings = Settings()
        try:
            if settings.get_setting("commands.subs") == True:
                channel.load_module(Subs(channel))
                log.log(f"[{channel.channel_name}]: Loaded Module Subs")
        except KeyError:
            pass # command.subs not in settings file
    except ConfigFileNotFound:
        pass # settings file not found


def teardown(channel):
    log.log(f"[{channel.channel_name}]: Removed Module Subs")
    
from .message import *

class Module():
    name : str

    def __init__(self, name):
        self.name = name

    def get_name(self):
        if self.name is None:
            return "undefined"
        return self.name

    def on_raw(self, data: RawMessage):
        """Invoked when a RawMessage message is sent to the bot."""
        pass

    def on_join(self, data: Join):
        """Invoked when a Join message is sent to the bot."""
        pass

    def on_part(self, data: Part):
        """Invoked when a Part message is sent to the bot."""
        pass

    def on_mode(self, data: Mode): 
        """Invoked when a Mode message is sent to the bot."""
        pass

    def on_names(self, data: Names): 
        """Invoked when a Names message is sent to the bot."""
        pass

    def on_clearchat(self, data: ClearChat): 
        """Invoked when a ClearChat message is sent to the bot."""
        pass

    def on_clearmessage(self, data: ClearMessage): 
        """Invoked when a ClearMessage message is sent to the bot."""
        pass

    def on_hosttarget(self, data: HostTarget): 
        """Invoked when a HostTarget message is sent to the bot."""
        pass

    def on_notice(self, data: Notice): 
        """Invoked when a Notice message is sent to the bot."""
        pass

    def on_reconnect(self, data: Reconnect): 
        """Invoked when a Reconnect message is sent to the bot."""
        pass

    def on_roomstate(self, data: RoomState): 
        """Invoked when a RoomState message is sent to the bot."""
        pass

    def on_userstate(self, data: UserState): 
        """Invoked when a UserState message is sent to the bot."""
        pass

    def on_globaluserstate(self, data: GlobalUserState): 
        """Invoked when a GlobalUserState message is sent to the bot."""
        pass

    def on_privmessage(self, data: PrivateMessage):
        """Invoked when a PrivateMessage message is sent to the bot."""
        pass

    def on_usernotice(self, data: UserNotice):
        """Invoked when a UserNotice message is sent to the bot."""
        pass

    def on_ritual_usernotice(self, data: RitualUserNotice):
        """Invoked when a RitualUserNotice message is sent to the bot."""
        pass

    def on_bitbadgeupgrade_usernotice(self, data: BitBadgeUpgradeUserNotice):
        """Invoked when a BitBadgeUpgradeUserNotice message is sent to the bot."""
        pass

    def on_raid_usernotice(self, data: RaidUserNotice):
        """Invoked when a RaidUserNotice message is sent to the bot."""
        pass

    def on_subscriber_usernotice(self, data: SubscriberUserNotice):
        """Invoked when a SubscriberUserNotice message is sent to the bot."""
        pass

    def on_giftedsubscriber_usernotice(self, data: GiftedSubscriberUserNotice):
        """Invoked when a GiftedSubscriberUserNotice message is sent to the bot."""
        pass

    def on_whisper(self, data: Whisper):
        """Invoked when a Whisper message is sent to the bot."""
        pass

    def on_command(self, data: CommandMessage):
        """Invoked when a CommandMessage message is sent to the bot."""
        pass

    def on_heartbeat(self):
        """Invoked when the core heartbeat runs."""
        pass


    def setup(self, channel):
        raise NotImplementedError()
        #client.log.debug(f"Loaded Command {self.name}")

    def teardown(self, channel):
        raise NotImplementedError()
        #client.log.debug(f"Removed Command {self.name}")



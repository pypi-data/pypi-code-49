from datetime import datetime


class RawMessage():
    inner:str = "RawMessage"
    line: str
    message_time: datetime

    def __repr__(self):
        return f"[{self.inner}]: {self.line}"

    

class Message(RawMessage):
    message: str
    inner:str = "Message"
    pass

    def __repr__(self):
        return f"[{self.inner}]: {self.message}"



# Twitch IRC: Membership | https://dev.twitch.tv/docs/irc/membership

class Join(RawMessage):
    inner:str = "Join"
    pass

class Mode(RawMessage):
    inner:str = "Mode"
    pass

class Names(RawMessage):
    inner:str = "Names"
    pass

class Part(RawMessage):
    inner:str = "Part"
    pass


class Whisper(RawMessage):
    inner: str = "Whisper"
    badges: dict
    color: str
    display_name: str
    emotes: list
    id: str
    user_id: str
    message_text: str
    channel: str
    pass

    def __repr__(self):
        return f"[{self.inner}]: {self.display_name} => {self.message_text}"




# Twitch IRC: Commands & Tags | 
# https://dev.twitch.tv/docs/irc/commands & https://dev.twitch.tv/docs/irc/tags

class ClearChat(RawMessage):
    inner: str = "ClearChat"
    target_all: bool
    ban_duration: int
    channel: str
    
    def __repr__(self):
        return f"""[CLEARCHAT]:
Ban Duration: {self.ban_duration}
Channel: {self.channel}
"""

class ClearMessage(Message):
    inner: str = "ClearMessage"
    login: str
    target_message_id: str
    pass

class HostTarget(RawMessage):
    inner: str = "HostTarget"
    number_of_viewers: int
    pass

class Notice(Message):
    inner: str = "Notice"
    message_id: str
    pass

class Reconnect(RawMessage):
    inner: str = "Reconnect"
    pass

class RoomState(RawMessage):
    inner: str = "RoomState"
    emote_only: bool
    follower_only: bool
    r9k: bool
    slow: int
    subs_only: bool
    channel: str
    
    def __repr__(self):
        return f"""[ROOMSTATE]:
Emote Only?: {self.emote_only}
Follower Only?: {self.follower_only}
R9K?: {self.r9k}
Slow Interval: {self.slow}
Subs Only?: {self.subs_only}
Channel: {self.channel}
"""



class UserState(RawMessage):
    """
    Sends user-state data when a user joins a channel or sends a PRIVMSG to a channel.

    info: https://dev.twitch.tv/docs/irc/tags#userstate-twitch-tags
    """
    inner: str = "UserState"
    badge_info: str
    badges: list
    color: str
    display_name: str
    emote_set: list
    mod: bool
    channel: str


    def __repr__(self):
        return f"""[USERSTATE]:
Badge info: {self.badge_info}
Badges: {self.badges}
Display Name: {self.display_name}
Emote Set: {self.emote_set}
Mod?: {self.mod}
Channel: {self.channel}
"""

class GlobalUserState(RawMessage):
    """
    On successful login, provides data about the current 
    logged-in user through IRC tags. It is sent after successfully 
    authenticating (sending a PASS/NICK command).

    info: https://dev.twitch.tv/docs/irc/tags#globaluserstate-twitch-tags
    """
    inner: str = "GlobalUserState"
    badge_info: dict
    badges: dict
    color: str
    display_name: str
    emote_set: list
    user_id: str
    pass
    
class PrivateMessage(RawMessage):
    """
    Sends a message to a channel. 
    A regular Twitch chat message.

    info: https://dev.twitch.tv/docs/irc/tags#privmsg-twitch-tags
    """
    inner: str = "PrivateMessage"
    badge_info: dict
    badges: dict
    bits: int
    color: str
    display_name: str
    emotes: list
    id: str
    mod: bool
    room_id: str
    sent_timestamp: datetime
    user_id: str
    message_text: str
    channel: str
    
    def __repr__(self):
        return f"""[PRIVMSG]:
Badge info: {self.badge_info}
Badges: {self.badges}
Bits: {self.bits}
Color: {self.color}
Display Name: {self.display_name}
Emotes: {self.emotes}
ID: {self.id}
Mod?: {self.mod}
Room-ID: {self.room_id}
Sent Timestamp: {self.sent_timestamp}
User-ID: {self.user_id}
Channel: {self.channel}
Message Text: {self.message_text}
"""

class UserNotice(PrivateMessage):
    """
    Sends a notice to the user when any of the following events occurs:

    - Subscription, resubscription, or gift subscription to a channel.
    - Incoming raid to a channel. Raid is a Twitch tool that allows broadcasters to send their viewers to another channel, to help support and grow other members in the community.)
    - Channel ritual. Many channels have special rituals to celebrate viewer milestones when they are shared. The rituals notice extends the sharing of these messages to other viewer milestones (initially, a new viewer chatting for the first time).

    info: https://dev.twitch.tv/docs/irc/tags#usernotice-twitch-tags
    """
    inner: str = "UserNotice"
    login: str
    msg_id: str
    system_message: str
    message_text: str
    pass

class RitualUserNotice(UserNotice):
    inner: str = "RitualUserNotice"
    ritual_name: str
    pass

class BitBadgeUpgradeUserNotice(UserNotice):
    inner: str = "BitBadgeUpgradeUserNotice"
    threshold: int
    pass

class RaidUserNotice(UserNotice):
    """
    A UserNotice Object for Raids
    """
    inner: str = "RaidUserNotice"
    raider_display_name: str
    raider_login: str
    viewer_count: int

class SubscriberUserNotice(UserNotice):
    """
    A UserNotice Object for Subscription or Re-subscription Events
    """
    inner: str = "SubscriberUserNotice"
    cumulative_months: int
    share_streak: bool
    streak_months: int
    sub_plan: str
    sub_plan_name: str

    pass

class GiftedSubscriberUserNotice(UserNotice):
    """
    A UserNotice Object for Gifted Subs, included Anonyumous Gifts.
    """
    inner: str = "GiftedSubscriberUserNotice"
    cumulative_months: int
    anonymous: bool
    active_promo: bool
    promo_gift_total: int
    promo_name: str
    mass_gift_count: int
    recipient_display_name: str
    recipient_id: str
    sender_login: str
    sender_display_name: str
    sub_plan: str
    sub_plan_name: str



class CommandMessage(PrivateMessage):
    KEYWORD: str
    args: list    
    inner: str = "CommandMessage"
    

    def __repr__(self):
        return f"""[PRIVMSG: Command]:
Badge info: {self.badge_info}
Badges: {self.badges}
Bits: {self.bits}
Color: {self.color}
Display Name: {self.display_name}
Emotes: {self.emotes}
ID: {self.id}
Mod?: {self.mod}
Room-ID: {self.room_id}
Sent Timestamp: {self.sent_timestamp}
User-ID: {self.user_id}
Channel: {self.channel}
Message Text: {self.message_text}
Keyword: {self.KEYWORD}
"""




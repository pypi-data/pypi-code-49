from .message import *
from datetime import datetime
import re


def parse_line(line: str) -> RawMessage:
    """Parse a raw line coming in and return a Message Object"""
    
    pattern = re.compile(":[a-z0-9]+![a-z0-9]+@[a-z0-9]+.tmi.twitch.tv JOIN #")
    if pattern.match(line): #join
        return __parse_join(line)
    pattern = re.compile(":[a-z0-9]+.tmi.twitch.tv 3(53|66)")
    if pattern.match(line): #names
        return __parse_names(line)
    pattern = re.compile(":tmi.twitch.tv USERSTATE")
    if pattern.search(line): #user state
        return __parse_userstate(line)
    
    pattern = re.compile(":tmi.twitch.tv ROOMSTATE")
    if pattern.search(line): #room state
        return __parse_roomstate(line)

    pattern = re.compile(":[a-z0-9]+![a-z0-9]+@[a-z0-9]+.tmi.twitch.tv PRIVMSG")
    if pattern.search(line): #Private Message
        return __parse_privatemessage(line)
    
    pattern = re.compile(":tmi.twitch.tv CLEARCHAT")
    if pattern.search(line): #Clear Chat
        return __parse_clearchat(line)
    
    pattern = re.compile(":tmi.twitch.tv CLEARMSG")
    if pattern.search(line): #Clear Message
        return __parse_clearchat(line)

    pattern = re.compile(":tmi.twitch.tv GLOBALUSERSTATE")
    if pattern.search(line): #Global user state
        return __parse_globaluserstate(line)
    

    pattern = re.compile(":tmi.twitch.tv USERNOTICE")
    if pattern.search(line): #user notice
        return __parse_usernotice(line)

    pattern = re.compile(":tmi.twitch.tv USERSTATE")
    if pattern.search(line): #user state
        return __parse_usernotice(line)
    
    pattern = re.compile(".tmi.twitch.tv WHISPER")
    if pattern.search(line): #user state
        return __parse_whisper(line)




    # Fallthrough case
    msg = RawMessage()
    msg.line = line
    msg.message_time = datetime.now()
    return msg

def __parse_whisper(line:str) -> Whisper:
    msg = Whisper()
    msg.line = line
    msg.message_time = datetime.now()
    msg.badges = [re.sub(r"\/\d","", badge) for badge in __get_list(line, "badges")]
    msg.color = __get_single(line, "color")
    msg.display_name = __get_single(line, "display-name")
    msg.emotes = __get_list(line, "emotes")
    msg.id = __get_single(line, "id")
    msg.user_id = __get_single(line, "user-id")
    msg.message_text = __get_whisper_message(line)
    msg.channel = __get_whisper_channel(line)
    return msg


def __parse_userstate(line: str) -> UserState:
    msg = UserState()
    msg.line = line
    msg.message_time = datetime.now()
    msg.badge_info = __get_single(line, "badge-info")
    msg.badges = [re.sub(r"\/\d","", badge) for badge in __get_list(line, "badges")]
    
    msg.color = __get_single(line, "color")
    msg.display_name = __get_single(line, "display-name")
    msg.emote_set = __get_list(line, "emote-set")
    msg.channel = __get_channel(line, "USERSTATE")
    msg.mod = "1" == __get_single(line, "mod")
    return msg


def __parse_usernotice(line: str) -> UserNotice:
    notice_type = __get_single(line, "msg-id")
    if notice_type in ("sub", "resub"):
        msg = SubscriberUserNotice()
        msg.cumulative_months = __get_single(line, "msg-param-cumulative-months")
        msg.share_streak = __get_single(line, "msg-param-should-share-streak")
        msg.streak_months = int(__get_single(line, "msg-param-streak-months"))
        msg.sub_plan = __get_single(line, "msg-param-sub-plan")
        msg.sub_plan_name = __get_single(line, "msg-param-sub-plan-name")
    elif notice_type in ("subgift","anonsubgift","submysterygift", "giftpaidupgrade", "rewardgift", "anongiftpaidupgrade"):
        msg = GiftedSubscriberUserNotice()
        msg.sub_plan = __get_single(line, "msg-param-sub-plan")
        msg.sub_plan_name = __get_single(line, "msg-param-sub-plan-name")
        msg.cumulative_months = __get_single(line, "msg-param-months")
        msg.promo_gift_total = __get_single(line, "msg-param-promo-gift-total")
        msg.mass_gift_count = __get_single(line, "msg-param-mass-gift-count")
        msg.promo_name = __get_single(line, "msg-param-promo-name")
        msg.recipient_display_name = __get_single(line, "msg-param-recipient-display-name")
        msg.recipient_id = __get_single(line, "msg-param-recipient-id")
        msg.sender_login = __get_single(line, "msg-param-sender-login")
        msg.sender_display_name = __get_single(line, "msg-param-sender-name")

    elif notice_type in ("raid", "unraid"):
        msg = RaidUserNotice()
        msg.raider_display_name = __get_single(line, "msg-param-displayName")
        msg.raider_login = __get_single(line, "msg-param-login")
        msg.viewer_count = int(__get_single(line, "msg-param-viewerCount"))
        
    elif notice_type == "ritual":
        msg = RitualUserNotice()
        msg.ritual_name = __get_single(line, "msg-param-ritual-name")
    elif notice_type == "bitsbadgetier":
        msg = BitBadgeUpgradeUserNotice()
        msg.threshold = __get_single(line, "msg-param-threshold")
    else:
        msg = UserNotice()
    
    msg.line = line
    msg.message_time = datetime.now()
    msg.badge_info = __get_single(line, "badge-info")
    msg.badges = [re.sub(r"\/\d","", badge) for badge in __get_list(line, "badges")]
    msg.bits = __get_single(line, "bits")
    msg.color = __get_single(line, "color")
    msg.display_name = __get_single(line, "display-name")
    msg.emotes = __get_list(line, "emotes")
    msg.id = __get_single(line, "id")
    msg.room_id = __get_single(line, "room-id")
    msg.sent_timestamp = __get_time_from_timestamp(line)
    msg.user_id = __get_single(line, "user-id")
    msg.mod = "1" == __get_single(line, "mod") or msg.room_id == msg.user_id
    msg.message_text = __get_message(line, "USERNOTICE")
    return msg


def __parse_globaluserstate(line: str) -> GlobalUserState:
    msg = GlobalUserState()
    msg.line = line
    msg.message_time = datetime.now()
    msg.badge_info = __get_single(line, "badge-info")
    msg.badges = [re.sub(r"\/\d","", badge) for badge in __get_list(line, "badges")]
    msg.color = __get_single(line, "color")
    msg.display_name = __get_single(line, "display-name")
    msg.emote_set = __get_list(line, "emote-set")
    msg.user_id = __get_single(line, "user-id")
    return msg


def __parse_clearmsg(line: str) -> ClearMessage:
    msg = ClearMessage()
    msg.line = line
    msg.message_time = datetime.now()
    msg.message = __get_message(line, "CLEARMSG")
    msg.login = __get_single(line, "login")
    msg.target_message_id = __get_single(line, "target-msg-id")
    return msg

def __parse_clearchat(line: str) -> ClearChat:
    msg = ClearChat()
    msg.line = line
    msg.message_time = datetime.now()
    msg.channel = __get_channel(line, "CLEARCHAT")
    msg.ban_duration = __get_single(line, "ban-duration")
    return msg


def __parse_privatemessage(line: str) -> PrivateMessage:
    t = __get_message(line, "PRIVMSG")
    if t[0] == "!":
        msg = CommandMessage()
        msg.args = t[1:].lower().split(" ")
        msg.KEYWORD = msg.args[0]
    else:
        msg = PrivateMessage()
    msg.channel = __get_channel(line, "PRIVMSG")
    msg.message_text = __get_message(line, "PRIVMSG")
    msg.line = line
    msg.message_time = datetime.now()
    msg.badge_info = __get_single(line, "badge-info")
    msg.badges = [re.sub(r"\/\d","", badge) for badge in __get_list(line, "badges")]
    msg.bits = __get_single(line, "bits")
    msg.color = __get_single(line, "color")
    msg.display_name = __get_single(line, "display-name")
    msg.emotes = __get_list(line, "emotes")
    msg.id = __get_single(line, "id")
    msg.room_id = __get_single(line, "room-id")
    msg.sent_timestamp = __get_time_from_timestamp(line)
    msg.user_id = __get_single(line, "user-id")
    msg.mod = "1" == __get_single(line, "mod") or msg.room_id == msg.user_id

    return msg



def __parse_roomstate(line: str) -> RoomState:
    msg = RoomState()
    msg.line = line
    msg.message_time = datetime.now()
    msg.channel = line.split("ROOMSTATE #", 1)[1]
    msg.emote_only = "1" == __get_single(line, "emote-only")
    msg.follower_only = int(__get_single(line, "followers-only")) > -1
    msg.r9k = "1" == __get_single(line, "r9k")
    msg.slow = int(__get_single(line, "slow"))
    msg.subs_only = "1" == __get_single(line, "subs-only")
    return msg

def __parse_userstate(line: str) -> UserState:
    msg = UserState()
    msg.line = line
    msg.message_time = datetime.now()
    msg.badge_info = __get_single(line, "badge-info")
    msg.badges = [re.sub(r"\/\d","", badge) for badge in __get_list(line, "badges")]
    msg.display_name = __get_single(line, "display-name")
    msg.mod = "1" == __get_single(line, "mod")
    msg.emote_set = __get_list(line, "emote-sets")
    msg.channel = __get_channel(line, "USERSTATE")
    return msg

def __parse_join(line: str) -> Join:
    msg = Join()
    msg.message_time = datetime.now()
    msg.line = line
    return msg

def __parse_names(line: str) -> Names:
    msg = Names()
    msg.line = line
    msg.message_time = datetime.now()
    return msg



# Helper Methods

def __get_single(line: str, key:str) -> str:
    try:
        return line.split(f"{key}=")[1].split(";")[0]
    except IndexError:
        return None

def __get_list(line: str, key:str) -> list:
    try:
        return line.split(f"{key}=")[1].split(";")[0].split(",")
    except IndexError:
        return None

def __get_channel(line: str, key: str) -> str:
    try:
        l = line.split(f"{key} #", 1)[1]
        try:
            return l.split(" ", 1)[0]
        except IndexError:
            return l
    except IndexError:
        return None

def __get_message(line: str, key: str) -> str:
    try:
        return line.split(f" {key} #",1)[1].split(" ",1)[1][1:].strip()
    except IndexError:
        return None

def __get_whisper_message(line: str) -> str:
    try:
        return line.split(" WHISPER ",1)[1].split(" ",1)[1][1:].strip()
    except IndexError:
        return None
    
def __get_whisper_channel(line: str) -> str:
    try:
        l = line.split("WHISPER ", 1)[1]
        try:
            return l.split(" ", 1)[0]
        except IndexError:
            return l
    except IndexError:
        return None

def __get_time_from_timestamp(line: str) -> datetime:
    tm = __get_single(line, "tmi-sent-ts")
    tm = tm[:-3]+ "." + tm[-3:]
    return datetime.utcfromtimestamp(float(tm))

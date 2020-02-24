import asyncio
import datetime
import json
import re
from pathlib import Path

import discord
import pytz

loop = asyncio.get_event_loop()

def format_ms_time(ms: int) -> str:
    """
    Format a timestamp to "%B %d, %Y - %H:%M:%S.%f (UTC)"
    """
    stamp = int(ms)
    stamp = stamp / 1000
    time = datetime.datetime.fromtimestamp(stamp, tz=pytz.timezone('UTC'))
    return time.strftime("%B %d, %Y - %H:%M:%S.%f (UTC)")


def format_ms_time_simple(ms: int) -> str:
    """
    Format a timestamp to "%B %d, %Y - %I:%M %p" in UTC
    """
    stamp = int(ms)
    stamp = stamp / 1000
    time = datetime.datetime.fromtimestamp(stamp, tz=pytz.timezone('UTC'))
    return time.strftime("%B %d, %Y - %I:%M %p")


def get_hex_color(d_color: discord.Colour) -> str:
    r = hex(d_color.r)[2:]
    g = hex(d_color.g)[2:]
    b = hex(d_color.b)[2:]
    color = '{}{}{}'.format(r, g, b)
    return color


def attachments_to_json(atts):
    arr = []

    for att in atts:
        dic = {'filename': att.filename, 'url': str(att.url), 'proxy_url': att.proxy_url}
        arr.append(dic)

    return json.dumps(arr)


def embed_dict(embed: discord.Embed):
    return embed.to_dict()


def embed_list(msg):
    rtn = []
    for embed in msg.embeds:
        rtn.append(embed_dict(embed))
    return rtn


def attachments_list(msg):
    rtn = []
    for att in msg.attachments:
        rtn.append({'url': str(att.url)})
    return rtn


def member_dict(au):
    if au is None:
        return {}
    return {
        'id': au.id,
        'displayName': au.display_name,
        'discriminator': au.discriminator,
        'avatar': au.avatar_url,
        'bot': au.bot
    }


def member_list(members):
    rtn = []
    for m in members:
        rtn.append(member_dict(m))
    return rtn


def msg_to_dict(msg: discord.Message):
    au: discord.User = msg.author
    rtn = {
        'id': msg.id,
        'pinned': msg.pinned,
        'author': member_dict(au),
        'edited': msg.edited_at is not None,
        'content': msg.system_content,
        'cleanContent': msg.clean_content,
        'createdAt': int(round(msg.created_at.timestamp() * 1000))
    }
    if len(msg.attachments) > 0:
        rtn['attachments'] = attachments_list(msg)
    if len(msg.embeds) > 0:
        rtn['embeds'] = embed_list(msg)
    if len(msg.mentions) > 0:
        rtn['mentions'] = member_list(msg.mentions)
    if msg.type != discord.MessageType.default:
        rtn['type'] = str(msg.type)
    return rtn


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)


async def check_nick(member: discord.Member):
    new_nick = re.sub(r'[^0-9A-Za-z_-]', '', member.display_name).strip()
    if new_nick == "":
        new_nick = "Member{}".format(member.guild.member_count)

    if new_nick != member.display_name:
        try:
            await member.edit(nick=new_nick)
        except discord.DiscordException:
            pass


def sync_exec(coro):
    global loop
    try:
        return loop.run_until_complete(coro)
    except RuntimeError:
        pass

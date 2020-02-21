#  Library to make crating bots for Twitch chat easier.
#  Copyright (c) 2019 Maciej Marciniak
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import typing

import twitchirc


def process_twitch_flags(flags) -> typing.Dict[str, typing.Union[str, typing.List[str]]]:
    """Process Twitch's tags."""
    # @<key>=<value>;[...]
    flags = flags[1:].split(';')
    # ['<key>=<value>', [...]]
    output = {}
    for i in flags:
        i = i.split('=', 1)
        val = i[1]
        if ',' in val:
            val = val.split(',')
        output[i[0]] = val
    return output


class Message:
    @staticmethod
    def from_match(m: typing.Match[str]):
        """
        Create a new object using a match

        :param m: Match
        :return: The new object
        """
        return Message(m.string)

    @staticmethod
    def from_text(text: str):
        """
        Create a new object from text

        :param text: Text to create it from.
        :return: The new object
        """
        new = Message('')
        new.raw_data = text
        if text.startswith(':'):
            new.source, new.action, new.args = text.split(' ', 2)
        else:
            new.args = text
        return new

    def __init__(self, args: str, outgoing=False, source=None, action='', parent=None, raw_data=None):
        """
        Message object.

        WARNING: If you receive this object at runtime, that means that, the packet you received is not known to this
        library

        :param args: Text received.
        """
        self.action = action
        self.source = source
        self.args: str = args
        self.outgoing = outgoing
        self.parent = parent
        self.raw_data = raw_data

    def __eq__(self, other):
        if isinstance(other, Message):
            return (other.args == self.args
                    and other.__class__ == self.__class__
                    and other.action == self.action
                    and other.source == self.source)
        else:
            return False

    def __repr__(self):
        if self.source is not None:
            return f'Message(source={self.source!r}, action={self.action!r}, args={self.args!r})'
        elif self.args:
            return f'Message(args={self.args!r})'
        elif self.raw_data:
            return f'Message(raw_data={self.raw_data!r})'
        else:
            return (f'Message({self.args!r}, source={self.source!r}, action={self.action!r}, '
                    f'raw_data={self.raw_data!r})')

    def __str__(self):
        return f'<Raw IRC message: {self.args!r}>'

    def __bytes__(self):
        if self.outgoing:
            if self.action:
                return bytes(self.action + ' ' + self.args)
            return bytes(self.args)
        else:
            return b''


class WhisperMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        flags = process_twitch_flags(m[1])
        new = WhisperMessage(flags=flags, user_from=m[2], user_to=m[3], text=m[4])
        new.raw_data = m[0]
        return new

    def __repr__(self):
        return (f'WhisperMessage(flags={self.flags!r}, user_from={self.user_from!r}, user_to={self.user_to!r}, '
                f'text={self.text!r})')

    def __str__(self):
        return f'{self.user_from} -> {self.user_to}: {self.text}'

    def __bytes__(self):
        if self.outgoing:
            return bytes(f'PRIVMSG #jtv :/w {self.user_to} {self.text}\r\n', 'utf-8')
        else:
            return b''

    def __init__(self, flags, user_from, user_to, text, outgoing=False):
        super().__init__(f'{"Outgoing" if outgoing else ""} WHISPER from {user_from} to {user_to}: {text}',
                         outgoing=outgoing)
        self.text = text
        self.user_to = user_to
        self.user_from = user_from
        self.flags = flags
        self.channel = 'whispers'

    @property
    def user(self):
        return self.user_from

    def reply(self, text: str):
        new = WhisperMessage(flags={}, user_from='OUTGOING', user_to=self.user_from, text=text, outgoing=True)
        return new


class ChannelMessage(Message):
    def moderate(self):
        if self.outgoing:
            raise RuntimeError('Cannot moderate a message that\'s going to be sent.')

        return twitchirc.ModerationContainer.from_message(self, self.parent)

    @staticmethod
    def from_match(m: typing.Match[str]):
        new = ChannelMessage(text=m[4], user=m[2], channel=m[3])
        new.flags = process_twitch_flags(m[1])
        new.raw_data = m[0]
        return new

    @staticmethod
    def from_text(text):
        m = re.match(twitchirc.PRIVMSG_PATTERN_TWITCH, text)
        if m:
            return ChannelMessage.from_match(m)
        else:
            raise ValueError(f'Cannot create a ChannelMessage from {text!r}')

    def __init__(self, text: str, user: str, channel: str, outgoing=False, parent=None):
        super().__init__(text, outgoing=outgoing, parent=parent)
        self._type = 'PRIVMSG'
        self.flags = {}
        self.text: str = text.replace('\r\n', '')
        self.user = user
        self.channel = channel

    def __repr__(self):
        return 'ChannelMessage(text={!r}, user={!r}, channel={!r})'.format(self.text, self.user, self.channel)

    def __str__(self):
        return '#{chan} <{user}> {text}'.format(user=self.user, text=self.text, chan=self.channel)

    def __bytes__(self):
        if self.outgoing:
            return bytes('PRIVMSG #{chan} :{text}\r\n'.format(chan=self.channel, text=self.text), 'utf-8')
        else:
            return b''

    def reply(self, text: str, force_slash=False):
        if not force_slash and text.startswith(('.', '/')):
            text = '/ ' + text
        new = ChannelMessage(text=text, user='OUTGOING', channel=self.channel)
        new.outgoing = True
        return new

    def reply_directly(self, text: str):
        new = WhisperMessage(flags={}, user_from='OUTGOING', user_to=self.user, text=text, outgoing=True)
        return new


class PingMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = PingMessage()
        new.host = m[1]
        new.raw_data = m[0]
        return new

    @staticmethod
    def from_text(text):
        m = re.match(twitchirc.PING_MESSAGSE_PATTERN, text)
        return PingMessage.from_match(m)

    def __init__(self, host: typing.Optional[str] = None):
        self.host = host
        super().__init__(str(self))
        self.outgoing = False

    def __repr__(self):
        return 'PingMessage(host={!r})'.format(self.host)

    def __str__(self):
        return 'PING :{}'.format(self.host)

    def reply(self):
        return PongMessage(self.host)


class PongMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        return None

    @staticmethod
    def from_text(text):
        return None

    def __init__(self, host):
        super().__init__(host)
        self.host = host
        self.outgoing = True

    def __repr__(self):
        return 'PongMessage(host={!r})'.format(self.host)

    def __str__(self):
        return 'PONG :{}'.format(self.host)

    def __bytes__(self):
        return bytes('PONG :{}\r\n'.format(self.host), 'utf-8')

    def reply(self):
        raise RuntimeError('Cannot reply to a PongMessage.')


class NoticeMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = NoticeMessage('')
        new.message_id = process_twitch_flags(m[1])['msg-id']
        new.host = m[2]
        new.channel = m[3]
        new.text = m[4]
        # @msg-id=%s :tmi.twitch.tv NOTICE #{chan} :{msg}
        new.raw_data = m[0]
        return new

    @staticmethod
    def from_text(text):
        m = re.match(twitchirc.NOTICE_MESSAGE_PATTERN, text)
        if m:
            return NoticeMessage.from_match(m)
        else:
            raise ValueError('Invalid NoticeMessage(NOTICE #chan): {!r}'.format(text))

    def __init__(self, text, message_id=None, channel=None, host=None):
        super().__init__(text)
        self.text = text
        self.message_id = message_id
        self.channel = channel
        self.host = host


class GlobalNoticeMessage(NoticeMessage):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = GlobalNoticeMessage('')
        new.host = m[1]
        new.text = m[2]
        new.raw_data = m[0]
        return new

    @staticmethod
    def from_text(text):
        m = re.match(twitchirc.GLOBAL_NOTICE_MESSAGE_PATTERN, text)
        if m:
            return GlobalNoticeMessage.from_match(m)
        else:
            raise Exception('Invalid GlobalNoticeMessage(NOTICE *) {!r}'.format(text))

    def __init__(self, text, host=None):
        super().__init__(text, message_id=None, channel='*', host=host)


class JoinMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = JoinMessage(m[1], m[2])
        new.raw_data = m[0]
        return new

    def __init__(self, user: str, channel: str, outgoing=False):
        super().__init__('{} JOIN {}'.format(user, channel), outgoing=outgoing)
        self.user = user
        self.channel = channel

    def __repr__(self) -> str:
        if self.outgoing:
            return f'JoinMessage(user={self.user!r}, channel={self.channel!r}, outgoing=True)>'
        else:
            return f'JoinMessage(user={self.user!r}, channel={self.channel!r})>'

    def __str__(self):
        if self.outgoing:
            return f'JOIN {self.channel}'
        else:
            return f'{self.user} JOIN {self.channel}'

    def __bytes__(self):
        if self.outgoing:
            return bytes(f'JOIN {self.channel}\r\n', 'utf-8')
        else:
            return b''


class PartMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = PartMessage(m[1], m[2])
        new.raw_data = m[0]
        return new

    def __init__(self, user: str, channel: str, outgoing=False):
        super().__init__(f'{user} PART {channel}', outgoing=outgoing)
        self.user = user
        self.channel = channel

    def __repr__(self):
        if self.outgoing:
            return f'PartMessage(user={self.user!r}, channel={self.channel!r})  # outgoing'
        else:
            return f'PartMessage(user={self.user!r}, channel={self.channel!r})'

    def __str__(self):
        if self.outgoing:
            return f'<PART {self.channel}>'
        else:
            return f'<{self.user} PART {self.channel}>'

    def __bytes__(self):
        if self.outgoing:
            return bytes(f'PART #{self.channel}', 'utf-8')
        else:
            return b''


class UsernoticeMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = UsernoticeMessage(m[1], m[2])
        new.raw_data = m[0]
        return new

    def __repr__(self):
        return f'UsernoticeMessage(flags={self.flags!r}, channel={self.channel!r})'

    def __str__(self):
        return f'<USERNOTICE {self.channel}>'

    def __init__(self, flags, channel):
        super().__init__(flags + ' ' + channel)
        self.flags = process_twitch_flags(flags)
        self.channel = channel


class UserstateMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = UserstateMessage(m[1], m[2])
        new.raw_data = m[0]
        return new

    def __repr__(self):
        return f'UserstateMessage(flags={self.flags!r}, channel={self.channel!r})'

    def __str__(self):
        return f'<USERSTATE {self.channel}>'

    def __init__(self, flags, channel):
        super().__init__(flags + ' ' + channel)
        self.flags = process_twitch_flags(flags)
        self.channel = channel


class ReconnectMessage(Message):
    @staticmethod
    def from_match(m: typing.Match[str]):
        new = ReconnectMessage()
        new.raw_data = m[0]
        return new

    def __repr__(self):
        return f'ReconnectMessage()'

    def __str__(self):
        return f'<RECONNECT>'

    def __init__(self):
        super().__init__('RECONNECT')


MESSAGE_PATTERN_DICT: typing.Dict[typing.Any, typing.Union[
    typing.Type[ChannelMessage],
    typing.Type[PingMessage],
    typing.Type[NoticeMessage],
    typing.Type[GlobalNoticeMessage],
    typing.Type[JoinMessage],
    typing.Type[PartMessage],
    typing.Type[WhisperMessage],
    typing.Type[ReconnectMessage],
    typing.Type[UsernoticeMessage]
]
] = {
    re.compile(twitchirc.PRIVMSG_PATTERN_TWITCH): ChannelMessage,
    re.compile(twitchirc.PING_MESSAGSE_PATTERN): PingMessage,
    re.compile(twitchirc.NOTICE_MESSAGE_PATTERN): NoticeMessage,
    re.compile(twitchirc.GLOBAL_NOTICE_MESSAGE_PATTERN): GlobalNoticeMessage,
    re.compile(twitchirc.JOIN_MESSAGE_PATTERN): JoinMessage,
    re.compile(twitchirc.PART_MESSAGE_PATTERN): PartMessage,
    re.compile(twitchirc.WHISPER_MESSAGE_PATTERN): WhisperMessage,
    re.compile(twitchirc.RECONNECT_MESSAGE_PATTERN): ReconnectMessage,
    re.compile(twitchirc.USERNOTICE_MESSAGE_PATTERN): UsernoticeMessage,
    re.compile(twitchirc.USERSTATE_MESSAGE_PATTERN): UserstateMessage,
}


def auto_message(message, parent=None):
    for k, v in MESSAGE_PATTERN_DICT.items():
        m = re.match(k, message)
        if m:
            new = v.from_match(m)
            new.parent = parent
            return new

    # if nothing matches return generic irc message.
    return Message.from_text(message)

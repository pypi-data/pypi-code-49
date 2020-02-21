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
import collections
import typing

import twitchirc

ChannelSettings = collections.namedtuple('ChannelSettings', [
    'emote',
    'followers',
    'slow',
    'unique',
    'subscribers'
], defaults=(
    False,
    False,
    False,
    False,
    False
))
COMMANDS = {
    'emote': {
        True: '/emoteonly',
        False: '/emoteonlyoff',
        'default': None
    },
    'followers': {
        True: '/followers {}',
        False: '/followersoff',
        'default': ''
    },
    'slow': {
        True: '/slow {}',
        False: '/slowoff',
        'default': '5'
    },
    'unique': {
        True: '/r9kbeta',
        False: '/r9kbetaoff',
        'default': None
    },
    'subscribers': {
        True: '/subscribers',
        False: '/subscribersoff',
        'default': None
    }
}


class ModerationContainer:
    """
    Run moderation commands in the context of the user, channel and message
    """

    def __init__(self, target_message_id, target_user, target_channel, parent=None):
        self.parent: twitchirc.Connection = parent
        self.target_message_id = target_message_id
        self.target_user = target_user
        self.target_channel = target_channel

    @classmethod
    def from_message(cls, msg, parent=None):
        new = cls(msg.flags['id'], msg.user, msg.channel, parent)
        return new

    def delete(self):
        self.parent.send(self.format_delete())

    def format_delete(self):
        """
        Create a message with the /delete command in it.

        :return: ChannelMessage containing generated command.
        """
        if self.target_message_id is not None:
            return twitchirc.ChannelMessage(user='OUTGOING', text=f'/delete {self.target_message_id}',
                                            channel=self.target_channel, outgoing=True)
        else:
            raise RuntimeError("This ModerationContainer doesn't target a message.")

    def timeout(self, time: typing.Union[int, str], reason: typing.Optional[str] = None):
        self.parent.send(self.format_timeout(time, reason))

    def format_timeout(self, time: typing.Union[int, str], reason: typing.Optional[str] = None):
        """
        Create a message with the /timeout command in it.

        :param time: Time to block the user for.
        :param reason: Reason for this action.
        :return: ChannelMessage containing generated command.
        """
        if isinstance(time, str) and (not time[-1].isalpha()) or time.isalpha():
            raise ValueError('Time needs to be an int or string with the last character indicating the unit.')
        if self.target_user is not None:
            return twitchirc.ChannelMessage(user='OUTGOING', text=f'/timeout {self.target_user} {time}'
                                                                  f'{f" {reason}" if reason is not None else ""}',
                                            channel=self.target_channel, outgoing=True)
        else:
            raise RuntimeError("This ModerationContainer doesn't target a user.")

    def purge(self, reason: typing.Optional[str] = None):
        self.parent.send(self.format_purge(reason))

    def format_purge(self, reason: typing.Optional[str] = None):
        """
        Use `format_timeout` to create a message with a one second timeout.

        :param reason: Reason for this action.
        :return: ChannelMessage containing generated command.
        """
        if self.target_user is not None:
            return self.format_timeout(1, reason)
        else:
            raise RuntimeError("This ModerationContainer doesn't target a user.")

    def permaban(self, reason: typing.Optional[str] = None):
        self.parent.send(self.format_permaban(reason))

    def format_permaban(self, reason: typing.Optional[str] = None):
        """
        Create a message with the /ban command in it.

        :param reason: Reason for this action.
        :return: ChannelMessage containing generated command.
        """
        if self.target_user is not None:
            return twitchirc.ChannelMessage(user='OUTGOING', text=f'/ban {self.target_user}'
                                                                  f'{f" {reason}" if reason is not None else ""}',
                                            channel=self.target_channel, outgoing=True)
        else:
            raise RuntimeError("This ModerationContainer doesn't target a user.")

    def set_vip(self, status):
        self.parent.send(self.format_set_vip(status))

    def format_set_vip(self, status):
        """
        Create a message with the /[un]vip command in it.

        :param status: New status for the user. True for vip, False for unvip.
        :return: ChannelMessage containing generated command.
        """
        if self.target_user is not None:
            return twitchirc.ChannelMessage(user='OUTGOING', text=f'/{"un" if not status else ""}vip {self.target_user}',
                                            channel=self.target_channel, outgoing=True)
        else:
            raise RuntimeError("This ModerationContainer doesn't target a user.")

    def set_mod(self, status):
        self.parent.send(self.format_set_mod(status))

    def format_set_mod(self, status):
        """
        Run the [un]mod command on the targeted user.

        :param status: New status for the user. True for mod, False for unmod.
        :return: ChannelMessage containing generated command.
        """
        if self.target_user is not None:
            return twitchirc.ChannelMessage(user='OUTGOING', text=f'/{"un" if not status else ""}mod {self.target_user}',
                                            channel=self.target_channel, outgoing=True)
        else:
            raise RuntimeError("This ModerationContainer doesn't target a user.")

    def clear_channel(self):
        self.parent.send(self.format_clear_channel())

    def format_clear_channel(self):
        """
        Run the clear command on the targeted channel.

        :return: ChannelMessage containing generated command.
        """
        return twitchirc.ChannelMessage(user='OUTGOING', text=f'/clear',
                                        channel=self.target_channel, outgoing=True)

    def untimeout(self):
        self.parent.send(self.format_untimeout())

    def format_untimeout(self):
        """
        Create a message with the /untimeout command in it.

        :return: ChannelMessage containing generated command.
        """
        if self.target_user is not None:
            return twitchirc.ChannelMessage(user='OUTGOING', text=f'/untimeout {self.target_user}',
                                            channel=self.target_channel, outgoing=True)
        else:
            raise RuntimeError("This ModerationContainer doesn't target a user.")

    # noinspection PyArgumentList
    def set_channel_mode(self, settings: ChannelSettings,
                         old_settings=ChannelSettings()):
        for m in self.format_set_channel_mode(settings, old_settings):
            self.parent.send(m)

    # noinspection PyArgumentList
    def format_set_channel_mode(self, settings: ChannelSettings,
                                old_settings=ChannelSettings()) -> typing.List:
        """
        Generate commands needed to change

        :param settings: Settings to apply.
        :param old_settings: Settings from before. Used to not execute commands that are not needed.
        :return: A list of ChannelMessages containing commands.
        """
        commands = []
        for num, val in enumerate(settings):
            if val != old_settings[num]:
                c_entry = COMMANDS[settings._fields[num]]
                if isinstance(settings[num], bool):
                    replacement = ''
                else:
                    replacement = str(settings[num])
                text = (c_entry[settings[num] is not False]
                        .replace('{}',
                                 replacement))
                msg = twitchirc.ChannelMessage(text=text,
                                               user='OUTGOING', outgoing=True,
                                               channel=self.target_channel, parent=self.parent)
                commands.append(msg)
        return commands

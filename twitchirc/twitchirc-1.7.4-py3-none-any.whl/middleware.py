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
import typing


class Event:
    name: str
    data: typing.Dict[str, typing.Any]

    def __init__(self, name: str, data: typing.Dict[str, typing.Any], source: typing.Any, cancelable=True,
                 has_result=False):
        """
        Representation of an event.

        :param name: Event name
        :param data: Data provided with the event.
        :param source: Source of the event.
        :param cancelable: Can this event be canceled?
        :param has_result: Does this event have a replacable result?
        """
        self._cancelable = cancelable
        self._has_result = has_result
        self._lock = True

        self.name = name
        self.data = data
        self.canceled = False
        self.source = source

        self.result = None

    def __setattr__(self, key, value):
        if key in ['_cancelable', '_lock', '_has_result'] and hasattr(self, '_lock'):
            # make _lock lock the cancelable attribute.
            raise RuntimeError(f'Cannot assign to {key}')
        else:
            super().__setattr__(key, value)

    def cancel(self):
        """
        Cancel the event

        :return: nothing.
        :raises RuntimeError: If the event was canceled before.
        """
        if self.canceled:
            raise RuntimeError(f'Event {self.name} was canceled before.')
        self.canceled = True


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class AbstractMiddleware:
    def __init__(self):
        """Base middleware class for Connections and Bots"""
        pass

    def __repr__(self):
        return f'<{self.__class__.__name__}()>'

    def __str__(self):
        return self.__repr__()

    def on_action(self, event: Event):
        """
        Called when an action is performed.

        :param event: Event
        :return: Action result
        """
        if event.name == 'send':
            self.send(event)
        elif event.name == 'receive':
            self.receive(event)
        elif event.name == 'command':
            self.command(event)
        elif event.name == 'permission_check':
            self.permission_check(event)
        elif event.name == 'join':
            self.join(event)
        elif event.name == 'part':
            self.part(event)
        elif event.name == 'disconnect':
            self.disconnect(event)
        elif event.name == 'connect':
            self.connect(event)
        elif event.name == 'add_command':
            self.add_command(event)
        elif event.name == 'reconnect':
            self.reconnect(event)
        # ignore unknown events.

    def send(self, event: Event) \
            -> None:
        """
        Called when sending a message.

        :param event: Event given. Required data keys: 'message'(str, bytes or a Message), optional: 'queue' (default \
        should be 'misc')
        Result: nothing.
        :return: Nothing
        """

    def receive(self, event: Event) -> None:
        """
        Called when receiving a message.

        :param event: Event given. Required data keys: 'message', optional: none. \
        Result: nothing.
        :return: Nothing
        """

    def command(self, event: Event) -> None:
        """
        Called when a command is run.

        :param event: Event given. Required data keys: 'message', 'command'. \
        Result: nothing.
        :return: Nothing
        """

    def permission_check(self, event: Event) -> None:
        """
        Called when permissions need to be checked.

        :param event: Event given. Required data keys: 'user', 'permissions', 'message', optional: 'command' \
        Result: Missing permissions

        :return: Nothing
        """

    def join(self, event: Event) -> None:
        """
        Called when joining a channel.

        :param event: Event given. Required data keys: 'channel'. \
        Result: nothing.
        :return: Nothing
        """

    def part(self, event: Event) -> None:
        """
        Called when parting a channel.

        :param event: Event given. Required data keys: 'channel'. \
        Result: nothing.
        :return: Nothing
        """

    def disconnect(self, event: Event) -> None:
        """
        Called when disconnecting from IRC.

        :param event: Event given. Required data keys: none. \
        Result: nothing.
        :return: Nothing
        """

    def connect(self, event: Event) -> None:
        """
        Called when connecting to IRC.

        :param event: Event given. Required data keys: 'username'. \
        Result: nothing.
        :return: Nothing
        """

    def add_command(self, event: Event) -> None:
        """
        Called when connecting to IRC.

        :param event: Event given. Required data keys: 'command'. \
        Result: nothing.
        :return: Nothing
        """

    def reconnect(self, event: Event) -> None:
        """
        Called when receiving a RECONNECT message from IRC or when getting kicked off.

        :param event: Event given. Required data keys: none, Result: nothing.
        :return: Nothing
        """

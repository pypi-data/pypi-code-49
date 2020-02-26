#!/usr/bin/env python3

""" AD1459, an IRC Client

  Copyright ©2019-2020 by Gaven Royer

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
  TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
  ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.

  The IRC client object.
"""

import asyncio
import logging
import pydle
import time

class Client(pydle.Client):
    """ This is the actual IRC Client. 

    Most of this functionality is provided by Pydle.
    """

    def __init__(self, nick, network, sasl_username=None, sasl_password=None, **kwargs):
        self.log = logging.getLogger('ad1459.client')
        super().__init__(nick, sasl_username=sasl_username, sasl_password=sasl_password, **kwargs)
        self.network_ = network
        self.log.debug('Created client for network %s', self.network_.name)
        self.bouncer = False
    
    async def connect(self, hostname=None, password=None, **kwargs):
        self.log.debug('Client initiating connection to %s', hostname)
        await super().connect(hostname=hostname, password=password, **kwargs)
    
    async def on_connect(self):
        self.log.info('Connected to %s', self.network_.name)
        await super().on_connect()
        await self.network_.on_connected()
    
    async def _disconnect(self, expected):
        """ We need to override this to stop the event loop getting closed."""
        # Shutdown connection.
        await self.connection.disconnect()

        # Reset any attributes.
        self._reset_attributes()

        # Callback.
        await self.on_disconnect(expected)

        """This is our override.
        # Shut down event loop.
        # if expected and self.own_eventloop:
        #     self.connection.stop()
        """
    
    async def on_raw(self, message):
        if message.command == ('CAP' or 'cap' or 'Cap'):
            if 'znc.in/' in " ".join(message.params):
                self.log.debug('Server appears to be a ZNC Bouncer')
                self.bouncer = True
        
        await super().on_raw(message)
    
    async def on_nick_change(self, old, new):
        self.log.debug('User %s is now %s', old, new)
        await self.network_.on_nick_change(old, new)
        await super().on_nick_change(old, new)
    
    async def on_join(self, channel, user):
        self.log.debug(f'User {user} joined {channel} on {self.network_.name}')
        await self.network_.on_join(channel, user)
        await super().on_join(channel, user)
    
    async def on_part(self, channel, user, message=None):
        self.log.debug(f'User {user} parted {channel} on {self.network_.name}')
        await self.network_.on_part(channel, user, message=message)
        await super().on_part(channel, user, message=message)
    
    async def on_kick(self, channel, target, by, reason=None):
        self.log.debug('%s was kicked from %s by %s (%s)', target, channel, by, reason)
        await self.network_.on_kick(channel, target, by, reason=reason)
        await super().on_kick(channel, target, by, reason=reason)
    
    async def on_quit(self, user, message=None):
        self.log.debug(f'User {user} has quit {self.network_.name}')
        await self.network_.on_quit(user, message=message)
        await super().on_quit(user, message=message)
    
    async def on_kill(self, target, by, reason):
        self.log.debug('%s was killed by %s, (%s)', target, by, reason)
        await self.network_.on_kill(target, by, reason=reason)
        super().on_kill(target, by, reason)

    async def on_channel_message(self, target, source, message):
        self.log.debug('New message in %s from %s: %s', target, source, message)
        await self.network_.on_message(target, source, message)
        await super().on_message(target, source, message)
    
    async def on_channel_notice(self, target, by, message):
        self.log.debug('Received notice to %s from %s', target, by)
        await self.network_.on_notice(target, by, message)
        await super().on_notice(target, by, message)
    
    async def on_private_message(self, target, by, message):
        self.log.debug('New private message to %s from %s: %s', target, by, message)
        await self.network_.on_private_message(target, by, message)
        await super().on_private_message(target, by, message)
    
    async def on_private_notice(self, target, by, message):
        self.log.debug('Received private notice to %s from %s', target, by)
        await self.network_.on_private_notice(target, by, message)
        await super().on_private_notice(target, by, message)
    
    async def on_mode_change(self, channel, modes, by):
        self.log.debug('%s set modes %s in %s', by, modes, channel)
        await self.network_.on_mode_change(channel, modes, by)
        await super().on_mode_change(channel, modes, by)
    
    async def on_topic_change(self, channel, message, by):
        self.log.debug('Topic in %s set to "%s" by %s', channel, message, by)
        await self.network_.on_topic_change(channel, message, by)
        await super().on_topic_change(channel, message, by)
    
    async def on_user_invite(self, target, channel, by):
        self.log.debug('%s was invited to %s by %s', target, channel, by)
        await self.network_.on_user_invite(target, channel, by)
        super().on_user_invite(target, channel, by)

    async def on_invite(self, channel, by):
        self.log.debug('Invited to %s by %s', channel, by)
        await self.network_.on_invite(channel, by)
        await super().on_invite(channel, by)
    
    # CTCP Support

    async def on_ctcp(self, by, target, what, contents):
        self.log.debug('%s received CTCP %s from %s: %s', target, what, by, contents)
        await super().on_ctcp(by, target, what, contents)
    
    async def on_ctcp_reply(self, by, target, what, contents):
        self.log.debug('%s received REPLY CTCP %s from %s: %s', target, what, by, contents)
        await super().on_ctcp(by, target, what, contents)

    async def on_ctcp_action(self, by, target, contents):
        await self.network_.on_ctcp_action(target, by, contents)
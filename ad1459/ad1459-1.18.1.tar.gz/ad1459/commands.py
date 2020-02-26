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

  Commands and their actions.
"""

import asyncio
import logging

class Commands:
    """ Commands for IRC.

    Each method in this class is a command to run. It should complete the 
    action required by the command.
    """
    log = logging.getLogger('ad1459.commands')
    def me(self, room, network, message):
        """ /me command

        Sends a CTCP Action.

        Arguments:
            room (:obj:`Room`): The room to ACTION
            client (:obj:`Client`): The client object
            message (str): The action to send.
        """
        self.log.debug('Sending action to %s: %s', room.name, message)
        asyncio.run_coroutine_threadsafe(
            network.client.ctcp(room.name, 'ACTION', contents=message),
            loop=asyncio.get_event_loop()
        )
    
    def join(self, room, network, command):
        """ /join command

        Joins a room on IRC.

        Arguments: 
            room : unused.
            client (:obj:'Client`): The client we're using to join.
            command (str): The text of the command.
        """
        channels = command.split()

        for channel in channels:
            if channel.startswith('#'):
                network.join_channel(channel)
    
    def quit(self, room, network, command):
        """ /quit command

        Disconnects from IRC.
        """
        if command:
            network.disconnect(message=command)
        else:
            network.disconnect()

    def part(self, room, network, command):
        if command:
            asyncio.run_coroutine_threadsafe(
                network.client.part(room.name, message=command),
                loop=asyncio.get_event_loop()
            )
        else:
            asyncio.run_coroutine_threadsafe(
                network.client.part(room.name),
                loop=asyncio.get_event_loop()
            )
    
    def kick(self, room, network, command):
        com = command.split()
        user = com.pop(0)
        reason = ' '.join(com)
        if network.nickname in room.ops:
            if reason:
                asyncio.run_coroutine_threadsafe(
                    network.client.kick(room.name, user, reason=reason),
                    loop=asyncio.get_event_loop()
                )
            else:
                asyncio.run_coroutine_threadsafe(
                    network.client.kick(room.name, user),
                    loop=asyncio.get_event_loop()
                )
        else:
            room.add_message(
                f'You are not an op in {room.name}', 
                sender=f'/kick {room.name} {user} reason={reason}',
                kind='notice'
            )
    
    def ban(self, room, network, command):
        com = command.split()
        user = com.pop(0)
        reason = ' '.join(com)
        if network.nickname in room.ops:
            asyncio.run_coroutine_threadsafe(
                network.client.ban(room.name, user),
                loop=asyncio.get_event_loop()
            )
        else:
            room.add_message(
                f'You are not an op in {room.name}', 
                sender=f'/ban {room.name} {user}',
                kind='notice'
            )
    
    def kickban(self, room, network, command):
        com = command.split()
        user = com.pop(0)
        reason = ' '.join(com)
        if network.nickname in room.ops:
            if reason:
                asyncio.run_coroutine_threadsafe(
                    network.client.kickban(room.name, user, reason=reason),
                    loop=asyncio.get_event_loop()
                )
            else:
                asyncio.run_coroutine_threadsafe(
                    network.client.kickban(room.name, user),
                    loop=asyncio.get_event_loop()
                )
        else:
            room.add_message(
                f'You are not an op in {room.name}', 
                sender=f'/kickban {room.name} {user} reason={reason}',
                kind='notice'
            )
    
    def nick(self, room, network, command):
        network.change_nick(command.split()[0])
    
    def query(self, room, network, command):
        com = command.split()
        user = com.pop(0)
        message = ' '.join(com)
        msgroom = network.get_room_for_name(user)
        network.window.switcher.switcher.select_row(msgroom.row)
        if message:
            network.send_message(msgroom, message)
    
    def msg(self, room, network, command):
        com = command.split()
        user = com.pop(0)
        message = ' '.join(com)
        msgroom = network.get_room_for_name(user)
        if message:
            network.send_message(msgroom, message)
    
    def notice(self, room, network, command):
        com = command.split()
        target = com.pop(0)
        notice = ' '.join(com)
        msgroom = network.get_room_for_name(target)
        if notice:
            asyncio.run_coroutine_threadsafe(
                network.client.notice(target, notice),
                loop=asyncio.get_event_loop()
            )
    
    def topic(self, room, network, command):
        com = command.split()
        if com[0].startswith('#'):
            channel = com.pop(0)
            topic = ' '. join(com)
        else:
            channel = room.name
            topic = command
        
        asyncio.run_coroutine_threadsafe(
            network.client.set_topic(channel, topic.strip()),
            loop=asyncio.get_event_loop()
        )

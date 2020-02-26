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

  Right-click menus for various widgets.
"""

import asyncio
import logging

import gi
gi.require_versions(
    {
        'Gtk': '3.0',
        'Pango': '1.0'
    }
)
from gi.repository import Gtk, GLib

class UserRowMenu(Gtk.Popover):

    def __init__(self, room, row):
        super().__init__()
        
        self.log = logging.getLogger('ad1459.user-row-menu')

        self.user = ''
        self.room = room
        self.row = row
        self.nick = self.room.network.nickname
        self.userop = False
        if self.nick in self.room.ops:
            self.userop = True

        layout_grid = Gtk.Grid()
        layout_grid.set_row_spacing(6)
        layout_grid.props.margin = 6
        self.add(layout_grid)

        self.whois_grid = Gtk.Grid()
        self.whois_grid.set_row_spacing(4)
        self.whois_grid.set_column_spacing(12)
        layout_grid.attach(self.whois_grid, 0, 1, 1, 1)

        self.nick = Gtk.Label()
        layout_grid.attach(self.nick, 0, 0, 1, 1)

        self.whois_spinner = Gtk.Spinner()
        self.whois_spinner.start()
        layout_grid.attach(self.whois_spinner, 0, 2, 1, 1)

        self.ident = Gtk.Label()
        self.whois_grid.attach(self.ident, 0, 1, 2, 1)

        self.realname_label = Gtk.Label.new('Real Name:')
        self.realname_label.set_halign(Gtk.Align.END)
        self.whois_grid.attach(self.realname_label, 0, 2, 1, 1)

        self.realname = Gtk.Label()
        self.realname.set_halign(Gtk.Align.START)
        self.whois_grid.attach(self.realname, 1, 2, 1, 1)

        self.account_label = Gtk.Label.new('Account:')
        self.account_label.set_halign(Gtk.Align.END)
        self.whois_grid.attach(self.account_label, 0, 3, 1, 1)

        self.account = Gtk.Label()
        self.account.set_halign(Gtk.Align.START)
        self.whois_grid.attach(self.account, 1, 3, 1, 1)

        self.server_label = Gtk.Label.new('Server:')
        self.server_label.set_halign(Gtk.Align.END)
        self.whois_grid.attach(self.server_label, 0, 4, 1, 1)

        self.server = Gtk.Label()
        self.server.set_halign(Gtk.Align.START)
        self.whois_grid.attach(self.server, 1, 4, 1, 1)

        deets_grid = Gtk.Grid()
        deets_grid.set_hexpand(False)
        deets_grid.set_halign(Gtk.Align.CENTER)
        deets_grid.set_column_spacing(18)
        self.whois_grid.attach(deets_grid, 0, 5, 2, 1)

        self.tls = Gtk.Label()
        self.tls.set_markup(f'<i>TLS</i>')
        Gtk.StyleContext.add_class(
            self.tls.get_style_context(), 'user-tag'
        )
        Gtk.StyleContext.add_class(
            self.tls.get_style_context(), 'tls'
        )
        deets_grid.attach(self.tls, 0, 0, 1, 1)

        self.login = Gtk.Label()
        self.login.set_markup(f'<i>Logged in</i>')
        Gtk.StyleContext.add_class(
            self.login.get_style_context(), 'user-tag'
        )
        Gtk.StyleContext.add_class(
            self.login.get_style_context(), 'login'
        )
        deets_grid.attach(self.login, 1, 0, 1, 1)
        self.show_all()

        self.oper = Gtk.Label()
        self.oper.set_markup(f'<i>IRCOp</i>')
        Gtk.StyleContext.add_class(
            self.oper.get_style_context(), 'user-tag'
        )
        Gtk.StyleContext.add_class(
            self.oper.get_style_context(), 'oper'
        )
        deets_grid.attach(self.oper, 2, 0, 1, 1)
        
        privmsg_button = Gtk.ModelButton()
        privmsg_button.set_label('Private Message')
        privmsg_button.connect('clicked', self.on_privmsg)
        layout_grid.attach(privmsg_button, 0, 3, 1, 1)

        self.op_actions = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        Gtk.StyleContext.add_class(self.op_actions.get_style_context(), 'linked')
        self.op_actions.set_halign(Gtk.Align.CENTER)
        layout_grid.attach(self.op_actions, 0, 4, 1, 1)

        self.op_voice = Gtk.ToggleButton()
        self.op_voice_image = Gtk.Image.new_from_icon_name(
            'user-voice-symbolic',
            Gtk.IconSize.SMALL_TOOLBAR
        )
        self.op_voice.set_image(self.op_voice_image)
        self.op_voice.set_tooltip_text('Voice')
        self.op_voice.connect('clicked', self.op_voice_clicked)
        self.op_actions.add(self.op_voice)

        self.op_op = Gtk.ToggleButton()
        self.op_op_image = Gtk.Image.new_from_icon_name(
            'user-op-symbolic',
            Gtk.IconSize.SMALL_TOOLBAR
        )
        self.op_op.set_image(self.op_op_image)
        self.op_op.set_tooltip_text('Op')
        self.op_op.connect('clicked', self.op_op_clicked)
        self.op_actions.add(self.op_op)

        self.op_mute = Gtk.ToggleButton()
        self.op_mute_image = Gtk.Image.new_from_icon_name(
            'user-mute-symbolic',
            Gtk.IconSize.SMALL_TOOLBAR
        )
        self.op_mute.set_image(self.op_mute_image)
        self.op_mute.set_tooltip_text('Mute')
        self.op_mute.connect('clicked', self.op_mute_clicked)
        self.op_actions.add(self.op_mute)

        self.op_kick = Gtk.ToggleButton()
        self.op_kick_image = Gtk.Image.new_from_icon_name(
            'user-kick-symbolic',
            Gtk.IconSize.SMALL_TOOLBAR
        )
        self.op_kick.set_image(self.op_kick_image)
        self.op_kick.set_tooltip_text('Kick')
        self.op_kick.connect('clicked', self.op_kick_clicked)
        self.op_actions.add(self.op_kick)

        self.op_ban = Gtk.ToggleButton()
        self.op_ban_image = Gtk.Image.new_from_icon_name(
            'user-ban-symbolic',
            Gtk.IconSize.SMALL_TOOLBAR
        )
        self.op_ban.set_image(self.op_ban_image)
        self.op_ban.set_tooltip_text('Ban')
        self.op_ban.connect('clicked', self.op_ban_clicked)
        self.op_actions.add(self.op_ban)


        self.show_all()
        self.ident.set_visible(False)
        self.realname_label.set_visible(False)
        self.realname.set_visible(False)
        self.account_label.set_visible(False)
        self.account.set_visible(False)
        self.server_label.set_visible(False)
        self.server.set_visible(False)
        self.tls.set_visible(False)
        self.login.set_visible(False)
        self.oper.set_visible(False)
        self.whois_grid.set_visible(False)

        self.popdown()
    
    def set_voice_button(self):
        self.op_voice.disconnect_by_func(self.op_voice_clicked)
        self.op_voice.set_active(self.row.get_voice())
        self.op_voice.connect('clicked', self.op_voice_clicked)

    def set_op_button(self):
        self.op_op.disconnect_by_func(self.op_op_clicked)
        self.op_op.set_active(self.row.get_op())
        self.op_op.connect('clicked', self.op_op_clicked)

    def set_mute_button(self):
        self.op_mute.disconnect_by_func(self.op_mute_clicked)
        self.op_mute.set_active(self.row.get_mute())
        self.op_mute.connect('clicked', self.op_mute_clicked)
    
    async def update_info(self, nick):
        self.log.debug('Getting whois info for %s', nick)
        self.nick.set_markup(f'<b>{nick}</b>')

        self.log.debug('user modes: %s', self.row.modes)

        GLib.idle_add(self.set_voice_button)
        GLib.idle_add(self.set_op_button)
        GLib.idle_add(self.set_mute_button)

        GLib.idle_add(self.whois_spinner.start)
        whois = await self.room.network.client.whois(nick)
        GLib.idle_add(self.whois_spinner.stop)

        self.log.debug('Whois: %s', whois)
        username = whois['username']
        host = whois['hostname']
        realname = whois['realname']
        account = whois['account']
        server = whois['server']
        tls = whois['secure']
        login = whois['identified']
        oper = whois['oper']

        self.log.info('Setting info...')
        if tls:
            GLib.idle_add(self.tls.set_visible, True)
        if login:
            GLib.idle_add(self.login.set_visible, True)
        if oper:
            GLib.idle_add(self.oper.set_visible, True)
        
        self.log.debug('Setting labels')
        if username and host:
            GLib.idle_add(
                self.ident.set_markup,
                f'<i><small>{username}@{host}</small></i>'
            )
            GLib.idle_add(self.ident.set_visible, True)
        if realname:
            GLib.idle_add(
                self.realname.set_text, realname
            )
            GLib.idle_add(self.realname_label.set_visible, True)
            GLib.idle_add(self.realname.set_visible, True)
        if account:
            GLib.idle_add(
                self.account.set_text, account
            )
            GLib.idle_add(self.account_label.set_visible, True)
            GLib.idle_add(self.account.set_visible, True)
        if server:
            GLib.idle_add(
                self.server.set_text, server
            )
            GLib.idle_add(self.server_label.set_visible, True)
            GLib.idle_add(self.server.set_visible, True)

        GLib.idle_add(
            self.op_voice.set_visible, self.userop
        )
        GLib.idle_add(
            self.op_op.set_visible, self.userop
        )
        GLib.idle_add(
            self.op_mute.set_visible, self.userop
        )
        GLib.idle_add(
            self.op_kick.set_visible, self.userop
        )
        GLib.idle_add(
            self.op_ban.set_visible, self.userop
        )

        GLib.idle_add(
            self.whois_grid.set_visible, True
        )
    
    def on_privmsg(self, button, data=None):
        """ `row-activated` handler for the list bow. 

        This opens a PM room with the selected user.
        """
        network = self.room.network
        user = self.row.nick
        new_room = network.get_room_for_name(user)
        window = self.room.window
        window.message_stack.set_visible_child_name(new_room.id)
        window.topic_stack.set_visible_child_name(new_room.id)
        window.irc_entry.grab_focus_without_selecting()
        window.nick_button.set_label(network.nickname)
        window.switcher.switcher.select_row(new_room.row)

    def op_voice_clicked(self, button, data=None):
        self.log.debug('self.op_voice clicked')
        client = self.room.network.client
        target = self.row.nick
        if button.get_active():
            asyncio.run_coroutine_threadsafe(
                client.set_mode(self.room.name, '+v', target),
                loop=asyncio.get_event_loop()
            )
        else:
            asyncio.run_coroutine_threadsafe(
                client.set_mode(self.room.name, '-v', target),
                loop=asyncio.get_event_loop()
            )

    def op_op_clicked(self, button, data=None):
        self.log.debug('self.op_op clicked')
        client = self.room.network.client
        target = self.row.nick
        if button.get_active():
            asyncio.run_coroutine_threadsafe(
                client.set_mode(self.room.name, '+o', target),
                loop=asyncio.get_event_loop()
            )
        else:
            asyncio.run_coroutine_threadsafe(
                client.set_mode(self.room.name, '-o', target),
                loop=asyncio.get_event_loop()
            )

    def op_mute_clicked(self, button, data=None):
        self.log.debug('self.op_mute clicked')
        client = self.room.network.client
        target = self.row.nick
        if button.get_active():
            asyncio.run_coroutine_threadsafe(
                client.set_mode(self.room.name, '+q', target),
                loop=asyncio.get_event_loop()
            )
        else:
            asyncio.run_coroutine_threadsafe(
                client.set_mode(self.room.name, '-q', target),
                loop=asyncio.get_event_loop()
            )

    def op_kick_clicked(self, button, data=None):
        self.log.debug('self.op_kick clicked')

    def op_ban_clicked(self, button, data=None):
        self.log.debug('self.op_ban clicked')

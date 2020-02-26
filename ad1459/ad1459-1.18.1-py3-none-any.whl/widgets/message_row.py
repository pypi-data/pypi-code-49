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

  ListBoxRows for messages.
"""

import logging

import gi
gi.require_versions(
    {
        'Gtk': '3.0',
        'Pango': '1.0'
    }
)
from gi.repository import Gtk, GLib, Pango

from ad1459.formatting import Parser

class MessageRow(Gtk.ListBoxRow):
    """ A ListBoxRow representing a message.

    The attributes for this class are stored directly in the Gtk.Label widgets
    drawn within these rows, as this obviates the need to store extra variables
    in memory.

    We use two copies of the message text, timestamp, and sender. This is to
    display the message differently depending on if this was a server message or
    a normal message. Server messages are combined into one long message, and 
    be collapsed to save space.

    Attributes:
        time (str): The time the message was sent.
        sender (str): The user/network who sent the message. "*" by default.
        text (str): The text of the message.
    """

    def __init__(self):
        Gtk.ListBoxRow.__init__(self)
        self.log = logging.getLogger('ad1459.message-row')

        # We don't want these to be selectable in the list
        self.props.selectable = False
        Gtk.StyleContext.add_class(self.get_style_context(), "message-row")
        self.props.margin = 1
        self.set_margin_start(6)
        self.set_margin_end(6)
        self.set_focus_on_click(False)

        # We use the stack to display server/message rows with a single widget
        self.stack = Gtk.Stack()
        self.add(self.stack)

        # This is the layout for normal messages
        self.message_grid = Gtk.Grid()
        self.message_grid.set_hexpand(True)
        self.message_grid.set_margin_top(1)
        self.message_grid.set_margin_bottom(2)
        self.message_grid.set_margin_start(12)
        self.message_grid.set_margin_end(12)
        self.message_grid.set_column_spacing(12)

        # This is the layout for server messages.
        self.server_grid = Gtk.Grid()
        self.server_grid.set_hexpand(True)
        self.server_grid.set_valign(Gtk.Align.CENTER)
        self.server_grid.set_margin_left(12)
        self.server_grid.set_margin_right(12)
        self.server_grid.set_column_spacing(12)

        # The sender for normal messages
        self.message_sender = Gtk.Label()
        self.message_sender.set_margin_bottom(1)
        self.message_sender.set_selectable(True)
        self.message_sender.set_use_markup(True)
        self.message_sender.set_halign(Gtk.Align.START)
        self.message_sender.set_line_wrap(True)
        self.message_sender.set_line_wrap_mode(Pango.WrapMode.CHAR)
        self.message_sender.props.opacity = 0.8
        self.message_grid.attach(self.message_sender, 0, 0, 1, 1)
        
        # The timestamp for normal messages
        self.message_time = Gtk.Label()
        self.message_time.set_selectable(True)
        self.message_time.set_use_markup(True)
        self.message_time.set_halign(Gtk.Align.END)
        self.message_time.props.opacity = 0.5
        self.message_grid.attach(self.message_time, 1, 0, 1, 1)
        
        # The text for normal messages
        self.message_text = Gtk.Label()
        self.message_text.set_selectable(True)
        self.message_text.set_use_markup(False)
        self.message_text.set_halign(Gtk.Align.START)
        self.message_text.set_line_wrap(True)
        self.message_text.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.message_text.set_hexpand(True)
        self.message_text.set_margin_start(12)
        self.message_text.props.xalign = 0
        self.message_grid.attach(self.message_text, 0, 1, 2, 1)

        # The sender for server messages
        self.server_sender = Gtk.Label()
        self.server_sender.set_selectable(True)
        self.server_sender.set_use_markup(True)
        self.server_sender.props.xalign = 1
        self.server_sender.props.halign = Gtk.Align.START
        self.server_sender.props.valign = Gtk.Align.START
        self.server_sender.props.opacity = 0.8
        self.server_grid.attach(self.server_sender, 0, 0, 1, 1)

        # The timestamp for server messages
        self.server_time = Gtk.Label()
        self.server_time.set_selectable(True)
        self.server_time.set_use_markup(True)
        self.server_time.set_width_chars(9)
        self.server_time.props.halign = Gtk.Align.END
        self.server_time.props.valign = Gtk.Align.START
        self.server_time.props.opacity = 0.5
        self.server_grid.attach(self.server_time, 2, 0, 1, 1)

        # We need expander + revealer to animate the message contents.
        self.server_message_expander = Gtk.Expander()
        self.server_message_expander.set_expanded(True)
        self.server_message_expander.set_hexpand(True)
        self.server_message_expander.props.opacity = 0.6
        self.server_message_expander.connect('notify::expanded', self.show_hide)
        self.server_grid.attach(self.server_message_expander, 1, 0, 1, 1)
        self.server_revealer = Gtk.Revealer()
        self.server_revealer.set_transition_type(
            Gtk.RevealerTransitionType.SLIDE_DOWN
        )
        self.server_revealer.props.reveal_child = True
        self.server_grid.attach(self.server_revealer, 0, 1, 3, 1)

        # The text for server messages
        self.server_text = Gtk.Label()
        self.server_text.set_selectable(True)
        self.server_text.set_use_markup(False)
        self.server_text.props.halign = Gtk.Align.START
        self.server_text.set_line_wrap(True)
        self.server_text.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.server_text.set_hexpand(True)
        self.server_text.props.xalign = 0
        self.server_text.props.opacity = 0.7
        self.server_revealer.add(self.server_text)

        # Show everything
        self.message_text.show()
        self.message_time.show()
        self.message_sender.show()
        self.message_grid.show()
        self.server_text.show()
        self.server_time.show()
        self.server_sender.show()
        self.server_grid.show()

        # Keep track of server messages (this is ignored for normal messages)
        self.server_count = 1
        self.server_message_expander.set_label(
            f'{self.server_count} server messages'
        )

        self.parser = Parser()
        self.kind = 'message'

        # Keep track of whether the user toggles the expander
        self.toggled = False
    
    def update_server_message(self, text):
        """ Adds text to a server message.

        We set the updated text (placing it on a newline) and increment the 
        count of the messages. 

        Arguments:
            text (str): The line to add to the server message.
        """
        # We use '/n' because our parsing later on filters out newlines.
        # It will ignore '/n', so we use that and replace it before setting.
        self.log.debug('Updating message text')
        self.log.debug('Old text: \n%s', self.text)
        oldtext = self.text.replace('\u000A', '/u000A')
        self.text = f'{oldtext} /u000A{text} '
        self.log.debug('New text: \n%s', self.text)
        self.server_count += 1
        self.server_message_expander.set_label(
            f'{self.server_count} server messages'
        )
        if self.server_count > 10 and not self.toggled:
            self.server_message_expander.set_expanded(False)
    
    # Internal Handlers
    def show_hide(self, expander, data=None):
        """ handler for the expander-revealer above. 
        
        When the expander is toggled, we set the revealer property to the same
        as the expander's property.
        """
        self.server_revealer.props.reveal_child = expander.get_expanded()
        # User toggled manually, remember that.
        self.toggled = True
    
    @property
    def kind(self):
        """str: The type of message this is, based on who sent it and 
        its contents.
        """
        return self._kind
    
    @kind.setter
    def kind(self, kind):
        self._kind = kind
        Gtk.StyleContext.add_class(self.get_style_context(), kind)
        for child in self.stack.get_children():
            self.stack.remove(child)

        if kind == 'server':
            self.stack.add_named(self.server_grid, 'server')
            self.stack.set_visible_child_name('server')
        else:
            self.stack.add_named(self.message_grid, 'message')
            self.stack.set_visible_child_name('message')


    @property
    def time(self):
        """str: The time the message was sent."""
        return self.message_time.get_text()
    
    @time.setter
    def time(self, time):
        self.message_time.set_markup(f'<small><i>{time}</i></small>')
        self.server_time.set_markup(f'<small><i>{time}</i></small>')
    
    @property
    def sender(self):
        """ The sender of the message, or * for none/network. """
        return self.message_sender.get_text()
    
    @sender.setter
    def sender(self, sender):
        self.message_sender.set_markup(f'<small><b>{sender}</b></small>')
        self.server_sender.set_markup(f'<small>{sender}</small>')
    
    @property
    def text(self):
        """ The message text."""
        return self.message_text.get_text()
    
    @text.setter
    def text(self, text):
        """ We need to make some conversions depending on the type of message
        this is.
        """
        self.log.debug('Setting text to %s', text)
        # Action message formatting
        if self.kind == 'action':
            text = f'\x1D{text}\x1D'
        
        # This is our message parsing for formatting and such.
        escaped_text = GLib.markup_escape_text(text, len(text.encode('utf-8')))
        formatted_text = self.parser.parse_text(escaped_text)
        linked_text = self.parser.hyperlinks(formatted_text.replace('/n', ' /n'))

        # Set both of the labels to the same text.
        self.message_text.set_markup(linked_text.replace('/u000A', '\u000A'))
        self.server_text.set_markup(linked_text.replace('/u000A', '\u000A'))
    
    def show_all_contents(self):
        self.show_all()
